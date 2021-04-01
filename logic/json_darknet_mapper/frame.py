import json
from json import JSONEncoder

class Frame:
    """ Frame from JSON obtained with YoloV4 (Darknet) """
    def __init__(self, id, filename, objects):
        self.id = id
        self.filename = filename
        self.objects = self.__getObjectsFromFrame(objects)
    
    def __getObjectsFromFrame(self, objects):
        """ Returns a list of ObjectFromFrame"""
        listOfObjects = []
        for item in objects:
            objectFromFrameDetected = ObjectFromFrame(item['name'], item['confidence'])
            listOfObjects.append(objectFromFrameDetected)
        return listOfObjects

    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getFilename(self):
        return self.filename
    
    def setFilename(self, filename):
        self.filename = filename
    
    def getObjects(self):
        """ Returns a list of ObjectFromFrame """
        return self.objects
    
    def setObjects(self, objects):
        """ Sets a list of ObjectFromFrame """
        self.objects = objects

class ObjectFromFrame:
    """ Object from Frame in JSON obtained with YoloV4 (Darknet) """
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getConfidence(self):
        return self.confidence
    
    def setConfidence(self, confidence):
        self.confidence = confidence

class DarknetYoloV4JsonMapper:
    """ Darknet YoloV4 JSON mapper  """
    def getFramesFromJSON(jsonOfImageProcessed):
        """ Function to return the frames from a JSON obtained with YoloV4 (Darknet) """
        inputFile = open(jsonOfImageProcessed)
        jsonArray = json.load(inputFile)
        listOfFrames = []
        for item in jsonArray:
            frameDetected = Frame(item['frame_id'], item['filename'], item['objects'])
            listOfFrames.append(frameDetected)
        return listOfFrames

    def getFrameFromJSON(jsonOfImageProcessed):
        """ Function to return the frame from a JSON obtained with YoloV4 (Darknet) """
        inputFile = open(jsonOfImageProcessed)
        jsonObject = json.load(inputFile)
        frameDetected = Frame(jsonObject['frame_id'], jsonObject['filename'], jsonObject['objects'])
        return frameDetected

    def printFrames(listOfFrames):
        """ Function to print a list of Frame """
        for item in listOfFrames:
            print("Frame: " + str(item.getId()) + ">>>")
            print("Filename: " + item.getFilename())
            print("Objects:")
            for currentObject in item.getObjects():
                print("Name: " + currentObject.getName() + " Confidence: " + str(currentObject.getConfidence()))