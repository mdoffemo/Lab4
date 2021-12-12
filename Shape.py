# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:23:35 2021

@author: User
"""
#define superclass SHape that has attribute stroke width, stroke color and fill color
class Shape:
    def __init__(self, strokeWidth = 1, strokeColor = "black", fillColor = "black"):
        self.__strokeWidth = strokeWidth
        self.__strokeColor = strokeColor
        self.__fillColor = fillColor
    
    #make setters and getters
    def setStrokeWidth(self, width):
        self.__strokeWidth = width
    
    def setStrokeColor(self, color):
        self.__strokeColor = color
    
    def setFillColor(self, color):
        self.__fillColor = color
    
    def getStrokeWidth(self):
        return self.__strokeWidth
    
    def getStrokeColor(self):
        return self.__strokeColor
    
    def getFillColor(self):
        return self.__fillColor
    