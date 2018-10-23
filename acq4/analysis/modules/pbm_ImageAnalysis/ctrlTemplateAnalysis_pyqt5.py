# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/analysis/modules/pbm_ImageAnalysis/ctrlTemplateAnalysis.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = Qt.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(Qt.QSize(0, 380))
        self.groupBox.setAlignment(Qt.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 1, 2, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 1)
        self.IAFuncs_widget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IAFuncs_widget.sizePolicy().hasHeightForWidth())
        self.IAFuncs_widget.setSizePolicy(sizePolicy)
        self.IAFuncs_widget.setObjectName("IAFuncs_widget")
        self.IAFuncs_checkbox_TraceLabels = QtWidgets.QCheckBox(self.IAFuncs_widget)
        self.IAFuncs_checkbox_TraceLabels.setGeometry(Qt.QRect(10, 360, 83, 18))
        self.IAFuncs_checkbox_TraceLabels.setChecked(True)
        self.IAFuncs_checkbox_TraceLabels.setObjectName("IAFuncs_checkbox_TraceLabels")
        self.widget = QtWidgets.QWidget(self.IAFuncs_widget)
        self.widget.setGeometry(Qt.QRect(180, 0, 196, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(Qt.QRect(10, 10, 136, 16))
        self.label_15.setObjectName("label_15")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(Qt.QRect(10, 30, 176, 186))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(9, 9, 9, 9)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.smc_Kd = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.smc_Kd.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.smc_Kd.setDecimals(0)
        self.smc_Kd.setMinimum(0.0)
        self.smc_Kd.setMaximum(5000.0)
        self.smc_Kd.setProperty("value", 345.0)
        self.smc_Kd.setObjectName("smc_Kd")
        self.horizontalLayout_2.addWidget(self.smc_Kd)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.smc_TCa = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.smc_TCa.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.smc_TCa.setDecimals(3)
        self.smc_TCa.setMinimum(0.001)
        self.smc_TCa.setMaximum(5.0)
        self.smc_TCa.setSingleStep(0.01)
        self.smc_TCa.setProperty("value", 0.025)
        self.smc_TCa.setObjectName("smc_TCa")
        self.horizontalLayout_3.addWidget(self.smc_TCa)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.smc_C0 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.smc_C0.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.smc_C0.setDecimals(3)
        self.smc_C0.setMinimum(0.01)
        self.smc_C0.setMaximum(1000.0)
        self.smc_C0.setObjectName("smc_C0")
        self.horizontalLayout_4.addWidget(self.smc_C0)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.smc_Amplitude = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.smc_Amplitude.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.smc_Amplitude.setMaximum(1000.0)
        self.smc_Amplitude.setSingleStep(0.1)
        self.smc_Amplitude.setProperty("value", 1.0)
        self.smc_Amplitude.setObjectName("smc_Amplitude")
        self.horizontalLayout.addWidget(self.smc_Amplitude)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.IAFuncs_Analysis_smcAnalyze = QtWidgets.QPushButton(self.layoutWidget)
        self.IAFuncs_Analysis_smcAnalyze.setObjectName("IAFuncs_Analysis_smcAnalyze")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.IAFuncs_Analysis_smcAnalyze)
        self.IAFuncs_Analysis_SpikeXCorr = QtWidgets.QPushButton(self.layoutWidget)
        self.IAFuncs_Analysis_SpikeXCorr.setObjectName("IAFuncs_Analysis_SpikeXCorr")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.IAFuncs_Analysis_SpikeXCorr)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(Qt.QRect(10, 220, 176, 140))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.widget1)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.line_4 = QtWidgets.QFrame(self.widget1)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.IAFuncs_Analysis_AFFT = QtWidgets.QPushButton(self.widget1)
        self.IAFuncs_Analysis_AFFT.setText("Avg FFT")
        self.IAFuncs_Analysis_AFFT.setObjectName("IAFuncs_Analysis_AFFT")
        self.verticalLayout.addWidget(self.IAFuncs_Analysis_AFFT)
        self.IAFuncs_Analysis_AFFT_Individual = QtWidgets.QPushButton(self.widget1)
        self.IAFuncs_Analysis_AFFT_Individual.setObjectName("IAFuncs_Analysis_AFFT_Individual")
        self.verticalLayout.addWidget(self.IAFuncs_Analysis_AFFT_Individual)
        self.IAFuncs_Analysis_FourierMap = QtWidgets.QPushButton(self.widget1)
        self.IAFuncs_Analysis_FourierMap.setObjectName("IAFuncs_Analysis_FourierMap")
        self.verticalLayout.addWidget(self.IAFuncs_Analysis_FourierMap)
        self.layoutWidget1 = QtWidgets.QWidget(self.IAFuncs_widget)
        self.layoutWidget1.setGeometry(Qt.QRect(10, 110, 171, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setContentsMargins(9, 9, 9, 9)
        self.formLayout_4.setSpacing(0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.IAFuncs_Analysis_AXCorr_Individual = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_Analysis_AXCorr_Individual.setObjectName("IAFuncs_Analysis_AXCorr_Individual")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_Analysis_AXCorr_Individual)
        self.IAFuncs_Analysis_UnbiasedXC = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_Analysis_UnbiasedXC.setObjectName("IAFuncs_Analysis_UnbiasedXC")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_Analysis_UnbiasedXC)
        self.IAFuncs_Distance = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_Distance.setObjectName("IAFuncs_Distance")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_Distance)
        self.IAFuncs_DistanceStrength = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_DistanceStrength.setObjectName("IAFuncs_DistanceStrength")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_DistanceStrength)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(9, 9, 9, 9)
        self.formLayout_3.setSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.IAFuncs_XCorrThreshold = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.IAFuncs_XCorrThreshold.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.IAFuncs_XCorrThreshold.setMaximum(1.0)
        self.IAFuncs_XCorrThreshold.setSingleStep(0.02)
        self.IAFuncs_XCorrThreshold.setProperty("value", 0.25)
        self.IAFuncs_XCorrThreshold.setObjectName("IAFuncs_XCorrThreshold")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.IAFuncs_XCorrThreshold)
        self.formLayout_4.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.formLayout_3)
        self.IAFuncs_NetworkGraph = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_NetworkGraph.setObjectName("IAFuncs_NetworkGraph")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_NetworkGraph)
        self.IAFuncs_DistanceStrengthPrint = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_DistanceStrengthPrint.setObjectName("IAFuncs_DistanceStrengthPrint")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_DistanceStrengthPrint)
        self.IAFuncs_MatplotlibCheckBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.IAFuncs_MatplotlibCheckBox.setObjectName("IAFuncs_MatplotlibCheckBox")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.IAFuncs_MatplotlibCheckBox)
        self.IAFuncs_Analysis_AXCorr = QtWidgets.QPushButton(self.layoutWidget1)
        self.IAFuncs_Analysis_AXCorr.setObjectName("IAFuncs_Analysis_AXCorr")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.IAFuncs_Analysis_AXCorr)
        self.widget2 = QtWidgets.QWidget(self.IAFuncs_widget)
        self.widget2.setGeometry(Qt.QRect(26, 13, 134, 96))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.widget2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.IAFuncs_AnalogRadioBtn = QtWidgets.QRadioButton(self.widget2)
        self.IAFuncs_AnalogRadioBtn.setChecked(True)
        self.IAFuncs_AnalogRadioBtn.setObjectName("IAFuncs_AnalogRadioBtn")
        self.verticalLayout_2.addWidget(self.IAFuncs_AnalogRadioBtn)
        self.IAFuncs_DigitalRadioBtn = QtWidgets.QRadioButton(self.widget2)
        self.IAFuncs_DigitalRadioBtn.setObjectName("IAFuncs_DigitalRadioBtn")
        self.verticalLayout_2.addWidget(self.IAFuncs_DigitalRadioBtn)
        self.IAFuncs_GetCSVFile = QtWidgets.QPushButton(self.widget2)
        self.IAFuncs_GetCSVFile.setObjectName("IAFuncs_GetCSVFile")
        self.verticalLayout_2.addWidget(self.IAFuncs_GetCSVFile)
        self.gridLayout_2.addWidget(self.IAFuncs_widget, 1, 0, 2, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        Qt.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = Qt.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Imaging Analysis Functions"))
        self.IAFuncs_checkbox_TraceLabels.setText(_translate("Form", "Trace Labels"))
        self.label_15.setText(_translate("Form", "SMC-Calcium Event Detection"))
        self.label_18.setText(_translate("Form", "Kd (nM)"))
        self.label_19.setText(_translate("Form", "TCa  (sec)"))
        self.label_17.setText(_translate("Form", "C0 (uM)"))
        self.label_16.setText(_translate("Form", "A (uM)"))
        self.IAFuncs_Analysis_smcAnalyze.setText(_translate("Form", "SMC"))
        self.IAFuncs_Analysis_SpikeXCorr.setText(_translate("Form", "Digital Xcorr"))
        self.label_13.setText(_translate("Form", "Intrinsic Imaging"))
        self.IAFuncs_Analysis_AFFT.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For Intrinsic Imaging: Compute the average FFT of images. </p></body></html>"))
        self.IAFuncs_Analysis_AFFT_Individual.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For Intrinsic Imaging: Compute the FFT of each image.</p></body></html>"))
        self.IAFuncs_Analysis_AFFT_Individual.setText(_translate("Form", "Individual FFT"))
        self.IAFuncs_Analysis_FourierMap.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For Intrinsic Imaging: Compute the Fourier Phase map relative the the stimulus (Valatsky et al., 2003)</p></body></html>"))
        self.IAFuncs_Analysis_FourierMap.setText(_translate("Form", "Fourier Map"))
        self.IAFuncs_Analysis_AXCorr_Individual.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compute the cross-correlation between each pair of ROI\'s. The computation is done on the analog waveform.</p></body></html>"))
        self.IAFuncs_Analysis_AXCorr_Individual.setText(_translate("Form", "Individual XCorr"))
        self.IAFuncs_Analysis_UnbiasedXC.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compute the cross-correlation between each pair of ROI\'s. The computation is done on the analog waveform.</p></body></html>"))
        self.IAFuncs_Analysis_UnbiasedXC.setText(_translate("Form", "Unbiased XCorr (slow)"))
        self.IAFuncs_Distance.setText(_translate("Form", "ROI Distances"))
        self.IAFuncs_DistanceStrength.setText(_translate("Form", "Distance-Strength"))
        self.label.setText(_translate("Form", "XCorr Thr"))
        self.IAFuncs_NetworkGraph.setText(_translate("Form", "Network Graph"))
        self.IAFuncs_DistanceStrengthPrint.setText(_translate("Form", "Print Dist-Strength"))
        self.IAFuncs_MatplotlibCheckBox.setText(_translate("Form", "MatPlotLib (slower)"))
        self.IAFuncs_Analysis_AXCorr.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compute the average cross-correlation across all pairs of ROIs in the field over time. The computation is done on the analog waveform.</p></body></html>"))
        self.IAFuncs_Analysis_AXCorr.setText(_translate("Form", "Average XCorr"))
        self.label_14.setText(_translate("Form", "Correlation Mode"))
        self.IAFuncs_AnalogRadioBtn.setText(_translate("Form", "Analog"))
        self.IAFuncs_DigitalRadioBtn.setText(_translate("Form", "CSV (digital)"))
        self.IAFuncs_GetCSVFile.setText(_translate("Form", "Select CSV File"))

