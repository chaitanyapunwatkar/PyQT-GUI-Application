from PySide2.QtWidgets import * 
import sys
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QPen, QColor
from PySide2.QtCore import Qt
from db_query import DbQueries

class PieChart(QWidget):
    def __init__(self):
        super(PieChart, self).__init__()        
        series = QtCharts.QPieSeries()
        self.Vlayout = QVBoxLayout(self) 
        db = DbQueries()
        g_count = db.status_filter('Good')
        b_count = db.status_filter('Bad')
        series.append("Good",len(g_count))
        series.append("Bad", len(b_count))
        Slice = QtCharts.QPieSlice()
        Slice = series.slices()[1]
        Slice.setExploded(True)
        Slice.setLabelVisible(True)
        Slice.setBrush(QColor("red"))
        Slice = series.slices()[0]
        Slice.setBrush(QColor('lightgreen'))
        
        chart = QtCharts.QChart()
        chart.legend().setVisible(True)
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("Item_1 Analysis")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.Vlayout.addWidget(chartview)
        self.setLayout(self.Vlayout)