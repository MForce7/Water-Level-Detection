# from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # ... (other window initialization code)

#         with open("trial_selector/main_style.qss", "r") as f:
#             style_sheet = f.read()
#         self.setStyleSheet(style_sheet)
#         self.page = 0
#         if self.page == 0:
#             label = QLabel("Ini adalah label", self)
#             label.setProperty("class", "important")
        
        
        
#         # ... (remaining window setup)

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec_()







import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QSS Example")
        self.setGeometry(100, 100, 800, 600)
        
        # Title
        self.main_title = QLabel("Water Level Detection", self)
        self.main_title.setProperty("title", "ehe")
        with open ("trial_selector/main_style.qss", "r") as file:
            MainWindow.setStyleSheet(file.read)

        # Button
        self.record_button = QPushButton("Record")
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.main_title)
        layout.addWidget(self.record_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
