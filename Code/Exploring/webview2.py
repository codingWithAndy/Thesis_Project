from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("Data Splash! - Learning Zone")
        self.setGeometry(20,20, 1920, 1080)
        self.browser = QWebEngineView()
        self.browser.setGeometry(20, 20, 1871, 921)
        self.browser.load(QUrl("https://www.nintendo.co.uk/"))

        self.setCentralWidget(self.browser)
    

        self.show()




app = QApplication(sys.argv)
window = MainWindow()

app.exec_()