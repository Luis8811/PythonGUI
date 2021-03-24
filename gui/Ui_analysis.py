# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Normandi\Desktop\codeGUI\TFM\gui\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'logic'))


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from detection import Detection

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.originalImageLabel = QtWidgets.QLabel(Dialog)
        self.originalImageLabel.setGeometry(QtCore.QRect(40, 50, 300, 200))
        self.originalImageLabel.setText("")
        self.originalImageLabel.setStyleSheet("background-color: white")
        self.originalImageLabel.setObjectName("originalImageLabel")
        
        self.titleOriginalImageLabel = QtWidgets.QLabel(Dialog)
        self.titleOriginalImageLabel.setGeometry(QtCore.QRect(40, -35, 201, 121))
        self.titleOriginalImageLabel.setText("Imagen Original")
        self.titleOriginalImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleOriginalImageLabel.setFont(QtGui.QFont("Arial",14,QtGui.QFont.Bold))
        self.originalImageLabel.setObjectName("titleOriginalImageLabel")

        self.ResultTableWidget = QtWidgets.QTableWidget(Dialog)
        self.ResultTableWidget.setGeometry(QtCore.QRect(200, 270, 290, 161))
        self.ResultTableWidget.setObjectName("ResultTableWidget")
        self.ResultTableWidget.setColumnCount(2)
        self.ResultTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTableWidget.setHorizontalHeaderItem(1, item)
        
        self.processedImageLabel = QtWidgets.QLabel(Dialog)
        self.processedImageLabel.setGeometry(QtCore.QRect(370, 50, 300, 200))
        self.processedImageLabel.setText("")
        self.processedImageLabel.setObjectName("processedImageLabel")
        self.processedImageLabel.setStyleSheet("background-color: white")
        
        self.titleProcessedImageLabel = QtWidgets.QLabel(Dialog)
        self.titleProcessedImageLabel.setGeometry(QtCore.QRect(290, -35, 201, 121))
        self.titleProcessedImageLabel.setText("Imagen Procesada")
        self.titleProcessedImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleProcessedImageLabel.setFont(QtGui.QFont("Arial",14,QtGui.QFont.Bold))
        self.titleProcessedImageLabel.setObjectName("titleOriginalImageLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setImage(self, imageName):
        originalImagesDirectory = 'C:\\Users\\Luis\\Desktop\\images'
        processedImagesDirectory ='C:\\Users\\Luis\\Desktop\\processedImages'
        self.imageName = imageName
        print('Nombre Imagen>>>>>>',self.imageName)
        original = ''
        original += originalImagesDirectory +'\\' + imageName
        processed = ''
        processed += processedImagesDirectory + '\\' + imageName
        pixmaporig= QPixmap(original).scaled(300,200)
        self.originalImageLabel.setPixmap(pixmaporig)
        pixmapprocess= QPixmap(processed).scaled(300,200)
        self.processedImageLabel.setPixmap(pixmapprocess)
        self.processedImagePath = processed
        self.loadResults()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Resultado Imágenes"))
        item = self.ResultTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Actividad Realizada"))
        item = self.ResultTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tasa Metabólica (met)"))
        
        
        for indice, ancho in enumerate((150, 130), start=0):
            self.ResultTableWidget.setColumnWidth(indice,ancho)


   
    # Displays results of processed image
    def loadResults(self):
        imageProcessed = Detection.parseProcessedImage(self.getPathOfProcessedImage())
        a = Detection()
        activities = a.detectActivities(imageProcessed)
        i = 0
        instanceOfDetection = Detection()
        for item in activities:
            self.ResultTableWidget.insertRow(i)
            currentItem = QtWidgets.QTableWidgetItem(instanceOfDetection.getNameOfActivity(item))
            currentItemValue = QtWidgets.QTableWidgetItem(str(item.value))
            print(currentItemValue)
            self.ResultTableWidget.setItem(i, 0, currentItem)
            self.ResultTableWidget.setItem(i, 1, currentItemValue)
            i += 1


    # Returns the path of the processed image displayed
    def getPathOfProcessedImage(self):
        return self.processedImagePath




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
