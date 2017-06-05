
import os

from PyQt4 import QtGui, QtCore


def getUi(uiFileName):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", uiFileName)


def openUrl(url):
    QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))


def showWidget(w, isModal=False):
    if isModal:
        w.setWindowModality(QtCore.Qt.ApplicationModal)
    w.show()
    w.raise_()
