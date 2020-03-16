from PyQt5.QtWidgets import *
from node_graphics_scene import QDMGraphicsScene


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(560, 240, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # graphics scene
        self.qtScene = QDMGraphicsScene()

        # graphics view
        self.view = QGraphicsView(self)
        self.view.setScene(self.qtScene)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()
