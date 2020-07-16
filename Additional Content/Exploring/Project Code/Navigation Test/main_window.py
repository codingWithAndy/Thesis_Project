from PyQt5.QtWidgets import QWidget, QMainWindow
from main_menu2 import Ui_MainMenu
from learning_zone2 import LearningZone
from main_window import Ui_MainWindow


class Ui_MainWindow(Ui_MainWindow, QMainWindow):
    """Main application window, handles the workflow of secondary windows"""

    def __init__(self):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self)

        self.setupUi(self)

        # start hidden
        self.hide()

        # show window A
        self.window_a = Ui_MainMenu()
        self.window_a.actionExit.triggered.connect(self.window_a_closed)
        self.window_a.show()

    def window_a_closed(self):
        # Show window B
        self.window_b = LearningZone()
        self.window_b.actionExit.triggered.connect(self.window_b_closed)
        self.window_b.show()

    def window_b_closed(self):
        #Close the application if window B is closed
        self.close()
