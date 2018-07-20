#import PyQt5.QtWidgets as QtWidgets

#qtApp = QtWidgets.QApplication([])

#def show():
#    window = QtWidgets.QMainWindow()
#    label = QtWidgets.QLabel('\tHello World!')
#    window.setCentralWidget(label)
#    window.show()

#if __name__ == "__main__":
#    show()

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import  QWebEngineView

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel("Test", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: red;}")

        self.button = QPushButton("Test", self)

        self.webView = QWebEngineView();
        self.webView.load(QUrl("http://google.com"))
        self.webView.show()

        self.layout = QGridLayout()
        #self.layout.addWidget(self.label, 0, 0)
        #self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.webView, 0, 0)

        self.setLayout(self.layout)

qtApp = QApplication(sys.argv)
qtWindow = Window()
qtWindow.show()
sys.exit(qtApp.exec_())
