from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit
)

from instr import *

class FinalWin(QWidget):
    def __init__(self):
        ''' the window in which the survey is being conducted '''
        super().__init__()

        # creating and configuring graphic elements
        self.initUI()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # start
        self.show()

    def initUI(self):
        ''' creates graphic elements '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        ''' sets what the window will look like (label, size, location) '''
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

''' sets what the window will look like (label, size, location) '''
def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
