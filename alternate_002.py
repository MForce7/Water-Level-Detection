from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ... (other window initialization code)
        self.setWindowTitle("Water Level Detection")
        self.setGeometry(100, 100, 1280, 720)
        
        with open("style.qss", "r") as f:
            style_sheet = f.read()
        self.setStyleSheet(style_sheet)
        self.page = 0
        if self.page == 0:
            main_title = QLabel("Water Level Detection", self)
            main_title.setProperty("heading","title")
            label = QLabel("Ini adalah label", self)
            label.setProperty("class", "important")
        
        
        
        # ... (remaining window setup)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()