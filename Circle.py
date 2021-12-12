# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:32:20 2021

@author: User
"""
import math
from Shape import Shape

#define the class Circle that inherits from the class Shape and has attributes centerpoint and radius
class Circle(Shape):
    def __init__(self, centerPoint, radius, *args):
        super(Circle, self).__init__(*args)
        self.__centerPoint = centerPoint
        self.__radius = radius
    
    #make setters and getters
    def getCenterPoint(self):
        return self.__centerPoint
    
    def getRadius(self):
        return self.__radius
    
    def setCenterPoint(self, centerPoint):
        self.__centerPoint = centerPoint
        
    def setRadius(self, radius):
        self.__radius = radius
    
    #make a function that calculates the area of the circle
    def area(self):
        return self.__radius**2*math.pi
    
    #make a function that calculates the perimeter of the circle
    def perimeter(self):
        return self.__radius*2*math.pi
    
    #make a function that determines if another point is inside the circle
    def contains(self, point):
        distance = point.distance(self.__centerPoint.getX(), self.__centerPoint.getY())
        return distance <= self.__radius
    
    #make a function that returns the description of the shape
    def toString(self):
        return("The Circle [centerPoint = {}, radius = {}]".format(self.__centerPoint.toString(), self.__radius))