# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Alumno\Desktop\PythonExample2\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,  QMainWindow, QAction
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from Ui_aboutDialog import Ui_AboutDialog
from Ui_datesDialog import Ui_datesDialog
from Ui_analysis import Ui_Dialog
from logic.detection import Detection

import cv2
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.photosTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.photosTableWidget.setGeometry(QtCore.QRect(90, 30, 351, 251))
        self.photosTableWidget.setObjectName("photosTableWidget")
        self.photosTableWidget.setColumnCount(2)
        self.photosTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.photosTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.photosTableWidget.setHorizontalHeaderItem(1, item)

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
        self.menuArchivo.addAction(self.actionTomar_fotos)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCargar_fotos)
        self.actionAcerca_de = QAction(QIcon('ojo.png'), 'Ayuda', MainWindow)
        self.actionAcerca_de.setShortcut('Ctrl+Q')
        self.actionAcerca_de.setStatusTip('Muestra la ayuda')
        self.actionAcerca_de.triggered.connect(self.showHelp)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getDataFromSelectedRow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ''' data = {
        'Imagen':['20190219-18h00','20190219-18h05','20190219-18h10'], '% procesamiento':['100%','80%','0%']}
        horHeaders = []
        for n, key in enumerate(data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QtWidgets.QTableWidgetItem(item)
                self.photosTableWidget.setItem(m, n, newitem)
        self.photosTableWidget.setHorizontalHeaderLabels(horHeaders)
        self.photosTableWidget.show() '''
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermal Comfort 1.2"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        item = self.photosTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Imagen Name"))
        item = self.photosTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "% Processing"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Ayuda"))
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
        files = os.listdir('C:\\Users\\Normandi\\Desktop\\images')
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
            image = QIcon("202006201830.jpg")
            currentImageName = QtWidgets.QTableWidgetItem(image, item)
            # self.photosTableWidget.setRowHeight()
            pixmap = QtGui.QPixmap("202006201830.jpg")
            labelImg = QtWidgets.QLabel()
            labelImg.setPixmap(pixmap)
            self.photosTableWidget.setItem(i, 0, currentImageName)
            self.photosTableWidget.setCellWidget(i, 1, labelImg)
            self.photosTableWidget.scrollToItem(self.photosTableWidget.itemAt(i, 1))
            i+=1

    def getDataFromSelectedRow(self):
        selectedRow = self.photosTableWidget.currentRow()
        print('Displaying selected row>>>>>')
        print(selectedRow)
        imageName = self.photosTableWidget.item(selectedRow, 0).text()
        #percentage = self.photosTableWidget.item(selectedRow, 1).text()
        self.showResultAnalysis(imageName)

    def takePhotos(self):
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
                if key == ord('s'):
                    cv2.imwrite('saved_img'+str(i)+'.jpg', frame)
                    i += 1
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
