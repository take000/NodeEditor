from PyQt5.QtWidgets import *


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.show()
