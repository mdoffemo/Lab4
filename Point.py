# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:38:06 2021

@author: User
"""
import numpy as np
from Shape import Shape

#define the class Point that inherits from the class Shape and has attributes x and y
class Point(Shape):
    def __init__(self, x=0, y=0, *args):
        super(Point, self).__init__(*args)
        self.__x = x
        self.__y = y
    
    #make setters and getters
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y    
        
    def setPosition(self, x, y):
        self.setX(x)
        self.setY(y)
    
    #make a function that returns the description of the shape
    def toString(self):
        return("Point ({}, {})".format(self.__x, self.__y))
    
    #make a function to calculate the disctance from the Point to point with given coordinates
    def distance(self, x, y):
        distance = np.sqrt((self.__x - x)**2 + (self.__y - y)**2)
        return distance