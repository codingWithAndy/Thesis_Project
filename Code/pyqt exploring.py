from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, time


class MyWindow(QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Coding with Andy!")
        self.initUI()

    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me!")
        self.b1.clicked.connect(self.clicked)

        
    def clicked(self):
        print("Clicked button")
        self.label.setText("you pressed the button! \n Boom!")
        self.update()
        self.label.repaint() # Need this to work on Mac OS
        

    def update(self):
        self.label.adjustSize()



#def clicked():
#    print("clicked")


def window():
    app = QApplication(sys.argv)
    
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

    # Taking code to the class

    '''
    win = QMainWindow()

    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Coding with Andy!")

    label = QtWidgets.QLabel(win)
    label.setText("My first label!")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me!")
    b1.clicked.connect(clicked) # Name of function with the ()
    '''
    

window()
