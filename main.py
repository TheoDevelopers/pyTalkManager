#!/usr/bin/env python3

import pyTalkManager as tm
from PySide import QtGui
from db import DB
from congregation import Congregation
import sys

# Importation of GUIs
import gui.MainWindow
import gui.DatabaseWindow
import gui.BrotherWindow
import gui.AddBrotherWindow
import gui.CongregationWindow


class MainWindow(QtGui.QMainWindow, gui.MainWindow.Ui_MainWindow):
    """The main window of pyTalkManager.

    From MainWindow all functions of pyTalkManager is accessed by the end user.

    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        tm.firstRunCheck()

        # Tool bar actions
        self.actionDatabase.triggered.connect(self.show_database_window)
        self.actionBrothers.triggered.connect(self.show_brother_window)
        self.actionCongregation.triggered.connect(self.show_congregation_window)

    def show_database_window(self):
        """Method that calls the Database Window"""

        self.db_window = DatabaseWindow()
        self.db_window.show()

    def show_brother_window(self):
        """Method that calls the Brother Window"""

        self.bro_window = BrotherWindow()
        self.bro_window.show()

    def show_congregation_window(self):
        """Method that calls the Congregation Window"""

        self.congregation_window = CongregationWindow()
        self.congregation_window.show()


class DatabaseWindow(QtGui.QDialog, gui.DatabaseWindow.Ui_DatabaseWindow):
    """Window for end user to manage pyTalkManager's database"""

    def __init__(self, parent=None):
        super(DatabaseWindow, self).__init__(parent)
        self.setupUi(self)


class BrotherWindow(QtGui.QDialog, gui.BrotherWindow.Ui_BrotherWindow):
    """Window for the end user to manage the list of brothers in the database."""

    def __init__(self, parent=None):
        super(BrotherWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_add.clicked.connect(self.show_add_brother_window)


    def show_add_brother_window(self):
        self.add_bro_window = AddBrotherWindow()
        self.add_bro_window.show()


class AddBrotherWindow(QtGui.QDialog, gui.AddBrotherWindow.Ui_AddBrotherWindow):
    """Window for the end user to add brothers to the database."""

    def __init__(self, parent=None):
        super(AddBrotherWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_add.clicked.connect(self.add_item)

    def add_item(self):

        first_name = self.line_f_name.displayText()
        middle_name = self.line_m_name.displayText()
        last_name = self.line_l_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        congregation = 'Congregation combo box'
        responsibility = 'Responsibility combo box'
        chairman = 'Chairman check box'
        speaker = 'Speaker check box'
        coordinator = 'Coordinator check box'
        note = 'Note text box'

        coloumns = ['first_name', 'middle_name', 'last_name', 'phone','email',
                    'congregation', 'responsibility', 'chairman', 'speaker',
                    'coordinator', 'note']
        values = [first_name, middle_name, last_name, phone, email,
                  congregation, responsibility, chairman, speaker,
                  coordinator, note]

class CongregationWindow(QtGui.QDialog, gui.CongregationWindow.Ui_CongregationWindow):

    def __init__(self, parent=None):
        super(CongregationWindow, self).__init__(parent)
        self.setupUi(self)
        self.populate_table()


    # Populate the congregation table
    def populate_table(self):

        list = Congregation.get_list(None)
return list
        for x in list:
            self.list_congregation.addItem("{}".format(x[0]))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
