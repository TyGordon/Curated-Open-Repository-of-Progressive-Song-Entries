import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
from PyQt6.uic import loadUi


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("corpus_gui.ui", self)

        #self.pushButton.clicked.connect(self.clickhandler)

    def clickhandler(self):
        print("Hello World")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
