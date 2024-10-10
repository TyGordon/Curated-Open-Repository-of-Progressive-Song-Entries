import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
from PyQt6.uic import loadUi


class MainUI(QMainWindow):

    lemma_search = False
    empty_tag = "\" \""
    tag_1968 = "\"1968\""
    tag_1969 = "\"1969\""
    tag_1970 = "\"1970\""
    tag_1971 = "\"1971\""
    tag_1972 = "\"1972\""
    tag_1973 = "\"1973\""
    tag_1974 = "\"1974\""
    tag_1975 = "\"1975\""
    tag_1976 = "\"1976\""
    tag_1977 = "\"1977\""
    tag_1978 = "\"1978\""
    tag_1979 = "\"1979\""
    tag_1980 = "\"1980\""
    tag_1981 = "\"1981\""
    tag_1982 = "\"1982\""
    tag_1983 = "\"1983\""
    tag_1984 = "\"1984\""

    # //album[@date=tag_1968
    # or @date=tag_1968
    # or @date=tag_1968
    # or @date=tag_1968]//tr[" "]//w[" "]

    #print(tag_1968 + empty_tag + tag_1976)

    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("corpus_gui.ui", self)


        self.searchButton.clicked.connect(self.on_search)
        #self.clearButton.clicked.connect(self.on_clear)

    def on_search(self):
        print("Search")

    #def on_clear(self):
    #    self.lineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
