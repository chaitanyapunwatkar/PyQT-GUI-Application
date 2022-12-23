import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import * 
from PySide2.QtGui import QPalette, QColor, QPixmap
from db_query import DbQueries
from math import ceil

class ImagePal(QWidget):
    def __init__(self, c, color):
        super(ImagePal, self).__init__()
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self) 
        img = QPixmap('Item1/{0}.jpg'.format(c))
        label = QLabel(self)
        img2 = img.scaled(128,128)
        label.setPixmap(img2)
        label.setGeometry(0, 0, 128, 128)
        ind_label = QLabel("", self)
        ind_label.setStyleSheet("background-color: {0};".format(color))
        #ind_label.setGeometry(0,0, 125 , 10)
        self.Vlayout.addWidget(label)
        self.setGeometry(0,0,128,50)
        self.Vlayout.addWidget(ind_label)


class Gallery_All(QWidget):
    def __init__(self):
            super(Gallery_All, self).__init__()
            self.setAutoFillBackground(True)
            self.Glayout = QGridLayout(self)

    

# Analysis Page UI components
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
        
        
#Gallery Page UI components
class Gallery(QWidget):
    def __init__(self):
        super(Gallery, self).__init__()
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self) 
        self.scrollArea = QScrollArea(self)
        self.Stack = QStackedWidget(self)
        status_filter = QComboBox(self)
        self.scrollWidgetContents = QWidget(self)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.Glayout = QGridLayout(self.scrollWidgetContents)
        status_filter.addItems(['All', 'Good', 'Bad'])
        status_filter.setGeometry(400,10,180,50)
        self.Vlayout.addWidget(status_filter)
        self.scrollArea.setWidget(self.scrollWidgetContents)
        self.Vlayout.addWidget(self.scrollArea)
        #self.Vlayout.addWidget(self.Stack)
        status_filter.currentTextChanged.connect(self.print_drop_text)
    
    def print_drop_text(self, text_select):
        db = DbQueries()
        if text_select == 'Good':
            self.Stack.setCurrentIndex(0)
            uIdList = db.status_filter(text_select)
            c = len(uIdList)
            print(c)
            rng = ceil(c/4)
            count = 0
            for row in range(1,rng+1):
                for column in range(4):
                    if count<c :
                        self.Glayout.addWidget(ImagePal(uIdList[count],'Green'), row, column)
                        count+=1

        elif text_select == 'Bad':
            self.Stack.setCurrentIndex(1)
            uIdList = db.status_filter(text_select)
            c = len(uIdList)
            rng = ceil(c/4)
            count = 0
            for row in range(1,rng+1):
                for column in range(4):
                    if count<c :
                        self.Glayout.addWidget(ImagePal(uIdList[count],'Red'), row, column)
                        count+=1
        
        else:
            self.Stack.setCurrentIndex(2)
            db = DbQueries()
            c = 100
            rng = ceil(c/4)
            count = 0
            stat_color = { 'Good': 'Green',
                            'Bad': 'red'}
        
            for row in range(1,rng+1):
                for column in range(4):
                    if count<c :
                        color = db.id_status(count+1)
                        self.Glayout.addWidget(ImagePal(count+1,stat_color[color]), row, column)
                        count+=1
                        

#Window Page - Parent Class        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Post_Inspection Analysis")
        widget = QWidget()
        pagelayout = QHBoxLayout()
        button_layout = QVBoxLayout()
        self.stacklayout = QStackedLayout()
             
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        
        btn = QPushButton("Analysis")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Analysis())

        btn = QPushButton("Image Gallery")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Gallery())
     
   
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()