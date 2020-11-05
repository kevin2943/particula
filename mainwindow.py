"""Clase principal"""
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from lista import Lista
from particula import Particula


class MainWindow(QMainWindow):
    """Clase main window"""

    def __init__(self):
        super(MainWindow, self).__init__()

        headers = ['id', 'Origen x', 'Origen y', 'Destino x',
                   'Destino y', 'Velocidad', 'Distancia', 'Red', 'Green', 'Blue']

        self.lista = Lista()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_show.clicked.connect(self.click_show)
        self.ui.pushButton_addEnd.clicked.connect(self.click_addEnd)
        self.ui.pushButton_addStart.clicked.connect(self.click_addStart)

        self.ui.actionAbrir.triggered.connect(self.action_abrir)
        self.ui.actionGuardar.triggered.connect(self.action_guardar)

        self.ui.pushButton_search.clicked.connect(self.click_search)
        self.ui.pushButton_show_2.clicked.connect(self.click_show_table)

        self.ui.table.setColumnCount(10)
        self.ui.table.setHorizontalHeaderLabels(headers)

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

    @Slot()
    def click_search(self):
        searchId = int(self.ui.LineEdit_search.text())
        # self.ui.table.clear()
        self.ui.table.setRowCount(0)
        for particula in self.lista:
            if(particula.id == searchId):
                self.ui.table.setRowCount(1)
                self.ui.table.setItem(
                    0, 0, QTableWidgetItem(str(particula.id)))
                self.ui.table.setItem(
                    0, 1, QTableWidgetItem(str(particula.origen_x)))
                self.ui.table.setItem(
                    0, 2, QTableWidgetItem(str(particula.origen_y)))
                self.ui.table.setItem(
                    0, 3, QTableWidgetItem(str(particula.destino_x)))
                self.ui.table.setItem(
                    0, 4, QTableWidgetItem(str(particula.destino_y)))
                self.ui.table.setItem(
                    0, 5, QTableWidgetItem(str(particula.velocidad)))
                self.ui.table.setItem(
                    0, 6, QTableWidgetItem(str(particula.distancia)))
                self.ui.table.setItem(
                    0, 7, QTableWidgetItem(str(particula.red)))
                self.ui.table.setItem(
                    0, 8, QTableWidgetItem(str(particula.green)))
                self.ui.table.setItem(
                    0, 9, QTableWidgetItem(str(particula.blue)))
                return
        QMessageBox.warning(
            self,
            "Atención",
            f'La particula con el id "{searchId}" no fue encontrada'
        )

    @Slot()
    def click_show_table(self):
        self.ui.table.setRowCount(len(self.lista))
        for row, particula in enumerate(self.lista):
            self.ui.table.setItem(
                row, 0, QTableWidgetItem(str(particula.id)))
            self.ui.table.setItem(
                row, 1, QTableWidgetItem(str(particula.origen_x)))
            self.ui.table.setItem(
                row, 2, QTableWidgetItem(str(particula.origen_y)))
            self.ui.table.setItem(
                row, 3, QTableWidgetItem(str(particula.destino_x)))
            self.ui.table.setItem(
                row, 4, QTableWidgetItem(str(particula.destino_y)))
            self.ui.table.setItem(
                row, 5, QTableWidgetItem(str(particula.velocidad)))
            self.ui.table.setItem(
                row, 6, QTableWidgetItem(str(particula.distancia)))
            self.ui.table.setItem(
                row, 7, QTableWidgetItem(str(particula.red)))
            self.ui.table.setItem(
                row, 8, QTableWidgetItem(str(particula.green)))
            self.ui.table.setItem(
                row, 9, QTableWidgetItem(str(particula.blue)))
