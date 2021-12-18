import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


App = QApplication(sys.argv)
QApplication.setApplicationName('Google')
window = mainwindow()
sys.exit(App.exec())
