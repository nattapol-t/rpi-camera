# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 481)
        self.ipaddrLabel = QtWidgets.QLabel(Form)
        self.ipaddrLabel.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.ipaddrLabel.setObjectName("ipaddrLabel")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 561, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_10.setObjectName("label_10")
        self.blueSliderLabel = QtWidgets.QLabel(self.tab)
        self.blueSliderLabel.setGeometry(QtCore.QRect(480, 130, 51, 16))
        self.blueSliderLabel.setObjectName("blueSliderLabel")
        self.saturationSliderLabel = QtWidgets.QLabel(self.tab)
        self.saturationSliderLabel.setGeometry(QtCore.QRect(480, 260, 51, 16))
        self.saturationSliderLabel.setObjectName("saturationSliderLabel")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 101, 21))
        self.label_5.setObjectName("label_5")
        self.redSliderLabel = QtWidgets.QLabel(self.tab)
        self.redSliderLabel.setGeometry(QtCore.QRect(480, 100, 51, 16))
        self.redSliderLabel.setObjectName("redSliderLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 41, 21))
        self.label_2.setObjectName("label_2")
        self.blueSlider = QtWidgets.QSlider(self.tab)
        self.blueSlider.setGeometry(QtCore.QRect(170, 130, 291, 22))
        self.blueSlider.setMinimum(0)
        self.blueSlider.setMaximum(800)
        self.blueSlider.setSingleStep(0)
        self.blueSlider.setProperty("value", 190)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")
        self.saturationSlider = QtWidgets.QSlider(self.tab)
        self.saturationSlider.setGeometry(QtCore.QRect(130, 260, 331, 22))
        self.saturationSlider.setMinimum(-100)
        self.saturationSlider.setMaximum(100)
        self.saturationSlider.setSingleStep(0)
        self.saturationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.saturationSlider.setObjectName("saturationSlider")
        self.brightnessSliderLabel = QtWidgets.QLabel(self.tab)
        self.brightnessSliderLabel.setGeometry(QtCore.QRect(480, 200, 51, 16))
        self.brightnessSliderLabel.setObjectName("brightnessSliderLabel")
        self.rotationBox = QtWidgets.QComboBox(self.tab)
        self.rotationBox.setGeometry(QtCore.QRect(130, 60, 51, 22))
        self.rotationBox.setObjectName("rotationBox")
        self.rotationBox.addItem("")
        self.rotationBox.addItem("")
        self.rotationBox.addItem("")
        self.rotationBox.addItem("")
        self.saveImageButton = QtWidgets.QPushButton(self.tab)
        self.saveImageButton.setGeometry(QtCore.QRect(110, 340, 91, 23))
        self.saveImageButton.setObjectName("saveImageButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 100, 81, 21))
        self.label.setObjectName("label")
        self.previewButton = QtWidgets.QPushButton(self.tab)
        self.previewButton.setGeometry(QtCore.QRect(390, 20, 141, 23))
        self.previewButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previewButton.setCheckable(False)
        self.previewButton.setObjectName("previewButton")
        self.brightnessSlider = QtWidgets.QSlider(self.tab)
        self.brightnessSlider.setGeometry(QtCore.QRect(130, 200, 331, 22))
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setSingleStep(0)
        self.brightnessSlider.setProperty("value", 50)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.isoSlider = QtWidgets.QSlider(self.tab)
        self.isoSlider.setGeometry(QtCore.QRect(130, 170, 331, 22))
        self.isoSlider.setMinimum(0)
        self.isoSlider.setMaximum(300)
        self.isoSlider.setSingleStep(0)
        self.isoSlider.setProperty("value", 100)
        self.isoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.isoSlider.setObjectName("isoSlider")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 81, 21))
        self.label_9.setObjectName("label_9")
        self.resolutionBox = QtWidgets.QComboBox(self.tab)
        self.resolutionBox.setGeometry(QtCore.QRect(130, 20, 131, 22))
        self.resolutionBox.setObjectName("resolutionBox")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.shutterspeedSlider = QtWidgets.QSlider(self.tab)
        self.shutterspeedSlider.setGeometry(QtCore.QRect(130, 290, 331, 22))
        self.shutterspeedSlider.setMouseTracking(False)
        self.shutterspeedSlider.setMinimum(0)
        self.shutterspeedSlider.setMaximum(33243)
        self.shutterspeedSlider.setSingleStep(0)
        self.shutterspeedSlider.setProperty("value", 20000)
        self.shutterspeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.shutterspeedSlider.setObjectName("shutterspeedSlider")
        self.redSlider = QtWidgets.QSlider(self.tab)
        self.redSlider.setGeometry(QtCore.QRect(170, 100, 291, 22))
        self.redSlider.setMinimum(0)
        self.redSlider.setMaximum(800)
        self.redSlider.setSingleStep(0)
        self.redSlider.setProperty("value", 90)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName("redSlider")
        self.shutterspeedSliderLabel = QtWidgets.QLabel(self.tab)
        self.shutterspeedSliderLabel.setGeometry(QtCore.QRect(480, 290, 51, 16))
        self.shutterspeedSliderLabel.setObjectName("shutterspeedSliderLabel")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 101, 21))
        self.label_6.setObjectName("label_6")
        self.contrastSlider = QtWidgets.QSlider(self.tab)
        self.contrastSlider.setGeometry(QtCore.QRect(130, 230, 331, 22))
        self.contrastSlider.setMinimum(-100)
        self.contrastSlider.setMaximum(100)
        self.contrastSlider.setSingleStep(0)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(130, 130, 41, 21))
        self.label_3.setObjectName("label_3")
        self.isoSliderLabel = QtWidgets.QLabel(self.tab)
        self.isoSliderLabel.setGeometry(QtCore.QRect(480, 170, 51, 16))
        self.isoSliderLabel.setObjectName("isoSliderLabel")
        self.captureButton = QtWidgets.QPushButton(self.tab)
        self.captureButton.setGeometry(QtCore.QRect(20, 340, 75, 23))
        self.captureButton.setObjectName("captureButton")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_7.setObjectName("label_7")
        self.contrastSliderLabel = QtWidgets.QLabel(self.tab)
        self.contrastSliderLabel.setGeometry(QtCore.QRect(480, 230, 51, 16))
        self.contrastSliderLabel.setObjectName("contrastSliderLabel")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 290, 101, 21))
        self.label_8.setObjectName("label_8")
        self.histogramButton = QtWidgets.QPushButton(self.tab)
        self.histogramButton.setGeometry(QtCore.QRect(460, 340, 75, 23))
        self.histogramButton.setObjectName("histogramButton")
        self.colorCvtButton = QtWidgets.QPushButton(self.tab)
        self.colorCvtButton.setGeometry(QtCore.QRect(370, 340, 75, 23))
        self.colorCvtButton.setObjectName("colorCvtButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.neoBSliderLabel = QtWidgets.QLabel(self.tab_2)
        self.neoBSliderLabel.setGeometry(QtCore.QRect(500, 140, 47, 13))
        self.neoBSliderLabel.setObjectName("neoBSliderLabel")
        self.neoBSlider = QtWidgets.QSlider(self.tab_2)
        self.neoBSlider.setGeometry(QtCore.QRect(130, 140, 351, 22))
        self.neoBSlider.setMaximum(255)
        self.neoBSlider.setProperty("value", 255)
        self.neoBSlider.setOrientation(QtCore.Qt.Horizontal)
        self.neoBSlider.setObjectName("neoBSlider")
        self.neoRSlider = QtWidgets.QSlider(self.tab_2)
        self.neoRSlider.setGeometry(QtCore.QRect(130, 80, 351, 22))
        self.neoRSlider.setMaximum(255)
        self.neoRSlider.setProperty("value", 255)
        self.neoRSlider.setOrientation(QtCore.Qt.Horizontal)
        self.neoRSlider.setObjectName("neoRSlider")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label_18.setObjectName("label_18")
        self.neoGSlider = QtWidgets.QSlider(self.tab_2)
        self.neoGSlider.setGeometry(QtCore.QRect(130, 110, 351, 22))
        self.neoGSlider.setMaximum(255)
        self.neoGSlider.setProperty("value", 255)
        self.neoGSlider.setOrientation(QtCore.Qt.Horizontal)
        self.neoGSlider.setObjectName("neoGSlider")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 47, 31))
        self.label_12.setObjectName("label_12")
        self.neoBrightSlider = QtWidgets.QSlider(self.tab_2)
        self.neoBrightSlider.setGeometry(QtCore.QRect(130, 30, 351, 22))
        self.neoBrightSlider.setMaximum(10)
        self.neoBrightSlider.setProperty("value", 10)
        self.neoBrightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.neoBrightSlider.setObjectName("neoBrightSlider")
        self.neoRSliderLabel = QtWidgets.QLabel(self.tab_2)
        self.neoRSliderLabel.setGeometry(QtCore.QRect(500, 80, 47, 13))
        self.neoRSliderLabel.setObjectName("neoRSliderLabel")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 130, 47, 31))
        self.label_16.setObjectName("label_16")
        self.neoBrightSliderLabel = QtWidgets.QLabel(self.tab_2)
        self.neoBrightSliderLabel.setGeometry(QtCore.QRect(500, 30, 47, 13))
        self.neoBrightSliderLabel.setObjectName("neoBrightSliderLabel")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 47, 31))
        self.label_14.setObjectName("label_14")
        self.neoGSliderLabel = QtWidgets.QLabel(self.tab_2)
        self.neoGSliderLabel.setGeometry(QtCore.QRect(500, 110, 47, 13))
        self.neoGSliderLabel.setObjectName("neoGSliderLabel")
        self.tabWidget.addTab(self.tab_2, "")
        self.saveSettingButton = QtWidgets.QPushButton(Form)
        self.saveSettingButton.setGeometry(QtCore.QRect(480, 440, 101, 23))
        self.saveSettingButton.setObjectName("saveSettingButton")
        self.resetSettingButton = QtWidgets.QPushButton(Form)
        self.resetSettingButton.setGeometry(QtCore.QRect(380, 440, 81, 23))
        self.resetSettingButton.setObjectName("resetSettingButton")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Camera"))
        self.ipaddrLabel.setText(_translate("Form", "xx.xx.xx.xxx"))
        self.label_10.setText(_translate("Form", "resolution"))
        self.blueSliderLabel.setText(_translate("Form", "blueSliderLabel"))
        self.saturationSliderLabel.setText(_translate("Form", "saturationSliderLabel"))
        self.label_5.setText(_translate("Form", "contrast"))
        self.redSliderLabel.setText(_translate("Form", "redSliderLabel"))
        self.label_2.setText(_translate("Form", "red"))
        self.brightnessSliderLabel.setText(_translate("Form", "brightnessSliderLabel"))
        self.rotationBox.setItemText(0, _translate("Form", "0"))
        self.rotationBox.setItemText(1, _translate("Form", "90"))
        self.rotationBox.setItemText(2, _translate("Form", "180"))
        self.rotationBox.setItemText(3, _translate("Form", "270"))
        self.saveImageButton.setText(_translate("Form", "Save Image"))
        self.label.setText(_translate("Form", "awb_gains"))
        self.previewButton.setText(_translate("Form", "Fullscreen Preview"))
        self.label_9.setText(_translate("Form", "iso"))
        self.resolutionBox.setItemText(0, _translate("Form", "1920x1080"))
        self.resolutionBox.setItemText(1, _translate("Form", "3280x2464"))
        self.resolutionBox.setItemText(2, _translate("Form", "1640x1232"))
        self.resolutionBox.setItemText(3, _translate("Form", "1640x922"))
        self.resolutionBox.setItemText(4, _translate("Form", "1280x720"))
        self.resolutionBox.setItemText(5, _translate("Form", "640x480"))
        self.shutterspeedSliderLabel.setText(_translate("Form", "shutterspeedSliderLabel"))
        self.label_6.setText(_translate("Form", "saturation"))
        self.label_3.setText(_translate("Form", "blue"))
        self.isoSliderLabel.setText(_translate("Form", "isoSliderLabel"))
        self.captureButton.setText(_translate("Form", "Capture"))
        self.label_7.setText(_translate("Form", "rotation"))
        self.contrastSliderLabel.setText(_translate("Form", "contrastSliderLabel"))
        self.label_4.setText(_translate("Form", "brightness"))
        self.label_8.setText(_translate("Form", "shutter_speed"))
        self.histogramButton.setText(_translate("Form", "Histogram"))
        self.colorCvtButton.setText(_translate("Form", "BGR2GRAY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "camera"))
        self.neoBSliderLabel.setText(_translate("Form", "255"))
        self.label_18.setText(_translate("Form", "brightness"))
        self.label_12.setText(_translate("Form", "red"))
        self.neoRSliderLabel.setText(_translate("Form", "255"))
        self.label_16.setText(_translate("Form", "blue"))
        self.neoBrightSliderLabel.setText(_translate("Form", "1.0"))
        self.label_14.setText(_translate("Form", "green"))
        self.neoGSliderLabel.setText(_translate("Form", "255"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "neopixel"))
        self.saveSettingButton.setText(_translate("Form", "Save setting"))
        self.resetSettingButton.setText(_translate("Form", "Reset"))
