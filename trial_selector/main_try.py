from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ... (other window initialization code)

        with open("trial_selector/main_style.qss", "r") as f:
            style_sheet = f.read()
        self.setStyleSheet(style_sheet)

        label = QLabel("Ini adalah label", self)
        label.setProperty("class", "important")
        
        
        
        # ... (remaining window setup)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()