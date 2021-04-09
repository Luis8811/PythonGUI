import numpy as np
import time
import cv2
import matplotlib.pyplot as plt
import json
import os
import datetime

def getNameOfImage(pathOfImage):
    """ Returns the name of the image."""
    posOfName = pathOfImage.rfind("/") + 1;
    nameOfImage = pathOfImage[posOfName:]
    return nameOfImage

def getPosOfNameOfImage(pathOfImage):
    """ Function to get the pos of the name of an image """
    posOfName = pathOfImage.rfind("\\") + 1;
    return posOfName
 
def readDirectoryOfProcessedImages():
    """ Function to read the directory of processed images """
    print("Directory of processed")
    basepath = "C:/users/Normandi/darknet/data/sample_test2/out"
    listOfFiles = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            print(entry)
            listOfFiles.append(entry)
    return listOfFiles

def readDirectoryOfImages():
    """ Function to read the directory of images """
    print("Directory of images")
    basepath = "C:/users/Normandi/darknet/data/sample_test2/"
    listOfFiles = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            print(entry)
            listOfFiles.append(entry)
    return listOfFiles
    
def processImages(listOfFiles, listOfProcessedFiles):
    """ Function to process the images from a directory not processed before"""
    listOfNotProcessedImages = []
    for image in listOfFiles:
        if image not in listOfProcessedFiles:
            listOfNotProcessedImages.append(image)
    print(listOfNotProcessedImages)
    return listOfNotProcessedImages

def Show_Image(path):
    """ Function to show an image """
    print('Function: Show_Image>>>>')
    print('Path: ' + path)
    image = cv2.imread(path)
    height, width = image.shape[:2]
    resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)
    fig = plt.gcf()
    fig.set_size_inches(18, 10)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.show()

def detectObjectsInImage(INPUT_FILE):
    """ Function to detect objects in an image """
    print('Function>>>detectObjectsInImage')
    print('Image path: ' + INPUT_FILE)
    LABELS_FILE='C:\\Users\\Normandi\\darknet\\data\\obj.names'
    CONFIG_FILE='C:\\Users\\Normandi\\darknet\\cfg\\yolov4-custom.cfg'
    WEIGHTS_FILE='C:\\users\\Normandi\\darknet\\backup\\yolov4-custom_last.weights'
    CONFIDENCE_THRESHOLD=0.7
    LABELS = open(LABELS_FILE).read().strip().split("\n")

    np.random.seed(4)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
        dtype="uint8")


    net = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)
    image = cv2.imread(INPUT_FILE)
    print('print of image readed>>>>')
    print(image)
    # cv2.imshow('image', image)
    (H, W) = image.shape[:2]

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
        swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > CONFIDENCE_THRESHOLD:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD,
        CONFIDENCE_THRESHOLD)
    
    myListOfClassIDs = []
    myListOfConfidences = []
    myListOfLabels = []
    myListOfBoxes = []

    # ensure at least one detection exists
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            color = [int(c) for c in COLORS[classIDs[i]]]

            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.2f}".format(LABELS[classIDs[i]], confidences[i])
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX,
                0.5, color, 2)
            myListOfLabels.append(LABELS[classIDs[i]])
            myListOfConfidences.append(confidences[i])
            myListOfClassIDs.append(classIDs[i])
            newBox = {}
            newBox["x"] = x
            newBox["y"] = y
            newBox["w"] = W
            newBox["h"] = h
            myListOfBoxes.append(newBox)

    # show the output image
    nameOfImage = getNameOfImage(INPUT_FILE)
    pos = getPosOfNameOfImage(nameOfImage)
    print('Displaying pos:' + str(pos))
    newPathOfImage = nameOfImage[:pos]
    newPathOfImage = newPathOfImage + '\\out\\' + nameOfImage[pos:]
    print('NewPathOfImage: ' + newPathOfImage)
    cv2.imwrite(newPathOfImage, image)
    #Writing JSON
    pathJson = newPathOfImage[:len(newPathOfImage) - 4]
    pathJson = pathJson + '.json'
    print('Path of Json: ' + pathJson + " >>>>>")
    
    with open(pathJson, 'w') as json_file:
            print('Printing image for JSON>>>>: ')
            print(image)
            print('Print type of image for JSON>>>>:')
            print(type(image))
            listOfNumpyArray = image.tolist()
            currentFrame = {}
            currentFrame["frame_id"] = 1
            myFileName = newPathOfImage.replace("\\\\", "\\")
            currentFrame["filename"] = myFileName
            objectsDetected = getDetectedObjects(myListOfClassIDs, myListOfBoxes, myListOfConfidences, myListOfLabels)
            currentFrame["objects"] = objectsDetected
            my_json_str = json.dump(currentFrame, json_file)
            json_file.close()

