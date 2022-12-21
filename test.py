import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import * 
from PySide2.QtGui import QPalette, QColor

class Analysis(QWidget):
    def __init__(self):
        super(Analysis, self).__init__()
        self.setAutoFillBackground(True)
        label_t = QLabel("SKU ID: ", self)
        drop = QComboBox(self)
        label_t.setGeometry(10,10,100, 50)
        drop.setGeometry(65,10,200,50)
        drop.addItems(['Item1', 'Item2']) 
        drop.currentTextChanged.connect(self.print_drop_text)
        #self.setCentralWidget(drop)
    
    def print_drop_text(self, text_select):
        print(text_select)

class Gallery(QWidget):
    def __init__(self):
        super(Gallery, self).__init__()
        self.setAutoFillBackground(True)
        status_filter = QComboBox(self)
        status_filter.addItems(['All', 'Good', 'Bad'])
        status_filter.setGeometry(400,10,180,50)
        status_filter.currentTextChanged.connect(self.print_drop_text)
        #self.setCentralWidget(drop)
    
    def print_drop_text(self, text_select):
        print(text_select)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Post_Inspection Analysis")

        pagelayout = QHBoxLayout()
        button_layout = QVBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("Analysis")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        #self.stacklayout.addWidget(Text())
        self.stacklayout.addWidget(Analysis())

        btn = QPushButton("Image Gallery")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Gallery())

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)
    
    def drop(self):
        drop = QComboBox(self)
        drop.addItems(['All', 'Good', 'Bad']) 
        drop.currentTextChanged.connect(self.print_drop_text)
        self.setCentralWidget(drop)
    
    def print_drop_text(self, text_select):
        print(text_select)
        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()