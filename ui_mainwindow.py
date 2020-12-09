# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(547, 485)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionid_ascendente = QAction(MainWindow)
        self.actionid_ascendente.setObjectName(u"actionid_ascendente")
        self.actionDistancia_descendente = QAction(MainWindow)
        self.actionDistancia_descendente.setObjectName(u"actionDistancia_descendente")
        self.actionVelocidad_ascendente = QAction(MainWindow)
        self.actionVelocidad_ascendente.setObjectName(u"actionVelocidad_ascendente")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBox_xOrigin = QSpinBox(self.groupBox_2)
        self.spinBox_xOrigin.setObjectName(u"spinBox_xOrigin")
        self.spinBox_xOrigin.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_xOrigin, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_xDestiny = QSpinBox(self.groupBox_2)
        self.spinBox_xDestiny.setObjectName(u"spinBox_xDestiny")
        self.spinBox_xDestiny.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_xDestiny, 3, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox_id = QSpinBox(self.groupBox_2)
        self.spinBox_id.setObjectName(u"spinBox_id")

        self.gridLayout_2.addWidget(self.spinBox_id, 0, 1, 1, 1)

        self.spinBox_speed = QSpinBox(self.groupBox_2)
        self.spinBox_speed.setObjectName(u"spinBox_speed")

        self.gridLayout_2.addWidget(self.spinBox_speed, 5, 1, 1, 1)

        self.spinBox_yOrigin = QSpinBox(self.groupBox_2)
        self.spinBox_yOrigin.setObjectName(u"spinBox_yOrigin")
        self.spinBox_yOrigin.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_yOrigin, 2, 1, 1, 1)

        self.pushButton_show = QPushButton(self.groupBox_2)
        self.pushButton_show.setObjectName(u"pushButton_show")

        self.gridLayout_2.addWidget(self.pushButton_show, 8, 0, 1, 2)

        self.spinBox_yDestiny = QSpinBox(self.groupBox_2)
        self.spinBox_yDestiny.setObjectName(u"spinBox_yDestiny")
        self.spinBox_yDestiny.setMaximum(500)

        self.gridLayout_2.addWidget(self.spinBox_yDestiny, 4, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.pushButton_addEnd = QPushButton(self.groupBox_2)
        self.pushButton_addEnd.setObjectName(u"pushButton_addEnd")

        self.gridLayout_2.addWidget(self.pushButton_addEnd, 7, 1, 1, 1)

        self.pushButton_addStart = QPushButton(self.groupBox_2)
        self.pushButton_addStart.setObjectName(u"pushButton_addStart")

        self.gridLayout_2.addWidget(self.pushButton_addStart, 7, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.spinBox_red = QSpinBox(self.groupBox)
        self.spinBox_red.setObjectName(u"spinBox_red")
        self.spinBox_red.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_red, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.spinBox_green = QSpinBox(self.groupBox)
        self.spinBox_green.setObjectName(u"spinBox_green")
        self.spinBox_green.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_green, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.spinBox_blue = QSpinBox(self.groupBox)
        self.spinBox_blue.setObjectName(u"spinBox_blue")
        self.spinBox_blue.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_blue, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 6, 0, 1, 2)

        self.push_recorrido = QPushButton(self.groupBox_2)
        self.push_recorrido.setObjectName(u"push_recorrido")

        self.gridLayout_2.addWidget(self.push_recorrido, 9, 0, 1, 2)


        self.gridLayout_6.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.LineEdit_search = QLineEdit(self.tab_4)
        self.LineEdit_search.setObjectName(u"LineEdit_search")

        self.gridLayout_4.addWidget(self.LineEdit_search, 1, 0, 1, 1)

        self.pushButton_search = QPushButton(self.tab_4)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.gridLayout_4.addWidget(self.pushButton_search, 1, 1, 1, 1)

        self.pushButton_show_2 = QPushButton(self.tab_4)
        self.pushButton_show_2.setObjectName(u"pushButton_show_2")

        self.gridLayout_4.addWidget(self.pushButton_show_2, 1, 2, 1, 1)

        self.table = QTableWidget(self.tab_4)
        self.table.setObjectName(u"table")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_draw = QPushButton(self.tab)
        self.pushButton_draw.setObjectName(u"pushButton_draw")

        self.gridLayout_5.addWidget(self.pushButton_draw, 1, 0, 1, 1)

        self.pushButton_clean = QPushButton(self.tab)
        self.pushButton_clean.setObjectName(u"pushButton_clean")

        self.gridLayout_5.addWidget(self.pushButton_clean, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 547, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.actionid_ascendente)
        self.menuOrdenar.addAction(self.actionDistancia_descendente)
        self.menuOrdenar.addAction(self.actionVelocidad_ascendente)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionid_ascendente.setText(QCoreApplication.translate("MainWindow", u"id (ascendente)", None))
        self.actionDistancia_descendente.setText(QCoreApplication.translate("MainWindow", u"Distancia (descendente)", None))
        self.actionVelocidad_ascendente.setText(QCoreApplication.translate("MainWindow", u"Velocidad (ascendente)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.pushButton_show.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.pushButton_addEnd.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.pushButton_addStart.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.push_recorrido.setText(QCoreApplication.translate("MainWindow", u"Recorrido profundidad/amplitud", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.LineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de particula", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_show_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.pushButton_draw.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.pushButton_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Dibujo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

