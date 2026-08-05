import os
from pathlib import Path

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QFont
from qgis.PyQt.QtWidgets import  QListWidgetItem,QDialog
from qgis.PyQt.uic import loadUi

class DialogImport(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.vues_a_importer = None
        self.tout_coche = False
        loadUi(Path(os.path.dirname(__file__), "dial_import.ui"), self)
        self.setWindowTitle("Liste des vues disponibles")

        self.pushButton_importer.clicked.connect(self.importer)
        self.pushButton_tout_rien.clicked.connect(self.tout_rien)

    def ini_list_view(self,list_vues):
        for vue_absolu in list_vues:
            vue = os.path.basename(vue_absolu)
            item = QListWidgetItem(vue)
            font = QFont()
            font.setPointSize(10)
            font.setBold(True)
            item.setFont(font)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.listWidget_vues.addItem(item)

    def get_vues_a_importer(self):
        self.vues_a_importer = []
        for i in range(self.listWidget_vues.count()):
            item = self.listWidget_vues.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                self.vues_a_importer.append(item.text())
        return self.vues_a_importer

    def tout_rien(self):
        for i in range(self.listWidget_vues.count()):
            item = self.listWidget_vues.item(i)
            if self.tout_coche:
                item.setCheckState(Qt.CheckState.Unchecked)
            else:
                item.setCheckState(Qt.CheckState.Checked)
        self.tout_coche = not self.tout_coche

    def importer(self):
        self.get_vues_a_importer()
        self.accept()

