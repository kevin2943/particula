"""Clase principal"""
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from lista import Lista
from particula import Particula


class MainWindow(QMainWindow):
    """Clase main window"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.lista = Lista()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_show.clicked.connect(self.click_show)
        self.ui.pushButton_addEnd.clicked.connect(self.click_addEnd)
        self.ui.pushButton_addStart.clicked.connect(self.click_addStart)

        self.ui.actionAbrir.triggered.connect(self.action_abrir)
        self.ui.actionGuardar.triggered.connect(self.action_guardar)

    def readInputs(self):
        Id = self.ui.spinBox_id.value()
        xOrigin = self.ui.spinBox_xOrigin.value()
        yOrigin = self.ui.spinBox_yOrigin.value()
        xDestiny = self.ui.spinBox_xDestiny.value()
        yDestiny = self.ui.spinBox_yDestiny.value()
        speed = self.ui.spinBox_speed.value()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(Id, xOrigin, yOrigin, xDestiny,
                              yDestiny, speed, red, green, blue)
        return particula

    @Slot()
    def click_addStart(self):
        particula = self.readInputs()
        self.lista.agregar_inicio(particula)

    @Slot()
    def click_addEnd(self):
        particula = self.readInputs()
        self.lista.agregar_final(particula)

    @Slot()
    def click_show(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lista))

    @Slot()
    def action_abrir(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
