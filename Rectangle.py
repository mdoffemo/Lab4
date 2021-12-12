# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:32:15 2021

@author: User
"""
from Shape import Shape
import Point

#define the class Rectangle that inherits from the class Shape and has attributes top left point, width and height
class Rectangle(Shape):
    def __init__(self, topLeftPoint, width, height, *args):
        super(Rectangle, self).__init__(*args)
        self.__topLeftPoint = topLeftPoint
        self.__width = width
        self.__height = height
    
    #make setters and getters
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getTopLeftPoint(self):
        return (self.__topLeftPoint)
    
    def setWidth(self, width):
        self.__width = width
        
    def setHeight(self, height):
        self.__height = height
        
    def setTopLeftPoint(self, topLeftPoint):
        self.__topLeftPoint = topLeftPoint
        
    #make a function that calculates the area of the rectangle
    def area(self):
        return self.__width * self.__height
    
    #make a function that calculates the perimeter of the rectangle
    def perimeter(self):
        return (self.__width + self.__height)*2
    
    #make a function that determines if another point is inside the rectangle
    def contains(self, point):
        return self.__topLeftPoint.getX() <= point.getX() <= self.__topLeftPoint.getX() + self.__width and self.__topLeftPoint.getY() <= point.getY() <= self.__topLeftPoint.getY() + self.__height 
    
    #make a function that returns the centroid of the rectangle
    def centroid(self):
        return Point.Point(self.__topLeftPoint.getX() + self.__width/2, self.__topLeftPoint.getY() + self.__height/2)
    
    #make a function that returns the description of the shape
    def toString(self):
        return ("Rectangle [topLeftPoint = {}, width = {}, height = {}]".format(self.__topLeftPoint.toString(), self.__width, self.__height))
    