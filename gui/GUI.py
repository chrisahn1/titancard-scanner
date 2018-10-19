from tkinter import *
import cv2
from Video import Video
# color = #00274C

#defined video source
cap = cv2.VideoCapture(0)

#instantiate video object
vid = Video(cap)

#loop to keep video running
vid.update()
