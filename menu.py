import pygame
import math, random
from pygame.locals import *
from tkinter import *
from tkinter import ttk
import tkinter as tk


#this is the main page
win = Tk()
win.title ('King Kong')
win.geometry ("400x500")
win.resizable(0,0)

img = PhotoImage (file= "menuImage.jpg")
w = img.width()
h = img.height()

win.mainloop ()

