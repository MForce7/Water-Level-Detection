import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QComboBox, QLabel, QVBoxLayout, 
    QHBoxLayout, QPushButton, QStyle, QGridLayout,QSlider
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Water Level Detection")
        self.setGeometry(100, 100, 1280, 720)
        
        # Title
        self.main_title = QLabel("Water Level Detection", self)
        
        # Player1==============================================
        self.player_title1 = QLabel("Full Container", self)
        
        self.record_button1 = QPushButton("rec")
        self.play_button1 = QPushButton("play")
        self.stop_button1 = QPushButton("stop")
        self.browse_button1 = QPushButton("browse")
        self.slider_1 = QSlider(Qt.Horizontal, self)

        self.controller1 = QHBoxLayout()
        self.controller1.addWidget(self.record_button1)
        self.controller1.addWidget(self.play_button1)
        self.controller1.addWidget(self.stop_button1)
        self.controller1.addWidget(self.browse_button1)
        self.controller1.addWidget(self.slider_1)
        self.player1_box = QVBoxLayout()
        self.player1_box.addWidget(self.player_title1)
        self.player1_box.addLayout(self.controller1)
        # Player2==============================================
        self.player_title2 = QLabel("Detected Container", self)
        
        self.record_button2 = QPushButton("rec")
        self.play_button2 = QPushButton("play")
        self.stop_button2 = QPushButton("stop")
        self.browse_button2 = QPushButton("browse")
        # self.slider_2 = QSlider(Qt.Horizontal, self)

        self.controller2 = QHBoxLayout()
        self.controller2.addWidget(self.record_button2)
        self.controller2.addWidget(self.play_button2)
        self.controller2.addWidget(self.stop_button2)
        self.controller2.addWidget(self.browse_button2)
        # self.controller2.addWidget(self.slider_2)
        self.player2_box = QVBoxLayout()
        self.player2_box.addWidget(self.player_title2)
        self.player2_box.addLayout(self.controller2)
        
        
        
        
        # player_graph_section
        self.player_graph_section = QVBoxLayout()
        self.player_graph_section.addLayout(self.player1_box)
        
        # Result Section
        self.result_section = QLabel("Result")
        
        # main_section
        self.main_section = QHBoxLayout()
        self.main_section.addLayout(self.player_graph_section)
        self.main_section.addWidget(self.result_section)
        
        # whole widgets
        self.main_container = QVBoxLayout()
        self.main_container.addWidget(self.main_title)
        self.main_container.addLayout(self.main_section)

        # Set central widget
        container_widget = QWidget()
        container_widget.setLayout(self.main_container)
        self.setCentralWidget(container_widget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
