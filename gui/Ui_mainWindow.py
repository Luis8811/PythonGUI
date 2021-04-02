# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Django y Python\Python_code\GUI_TFM_Normandi\PythonGUI\gui\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,  QMainWindow, QAction, QHeaderView
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon
import datetime
from Ui_aboutDialog import Ui_AboutDialog
from Ui_datesDialog import Ui_datesDialog
from Ui_analysis import Ui_Dialog
import cv2
import sys, os
sys.path.append('C:\\Users\\Normandi\\darknet\\ThermalComfortGUI\\PythonGUI\\logic\\darknet')
import detection


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.photosTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.photosTableWidget.setObjectName("photosTableWidget")
        self.photosTableWidget.setColumnCount(2)
        self.photosTableWidget.setHorizontalHeaderLabels(['Fecha/hora', 'Imagen'])
        self.photosTableWidget.setRowCount(0)
        self.photosTableWidget.horizontalHeader().setStretchLastSection(True)
        self.photosTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        self.gridLayout.addWidget(self.photosTableWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
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
        self.actionCargar_fotos = QtWidgets.QAction(MainWindow)
        self.actionCargar_fotos.setObjectName("actionCargar_fotos")
        self.actionCargar_fotos = QAction('Cargar fotos', MainWindow)
        self.actionCargar_fotos.setShortcut('Ctrl+L')
        self.actionCargar_fotos.setStatusTip('Seleccionar las fotos a cargar')
        self.actionCargar_fotos.triggered.connect(self.selectDateRange)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionTomar_fotos)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermal Comfort 1.0"))
        self.pushButton.setText(_translate("MainWindow", "Procesar imagen"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionTomar_fotos.setText(_translate("MainWindow", "Tomar fotos"))
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
        dialog = Dialog(MainWindow)
        about = Ui_AboutDialog()
        about.setupUi(dialog)
        dialog.show()
        rsp = dialog.exec_()

    def readDirectory(self, date):
        files = os.listdir('C:\\Users\\Normandi\\darknet\\data\\sample_test2')
        filteredFiles = []
        day = date.day()
        month = date.month()
        year = date.year()
        
        patternOfSearch = ""
        patternOfSearch += str(year) + str(month) + str(day)
        print('Displaying patternOfSearch: ' + patternOfSearch)
        cont=0
        for item in files:
            if patternOfSearch in item:
                filteredFiles.append(item)
                cont +=1
                
        self.photosTableWidget.setRowCount(cont)
        print('Displaying filtered files:')
        print(filteredFiles)
                
        return filteredFiles

    def loadNamesOfImagesFromDirectory(self, images):
        self.photosTableWidget.setRowHeight(0, 340)
        i = 0
        for item in images:
            image = QIcon("202103261640.jpg")
            currentImageName = QtWidgets.QTableWidgetItem(image, item)
            dirImg = 'C:\\Users\\Normandi\\darknet\\data\\sample_test2\\' + item
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
        imageName = self.photosTableWidget.item(selectedRow, 0).text()
        print('Displaying imageName>>>>')
        print(imageName)
        #percentage = self.photosTableWidget.item(selectedRow, 1).text()
        self.showResultAnalysis(imageName)

    def takePhotos(self):
        """Function to take photos"""
        #TODO Fix to save images and jsons related
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        i = 0
        while True:
            try:
                check, frame = webcam.read()
                print(check) #prints true as long as the webcam is running
                print(frame) #prints matrix values of each framecd
                cv2.imshow("Capturing Image", frame) 
                key = cv2.waitKey(1)
                x = datetime.datetime.now()
                strDate = x.strftime("%Y%m%d%H%M")
                if key == ord('s'):
                    pathOfNewImage = 'C:\\Users\\Normandi\\darknet\\data\\sample_test2\\'+ strDate + '.jpg'
                    cv2.imwrite(pathOfNewImage, frame)
                    imageName = strDate + '.jpg'
                    detection.processAutomatizationDarknet([imageName])
                    
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break
            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
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
