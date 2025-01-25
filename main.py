from PySide6.QtWidgets import QApplication, QMainWindow
from prototype_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_signals()

    def setup_signals(self):
        # Tambahkan logika tombol di sini
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Tombol diklik!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
