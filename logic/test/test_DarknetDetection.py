import sys, os
sys.path.append('C:\\Users\\Normandi\\darknet\\ThermalComfortGUI\\PythonGUI\\logic\\darknet')
import detection
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
import datetime
# TESTING 
listOfFiles = detection.readDirectoryOfImages()
listOfProcessed = detection.readDirectoryOfProcessedImages()
print("Not processed")
listOfNotProcessedImages= detection.processImages(listOfFiles, listOfProcessed)
print("Processing not processed images...")
detection.processAutomatizationDarknet(listOfNotProcessedImages)
print('Testing activities from date')
pathOfJsons = 'C:\\Users\\Normandi\\darknet\\data\\sample_test2\\out'
date = QDate(2020, 10, 13)
listOfActivitiesOnDate = detection.getListOfActivitiesFromDate(date, pathOfJsons)
print("Actividades en una fecha: ")
print(listOfActivitiesOnDate)
