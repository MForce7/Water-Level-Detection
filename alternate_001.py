import numpy as np 
import time
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import serial.tools.list_ports
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QLineEdit, QStyle, QFileDialog, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Water Level Detection")
        # self.setWindowIcon(QIcon(r"Icon_keithley-min.png"))
        self.setGeometry(100, 100, 1280, 720)
        
        # Title
        self.main_title = QLabel("Water Level Detection")
        
        # Main Section
        main_section = QHBoxLayout()
        
        # player_graph_section
        player_graph_section = QVBoxLayout()
        # Result Section
        result_section = QLabel("Result")
        
        
        
        main_container = QVBoxLayout()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())