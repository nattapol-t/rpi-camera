#!/usr/bin/env python3

import os
import cv2
import picamera
import numpy as np
import picamera.array
from time import sleep
from datetime import datetime


class Camera():

    path = os.path.dirname(os.path.realpath(__file__))

    def setup(self,resolution='3280x2464'):
        self.camera                 = picamera.PiCamera()
        self.camera.resolution      = resolution
        self.camera.framerate       = 30
        self.camera.image_denoise   = True
        self.camera.iso             = 100
        self.camera.rotation        = 0
        self.camera.awb_mode        = 'off'
        self.camera.awb_gains       = (1.5,1.5)
        self.camera.brightness      = 50
        self.camera.contrast        = 0
        self.camera.saturation      = 0
        self.camera.shutter_speed   = 20000
        self.preview_fullscreen     = False
        self.use_video_port         = False
        for the_file in os.listdir(self.path+'/pictures'):
            file_path = os.path.join(self.path+'/pictures', the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        sleep(1)

    def preview(self,position_size=None):
        if self.preview_fullscreen:
            self.camera.start_preview()
        else:
            self.camera.start_preview(fullscreen=False,window=(0,0,500,500))
        
        self.preview_fullscreen = not self.preview_fullscreen

    def capture(self):
        # start = datetime.now()
        
        # print('-------------------------------')
        # print('resolution',self.camera.resolution)
        # print('rotation',self.camera.rotation)
        # print('awb_gains',self.camera.awb_gains)
        # print('iso',self.camera.iso)
        # print('brightness',self.camera.brightness)
        # print('contrast',self.camera.contrast)
        # print('saturation',self.camera.saturation)
        # print('shutter_speed',self.camera.shutter_speed)
        # print('-------------------------------')

        # self.rawCapture = picamera.array.PiRGBArray(self.camera)
        # self.camera.capture(self.rawCapture,format="bgr",use_video_port=False)
        # image = self.rawCapture.array
        # self.rawCapture.seek(0)
        # self.rawCapture.truncate(0)
        # print('Capture :',(datetime.now() - start).total_seconds(),'secs.')
        # cv2.imshow('Capture',image)
        # return image
        with picamera.array.PiRGBArray(self.camera) as stream:
            self.camera.capture(stream, 'bgr', use_video_port=self.use_video_port)
            img = stream.array
            stream.seek(0)
            stream.truncate()
            return img


def main():
    cam = Camera()
    cam.setup('1920x1080')
    cam.preview((0,0,int(500),int(500)))

    while True:
        key = cv2.waitKey()
        if key == 27:
            break
        elif key == ord('c'):
            cv2.imshow('Capture',cam.capture())
        elif key == ord('s'):
            img = cam.capture()
            cv2.imwrite(path+'/output/save.bmp',img)
            cv2.imshow('Capture',img)
        sleep(0.01)


if __name__ == '__main__':
    main()