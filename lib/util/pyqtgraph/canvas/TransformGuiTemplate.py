# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/util/pyqtgraph/canvas/TransformGuiTemplate.ui'
#
# Created: Thu Feb  2 15:25:11 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(169, 82)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.translateLabel = QtGui.QLabel(Form)
        self.translateLabel.setObjectName(_fromUtf8("translateLabel"))
        self.verticalLayout.addWidget(self.translateLabel)
        self.rotateLabel = QtGui.QLabel(Form)
        self.rotateLabel.setObjectName(_fromUtf8("rotateLabel"))
        self.verticalLayout.addWidget(self.rotateLabel)
        self.scaleLabel = QtGui.QLabel(Form)
        self.scaleLabel.setObjectName(_fromUtf8("scaleLabel"))
        self.verticalLayout.addWidget(self.scaleLabel)
        self.mirrorImageBtn = QtGui.QPushButton(Form)
        self.mirrorImageBtn.setToolTip(_fromUtf8(""))
        self.mirrorImageBtn.setObjectName(_fromUtf8("mirrorImageBtn"))
        self.verticalLayout.addWidget(self.mirrorImageBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.translateLabel.setText(QtGui.QApplication.translate("Form", "Translate:", None, QtGui.QApplication.UnicodeUTF8))
        self.rotateLabel.setText(QtGui.QApplication.translate("Form", "Rotate:", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleLabel.setText(QtGui.QApplication.translate("Form", "Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.mirrorImageBtn.setText(QtGui.QApplication.translate("Form", "Mirror", None, QtGui.QApplication.UnicodeUTF8))

