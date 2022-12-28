import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import * 
from PySide2.QtGui import *
from db_query import DbQueries
from math import ceil
from GraphView import BarChart, PieChart

class ImagePal(QWidget):
    """ This class is about representing the product images with color palette below it. 
    This is GridLayout, Vertical layout is added to show color palette below image.
    Args:
        QWidget (_type_): The QWidget is the superclass inherited to use its methods 
        like QVBoxLayout, QHBoxLayout, QLabel.
    """
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
        self.Vlayout.addWidget(self.ind_label)
        # Size of the color palette is fixed
        self.ind_label.setFixedSize(130,10)
       

class Gallery_All(QWidget):
    """ This Class is called when 'All' Status is selected in the Image Gallery tab. Here All the Images 
        present in the database for particular SKU ID are showcased.

    Args:
        QWidget (Class Imprted from PySide2.QtWidget): The QWidget is the superclass inherited to use its methods like QVBoxLayout, 
        QStackedWidget, QScrollArea.
    """
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
    """ This Class is called when 'Bad' Status is selected in the Image Gallery tab. This will showcase product Images
        whose quality is labeled as Bad.

    Args:
        QWidget (Class Imprted from PySide2.QtWidget): The QWidget is the superclass inherited to use its methods like 
        QVBoxLayout, QStackedWidget, QScrollArea.
    """
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
    """ This Class is called when 'Good' Status is selected in the Image Gallery tab. This will showcase product Images
        whose quality is labeled as Good.

    Args:
        QWidget (Class Imprted from PySide2.QtWidget): The QWidget is the superclass inherited to use its methods like QVBoxLayout, 
        QStackedWidget, QScrollArea.
    """
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
 
 
class Analysis(QWidget):
    """ This Class represents the Analytics Page Tab and includes necessary UI components for the same.
        Horizontal Layout is added inside Vertical Layout includes SKU ID label and
        DropDown list. Below horizontal Layout GraphFrame widget is added.
        
    Args:
        QWidget (Class Imported from Pyside2.QtWidget): This class is inherited to use methods 
        like StackedLayout(), ScrollArea(), QVBoxLayout(), QComboBox(), QLabel().
        
    """
    def __init__(self):
        super(Analysis, self).__init__()
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self) 
        self.Hlayout = QHBoxLayout(self)

        self.Vlayout.addLayout(self.Hlayout)
        label_t = QLabel("SKU ID: ", self)
        dropBox = QComboBox(self)
        dropBox.addItems(['Item1', 'Item2'])
        self.Hlayout.addWidget(label_t)
        self.Hlayout.addWidget(dropBox)
        self.Hlayout.setAlignment(Qt.AlignLeft)
        dropBox.currentTextChanged.connect(self.print_drop_text)
        self.Vlayout.addWidget(BarChart())
        self.Vlayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.Vlayout)
        
         
    def print_drop_text(self, text_select):
        """ This function will set the chart according to SKU ID selected. 

        Args:
            text_select (String): A variable which contains SKU ID text selected bu user.
        """
        print(text_select)
        
        

class Gallery(QWidget): 
    """This class is called when user selects the Image Gallery Tab. This includes necessary 
        UI Components for Gallery Page. This includes VerticalLayout where top most widget includes filter option
        and another layout includes stacked widget with scroll area where images placed according to filter option
        selected by user

    Args:
        QWidget (Class Imported from Pyside2.QtWidget): This class is inherited to use methods 
        like StackedLayout(), ScrollArea(), QVBoxLayout(), QComboBox(), QLabel().
    """
    def __init__(self):
        super(Gallery, self).__init__()
        
        self.setAutoFillBackground(True)
        self.Vlayout = QVBoxLayout(self) 
        self.Hlayout = QHBoxLayout(self)
        self.Stack = QStackedWidget(self)
        status_filter = QComboBox(self)
        text = QLabel("Status: ", self)
        self.scrollWidgetContents = QWidget(self)

        self.Stack.addWidget(Gallery_All())
        self.Stack.addWidget(Gallery_Good())
        self.Stack.addWidget(Gallery_Bad())

        status_filter.addItems(['All', 'Good', 'Bad'])
        self.Hlayout.addStretch(1)
        self.Vlayout.addLayout(self.Hlayout)
        self.Hlayout.addWidget(text)
        self.Hlayout.addWidget(status_filter)
        self.Vlayout.addWidget(self.Stack)
        status_filter.currentTextChanged.connect(self.set_index)
    
    def set_index(self, text_select):
        """This function is used to set particular Index of StackWidget according to user selected status filter.

        Args:
            text_select (String): This variable contains Text from User selects from DropDown box.
        """
        if text_select == 'Good':
            self.Stack.setCurrentIndex(1)
        elif text_select == 'Bad':
            self.Stack.setCurrentIndex(2)  
        else:
            self.Stack.setCurrentIndex(0)                    

       
class MainWindow(QMainWindow):
    """ This is the Parent Window Class, To set the MainWindows settings and UI components.
    
    Args:
        QMainWindow (Class inherits from QWidget): To use methods like setWindowTitle(), QTabWidget()
    """
    def __init__(self):
        super().__init__()
        """ We have created two tabs 
            1. Analytics Tab - Chart View of the Product Inspection
            2. Image Gallery Tab - View images of Inspected with color label 
               indicating the status of product good or bad.
        """
        
        self.setWindowTitle("Post_Inspection Analysis")
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)
        tabs.addTab(Analysis(), "Analytics Tab")
        tabs.addTab(Gallery(), "Image Gallery Tab")
        self.setCentralWidget(tabs)


if __name__ == "__main__":
    """ This part of code is excuted first when we run the code."""

    app = QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(1100,800)
    window.show()
    #Below line opens the App
    app.exec_()