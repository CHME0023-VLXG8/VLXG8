# Form implementation generated from reading ui file 'pathology.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_pathology_dlg(object):
    def setupUi(self, pathology_dlg):
        pathology_dlg.setObjectName("pathology_dlg")
        pathology_dlg.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(pathology_dlg)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pathology_table = QtWidgets.QTableView(pathology_dlg)
        self.pathology_table.setGeometry(QtCore.QRect(10, 40, 381, 191))
        self.pathology_table.setSortingEnabled(True)
        self.pathology_table.setObjectName("pathology_table")
        self.pathology_label = QtWidgets.QLabel(pathology_dlg)
        self.pathology_label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.pathology_label.setObjectName("pathology_label")

        self.retranslateUi(pathology_dlg)
        self.buttonBox.accepted.connect(pathology_dlg.accept) # type: ignore
        self.buttonBox.rejected.connect(pathology_dlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(pathology_dlg)

    def retranslateUi(self, pathology_dlg):
        _translate = QtCore.QCoreApplication.translate
        pathology_dlg.setWindowTitle(_translate("pathology_dlg", "Dialog"))
        self.pathology_label.setText(_translate("pathology_dlg", "Pathology"))