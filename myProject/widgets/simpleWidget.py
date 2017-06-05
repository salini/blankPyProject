


import PyQt4.uic
from PyQt4 import QtGui

from common import getUi, openUrl

from ..core import helloFunction


class SimpleWidget(QtGui.QWidget):

    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)
        PyQt4.uic.loadUi(getUi("SimpleWidget.ui"), self)

        self.printBtn.clicked.connect(self.printBtn_clicked)
        self.webBtn.clicked.connect(self.webBtn_clicked)
        self.quitBtn.clicked.connect(self.quitBtn_clicked)


    def printBtn_clicked(self):
        self.printLabel.setText(helloFunction())

    @staticmethod
    def webBtn_clicked():
        openUrl("https://github.com/salini/virginPyProject")

    @staticmethod
    def quitBtn_clicked():
        QtGui.QApplication.quit()
