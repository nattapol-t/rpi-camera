import cv2
import board
import neopixel
import numpy as np
import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect
from ui import Ui_Form
from camera import Camera
from time import sleep
from matplotlib import pyplot as plt

class CameraInterface(Ui_Form,Camera):

    config = configparser.ConfigParser()
    pixels = neopixel.NeoPixel(board.D18,8,brightness=0.2)

    def __init__(self,title=""):
        self.title = title
        cv2.namedWindow('capture',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('capture',int(round(1920/2)),int(round(1080/2)))
        cv2.setMouseCallback('capture',self.mouseCallback)
        self.picture = None
        self.img_index = 1
    
    def mouseCallback(self,e,x,y,f,p):
        if e==cv2.EVENT_LBUTTONDOWN:
            self.x1y1 = (x,y)
        elif e==cv2.EVENT_LBUTTONUP:
            self.x2y2 = (x,y)
            if self.picture is not None and self.x1y1 != self.x2y2:
                self.picture = self.picture[self.x1y1[1]:self.x2y2[1],self.x1y1[0]:self.x2y2[0]]
                self.resizeWindow(int(self.picture.shape[1]),int(self.picture.shape[0]),True)
                cv2.imshow('capture',self.picture)

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.loadConfig()
        self.preview()
        MainWindow.setWindowTitle(self.title)
        self.brightnessSliderLabel.setText(str(self.brightnessSlider.value()))
        self.contrastSliderLabel.setText(str(self.contrastSlider.value()))
        self.saturationSliderLabel.setText(str(self.saturationSlider.value()))
        self.shutterspeedSliderLabel.setText(str(self.shutterspeedSlider.value()))
        self.isoSliderLabel.setText(str(self.isoSlider.value()))
        self.blueSliderLabel.setText(str(int(self.blueSlider.value())/100))
        self.redSliderLabel.setText(str(int(self.redSlider.value())/100))
        try:
            self.ipaddrLabel.setText(os.popen('ip addr show wlan0').read().split('inet ')[1].split('/')[0])
        except:
            self.ipaddrLabel.setText('xx.xx.xxx.xxx')
        self.resolutionBox.currentIndexChanged.connect(lambda: self.objValueChange(
            self.resolutionBox,'resolution'))
        self.rotationBox.currentIndexChanged.connect(lambda: self.objValueChange(
            self.rotationBox,'rotation'))
        self.redSlider.valueChanged.connect(lambda: self.objValueChange(
            self.redSlider,self.redSliderLabel,'red_color'))
        self.blueSlider.valueChanged.connect(lambda: self.objValueChange(
            self.blueSlider,self.blueSliderLabel,'blue_color'))
        self.isoSlider.valueChanged.connect(lambda: self.objValueChange(
            self.isoSlider,self.isoSliderLabel,'iso'))
        self.brightnessSlider.valueChanged.connect(lambda: self.objValueChange(
            self.brightnessSlider,self.brightnessSliderLabel,'brightness'))
        self.contrastSlider.valueChanged.connect(lambda: self.objValueChange(
            self.contrastSlider,self.contrastSliderLabel,'contrast'))
        self.saturationSlider.valueChanged.connect(lambda: self.objValueChange(
            self.saturationSlider,self.saturationSliderLabel,'saturation'))
        self.shutterspeedSlider.valueChanged.connect(lambda: self.objValueChange(
            self.shutterspeedSlider,self.shutterspeedSliderLabel,'shutter_speed'))
        self.saveSettingButton.clicked.connect(self.saveConfig)
        self.previewButton.clicked.connect(lambda: self.preview())
        self.captureButton.clicked.connect(lambda: self.captureEvent())
        self.resetSettingButton.clicked.connect(lambda: self.resetSetting())
        self.neoBrightSlider.valueChanged.connect(lambda: self.objValueChange(
            self.neoBrightSlider,self.neoBrightSliderLabel,'neopixel_brigntness'))
        self.neoBSlider.valueChanged.connect(lambda: self.objValueChange(
            self.neoBSlider,self.neoBSliderLabel,'neopixel_blue'))
        self.neoGSlider.valueChanged.connect(lambda: self.objValueChange(
            self.neoGSlider,self.neoGSliderLabel,'neopixel_green'))
        self.neoRSlider.valueChanged.connect(lambda: self.objValueChange(
            self.neoRSlider,self.neoRSliderLabel,'neopixel_red'))
        self.saveImageButton.clicked.connect(self.savePicture)
        self.colorCvtButton.clicked.connect(self.colorConverter)
        self.histogramButton.clicked.connect(self.histogram)
        MainWindow.keyPressEvent = self.pressEvent

    def objValueChange(self, obj, label, conf=None):
        if conf is not None:
            self.config['configs'][conf] = str(obj.value())
            label.setText(self.config['configs'][conf])
        if conf == 'iso':
            self.camera.iso = obj.value()
        elif conf == 'brightness':
            self.camera.brightness = obj.value()
        elif conf == 'contrast':
            self.camera.contrast = obj.value()
        elif conf == 'saturation':
            self.camera.saturation = obj.value()
        elif conf == 'shutter_speed':
            self.camera.shutter_speed = obj.value()
        elif conf == 'red_color':
            self.config['configs']['red_color'] = str(round(obj.value()*0.01,2))
            label.setText(self.config['configs']['red_color'])
            self.camera.awb_gains = (float(round(self.redSlider.value()*0.01,2))
            ,float(round(self.blueSlider.value()*0.01,2)))
        elif conf == 'blue_color':
            self.config['configs']['blue_color'] = str(round(obj.value()*0.01,2))
            label.setText(self.config['configs']['blue_color'])
            self.camera.awb_gains = (float(round(self.redSlider.value()*0.01,2))
            ,float(round(self.blueSlider.value()*0.01,2)))
        elif label == 'resolution':
            self.config['configs'][label] = self.camera.resolution = obj.currentText()
            if str(self.camera.resolution) == '1920x1080':
                self.use_video_port = True
            else:
                self.use_video_port = False
            self.config['configs']['use_video_port'] = str(self.use_video_port)
            w,h = self.config['configs'][label].split('x')
            self.resizeWindow(int(w),int(h))
        elif label == 'rotation':
            self.config['configs'][label] = str(obj.currentText())
            self.camera.rotation = int(self.config['configs'][label])
        elif conf == 'neopixel_brigntness':
            self.config['configs']['neopixel_brigntness'] = str(round(obj.value()/10,1))
            label.setText(self.config['configs']['neopixel_brigntness'])
            self.pixels.brightness = float(self.config['configs']['neopixel_brigntness'])
            self.pixels.show()
        elif conf in ['neopixel_blue','neopixel_green','neopixel_red']:
            self.config['configs']['neopixel_blue'] = str(self.neoBSlider.value())
            self.config['configs']['neopixel_green'] = str(self.neoGSlider.value())
            self.config['configs']['neopixel_red'] = str(self.neoRSlider.value())
            label.setText(str(obj.value()))
            self.pixels.fill((self.neoRSlider.value(), self.neoGSlider.value(), self.neoBSlider.value()))
            self.pixels.show()

    def saveConfig(self):
        print('saveConfig')
        with open(self.path + '/camera.ini','w') as configfile:
            self.config.write(configfile)

    def loadConfig(self):
        if os.path.isfile(self.path + '/camera.ini'):
            self.config.read(self.path + '/camera.ini')
            self.resolutionBox.setCurrentIndex(self.resolutionBox.findText(
                self.config['configs']['resolution'],QtCore.Qt.MatchFixedString))
            self.rotationBox.setCurrentIndex(self.rotationBox.findText(
                self.config['configs']['rotation'],QtCore.Qt.MatchFixedString))
            self.brightnessSliderLabel.setText(self.config['configs']['brightness'])
            self.contrastSliderLabel.setText(self.config['configs']['contrast'])
            self.saturationSliderLabel.setText(self.config['configs']['saturation'])
            self.shutterspeedSliderLabel.setText(self.config['configs']['shutter_speed'])
            self.isoSliderLabel.setText(self.config['configs']['iso'])
            self.redSliderLabel.setText(self.config['configs']['red_color'])
            self.blueSliderLabel.setText(self.config['configs']['blue_color'])
            self.brightnessSlider.setValue(int(self.config['configs']['brightness']))
            self.contrastSlider.setValue(int(self.config['configs']['contrast']))
            self.saturationSlider.setValue(int(self.config['configs']['saturation']))
            self.shutterspeedSlider.setValue(int(self.config['configs']['shutter_speed']))
            self.isoSlider.setValue(int(self.config['configs']['iso']))
            self.blueSlider.setValue(int(float(self.config['configs']['blue_color'])*100))
            self.redSlider.setValue(int(float(self.config['configs']['red_color'])*100))
            self.neoBrightSlider.setValue(int(float(self.config['configs']['neopixel_brigntness'])*10))
            self.neoBSlider.setValue(int(self.config['configs']['neopixel_blue']))
            self.neoGSlider.setValue(int(self.config['configs']['neopixel_green']))
            self.neoRSlider.setValue(int(self.config['configs']['neopixel_red']))
            self.neoBrightSliderLabel.setText(self.config['configs']['neopixel_brigntness'])
            self.neoBSliderLabel.setText(self.config['configs']['neopixel_blue'])
            self.neoGSliderLabel.setText(self.config['configs']['neopixel_green'])
            self.neoRSliderLabel.setText(self.config['configs']['neopixel_red'])
            self.use_video_port=self.config['configs']['use_video_port']
        else:
            self.config['configs'] = {
                'resolution':str(self.resolutionBox.currentText()),
                'rotation':self.rotationBox.currentText(),
                'red_color':str(int(self.redSlider.value())/100),
                'blue_color':str(int(self.blueSlider.value())/100),
                'iso':self.isoSlider.value(),
                'brightness':self.brightnessSlider.value(),
                'contrast':self.contrastSlider.value(),
                'saturation':self.saturationSlider.value(),
                'shutter_speed':self.shutterspeedSlider.value(),
                'neopixel_blue':self.neoBSlider.value(),
                'neopixel_green':self.neoGSlider.value(),
                'neopixel_red':self.neoRSlider.value(),
                'neopixel_brigntness':str(round(self.neoBrightSlider.value()/10,1)),
                'use_video_port':False
            }

        self.backup_config = {}
        for k,v in self.config['configs'].items():
            self.backup_config[k] = v

        super().setup(self.config['configs']['resolution'])
        self.camera.rotation = self.config['configs']['rotation']
        self.camera.awb_gains = (float(self.config['configs']['red_color']),
            float(self.config['configs']['blue_color']))
        self.camera.iso = int(self.config['configs']['iso'])
        self.camera.brightness = int(self.config['configs']['brightness'])
        self.camera.contrast = int(self.config['configs']['contrast'])
        self.camera.saturation = int(self.config['configs']['saturation'])
        self.camera.shutter_speed = int(self.config['configs']['shutter_speed'])
        if self.config['configs']['resolution'] == '1920x1080':
            self.use_video_port = True
        else:
            self.use_video_port = False
        sleep(1)

        color = (int(self.config['configs']['neopixel_red']),
            int(self.config['configs']['neopixel_green']),
            int(self.config['configs']['neopixel_blue']))
        self.pixels.fill(color)
        self.pixels.brightness = float(self.config['configs']['neopixel_brigntness'])
        self.pixels.show()

    def resetSetting(self):
        self.resolutionBox.setCurrentIndex(self.resolutionBox.findText(
            self.backup_config['resolution'],QtCore.Qt.MatchFixedString))
        self.rotationBox.setCurrentIndex(self.rotationBox.findText(
            self.backup_config['rotation'],QtCore.Qt.MatchFixedString))
        self.brightnessSliderLabel.setText(self.backup_config['brightness'])
        self.contrastSliderLabel.setText(self.backup_config['contrast'])
        self.saturationSliderLabel.setText(self.backup_config['saturation'])
        self.shutterspeedSliderLabel.setText(self.backup_config['shutter_speed'])
        self.isoSliderLabel.setText(self.backup_config['iso'])
        self.redSliderLabel.setText(self.backup_config['red_color'])
        self.blueSliderLabel.setText(self.backup_config['blue_color'])
        self.brightnessSlider.setValue(int(self.backup_config['brightness']))
        self.contrastSlider.setValue(int(self.backup_config['contrast']))
        self.saturationSlider.setValue(int(self.backup_config['saturation']))
        self.shutterspeedSlider.setValue(int(self.backup_config['shutter_speed']))
        self.isoSlider.setValue(int(self.backup_config['iso']))
        self.blueSlider.setValue(int(float(self.backup_config['blue_color'])*100))
        self.redSlider.setValue(int(float(self.backup_config['red_color'])*100))

        self.config['configs'] = {
            'resolution':self.resolutionBox.currentText(),
            'rotation':self.rotationBox.currentText(),
            'red_color':str(int(self.redSlider.value())/100),
            'blue_color':str(int(self.blueSlider.value())/100),
            'iso':self.isoSlider.value(),
            'brightness':self.brightnessSlider.value(),
            'contrast':self.contrastSlider.value(),
            'saturation':self.saturationSlider.value(),
            'shutter_speed':self.shutterspeedSlider.value()
        }

    def pressEvent(self, event):
        # print('press', event.key())
        if event.key() == 16777275:
            self.preview()

    def resizeWindow(self,w,h,mode=False):
        if mode:
            cv2.resizeWindow('capture',int(round(int(w))),int(round(int(h))))
        else:
            cv2.resizeWindow('capture',int(round(int(w)/2.5)),int(round(int(h)/2.5)))

    def captureEvent(self):
        self.picture = self.capture()
        self.resizeWindow(int(self.picture.shape[1]),int(self.picture.shape[0]))
        cv2.imshow('capture',self.picture)

    def colorConverter(self):
        self.picture = cv2.cvtColor(self.picture,cv2.COLOR_BGR2GRAY)
        cv2.imshow('capture',self.picture)

    def histogram(self):
        if len(self.picture.shape)==2:
            hist = self.picture.ravel()
            plt.hist(hist,256,[0,256])
            plt.show()
        else:
            for i,col in enumerate(('b','g','r')):
                histr = cv2.calcHist([self.picture],[i],None,[256],[0,256])
                plt.plot(histr,color = col)
                plt.xlim([0,256])
            plt.show()

    def savePicture(self):
        cv2.imwrite(self.path+'/pictures/'+str(self.img_index)+'.bmp',self.picture)
        self.img_index += 1

if __name__ == "__main__":
    import os
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CameraInterface('Camera')
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())