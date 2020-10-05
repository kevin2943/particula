"""Clase principal"""
from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    """Clase main window"""
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.pushButton.clicked.connect(self.click_agregar)

    @Slot()
    def click_agregar(self):
        print('click')
