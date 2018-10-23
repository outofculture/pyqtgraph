# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/devices/SutterMP285/devTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 221)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setAlignment(Qt.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setMinimumSize(Qt.QSize(100, 0))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.xPosLabel = QtWidgets.QLabel(self.widget)
        self.xPosLabel.setObjectName("xPosLabel")
        self.gridLayout.addWidget(self.xPosLabel, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.yPosLabel = QtWidgets.QLabel(self.widget)
        self.yPosLabel.setObjectName("yPosLabel")
        self.gridLayout.addWidget(self.yPosLabel, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.zPosLabel = QtWidgets.QLabel(self.widget)
        self.zPosLabel.setObjectName("zPosLabel")
        self.gridLayout.addWidget(self.zPosLabel, 2, 1, 1, 1)
        self.updatePosBtn = QtWidgets.QPushButton(self.widget)
        self.updatePosBtn.setObjectName("updatePosBtn")
        self.gridLayout.addWidget(self.updatePosBtn, 3, 0, 1, 2)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.joyBtn = JoystickButton(self.groupBox_2)
        self.joyBtn.setMinimumSize(Qt.QSize(50, 50))
        self.joyBtn.setText("")
        self.joyBtn.setObjectName("joyBtn")
        self.gridLayout_3.addWidget(self.joyBtn, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fineStepRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.fineStepRadio.setChecked(True)
        self.fineStepRadio.setObjectName("fineStepRadio")
        self.horizontalLayout_2.addWidget(self.fineStepRadio)
        self.coarseStepRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.coarseStepRadio.setObjectName("coarseStepRadio")
        self.horizontalLayout_2.addWidget(self.coarseStepRadio)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.limitsGroup = QtWidgets.QGroupBox(Form)
        self.limitsGroup.setAlignment(Qt.Qt.AlignCenter)
        self.limitsGroup.setCheckable(False)
        self.limitsGroup.setObjectName("limitsGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.limitsGroup)
        self.gridLayout_2.setContentsMargins(3, 0, 3, 0)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xMinBtn = QtWidgets.QPushButton(self.limitsGroup)
        self.xMinBtn.setMaximumSize(Qt.QSize(70, 20))
        self.xMinBtn.setObjectName("xMinBtn")
        self.gridLayout_2.addWidget(self.xMinBtn, 0, 3, 1, 1)
        self.xMinLabel = QtWidgets.QLabel(self.limitsGroup)
        self.xMinLabel.setObjectName("xMinLabel")
        self.gridLayout_2.addWidget(self.xMinLabel, 0, 4, 1, 1)
        self.xMaxLabel = QtWidgets.QLabel(self.limitsGroup)
        self.xMaxLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.xMaxLabel.setObjectName("xMaxLabel")
        self.gridLayout_2.addWidget(self.xMaxLabel, 0, 6, 1, 1)
        self.xMaxBtn = QtWidgets.QPushButton(self.limitsGroup)
        self.xMaxBtn.setMaximumSize(Qt.QSize(70, 20))
        self.xMaxBtn.setObjectName("xMaxBtn")
        self.gridLayout_2.addWidget(self.xMaxBtn, 0, 7, 1, 1)
        self.yMinBtn = QtWidgets.QPushButton(self.limitsGroup)
        self.yMinBtn.setMaximumSize(Qt.QSize(70, 20))
        self.yMinBtn.setObjectName("yMinBtn")
        self.gridLayout_2.addWidget(self.yMinBtn, 1, 3, 1, 1)
        self.yMinLabel = QtWidgets.QLabel(self.limitsGroup)
        self.yMinLabel.setObjectName("yMinLabel")
        self.gridLayout_2.addWidget(self.yMinLabel, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.limitsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 5, 1, 1)
        self.yMaxLabel = QtWidgets.QLabel(self.limitsGroup)
        self.yMaxLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.yMaxLabel.setObjectName("yMaxLabel")
        self.gridLayout_2.addWidget(self.yMaxLabel, 1, 6, 1, 1)
        self.yMaxBtn = QtWidgets.QPushButton(self.limitsGroup)
        self.yMaxBtn.setMaximumSize(Qt.QSize(70, 20))
        self.yMaxBtn.setObjectName("yMaxBtn")
        self.gridLayout_2.addWidget(self.yMaxBtn, 1, 7, 1, 1)
        self.zMinBtn = QtWidgets.QPushButton(self.limitsGroup)
        self.zMinBtn.setMaximumSize(Qt.QSize(70, 20))
        self.zMinBtn.setObjectName("zMinBtn")
        self.gridLayout_2.addWidget(self.zMinBtn, 2, 3, 1, 1)
        self.zMinLabel = QtWidgets.QLabel(self.limitsGroup)
        self.zMinLabel.setObjectName("zMinLabel")
        self.gridLayout_2.addWidget(self.zMinLabel, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.limitsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 5, 1, 1)
        self.zMaxLabel = QtWidgets.QLabel(self.limitsGroup)
        self.zMaxLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.zMaxLabel.setObjectName("zMaxLabel")
        self.gridLayout_2.addWidget(self.zMaxLabel, 2, 6, 1, 1)
        self.zMaxBtn = QtWidgets.QPushButton(self.limitsGroup)
        self.zMaxBtn.setMaximumSize(Qt.QSize(70, 20))
        self.zMaxBtn.setObjectName("zMaxBtn")
        self.gridLayout_2.addWidget(self.zMaxBtn, 2, 7, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.limitsGroup)
        self.label_4.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.maxSpeedSpin = SpinBox(self.limitsGroup)
        self.maxSpeedSpin.setObjectName("maxSpeedSpin")
        self.horizontalLayout_3.addWidget(self.maxSpeedSpin)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 3, 1, 5)
        self.xMinCheck = QtWidgets.QCheckBox(self.limitsGroup)
        self.xMinCheck.setText("")
        self.xMinCheck.setObjectName("xMinCheck")
        self.gridLayout_2.addWidget(self.xMinCheck, 0, 0, 1, 1)
        self.yMinCheck = QtWidgets.QCheckBox(self.limitsGroup)
        self.yMinCheck.setText("")
        self.yMinCheck.setObjectName("yMinCheck")
        self.gridLayout_2.addWidget(self.yMinCheck, 1, 0, 1, 1)
        self.zMinCheck = QtWidgets.QCheckBox(self.limitsGroup)
        self.zMinCheck.setText("")
        self.zMinCheck.setObjectName("zMinCheck")
        self.gridLayout_2.addWidget(self.zMinCheck, 2, 0, 1, 1)
        self.xMaxCheck = QtWidgets.QCheckBox(self.limitsGroup)
        self.xMaxCheck.setText("")
        self.xMaxCheck.setObjectName("xMaxCheck")
        self.gridLayout_2.addWidget(self.xMaxCheck, 0, 9, 1, 1)
        self.yMaxCheck = QtWidgets.QCheckBox(self.limitsGroup)
        self.yMaxCheck.setText("")
        self.yMaxCheck.setObjectName("yMaxCheck")
        self.gridLayout_2.addWidget(self.yMaxCheck, 1, 9, 1, 1)
        self.zMaxCheck = QtWidgets.QCheckBox(self.limitsGroup)
        self.zMaxCheck.setText("")
        self.zMaxCheck.setObjectName("zMaxCheck")
        self.gridLayout_2.addWidget(self.zMaxCheck, 2, 9, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.limitsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 5, 1, 1)
        self.xMinSpin = SpinBox(self.limitsGroup)
        self.xMinSpin.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.xMinSpin.setDecimals(3)
        self.xMinSpin.setMinimum(-25000.0)
        self.xMinSpin.setMaximum(25000.0)
        self.xMinSpin.setSingleStep(0.1)
        self.xMinSpin.setObjectName("xMinSpin")
        self.gridLayout_2.addWidget(self.xMinSpin, 0, 2, 1, 1)
        self.yMinSpin = SpinBox(self.limitsGroup)
        self.yMinSpin.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.yMinSpin.setDecimals(3)
        self.yMinSpin.setMinimum(-25000.0)
        self.yMinSpin.setMaximum(25000.0)
        self.yMinSpin.setSingleStep(0.1)
        self.yMinSpin.setObjectName("yMinSpin")
        self.gridLayout_2.addWidget(self.yMinSpin, 1, 2, 1, 1)
        self.zMinSpin = SpinBox(self.limitsGroup)
        self.zMinSpin.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.zMinSpin.setDecimals(3)
        self.zMinSpin.setMinimum(-25000.0)
        self.zMinSpin.setMaximum(25000.0)
        self.zMinSpin.setSingleStep(0.1)
        self.zMinSpin.setObjectName("zMinSpin")
        self.gridLayout_2.addWidget(self.zMinSpin, 2, 2, 1, 1)
        self.xMaxSpin = SpinBox(self.limitsGroup)
        self.xMaxSpin.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.xMaxSpin.setDecimals(3)
        self.xMaxSpin.setMinimum(-25000.0)
        self.xMaxSpin.setMaximum(25000.0)
        self.xMaxSpin.setSingleStep(0.1)
        self.xMaxSpin.setObjectName("xMaxSpin")
        self.gridLayout_2.addWidget(self.xMaxSpin, 0, 8, 1, 1)
        self.yMaxSpin = SpinBox(self.limitsGroup)
        self.yMaxSpin.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.yMaxSpin.setDecimals(3)
        self.yMaxSpin.setMinimum(-25000.0)
        self.yMaxSpin.setMaximum(25000.0)
        self.yMaxSpin.setSingleStep(0.1)
        self.yMaxSpin.setObjectName("yMaxSpin")
        self.gridLayout_2.addWidget(self.yMaxSpin, 1, 8, 1, 1)
        self.zMaxSpin = SpinBox(self.limitsGroup)
        self.zMaxSpin.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.zMaxSpin.setDecimals(3)
        self.zMaxSpin.setMinimum(-25000.0)
        self.zMaxSpin.setMaximum(25000.0)
        self.zMaxSpin.setSingleStep(0.1)
        self.zMaxSpin.setObjectName("zMaxSpin")
        self.gridLayout_2.addWidget(self.zMaxSpin, 2, 8, 1, 1)
        self.gridLayout_4.addWidget(self.limitsGroup, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 1, 1, 1)

        self.retranslateUi(Form)
        Qt.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = Qt.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Position"))
        self.label_5.setText(_translate("Form", "X"))
        self.xPosLabel.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "Y"))
        self.yPosLabel.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "Z"))
        self.zPosLabel.setText(_translate("Form", "0"))
        self.updatePosBtn.setText(_translate("Form", "Update"))
        self.fineStepRadio.setText(_translate("Form", "Fine step"))
        self.coarseStepRadio.setText(_translate("Form", "Coarse step"))
        self.limitsGroup.setTitle(_translate("Form", "Limits"))
        self.xMinBtn.setText(_translate("Form", "get Current"))
        self.xMinLabel.setText(_translate("Form", "<--"))
        self.xMaxLabel.setText(_translate("Form", "-->"))
        self.xMaxBtn.setText(_translate("Form", "get Current"))
        self.yMinBtn.setText(_translate("Form", "get Current"))
        self.yMinLabel.setText(_translate("Form", "<--"))
        self.label_3.setText(_translate("Form", "Y"))
        self.yMaxLabel.setText(_translate("Form", "-->"))
        self.yMaxBtn.setText(_translate("Form", "get Current"))
        self.zMinBtn.setText(_translate("Form", "get Current"))
        self.zMinLabel.setText(_translate("Form", "<--"))
        self.label.setText(_translate("Form", "Z"))
        self.zMaxLabel.setText(_translate("Form", "-->"))
        self.zMaxBtn.setText(_translate("Form", "get Current"))
        self.label_4.setText(_translate("Form", "Max Speed"))
        self.label_2.setText(_translate("Form", "X"))
        self.xMinSpin.setSuffix(_translate("Form", " mm"))
        self.yMinSpin.setSuffix(_translate("Form", " mm"))
        self.zMinSpin.setSuffix(_translate("Form", " mm"))
        self.xMaxSpin.setSuffix(_translate("Form", " mm"))
        self.yMaxSpin.setSuffix(_translate("Form", " mm"))
        self.zMaxSpin.setSuffix(_translate("Form", " mm"))

from acq4.pyqtgraph import JoystickButton, SpinBox
