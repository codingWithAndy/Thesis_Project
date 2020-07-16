import PyQt5
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow.


class App(QApplication):
    """Main application wrapper, loads and shows the main window"""

    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        # Show main window
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == '__main__':
    app = App(sys.argv)

    sys.exit(app.exec_())
