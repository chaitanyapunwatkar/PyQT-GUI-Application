import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import * 
from PySide2.QtGui import QPalette, QColor, QPixmap
from db_query import DbQueries
from math import ceil
from GraphView import PieChart

class ImagePal(QWidget):
    def __init__(self, c, color):
        super(ImagePal, self).__init__()
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self)
        self.img = QPixmap('Item1/{0}.jpg'.format(c))
        self.label = QLabel(self)
        self.img2 = self.img.scaled(128,128)
        self.label.setPixmap(self.img2)
        
        self.ind_label = QLabel(" ", self)
        self.ind_label.setStyleSheet("background-color: {0};width: 6px; margin: 0px px 0px 0px;".format(color))
        self.Vlayout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.Vlayout.addWidget(self.ind_label)
        self.ind_label.setAlignment(Qt.AlignCenter)
        self.ind_label.setFixedSize(150,10)
       

class Gallery_All(QWidget):
    def __init__(self):
            super(Gallery_All, self).__init__()
            self.setAutoFillBackground(True)
            self.Vlayout = QVBoxLayout(self) 
            self.scrollArea = QScrollArea(self)
            self.Stack = QStackedWidget(self)
            self.scrollWidgetContents = QWidget(self)
            
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scrollArea.setWidgetResizable(True)
            self.Glayout = QGridLayout(self.scrollWidgetContents)
            
            self.scrollArea.setWidget(self.scrollWidgetContents)
            self.Vlayout.addWidget(self.scrollArea)
            text_select ='All'
            db = DbQueries()
            c = 100
            rng = ceil(c/5)
            count = 0
            stat_color = { 'Good': 'Green',
                            'Bad': 'red'}
        
            for row in range(1,rng+1):
                for column in range(5):
                    if count<c :
                        color = db.id_status(count+1)
                        self.Glayout.addWidget(ImagePal(count+1,stat_color[color]), row, column)
                        count+=1
                        
            self.setLayout(self.Vlayout)


class Gallery_Bad(QWidget):
    def __init__(self):
            super(Gallery_Bad, self).__init__()
            self.setAutoFillBackground(True)
            self.Vlayout = QVBoxLayout(self) 
            self.scrollArea = QScrollArea(self)
            self.Stack = QStackedWidget(self)
            self.scrollWidgetContents = QWidget(self)
            

            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scrollArea.setWidgetResizable(True)
            self.Glayout = QGridLayout(self.scrollWidgetContents)
            self.Glayout.setSpacing(0)
            self.Glayout.setContentsMargins(0,0,0,0)
            self.scrollArea.setWidget(self.scrollWidgetContents)
            self.Vlayout.addWidget(self.scrollArea)
            text_select ='Bad'
            db = DbQueries()
            uIdList = db.status_filter(text_select)
            c = len(uIdList)
            print(c)
            rng = ceil(c/5)
            count = 0
            for row in range(1,rng+1):
                for column in range(5):
                    if count<c :
                        self.Glayout.addWidget(ImagePal(uIdList[count],'red'), row, column)
                        self.Glayout.setRowMinimumHeight(3,400)
                        count+=1
            self.setLayout(self.Vlayout)

class Gallery_Good(QWidget):
    def __init__(self):
            super(Gallery_Good, self).__init__()
            self.setAutoFillBackground(True)
            self.Vlayout = QVBoxLayout(self) 
            self.scrollArea = QScrollArea(self)
            self.Stack = QStackedWidget(self)
            self.scrollWidgetContents = QWidget(self)
            
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scrollArea.setWidgetResizable(True)
            self.Glayout = QGridLayout(self.scrollWidgetContents)
            
            self.scrollArea.setWidget(self.scrollWidgetContents)
            self.Vlayout.addWidget(self.scrollArea)
            text_select ='Good'
            db = DbQueries()
            uIdList = db.status_filter(text_select)
            c = len(uIdList)
            print(c)
            rng = ceil(c/5)
            count = 0
            for row in range(1,rng+1):
                for column in range(5):
                    if count<c :
                        self.Glayout.addWidget(ImagePal(uIdList[count],'Green'), row, column)
                        count+=1
            self.setLayout(self.Vlayout)
 
 
# Analysis Page UI components
class Analysis(QWidget):
    def __init__(self):
        super(Analysis, self).__init__()
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self) 
        self.Hlayout = QHBoxLayout(self)
        self.Vlayout.addLayout(self.Hlayout)
        label_t = QLabel("SKU ID: ", self)
        dropBox = QComboBox(self)
        label_t.setGeometry(10,10,100, 50)
        dropBox.setGeometry(65,10,200,50)
        dropBox.addItems(['Item1', 'Item2'])
        self.Hlayout.addWidget(label_t)
        self.Hlayout.addWidget(dropBox)
        dropBox.currentTextChanged.connect(self.print_drop_text)
        self.Vlayout.addWidget(PieChart())
        self.setLayout(self.Vlayout)
        
         
    def print_drop_text(self, text_select):
        print(text_select)
        
        
#Gallery Page UI components
class Gallery(QWidget):
    def __init__(self):
        super(Gallery, self).__init__()
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self) 
        self.Stack = QStackedWidget(self)
        status_filter = QComboBox(self)
        self.scrollWidgetContents = QWidget(self)

        self.Stack.addWidget(Gallery_All())
        self.Stack.addWidget(Gallery_Good())
        self.Stack.addWidget(Gallery_Bad())

        status_filter.addItems(['All', 'Good', 'Bad'])
        status_filter.setGeometry(400,10,180,50)
        self.Vlayout.addWidget(status_filter)
        self.Vlayout.addWidget(self.Stack)
        status_filter.currentTextChanged.connect(self.print_drop_text)
    
    def print_drop_text(self, text_select):
        if text_select == 'Good':
            self.Stack.setCurrentIndex(1)
        elif text_select == 'Bad':
            self.Stack.setCurrentIndex(2)  
        else:
            self.Stack.setCurrentIndex(0)                    

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(1100,800)
    window.show()

    app.exec_()