def getDetectedObjects(listOfClassIds, listOfBoxes, listOfConfidences, listOfLabels):
    """Function to get a list of dictionaries representing objects detected"""
    listOfDetectedObjects = []
    i = 0
    for item in listOfConfidences:
        newObject = {}
        newObject["confidence"] = item
        newObject["name"] =  str(listOfLabels[i])
        newObject["class_id"] = str(listOfClassIds[i])
        newRelativeCoordinates = {}
        newRelativeCoordinates["center_x"] = listOfBoxes[i]["x"]
        newRelativeCoordinates["center_y"] = listOfBoxes[i]["y"]
        newRelativeCoordinates["width"] = listOfBoxes[i]["w"]
        newRelativeCoordinates["height"] = listOfBoxes[i]["h"]
        newObject["relative_coordinates"] = newRelativeCoordinates
        listOfDetectedObjects.append(newObject)
        i = i + 1
    return listOfDetectedObjects

def processAutomatizationDarknet(listOfNotProcessedImages):
    """ Function to detect objects in a list of images. Returns the list of processed images. """
    
    basepath = r'C:\\Users\\Normandi\\darknet\\data\\sample_test2'
    
    # Procesar cada imagen y la ubica en la carpeta out con el mismo nombre    
    results = []
    for image in listOfNotProcessedImages:
        newImagePath = basepath + '\\' + image
        results.append(newImagePath)
        print(newImagePath)
        detectObjectsInImage(newImagePath)
    return results

def getListOfActivitiesFromDate(date, directoryOfImages):
    """Function to get a list of activities from all the images of day"""
    files = os.listdir(directoryOfImages)
    listOfActivities = []
    day = date.day()
    month = date.month()
    year = date.year()
    parsedDate = datetime.datetime(year, month, day)
    patternOfSearch = ""
    patternOfSearch += str(year) + parsedDate.strftime("%m") + parsedDate.strftime("%d")
    for item in files:
        if patternOfSearch in item and item.endswith(".json"):
            listOfActivities.extend(getActivitiesFromJSON(item, directoryOfImages))
    return listOfActivities

def getActivitiesFromJSON(jsonFileName, path):
    """Get the activities from a JSON"""
    jsonFilePath = path + '//' + jsonFileName
    with open(jsonFilePath) as json_file:
        data = json.load(json_file)
        listOfObjects = data['objects']
        print(type(listOfObjects))
        listOfActivities = []
        for item in listOfObjects:
            listOfActivities.append(item['name'])
        return listOfActivities

    


def getCountOfItemInList(listOfItems, item):
    """Function to get the count of occurrences of item in listOfItems """
    count = 0
    for currentItem in listOfItems:
        if currentItem == item:
            count += 1
    return count

def moreFrequentActivities(activities):
    #Function to return the more frequent activities in the list of activities
    #TODO To implement (it depends of getListOfActivitiesFromDay)
     
    listOfCounts = []
    listOfDifferentActivities = []
    listOfResults = []
    
    for item in activities:
        if item not in listOfDifferentActivities:
            listOfDifferentActivities.append(item)

    print("Lista Original: ",activities)
    print("Lista Diferente:",listOfDifferentActivities)
    
    """for currentActivity in listOfDifferentActivities:
        listOfCounts.append(getCountOfItemInList(activities, currentActivity))
    """
    i = 0
    for currentActivity in listOfDifferentActivities:
        listOfCounts[i] = getCountOfItemInList(activities, currentActivity)
        i += 1
    nummax = max(listOfCounts)
    
    for i in range(0, len(listOfCounts)):
        if listOfCounts[i] == nummax:
            listOfResults.append(listOfDifferentActivities[i])
    #print('Displaying resultados: ', listOfResults)
    return(listOfResults)

def getNonDetectedActivities(listOfActivities, listOfDifferentActivities):
    """Function to get the list of activities in listOfDifferentActivities that isn't present in listOfActivities"""
    result = []
    for item in listOfDifferentActivities:
        if item not in listOfActivities:
            result.append(item)
    return result

def getTotalOfImages(date):
    """Function to get the number of images of a date(YYYYMMDD)"""
    #TODO To implement


def getNumberOfImagesWithNoDetectedActivities(date):
    """Function to get the number of images with no detected activities from a date(YYYYMMDD)"""
    #TODO To implement

def percentageOfImagesWithNoDetectedActivities(totalOfImages, numberOfImagesWithNoDetectedActivities):
    """Function that returns the percentage of images with no detected activities"""
    percentage = (numberOfImagesWithNoDetectedActivities / totalOfImages) * 100
    return percentage