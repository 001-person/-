import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Child_read_win import Ui_Form
from book import Book
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class ReadWin(QMainWindow, Ui_Form):
    def __init__(self,path,parent=None):
        super(ReadWin,self).__init__(parent)
        self.setupUi(self)
        
        self.path = path
        self.book = None
        self.chapters = None
        self.browser = QWebEngineView()
        self.load_chapter()
        self.chapter.itemClicked.connect(self.load_content)

    def load_chapter(self):
        self.book = Book(self.path)
        self.chapters = self.book.get_chapter()
        for ch in self.chapters:
            self.chapter.addItem(ch)
        self.chapter.setCurrentRow(0)

    def load_content(self,item):
        print("才能使南昌")
        print(self.chapters[item.text()])
        #self.content.setHtml(self.chapters[item.text()])
        self.browser.load(QUrl(self.chapters[item.text()]))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    read_win = ReadWin("resource\小王子.epub")
    read_win.show()
    sys.exit(app.exec_())