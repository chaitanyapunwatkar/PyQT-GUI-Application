
""" This Module will help to view Charts """

from PySide2.QtWidgets import * 
import sys
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QPen, QColor
from PySide2.QtCore import Qt
from db_query import DbQueries

class PieChart(QWidget):
    """ This Class will help to view the inspection data present in table in Pie Chart View.

    Args:
        QWidget (Class inherits the QtWidgets): To view the 
    """
    def __init__(self):
        super(PieChart, self).__init__()        
        series = QtCharts.QPieSeries()
        self.Vlayout = QVBoxLayout(self) 
        db = DbQueries()
        g_count = db.status_filter('Good')
        b_count = db.status_filter('Bad')
        total_count = db.count()
        series.append("Good {}%".format((len(g_count)*100)/total_count),len(g_count))
        series.append("Bad {}%".format((len(b_count)*100)/total_count),len(b_count))
        Slice = QtCharts.QPieSlice()
        Slice = series.slices()[1]
        Slice.setExploded(True)
        Slice.setLabelVisible(True)
        Slice.setBrush(QColor("red"))
        Slice = series.slices()[0]
        Slice.setBrush(QColor('lightgreen'))
        Slice.setLabelVisible(True)
        
        chart = QtCharts.QChart()
        chart.legend().setVisible(True)
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("Item1 Analysis")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.Vlayout.addWidget(chartview)
        self.setLayout(self.Vlayout)


class BarChart(QWidget):
    """ This Class represents BarGraph of 30 minutes interval of time with percentage of good and bad status

    Args:
        QWidget (Class): Inherits Properties of QWidgets to Add layouts and widgets 
    """
    def __init__(self):
        super(BarChart, self).__init__() 
        self.Vlayout = QVBoxLayout(self) 
        db = DbQueries()
        g_count = db.status_filter('Good')
        b_count = db.status_filter('Bad')
        
        set0 = QtCharts.QBarSet("Good")
        set1 = QtCharts.QBarSet("Bad")

        set0.setBrush(QColor('lightgreen'))
        set1.setBrush(QColor('red'))

        
        set0 << len(g_count) << len(g_count) << len(g_count) << len(g_count) << len(g_count) << len(g_count)
        set1 << len(b_count) << len(b_count) << len(b_count) << len(b_count) << len(b_count) << len(b_count)


        series = QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Percent Example")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM",
                      "11:30 AM"]
        
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QtCharts.QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.Vlayout.addWidget(chartView)