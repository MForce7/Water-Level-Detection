import sys
from PyQt5.QtGui import QIcon
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QComboBox, QLabel, QVBoxLayout, 
    QHBoxLayout, QPushButton, QStyle, QGridLayout,QSlider, QFrame
)
from PyQt5.QtCore import Qt, QFile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Water Level Detection")
        self.setGeometry(100, 100, 1280, 720)
        self.page = 0
    
        
        if self.page == 0:
            # Title
            main_title = QLabel("Water Level Detection", self)
            main_title.setProperty("heading","title")
            main_title.setStyleSheet("color: red;")
            
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
            self.slider_2 = QSlider(Qt.Horizontal, self)

            self.controller2 = QHBoxLayout()
            self.controller2.addWidget(self.record_button2)
            self.controller2.addWidget(self.play_button2)
            self.controller2.addWidget(self.stop_button2)
            self.controller2.addWidget(self.browse_button2)
            self.controller2.addWidget(self.slider_2)
            self.player2_box = QVBoxLayout()
            self.player2_box.addWidget(self.player_title2)
            self.player2_box.addLayout(self.controller2)
            # Player
            self.player_container = QHBoxLayout()
            self.player_container.addLayout(self.player1_box)
            self.player_container.addLayout(self.player2_box)
            
            # graph section ================================
            
            self.main_graph = QHBoxLayout()
            
            # transform graph
            self.transform_graph = Figure()  # Membuat figure matplotlib
            self.transform_canvas = FigureCanvas(self.transform_graph)  # Membungkus figure dengan canvas
            self.main_graph.addWidget(self.transform_canvas)

            # spectogram1
            self.spectogram = QVBoxLayout()
            self.main_graph.addLayout(self.spectogram)
            
            self.spectogram1 = Figure()  # Membuat figure matplotlib
            self.spectogram1_canvas = FigureCanvas(self.spectogram1)  # Membungkus figure dengan canvas
            self.spectogram.addWidget(self.spectogram1_canvas)
            
            self.spectogram2 = Figure()  # Membuat figure matplotlib
            self.spectogram2_canvas = FigureCanvas(self.spectogram2)  # Membungkus figure dengan canvas
            self.spectogram.addWidget(self.spectogram2_canvas)

            # # Plot grafik awal
            # self.plot_graph()
            
            
            # player_graph_section
            self.player_graph_section = QVBoxLayout()
            self.player_graph_section.addLayout(self.player_container)
            self.player_graph_section.addLayout(self.main_graph)
            
            # Result Section
            self.result_section = QLabel("Result")
            self.result_section.setMinimumSize(207,543)
            
            
            # main_section
            self.main_section = QHBoxLayout()
            self.main_section.addLayout(self.player_graph_section)
            self.main_section.addWidget(self.result_section)
        
        
        
        if self.page == 1:
            
            self.pitch_title = QLabel("Pitch Detection", self)
            
            
            # player
            self.player_title1 = QLabel("Detection Container", self)
            
            self.record_button1 = QPushButton("rec")
            self.play_button1 = QPushButton("play")
            self.stop_button1 = QPushButton("stop")
            self.browse_button1 = QPushButton("browse")
            self.slider_1 = QSlider(Qt.Horizontal, self)

            self.pitch_controller = QHBoxLayout()
            self.pitch_controller.addWidget(self.record_button1)
            self.pitch_controller.addWidget(self.play_button1)
            self.pitch_controller.addWidget(self.stop_button1)
            self.pitch_controller.addWidget(self.browse_button1)
            self.pitch_controller.addWidget(self.slider_1)
            self.pitch_controller_box = QVBoxLayout()
            self.pitch_controller_box.addWidget(self.player_title1)
            self.pitch_controller_box.addLayout(self.pitch_controller)
            
            self.pitch_result_title = QLabel("Pitch:", self)
            self.pitch_result_value = QLabel("A#", self)
            
            self.detection_section = QHBoxLayout()
            self.detection_section.addLayout(self.pitch_controller_box)
            
            self.main_pitch = QVBoxLayout()
            self.main_pitch.addWidget(self.pitch_title)
            self.main_pitch.addLayout(self.detection_section)
            self.main_pitch.addWidget(self.pitch_result_title)
            self.main_pitch.addWidget(self.pitch_result_value)
        
        
        
        # whole widgets
        self.main_container = QVBoxLayout()
        if self.page == 0:
            self.main_container.addWidget(main_title)
            self.main_container.addLayout(self.main_section)
        if self.page == 1:
            self.main_container.addLayout(self.main_pitch)
            
        # Set central widget
        container_widget = QFrame()
        container_widget.setLayout(self.main_container)
        self.setCentralWidget(container_widget)
        
        
        
        
        self.is_menu_visible = False
        
        
        # Side menu (dengan posisi di luar layar awalnya)
        self.side_menu = QFrame(self)
        self.side_menu.setGeometry(-200, 0, 200, self.height())  # Mulai di luar layar
        self.side_menu.setStyleSheet("background-color: #f0f0f0; border-right: 1px solid #ccc;")
        
        # Konten menu (tombol-tombol)
        side_menu_layout = QVBoxLayout()
        side_menu_layout.addWidget(QPushButton("Menu 1"))
        side_menu_layout.addWidget(QPushButton("Menu 2"))
        side_menu_layout.addWidget(QPushButton("Menu 3"))
        side_menu_layout.addStretch()
        self.side_menu.setLayout(side_menu_layout)

        # Tombol toggle untuk menampilkan/menyembunyikan side menu
        self.toggle_button = QPushButton("☰", self)
        self.toggle_button.setFixedSize(50, 30)
        self.toggle_button.setStyleSheet("font-size: 18px;")
        self.toggle_button.move(10, 10)
        self.toggle_button.clicked.connect(self.toggle_menu)
        
        
        
        
        
        
        
        
        
        
    def toggle_menu(self):
        """
        Fungsi untuk menampilkan/menyembunyikan side menu.
        """
        if self.is_menu_visible:
            self.hide_menu()
        else:
            self.show_menu()
        
    def show_menu(self):
        """
        Menampilkan side menu dengan animasi.
        """
        self.is_menu_visible = True
        for x in range(-200, 0, 10):  # Animasi geser menu dari -200 ke 0
            self.side_menu.setGeometry(x, 0, 200, self.height())
            QApplication.processEvents()  # Perbarui tampilan selama animasi

    def hide_menu(self):
        """
        Menyembunyikan side menu dengan animasi.
        """
        self.is_menu_visible = False
        for x in range(0, -200, -10):  # Animasi geser menu dari 0 ke -200
            self.side_menu.setGeometry(x, 0, 200, self.height())
            QApplication.processEvents()  # Perbarui tampilan selama animasi

        
        
        
        
        
        
        
        
        
def load_stylesheet(app, stylesheet_path):
        try:
            with open(stylesheet_path, "r") as f:
                app.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Error: {stylesheet_path} not found.") 
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app, "style.qss")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
