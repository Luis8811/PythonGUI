from enum import Enum
import json
from json import JSONEncoder
class ObjectDetected:

    def __init__(self, label, topLeftX, topLeftY, bottomRightX, bottomRightY, confidence):
        self.label = label
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY
        self.confidence = confidence
        if label == 'person':
            self.object = Object.person
        elif (label == 'chair'):
            self.object = Object.chair
        elif (label == 'sofa'):
            self.object = Object.sofa
        elif (label == 'book'):
            self.object = Object.book
        elif (label == 'laptop'):
            self.object = Object.laptop
        elif (label == 'tvmonitor'):
            self.object = Object.tvmonitor
        else:
            self.object = Object.keyboard

    def getLabel(self):
        return self.label

    def getTopLeftX(self):
        return self.topLeftX
    
    def getTopLeftY(self):
        return self.topLeftY

    def getBottomRightX(self):
        return self.bottomRightX
    
    def getBottomRightY(self):
        return self.bottomRightY
    
    def setLabel(self, label):
        self.label = label
    
    def setTopLeftX(self, topLeftX):
        self.topLeftX = topLeftX
    
    def setTopLeftY(self, topLeftY):
        self.topLeftY = topLeftY
    
    def setBottomRightX(self, bottomRightX):
        self.bottomRightX = bottomRightX
    
    def setBottomRightY(self, bottomRightY):
        self.bottomRightY = bottomRightY
    
    def getCenterX(self):
        centerX = (self.getTopLeftX() + self.getBottomRightX())/2
        return centerX
    
    def getCenterY(self):
        centerY = (self.getTopLeftY() + self.getBottomRightY())/2
        return centerY
    
    def getConfidence(self):
        return self.confidence
    
    def setConfidence(self, confidence):
        self.confidence = confidence

    def getObject(self):
        return self.object


class Object(Enum):
    person = 1
    chair = 2
    sofa = 3
    book = 4
    laptop = 5
    tvmonitor = 6
    keyboard = 7

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
        
        print('Displaying frames:')
        print(listOfObjects)
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
        """ Returns a list of ObjectFromFrame"""
        return self.objects
    
    def setObjects(self, objects):
        """ Sets a list of ObjectFromFrame"""
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
    
