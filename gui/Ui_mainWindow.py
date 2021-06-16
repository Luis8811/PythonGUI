# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Django y Python\Python_code\GUI_TFM_Normandi\PythonGUI\gui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,  QMainWindow, QAction, QHeaderView
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon, QFont
import datetime
from Ui_aboutDialog import Ui_AboutDialog
from Ui_datesDialog import Ui_datesDialog
from Ui_analysis import Ui_Dialog
import cv2
import sys, os, subprocess
sys.path.append('D:\\Back-end\\Django y Python\\Python_code\\Thermal_comfort\\PythonGUI\\logic\\darknet')
import detection
import threading
import time


class Ui_MainWindow(object):
    #TODO To fix design
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.waitForTakePhotos = False
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #TODO Modificar Logo
        self.logo = QtWidgets.QLabel(MainWindow)
        #self.pixmap = QtGui.QPixmap('PythonGUI\\images\\logo.png')
        #self.pixmapAspect = self.pixmap.scaled(800, 106, Qt.KeepAspectRatio, Qt.FastTransformation)
        #self.logo.setPixmap(self.pixmapAspect)
        #self.setAlignment(Qt.AlignCenter)
        self.logo.setText("Metabolic Rate")
        self.logoFont = QFont('Arial', 36)
        self.logoFont.setBold(True)
        self.logo.setFont(self.logoFont)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setStyleSheet("background-color: DodgerBlue; border: 1px double LightSkyBlue; color: white;")
        #TODO End Modificar Logo
        self.dateLabel = QtWidgets.QLabel(MainWindow)
        self.dateLabel.setText("Fecha de las imágenes: ")
        self.countOfImagesLabel = QtWidgets.QLabel(MainWindow)
        self.countOfImagesLabel.setText("Cantidad de imágenes: ")
        self.moreFrequentActivitiesLabel = QtWidgets.QLabel(MainWindow)
        self.moreFrequentActivitiesLabel.setText("Actividades más frecuentes detectadas: ")
        self.nonDetectedActivitiesLabel = QtWidgets.QLabel(MainWindow)
        self.nonDetectedActivitiesLabel.setText("Actividades no detectadas: ")
        self.percentageOfImagesWithNoDetectedActivitiesLabel = QtWidgets.QLabel(MainWindow)
        self.percentageOfImagesWithNoDetectedActivitiesLabel.setText("% de imágenes en las que no se detectó actividad:")
        self.averageOfDetectedActivitiesLabel = QtWidgets.QLabel(MainWindow)
        self.averageOfDetectedActivitiesLabel.setText("Promedio de actividades detectadas: ")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.photosTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.photosTableWidget.setObjectName("photosTableWidget")
        self.photosTableWidget.setColumnCount(2)
        self.photosTableWidget.setHorizontalHeaderLabels(['Hora', 'Imagen'])
        self.photosTableWidget.setRowCount(0)
        self.photosTableWidget.horizontalHeader().setStretchLastSection(True)
        self.photosTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.gridLayout.addWidget(self.logo, 0, 0, 2, 2)
        self.gridLayout.addWidget(self.dateLabel, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.countOfImagesLabel, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.moreFrequentActivitiesLabel, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.nonDetectedActivitiesLabel, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.percentageOfImagesWithNoDetectedActivitiesLabel, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.averageOfDetectedActivitiesLabel, 8, 0, 1, 1)       
        self.gridLayout.addWidget(self.photosTableWidget, 9, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionTomar_fotos = QtWidgets.QAction(MainWindow)
        self.actionTomar_fotos.setObjectName("actionTomar_fotos")
        self.actionTomar_fotos.triggered.connect(self.takePhotos)
        self.actionTomar_fotos.setStatusTip('Permite tomar fotos manualmente')
        self.actionTomar_fotos_auto = QtWidgets.QAction(MainWindow)
        self.actionTomar_fotos_auto.setObjectName("actionTomar_fotos_auto")
        self.actionTomar_fotos_auto.setStatusTip('Toma fotos cada 5 minutos')
        self.actionTomar_fotos_auto.triggered.connect(self.takePhotosAuto)
        self.actionCargar_fotos = QtWidgets.QAction(MainWindow)
        self.actionCargar_fotos.setObjectName("actionCargar_fotos")
        self.actionCargar_fotos = QAction('Cargar fotos', MainWindow)
        self.actionCargar_fotos.setShortcut('Ctrl+L')
        self.actionCargar_fotos.setStatusTip('Seleccionar las fotos a cargar')
        self.actionCargar_fotos.triggered.connect(self.selectDateRange)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionTomar_fotos)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionTomar_fotos_auto)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCargar_fotos)
        self.actionAcerca_de = QAction(QIcon('images\\ojo.png'), 'Ayuda', MainWindow)
        self.actionAcerca_de.setShortcut('Ctrl+Q')
        self.actionAcerca_de.setStatusTip('Muestra la ayuda')
        self.actionAcerca_de.triggered.connect(self.showHelp)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getDataFromSelectedRow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Metabolic rate for office activities 1.0"))
        self.pushButton.setText(_translate("MainWindow", "Procesar imagen"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionTomar_fotos.setText(_translate("MainWindow", "Tomar fotos manualmente"))
        self.actionTomar_fotos_auto.setText(_translate("MainWindow", "Tomar fotos automáticamente"))
        self.actionCargar_fotos.setText(_translate("MainWindow", "Cargar fotos"))
    
    def selectDateRange(self):
        print('Calling selectDateRange>>>>')
        dialog = Dialog(MainWindow)
        ui = Ui_datesDialog()
        ui.setupUi(dialog)
        dialog.show()
        rsp = dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            print('OK was pressed')
            print(ui.getSelectedDate())
            files = self.readDirectory(ui.getSelectedDate())
            self.loadNamesOfImagesFromDirectory(files)

        if rsp == QtWidgets.QDialog.Rejected:
            print('Cancel was pressed')
    
    def showHelp(self):
        print('Calling showHelp>>>>>>>>>>>>')
        #dialog = Dialog(MainWindow)
        #about = Ui_AboutDialog()
        #about.setupUi(dialog)
        result = subprocess.Popen("D:\\Back-end\\Django y Python\\Python_code\\Thermal_comfort\\User_guide\\tfm.chm", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output,error = result.communicate()
        print(output)
        #dialog.show()
        #rsp = dialog.exec_()

    def readDirectory(self, date):
        files = os.listdir('C:\\Users\\Luis\\darknet\\data\\sample_test2')
        filteredFiles = []
        day = date.day()
        month = date.month()
        year = date.year()
        parsedDate = datetime.datetime(year, month, day)
        patternOfSearch = ""
        patternOfSearch += str(year) + parsedDate.strftime("%m") + parsedDate.strftime("%d")
        print('Displaying patternOfSearch: ' + patternOfSearch)
        cont=0
        for item in files:
            if patternOfSearch in item:
                filteredFiles.append(item)
                cont +=1
        countOfImages = "Cantidad de imágenes: " + str(cont)
        self.countOfImagesLabel.setText(countOfImages)
                
        self.photosTableWidget.setRowCount(cont)
        print('Displaying filtered files:')
        print(filteredFiles)
        newDate ="Fecha de las imágenes: "  + parsedDate.strftime("%d") + "/" + parsedDate.strftime("%m") + "/" + str(year)
        self.dateLabel.setText(newDate)
        listOfMoreFrequentActivities = detection.getListOfMoreFrequentActivitiesInDate(date, detection.getPathOfProcessedImages())
        moreFrequentActivitiesLabel = 'Actividades más frecuentes detectadas: ' + self.parseToStr(listOfMoreFrequentActivities)
        self.moreFrequentActivitiesLabel.setText(moreFrequentActivitiesLabel)
        listOfNonDetectedActivities = detection.getNonDetectedActivitiesInDate(date)
        nonDetectedActivitiesLabel = "Actividades no detectadas: " + self.parseToStr(listOfNonDetectedActivities)
        self.nonDetectedActivitiesLabel.setText(nonDetectedActivitiesLabel)
        percentageOfImagesWithNoDetectedActivities = "% de imágenes en las que no se detectó actividad:"
        valueOfPercentageOfImagesWithNoDetectedActivities = detection.percentageOfImagesWithNoDetectedActivities(date)
        percentageOfImagesWithNoDetectedActivities += ' ' + str(valueOfPercentageOfImagesWithNoDetectedActivities)
        self.percentageOfImagesWithNoDetectedActivitiesLabel.setText(percentageOfImagesWithNoDetectedActivities)
        averageOfDetectedActivities = "Promedio de actividades detectadas: "
        valueOfAverageOfDetectedActivities = detection.averageOfDetectedActivities(date)
        averageOfDetectedActivities += str(valueOfAverageOfDetectedActivities)
        self.averageOfDetectedActivitiesLabel.setText(averageOfDetectedActivities)
        return filteredFiles
    
    def parseToStr(self, list):
        """Returns a string that is a representation of all the items in list"""
        strRepresentation = ', '.join(list)
        return strRepresentation

    def loadNamesOfImagesFromDirectory(self, images):
        self.photosTableWidget.setRowHeight(0, 340)
        i = 0
        for item in images:
            image = QIcon("202103261640.jpg")
            hourOfImage = item[8:10]
            minutesOfImage = item[10:12]
            timeOfImage = hourOfImage + ":" + minutesOfImage 
            currentImageName = QtWidgets.QTableWidgetItem(image, timeOfImage)
            currentImageName.setTextAlignment(Qt.AlignCenter)
            dirImg = 'C:\\Users\\Luis\\darknet\\data\\sample_test2\\' + item
            pixmap = QtGui.QPixmap(dirImg)
            pixmapAspect = pixmap.scaled(180, 300, Qt.KeepAspectRatio, Qt.FastTransformation)
            labelImg = QtWidgets.QLabel()
            labelImg.setPixmap(pixmapAspect)
            labelImg.setAlignment(Qt.AlignCenter)
            self.photosTableWidget.setItem(i, 0, currentImageName)
            self.photosTableWidget.setCellWidget(i, 1, labelImg)
            self.photosTableWidget.scrollToItem(self.photosTableWidget.itemAt(i, 1))
            self.photosTableWidget.setRowHeight(i, 420)
            self.photosTableWidget.setColumnWidth(1, 200)
            i+=1
    
    def getDataFromSelectedRow(self):
        selectedRow = self.photosTableWidget.currentRow()
        print('Displaying selected row>>>>>')
        print(selectedRow)
        #TODO
        if selectedRow != -1 :
            imageName = self.photosTableWidget.item(selectedRow, 0).text()
            text = self.dateLabel.text()
            posOfDate = text.find(": ")
            day = text[posOfDate + 1 + 1: posOfDate + 1 + 3]
            month = text[posOfDate + 1 + 4: posOfDate + 1  + 6]
            year = text[posOfDate + 7:]
            newImageName = year + month + day + imageName[0:2] + imageName[3:] + '.jpg'
            self.showResultAnalysis(newImageName)
        else:
            print("Seleccione una imagen")
        #TOEND
    def takePhotos(self):
        """Function to take photos manually"""
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        i = 0
        while True:
            try:
                check, frame = webcam.read()
                #print(check) #prints true as long as the webcam is running
                #print(frame) #prints matrix values of each framecd
                cv2.imshow("Capturing Image", frame) 
                key = cv2.waitKey(1)
                x = datetime.datetime.now()
                strDate = x.strftime("%Y%m%d%H%M")
                if key == ord('s'):
                    pathOfNewImage = 'C:\\Users\\Luis\\darknet\\data\\sample_test2\\'+ strDate + '.jpg'
                    cv2.imwrite(pathOfNewImage, frame)
                    imageName = strDate + '.jpg'
                    detection.processAutomatizationDarknet([imageName])
                    
                elif key == ord('q'):
                    #print("Turning off camera.")
                    webcam.release()
                    #print("Camera off.")
                    #print("Program ended.")
                    cv2.destroyAllWindows()
                    break
            except(KeyboardInterrupt):
                #print("Turning off camera.")
                webcam.release()
                #print("Camera off.")
                #print("Program ended.")
                cv2.destroyAllWindows()
                break
        #print("Turning off camera.")
        webcam.release()
        #print("Camera off.")
        #print("Program ended.")
        cv2.destroyAllWindows()
    
    def takePhotosAuto(self):
        """Function to take photos every 5 minutes"""
        process = threading.Thread(target=self.takePhotoWithoutConfirmation, daemon=True)
        if self.waitForTakePhotos == False:
            self.waitForTakePhotos = True
            process.start()
            self.actionTomar_fotos_auto.setText("Detener toma de fotos automáticamente")
        else:
            self.waitForTakePhotos = True
            self.actionTomar_fotos_auto.setText("Tomar fotos automáticamente")
    
    def closeEvent(self, event):
        self.waitForTakePhotos = False
        self.close()
        sys.exit()

   
    def takePhotoWithoutConfirmation(self):
        """Function to take a photo without the confirmation of the user"""
        print("Function takePhotoWithoutConfirmation:>>>>")
        while self.waitForTakePhotos == True:
            
            print('Value of self.WaitForTakePhotos: ' + str(self.waitForTakePhotos) + ' >>>>')
            
            try:
                webcam = cv2.VideoCapture(0)
                check, frame = webcam.read()
                #print(check) #prints true as long as the webcam is running
                #print(frame) #prints matrix values of each framecd
                time.sleep(30)
                cv2.imshow("Capturing Image", frame)
                x = datetime.datetime.now()
                strDate = x.strftime("%Y%m%d%H%M")
                print("Fecha y hora actual:>>>>")
                print(strDate)
                pathOfNewImage = 'C:\\Users\\Luis\\darknet\\data\\sample_test2\\'+ strDate + '.jpg'
                cv2.imwrite(pathOfNewImage, frame)
                imageName = strDate + '.jpg'
                detection.processAutomatizationDarknet([imageName])
                #print("Turning off camera.")
                webcam.release()
                #print("Camera off.")
                #print("Program ended.")
                cv2.destroyAllWindows()
            except(KeyboardInterrupt):
                #print("Turning off camera.")
                webcam.release()
                #print("Camera off.")
                #print("Program ended.")
                cv2.destroyAllWindows()

    def showResultAnalysis(self, imageName):
        print('Calling showResultAnalysis>>>>>>>>>>>>')
        dialog = Dialog(MainWindow)
        about = Ui_Dialog()
        about.setupUi(dialog)
        about.setImage(imageName)
        dialog.show()

class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
