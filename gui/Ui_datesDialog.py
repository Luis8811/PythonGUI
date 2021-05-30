# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Alumno\Desktop\tfmcodeluis\PythonGUI\gui\datesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime

class Ui_datesDialog(object):
    def setupUi(self, datesDialog):
        datesDialog.setObjectName("datesDialog")
        datesDialog.resize(400, 300)
        datesDialog.setModal(True)
        self.widget = QtWidgets.QWidget(datesDialog)
        self.widget.setGeometry(QtCore.QRect(40, 20, 300, 242))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
        self.verticalLayout.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.okButtonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.okButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.okButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okButtonBox.setObjectName("okButtonBox")
        self.verticalLayout_2.addWidget(self.okButtonBox)
        self.calendarWidget.selectionChanged.connect(self.changedDate)
        self.dateEdit.dateChanged.connect(self.changeDateInCalendar)
        datesDialog.setLayout(self.verticalLayout_2)
        self.retranslateUi(datesDialog)
        self.okButtonBox.accepted.connect(datesDialog.accept)
        self.okButtonBox.rejected.connect(datesDialog.reject)
        

        QtCore.QMetaObject.connectSlotsByName(datesDialog)
        
    def retranslateUi(self, datesDialog):
        _translate = QtCore.QCoreApplication.translate
        datesDialog.setWindowTitle(_translate("datesDialog", "Seleccionar imágenes de fecha"))
    
    def changedDate(self):
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
    
    def changeDateInCalendar(self):
       date = self.dateEdit.date()
       self.calendarWidget.setSelectedDate(date)

    def getSelectedDate(self):
        return self.dateEdit.date()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    datesDialog = QtWidgets.QDialog()
    ui = Ui_datesDialog()
    ui.setupUi(datesDialog)
    datesDialog.show()
    sys.exit(app.exec_())
