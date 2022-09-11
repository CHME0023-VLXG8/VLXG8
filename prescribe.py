# Form implementation generated from reading ui file 'prescribe.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_prescribe_dlg(object):
    def setupUi(self, prescribe_dlg):
        prescribe_dlg.setObjectName("prescribe_dlg")
        prescribe_dlg.resize(448, 304)
        self.buttonBox = QtWidgets.QDialogButtonBox(prescribe_dlg)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(prescribe_dlg)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 20, 241, 85))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.medication_label = QtWidgets.QLabel(self.layoutWidget)
        self.medication_label.setObjectName("medication_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.medication_label)
        self.medication_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.medication_edit.setObjectName("medication_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.medication_edit)
        self.dose_label = QtWidgets.QLabel(self.layoutWidget)
        self.dose_label.setObjectName("dose_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dose_label)
        self.dose_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.dose_edit.setObjectName("dose_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dose_edit)
        self.duration_label = QtWidgets.QLabel(self.layoutWidget)
        self.duration_label.setObjectName("duration_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.duration_label)
        self.duration_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.duration_edit.setObjectName("duration_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.duration_edit)
        self.label = QtWidgets.QLabel(prescribe_dlg)
        self.label.setGeometry(QtCore.QRect(29, 140, 301, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(prescribe_dlg)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 341, 51))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.units_comboBox = QtWidgets.QComboBox(prescribe_dlg)
        self.units_comboBox.setGeometry(QtCore.QRect(320, 50, 103, 32))
        self.units_comboBox.setObjectName("units_comboBox")
        self.units_comboBox.addItem("")
        self.units_comboBox.addItem("")
        self.units_comboBox.addItem("")
        self.units_comboBox.addItem("")
        self.units_comboBox.addItem("")

        self.retranslateUi(prescribe_dlg)
        self.buttonBox.accepted.connect(prescribe_dlg.accept) # type: ignore
        self.buttonBox.rejected.connect(prescribe_dlg.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(prescribe_dlg)

    def retranslateUi(self, prescribe_dlg):
        _translate = QtCore.QCoreApplication.translate
        prescribe_dlg.setWindowTitle(_translate("prescribe_dlg", "Prescribe"))
        self.medication_label.setText(_translate("prescribe_dlg", "Medication Name"))
        self.dose_label.setText(_translate("prescribe_dlg", "Dose (units)"))
        self.duration_label.setText(_translate("prescribe_dlg", "Duration (days)"))
        self.label.setText(_translate("prescribe_dlg", "WARNING: CLICKING OK WILL CLOSE THE CASE"))
        self.label_2.setText(_translate("prescribe_dlg", "IF YOU WANT TO RETURN TO THE CASE DETAILS CLICK CANCEL"))
        self.units_comboBox.setItemText(0, _translate("prescribe_dlg", "grams"))
        self.units_comboBox.setItemText(1, _translate("prescribe_dlg", "micrograms"))
        self.units_comboBox.setItemText(2, _translate("prescribe_dlg", "milligrams"))
        self.units_comboBox.setItemText(3, _translate("prescribe_dlg", "mls"))
        self.units_comboBox.setItemText(4, _translate("prescribe_dlg", "units"))