import enum
from obj import ObjectDetected,Object, Frame, ObjectFromFrame
import math
import cv2
import numpy as np
import sys
sys.path.append('c:\\Users\\Normandi\\darknet\\ThermalComfortGUI\\PythonGUI\\logic\\thermal_comfort')
from activity import Activity
from image import Image
import json
from collections import namedtuple
from json import JSONEncoder

class Detection:
    
    def distanceBetweenObjects(self, object1, object2):
        xM1 = object1.getCenterX()
        xM2 = object2.getCenterX()
        yM1 = object1.getCenterY()
        yM2 = object2.getCenterY()
        sumX = pow((xM1 - xM2), 2)
        sumY = pow((yM1 - yM2), 2)
        distance = math.sqrt((sumX + sumY))
        return distance
        
    def loadObjectsFromJSON():
        return 0
        
    def imageDecoder(imageDict):
        return namedtuple('X', imageDict.keys())(*imageDict.values())


    # Parses the processed information from Yolo to an Image
    def parseProcessedImage(pathToImage):
        image = Detection.detectImageSize(pathToImage)
        pos = pathToImage.rfind(".")
        print('pos: ' + str(pos))
        pathToJSON = pathToImage[0:pos + 1]
        pathToJSON += "json"
        objects = Detection.detectObjectsFromJSON(pathToJSON)
        image.setObjects(objects)
        print('It works')
        return image

    # Detects the size of the image (height and width)
    def detectImageSize(pathToImage):
        image = cv2.imread(pathToImage)
        height, width = image.shape[0:2]
        print('Height:' + str(height))
        print('Width:' + str(width))
        objects = []
        imageDetected = Image(height, width, objects)
        return imageDetected

    
    # Getting frames from JSON obtained with YoloV4 (Darknet)
    def getFramesFromJSON(jsonOfImageProcessed):
        """ Function to return the frames from a JSON obtained with YoloV4 (Darknet) """
        inputFile = open(jsonOfImageProcessed)
        jsonArray = json.load(inputFile)
        listOfFrames = []
        for item in jsonArray:
            frameDetected = Frame(item['frame_id'], item['filename'], item['objects'])
            listOfFrames.append(frameDetected)
        return listOfFrames

    def printFrames(listOfFrames):
        """ Function to print a list of Frame (logic.obj)"""
        for item in listOfFrames:
            print("Frame: " + str(item.getId()) + ">>>")
            print("Filename: " + item.getFilename())
            print("Objects:")
            for currentObject in item.getObjects():
                print("Name: " + currentObject.getName() + " Confidence: " + str(currentObject.getConfidence()))

    
    # Parses JSON of obj
    def detectObjectsFromJSON(jsonOfImageProcessed):
         inputFile = open(jsonOfImageProcessed)
         jsonArray = json.load(inputFile)
         objectsList = []
         for item in jsonArray:
             objectDetected = ObjectDetected(item['label'], item['topleft']['x'], item['topleft']['y'], item['bottomright']['x'], item['bottomright']['y'], item['confidence'])
             objectsList.append(objectDetected)
         return objectsList


    # Returns the activities inferred from the list of objects in an image processed
    def detectActivities(self, image):
        objects = image.getObjects()
        persons = self.detectPersons(objects)
        nonPersons = self.detectNonPersons(objects)
        matrixSize = [len(persons), len(nonPersons)]
        matrixOfDistances = np.zeros(matrixSize, dtype=bool)
        matrixOfMarksOfProximity = np.zeros(matrixSize)
        activities = []
        i = 0
        j = 0
        for i in range(len(persons)):
            for j in range(len(nonPersons)):
                currentDistance = self.distanceBetweenObjects(persons[i], nonPersons[j])
                matrixOfDistances[i, j] = currentDistance
                matrixOfMarksOfProximity[i, j] = self.areClose(image.getHeight(), image.getWidth(), currentDistance)
            currentActivity = self.getActivityPerformed(matrixOfMarksOfProximity[i], nonPersons)
            print('Current activity:' + str(currentActivity))
            if currentActivity is not Activity.other:
                activities.append(currentActivity)
        print('Displaying proximity matrix>>>>>:')
        print(matrixOfDistances)
        print('Displaying matrix of marks of proximity>>>:')
        print(matrixOfMarksOfProximity)       
        return activities

    # Returns True if two objects are close to each other
    # distanceBetweenTwoObjects is less than 10% of average between imageHeight and imageWidth 
    def areClose(self, imageHeight, imageWidth, distanceBetweenTwoObjects):
        averageOfImageSize = (imageHeight + imageWidth)/2
        if distanceBetweenTwoObjects >= averageOfImageSize:
            return False
        else:
            percentageOf10 = (10/1000) * averageOfImageSize
            if distanceBetweenTwoObjects < percentageOf10:
                return True
            else:
                return False
            

    # Returns the Activity performed by a person that is close to several objects
    def getActivityPerformed(self, rowOfMatrixOfMarksOfProximity, objectsCloseToAPerson):
        objects = []
        for i in range(len(rowOfMatrixOfMarksOfProximity)):
            if rowOfMatrixOfMarksOfProximity[i] == True:
                objects.append(objectsCloseToAPerson[i])
        print('Displaying objects received in getActivityPerformed>>>:')
        print(objects)
        print('Objects detailed>>>:')
        self.printArrayOfObjects(objects)
        return self.getActivity(objects)
        



    # Returns the persons from the list of objects in an image proccessed
    def detectPersons(self, objects):
        persons = []
        for item in objects:
            if item.getObject() == Object.person:
                persons.append(item)
        print('Displaying detectPersons>>>')
        print(persons)
        return persons
    
    # Returns the objects different to Person from the list of objects in an image processed
    def detectNonPersons(self, objects):
        nonPersons = []
        for item in objects:
            if item.getObject() is not Object.person:
                nonPersons.append(item)
        print('Displaying detectNonPersons>>>>')
        print(nonPersons)
        return nonPersons
    

    # Returns the objects close to a person
    # def getNearObjectsTo
    
    # Returns the actitity performed by a person using the objects close to it
    def getActivity(self, objects):
        if self.isReading(objects):
            return Activity.reading_seated
        
        if self.isTyping(objects):
            return Activity.typing
        
        return Activity.other

    # Returns true if the objects are consistent with the activity of reading seated
    def isReading(self, objects):
        bookWasFound = False
        chairWasFound = False
        for item in objects:
            if item.getObject() is Object.chair:
                chairWasFound = True
            if item.getObject() is Object.book:
                bookWasFound = True
        if bookWasFound and chairWasFound:
            return True
        return False
    
    # Prints an array of objects (objects should be: person, tvmonitor, keyboard, book, chair)
    def printArrayOfObjects(self, arrayOfObjects):
        for item in arrayOfObjects:
            print(item.getObject())


    # Returns true if the objects are consistent with the activity of typing seated
    def isTyping(self, objects):
        keyboardWasFound = False
        chairWasFound = False
        tvMonitorWasFound = False
        for item in objects:
            if item.getObject() is Object.chair:
                chairWasFound = True
            if item.getObject() is Object.keyboard:
                keyboardWasFound = True
            if item.getObject() is Object.tvmonitor:
                tvMonitorWasFound = True
        if chairWasFound and tvMonitorWasFound and keyboardWasFound:
            return True
        return False


    def getMetabolicRate(activity):
        if (activity == Activity.reading_seated or activity == Activity.writing):
            return 1
        
        if (activity == Activity.typing):
            return 1.1
            
        if (activity == Activity.archive_seated):
            return 1.2
        
        if (activity == Activity.archive):
            return 1.4
        
        if (activity == Activity.walking):
            return 1.7
        
        if (activity == Activity.packing):
            return 2.1
        return 0 

     # Returns a list when the first item is the height and the second item is the width
    def getHeightAndWidthFromRectangle(upperLeftX, upperLeftY, bottomRightX, bottomRightY):
        height = abs(bottomRightY - upperLeftY)
        width = abs(bottomRightX - upperLeftX)
        result = [height, width]
        return result

    # Returns the String representation of the activity
    def getNameOfActivity(self, activity):
        print('Calling getNameOfActivity>>>>:')
        print('Activity: ')
        if (activity is Activity.reading_seated):
            print('Leyendo sentado')
            return 'Leyendo sentado'
        elif (activity is Activity.typing):
            print('Tecleando')
            return 'Tecleando'
        elif activity is Activity.walking:
            print('Caminando')
            return 'Caminando'
        elif activity is Activity.packing:
            print('Archivando')
            return 'Archivando'
        else:
            print('Otra')
            return 'Otra'
            
            


    # Prints an image processed by the function parseProcessedImage
    def printImage(imageProcessed):
        print('Height:' + str(imageProcessed.getHeight()))
        print('Width:' + str(imageProcessed.getWidth()))
        print('Cantidad de objetos:' + str(len(imageProcessed.getObjects())))
        for currentObject in imageProcessed.getObjects():
            print('<<')
            print('Label: ' + currentObject.getLabel() + ' Confidence: ' + str(currentObject.getConfidence()) +' Topleft>> X: ' + str(currentObject.getTopLeftX()) + ' Y: ' + str(currentObject.getTopLeftY()) + ' BottomRight X: ' + str(currentObject.getBottomRightX()) + ' Y: ' + str(currentObject.getBottomRightY()) + ' CenterX: ' + str(currentObject.getCenterX()) + ' CenterY: ' + str(currentObject.getCenterY()))



# testing
# p1 = ObjectDetected('Person', 5, 2, 5, 2, 7)
# p2 = ObjectDetected('PC', 3, 1, 3, 1, 8)
# print(distanceBetweenObjects(p1, p2))
# print(getMetabolicRate(Activity.archive))
# pathToJson = 'C:\\Users\\Normandi\\Desktop\\sample_person.json'
pathToImage ='C:\\Users\\Luis\\Desktop\\20206221850.jpg'
imageProcessed = Detection.parseProcessedImage(pathToImage)
a = Detection()
print(a.detectActivities(imageProcessed))
# Detection.printImage(imageProcessed)

# Testing detection from JSON of YoloV4 (Darknet)
print('TESTING MAPPING OF JSON FROM DARKNET (YOLOV4)')
pathToJsonYolov4 = 'C:\\Users\\Luis\\Desktop\\processedImages\\result2.json'
listOfFramesForTest = Detection.getFramesFromJSON(pathToJsonYolov4)
Detection.printFrames(listOfFramesForTest)
