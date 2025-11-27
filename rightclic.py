from PyQt5.QtCore import QObject, QEvent
from PyQt5.QtWidgets import QPushButton
from qgis.PyQt.QtCore import Qt


class ClicDroit(QObject):
    def __init__(self, class_parent):
        super().__init__()
        self.class_parent = class_parent

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:
            if isinstance(obj, QPushButton):
                self.class_parent.clic_droit(obj)
                return True
                # QMessageBox.warning(None, "fd","sdf")
        return False