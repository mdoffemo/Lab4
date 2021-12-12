# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:37:10 2021

@author: User
"""

import unittest
import math
import Point
import Rectangle
import Circle


class TestPoint(unittest.TestCase):

    def test_getX(self):
        test_point = Point.Point(15, 35)
        self.assertEqual(15, test_point.getX())
    
    def test_getY(self):
        test_point = Point.Point(15, 35)
        self.assertEqual(35, test_point.getY())
        
    def test_getStrokeWidth(self):
        test_point = Point.Point(15, 35)
        self.assertEqual(1, test_point.getStrokeWidth())
        
    def test_getStrokeColor(self):
        test_point = Point.Point(15, 35)
        self.assertEqual("black", test_point.getStrokeColor())
        
    def test_getFillColor(self):
        test_point = Point.Point(15, 35)
        self.assertEqual("black", test_point.getFillColor())
        
    def test_setX(self):
        test_point = Point.Point(15, 35)
        test_point.setX(10)
        self.assertEqual(10, test_point.getX())
        
    def test_setY(self):
        test_point = Point.Point(15, 35)
        test_point.setY(10)
        self.assertEqual(10, test_point.getY())
        
    def test_setStrokeWidth(self):
        test_point = Point.Point(15, 35)
        test_point.setStrokeWidth(2)
        self.assertEqual(2, test_point.getStrokeWidth())
        
    def test_setStrokeColor(self):
        test_point = Point.Point(15, 35)
        test_point.setStrokeColor("red")
        self.assertEqual("red", test_point.getStrokeColor())
    
    def test_setFillColor(self):
        test_point = Point.Point(15, 35)
        test_point.setFillColor("green")
        self.assertEqual("green", test_point.getFillColor())
    
    def test_toString(self):
        test_point = Point.Point(15, 35)
        self.assertEqual("Point (15, 35)", test_point.toString())
    
    def test_setposition(self):
        test_point = Point.Point(15, 35)
        test_point.setPosition(10, 10)
        self.assertEqual((10, 10), (test_point.getX(), test_point.getY()))
        
    def test_distance(self):
        test_point = Point.Point(15, 35)
        self.assertEqual(1, test_point.distance(16, 35))
        

class TestRectangle(unittest.TestCase):

    def test_getWidth(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual(5, test_rectangle.getWidth())
        
    def test_getTopLeftPoint(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual((10, 35), (test_rectangle.getTopLeftPoint().getX(), test_rectangle.getTopLeftPoint().getY()))
    
    def test_getHeight(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual(8, test_rectangle.getHeight())
        
    def test_getStrokeWidth(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual(1, test_rectangle.getStrokeWidth())
        
    def test_getStrokeColor(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual("black", test_rectangle.getStrokeColor())
        
    def test_getFillColor(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual("black", test_rectangle.getFillColor())
        
    def test_setWidth(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        test_rectangle.setWidth(10)
        self.assertEqual(10, test_rectangle.getWidth())
        
    def test_setHeight(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        test_rectangle.setHeight(10)
        self.assertEqual(10, test_rectangle.getHeight())
        
    def test_setTopLeftPoint(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        test_rectangle.setTopLeftPoint(Point.Point(12, 15))
        self.assertEqual((12, 15), (test_rectangle.getTopLeftPoint().getX(), test_rectangle.getTopLeftPoint().getY()))
        
    def test_setStrokeWidth(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        test_rectangle.setStrokeWidth(2)
        self.assertEqual(2, test_rectangle.getStrokeWidth())
        
    def test_setStrokeColor(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        test_rectangle.setStrokeColor("red")
        self.assertEqual("red", test_rectangle.getStrokeColor())
    
    def test_setFillColor(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        test_rectangle.setFillColor("green")
        self.assertEqual("green", test_rectangle.getFillColor())
    
    def test_toString(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual("Rectangle [topLeftPoint = Point (10, 35), width = 5, height = 8]", test_rectangle.toString())
    
    def test_perimeter(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual(26, test_rectangle.perimeter())
        
    def test_area(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual(40, test_rectangle.area())
        
    def test_centroid(self):
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual((12.5, 39), (test_rectangle.centroid().getX(), test_rectangle.centroid().getY()))
        
    def test_contains(self):
        test_point1 = Point.Point(15, 40)
        test_point2 = Point.Point(15, 25)
        test_rectangle = Rectangle.Rectangle(Point.Point(10, 35), 5, 8)
        self.assertEqual((True, False), (test_rectangle.contains(test_point1), test_rectangle.contains(test_point2)))
        
class TestCircle(unittest.TestCase):
    
    def test_getCenterPoint(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual((10, 15), (test_circle.getCenterPoint().getX(), test_circle.getCenterPoint().getY()))
        
    def test_getRadius(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual(5, test_circle.getRadius())
    
    def test_getStrokeWidth(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual(1, test_circle.getStrokeWidth())
        
    def test_getStrokeColor(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual("black", test_circle.getStrokeColor())
        
    def test_getFillColor(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual("black", test_circle.getFillColor())
        
    def test_setCenterPoint(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        test_circle.setCenterPoint(Point.Point(20, 25))
        self.assertEqual((20, 25), (test_circle.getCenterPoint().getX(), test_circle.getCenterPoint().getY()))
        
    def test_setRadius(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        test_circle.setRadius(10)
        self.assertEqual(10, test_circle.getRadius())
        
    def test_setStrokeWidth(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        test_circle.setStrokeWidth(2)
        self.assertEqual(2, test_circle.getStrokeWidth())
        
    def test_setStrokeColor(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        test_circle.setStrokeColor("red")
        self.assertEqual("red", test_circle.getStrokeColor())
    
    def test_setFillColor(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        test_circle.setFillColor("green")
        self.assertEqual("green", test_circle.getFillColor())
        
    def test_area(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual(25*math.pi, test_circle.area())
        
    def test_perimeter(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual(10*math.pi, test_circle.perimeter())
    
    def test_toString(self):
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual("The Circle [centerPoint = Point (10, 15), radius = 5]", test_circle.toString())
        
    def test_contains(self):
        test_point1 = Point.Point(14, 13)
        test_point2 = Point.Point(15, 25)
        test_circle = Circle.Circle(Point.Point(10, 15), 5)
        self.assertEqual((True, False), (test_circle.contains(test_point1), test_circle.contains(test_point2)))
        
if __name__ == '__main__': 
     unittest.main()