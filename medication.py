# Form implementation generated from reading ui file 'medication.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_medication_dlg(object):
    def setupUi(self, medication_dlg):
        medication_dlg.setObjectName("medication_dlg")
        medication_dlg.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(medication_dlg)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.medication_label = QtWidgets.QLabel(medication_dlg)
        self.medication_label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.medication_label.setObjectName("medication_label")
        self.medication_table = QtWidgets.QTableView(medication_dlg)
        self.medication_table.setGeometry(QtCore.QRect(10, 30, 381, 141))
        self.medication_table.setSortingEnabled(False)
        self.medication_table.setObjectName("medication_table")
        self.allergy_textBrowser = QtWidgets.QTextBrowser(medication_dlg)
        self.allergy_textBrowser.setGeometry(QtCore.QRect(10, 170, 381, 41))
        self.allergy_textBrowser.setObjectName("allergy_textBrowser")

        self.retranslateUi(medication_dlg)
        self.buttonBox.accepted.connect(medication_dlg.accept) # type: ignore
        self.buttonBox.rejected.connect(medication_dlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(medication_dlg)

    def retranslateUi(self, medication_dlg):
        _translate = QtCore.QCoreApplication.translate
        medication_dlg.setWindowTitle(_translate("medication_dlg", "Dialog"))
        self.medication_label.setText(_translate("medication_dlg", "Medication"))
        self.allergy_textBrowser.setHtml(_translate("medication_dlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">NO KNOWN DRUG ALLERGIES</span></p></body></html>"))
