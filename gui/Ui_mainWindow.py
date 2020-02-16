# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Alumno\Desktop\PythonExample2\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_aboutDialog import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.photosTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.photosTableWidget.setGeometry(QtCore.QRect(20, 40, 551, 251))
        self.photosTableWidget.setObjectName("photosTableWidget")
        self.photosTableWidget.setColumnCount(2)
        self.photosTableWidget.setRowCount(3)
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
        self.actionCargar_fotos = QtWidgets.QAction(MainWindow)
        self.actionCargar_fotos.setObjectName("actionCargar_fotos")
        self.menuArchivo.addAction(self.actionTomar_fotos)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCargar_fotos)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.showAbout)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        data = {
        'Imagen':['20190219-18h00','20190219-18h05','20190219-18h10'], '% procesamiento':['100%','80%','0%']}
        horHeaders = []
        for n, key in enumerate(data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QtWidgets.QTableWidgetItem(item)
                self.photosTableWidget.setItem(m, n, newitem)
        self.photosTableWidget.setHorizontalHeaderLabels(horHeaders)
        self.photosTableWidget.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermal Comfort 1.0"))
        self.pushButton.setText(_translate("MainWindow", "Say Hello"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionTomar_fotos.setText(_translate("MainWindow", "Tomar fotos"))
        self.actionCargar_fotos.setText(_translate("MainWindow", "Cargar fotos"))

    def showAbout(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
       

   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
