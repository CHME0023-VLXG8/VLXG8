from mongoengine import *
from database import Patient
from cases import Ui_MainWindow
from between_window import Ui_between_window
from within_window import Ui_within_window
from prescribe import Ui_prescribe_dlg
from pmh import Ui_pmh_dlg
from medication import Ui_medication_dlg
from pathology import Ui_pathology_dlg
from bloodpressure import Ui_bp_dlg
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QStyledItemDelegate
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QPoint, QEvent, QAbstractTableModel, Qt, QSortFilterProxyModel, QDateTime, QUrl
from PyQt6 import QtCore
from PyQt6.QtGui import QDesktopServices
import sys
import time
from datetime import datetime
from csv import writer

# Connect to Database holding case histories
db = connect('med_data')
patient1a = Patient.objects(patient_id='1a')[0]
patient1b = Patient.objects(patient_id='1b')[0]
patient2a = Patient.objects(patient_id='2a')[0]
patient2b = Patient.objects(patient_id='2b')[0]
patient3a = Patient.objects(patient_id='3a')[0]
patient3b = Patient.objects(patient_id='3b')[0]

# Declare global variables
# clicks = number of clicks, ui_type = string for UI type used
clicks = 0
ui_type = ''

# Logger function to capture outputs for each user


def logUsage(clicks, filename):
    f = open(filename, "a")
    f.write(f"{clicks}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
    f.close()


def case_logger_csv(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


# Fucntion to catpure mouse events. Taken from: https://stackoverflow.com/questions/59127313/track-mouse-movements-in-several-widgets-at-the-same-time

class MouseListener(QObject):
    posChanged = pyqtSignal(QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self._childrens = []

        self._setup_widget(self._widget)

        for w in self._widget.findChildren(QWidget):
            self._setup_widget(w)
            self._childrens.append(w)

    def _setup_widget(self, w):
        w.installEventFilter(self)
        w.setMouseTracking(True)

    def eventFilter(self, obj, event):
        global clicks
        if obj in [self._widget] + self._childrens and event.type() == QEvent.Type.MouseButtonRelease:
            clicks = clicks + 1
            print(f'{clicks}')

        if event.type() == QEvent.Type.ChildAdded:
            obj = event.child()
            if obj.isWidgetType():
                self._setup_widget(obj)
                self._childrens.append(obj)

        if event.type() == QEvent.Type.ChildRemoved:
            c = event.child()
            if c in self._childrens:
                c.removeEventFilter(self)
                self._childrens.remove(c)
        return super().eventFilter(obj, event)

# Define Cases Selection screen object. Allows passing of the database object (i.e patient1a) to each child window opened.


class Cases(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Cases, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.between_window = None

        self.case1_btn.setText(
            f"{patient1a.name}")
        self.case2_btn.setText(
            f"{patient1b.name}")
        self.case3_btn.setText(
            f"{patient2a.name}")
        self.case4_btn.setText(
            f"{patient2b.name}")
        self.case5_btn.setText(
            f"{patient3a.name}")
        self.case6_btn.setText(
            f"{patient3b.name}")

        # Lamda to push variable
        self.case1_btn.clicked.connect(
            lambda i: self.show_between_windows(i, patient1a))
        self.case2_btn.clicked.connect(
            lambda i: self.show_within_windows(i, patient1b))
        self.case3_btn.clicked.connect(
            lambda i: self.show_between_windows(i, patient2a))
        self.case4_btn.clicked.connect(
            lambda i: self.show_within_windows(i, patient2b))
        self.case5_btn.clicked.connect(
            lambda i: self.show_between_windows(i, patient3a))
        self.case6_btn.clicked.connect(
            lambda i: self.show_within_windows(i, patient3b))

        self.case1_btn.clicked.connect(
            lambda: self.disable_button(self.case1_btn))
        self.case2_btn.clicked.connect(
            lambda: self.disable_button(self.case2_btn))
        self.case3_btn.clicked.connect(
            lambda: self.disable_button(self.case3_btn))
        self.case4_btn.clicked.connect(
            lambda: self.disable_button(self.case4_btn))
        self.case5_btn.clicked.connect(
            lambda: self.disable_button(self.case5_btn))
        self.case6_btn.clicked.connect(
            lambda: self.disable_button(self.case6_btn))
        self.resetButton.clicked.connect(self.reset)

    def disable_button(self, b):
        b.setText('COMPLETED')
        b.setEnabled(False)

    def reset(self):
        self.case1_btn.setEnabled(True)
        self.case2_btn.setEnabled(True)
        self.case3_btn.setEnabled(True)
        self.case4_btn.setEnabled(True)
        self.case5_btn.setEnabled(True)
        self.case6_btn.setEnabled(True)
        self.case1_btn.setText(
            f"{patient1a.name}")
        self.case2_btn.setText(
            f"{patient1b.name}")
        self.case3_btn.setText(
            f"{patient2a.name}")
        self.case4_btn.setText(
            f"{patient2b.name}")
        self.case5_btn.setText(
            f"{patient3a.name}")
        self.case6_btn.setText(
            f"{patient3b.name}")

    @pyqtSlot()
    def show_between_windows(self, checked, patient):
        """Launch the case1 dialog."""
        print(patient.name, patient.age)
        print(self.sender())
        self.between_window = BetweenWindow()
        # sender method to get button name
        self.between_window.ui.patientName.setText(
            f"{patient.name}")
        self.between_window.ui.patientAge.setText(
            f"{patient.age}")
        self.between_window.ui.history_text.setText(
            f'{patient.presenting_complaint}')
        self.between_window.ui.examination_text.setText(
            f'{patient.examination}')
        self.between_window.ui.conclusion_text.setText(
            f'{patient.conclusion}')
        # Pass variable patient to the show_path_dlg function when the pathology_BTN is clicked
        self.between_window.ui.pathology_BTN.clicked.connect(
            lambda i: self.between_window.show_path_dlg(i, patient))
        self.between_window.ui.medication_BTN.clicked.connect(
            lambda i: self.between_window.show_med_dlg(i, patient))
        self.between_window.ui.pastmedicalhistory_BTN.clicked.connect(
            lambda i: self.between_window.show_pmh_dlg(i, patient))
        self.between_window.ui.bloodpressure_BTN.clicked.connect(
            lambda i: self.between_window.show_bp_dlg(i, patient))
        self.between_window.ui.prescribe_BTN.clicked.connect(
            lambda i: self.between_window.show_prescribeWindow(i, patient))
        # start timer and set clicks to 0
        global clicks
        global start
        global ui_type
        clicks = 0
        ui_type = 'between_window'
        start = time.time()
        self.between_window.show()

    @pyqtSlot()
    def show_within_windows(self, checked, patient):
        """Launch the case1 dialog."""
        print(patient.name, patient.age)
        print(self.sender())
        self.within_window = WithinWindow()

        # sender method to get button name
        self.within_window.ui.patientName.setText(
            f"{patient.name}")
        self.within_window.ui.patientAge.setText(
            f"{patient.age}")
        self.within_window.ui.history_text.setText(
            f'{patient.presenting_complaint}')
        self.within_window.ui.examination_text.setText(
            f'{patient.examination}')
        self.within_window.ui.conclusion_text.setText(
            f'{patient.conclusion}')


        # Define each tables model-view

        # PMH Table
        self.within_window.model_pmh = CustomModel(['date', 'condition'])
        self.within_window.model_pmh.datatable = patient.history
        self.within_window.ui.past_medical_history_table.setModel(
            self.within_window.model_pmh)
        # Medication table
        self.within_window.model_medication = CustomModel(
            ['name', 'dose', 'units'])
        self.within_window.model_medication.datatable = patient.medication
        self.within_window.ui.medication_table.setModel(
            self.within_window.model_medication)

        # Pathology table
        self.within_window.model_pathology = CustomModel(
            ['date', 'test_name', 'result', 'units'])
        self.within_window.model_pathology.datatable = patient.pathology
        # Implement this code on other tables to enable sorting by default. Note the between windows path is broken for some reason.
        self.within_window.proxyModel = QSortFilterProxyModel(self)
        self.within_window.proxyModel.setSourceModel(
            self.within_window.model_pathology)
        self.within_window.ui.pathology_table.setModel(
            self.within_window.proxyModel)
        self.within_window.ui.pathology_table.sortByColumn(
            0, Qt.SortOrder.DescendingOrder)
        # Pass variable patient to the show_path_dlg function when the pathology_BTN is clicked
        self.within_window.ui.prescribe_BTN.clicked.connect(
            lambda i: self.within_window.show_prescribeWindow(i, patient))

        # blood pressure table
        self.within_window.model_bp = CustomModel(['date', 'reading'])
        self.within_window.model_bp.datatable = patient.blood_pressure
        self.within_window.ui.bloodpressure_table.setModel(
            self.within_window.model_bp)

        # start timer and set clicks to 0

        global start
        global ui_type
        global clicks
        clicks = 0
        ui_type = 'within_window'
        start = time.time()
        self.within_window.show()


class WithinWindow(QMainWindow, Ui_within_window):
    def __init__(self, parent=None):
        super(WithinWindow, self).__init__(parent)
        self.ui = Ui_within_window()
        self.ui.setupUi(self)
        listener = MouseListener(self)


    def show_prescribeWindow(self, checked, patient):
        """Launch the employee dialog."""

        prescribe_window = Prescribing_Dlg(self, patient=patient)
        prescribe_window.accepted.connect(self.close_window)
        prescribe_window.exec()

    def close_window(self):
        print("signal recieved - withinwindow closed")
        self.close()


class BetweenWindow(QMainWindow, Ui_between_window):
    def __init__(self, parent=None):
        super(BetweenWindow, self).__init__(parent)
        self.ui = Ui_between_window()
        self.ui.setupUi(self)
        listener = MouseListener(self)


    def show_prescribeWindow(self, checked, patient):
        """Launch the employee dialog."""

        prescribe_window = Prescribing_Dlg(self, patient=patient)
        prescribe_window.accepted.connect(self.close_window)
        prescribe_window.exec()

    def show_pmh_dlg(self, checked, patient):
        """Launch the employee dialog."""
        dlg = pmh_dlg(self, patient=patient)
        dlg.exec()

    def show_med_dlg(self, checked, patient):
        """Launch the employee dialog."""
        # accept a patient variable
        dlg = medication_dlg(self, patient=patient)
        dlg.exec()

    def show_path_dlg(self, checked, patient):
        """Launch the employee dialog."""
        # pass patient variable to path_dlg
        dlg = pathology_dlg(self, patient=patient)
        dlg.exec()

    def show_bp_dlg(self, checked, patient):
        """Launch the employee dialog."""
        # pass patient variable to path_dlg
        dlg = bp_dlg(self, patient=patient)
        dlg.exec()

    def close_window(self):
        print("signal recieved - withinwindow closed")
        self.close()


class Prescribing_Dlg(QDialog, Ui_between_window):
    """Prescribing dialog"""

    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        self.ui = Ui_prescribe_dlg()
        self.ui.setupUi(self)
        listener = MouseListener(self)
        self.accepted.connect(lambda: self.onOKBtnClicked(patient))

    def onOKBtnClicked(self, patient):
        # What to do when ok button clicked. 
        print(patient.name)
        medication = self.ui.medication_edit.text()
        dose = self.ui.dose_edit.text()
        units = self.ui.units_comboBox.currentText()
        duration = self.ui.duration_edit.text()

        #End timer
        global start
        global end
        global ui_type
        end = time.time()
        time_to_task = end - start
        time_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        #Log relevant outputs to csv file for results
        case_logger_csv('experiment.csv', [ui_type, time_now, patient.patient_id, patient.case_pair, patient.name, medication, dose, units,
                        duration, clicks, time_to_task])
        'save output to csv'


class pmh_dlg(QDialog, Ui_pmh_dlg):
    """Employee dialog."""

    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_pmh_dlg()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.model = CustomModel(['date', 'condition'])
        self.model.datatable = patient.history
        self.ui.past_medical_history_table.setModel(self.model)


class medication_dlg(QDialog, Ui_medication_dlg):
    """Employee dialog."""
    # accept patient varible

    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_medication_dlg()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.model = CustomModel(['name', 'dose', 'units'])
        self.model.datatable = patient.medication
        self.ui.medication_table.setModel(self.model)


class pathology_dlg(QDialog, Ui_pathology_dlg):
    """Employee dialog."""

    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_pathology_dlg()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.model = CustomModel(['date', 'test_name', 'result', 'units'])
        self.model.datatable = patient.pathology
        self.ui.pathology_table.setModel(self.model)


class bp_dlg(QDialog, Ui_bp_dlg):
    """Employee dialog."""

    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_bp_dlg()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.model = CustomModel(['date', 'reading'])
        self.model.datatable = patient.blood_pressure
        self.ui.bloodpressure_table.setModel(self.model)

# Database model to read mongoDB database and create QT object
class CustomModel(QtCore.QAbstractTableModel):
    def __init__(self, columns, parent=None):
        super(CustomModel, self).__init__(parent)
        self.columns = columns
        self.datatable = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.datatable)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.columns)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.columns[section].title()

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = self.datatable[index.row()]
            column_key = self.columns[index.column()]
            value = row[column_key]
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                value = value.strftime('%Y-%m-%d')
                # value = value.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
                return value
            return value
        else:
            return None


app = QApplication(sys.argv)


w = Cases()


w.show()


app.exec()

# start console logging function
logUsage(clicks, 'log.text')
print(clicks)
