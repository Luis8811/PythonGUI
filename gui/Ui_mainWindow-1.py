# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Normandi\Desktop\codeGUI\TFM\gui\mainWindow-1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 564)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermal Comfort 1.0"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        item = self.photosTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Imagen Name"))
        item = self.photosTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "% Processing"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionTomar_fotos.setText(_translate("MainWindow", "Tomar fotos"))
        self.actionCargar_fotos.setText(_translate("MainWindow", "Cargar fotos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
