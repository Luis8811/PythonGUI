import sys, os
sys.path.append('C:\\Users\\Normandi\\darknet\\ThermalComfortGUI\\PythonGUI\\logic\\darknet')
import detection
# TESTING 
listOfFiles = detection.readDirectoryOfImages()
listOfProcessed = detection.readDirectoryOfProcessedImages()
print("Not processed")
listOfNotProcessedImages= detection.processImages(listOfFiles, listOfProcessed)
print("Processing not processed images...")
detection.processAutomatizationDarknet(listOfNotProcessedImages)