import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFrame
)
from PyQt5.QtCore import Qt

class SideMenuExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Status menu (terlihat atau tidak)
        self.is_menu_visible = False

        # Widget utama
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Layout utama
        self.main_layout = QVBoxLayout(self.main_widget)

        # Konten utama
        self.content_area = QFrame()
        self.content_area.setStyleSheet("background-color: #ffffff;")
        content_layout = QVBoxLayout()
        content_layout.addWidget(QPushButton("Konten Utama"))
        self.content_area.setLayout(content_layout)
        self.main_layout.addWidget(self.content_area)

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

        # Pengaturan utama jendela
        self.setWindowTitle("Contoh Side Menu yang Menutupi Halaman Utama")
        self.setGeometry(100, 100, 800, 600)

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

# Main aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = SideMenuExample()
    example.show()
    sys.exit(app.exec_())
