#!/usr/bin/python

class Train:
   def __init__(self, WheelCount, speed):
      self.WheelCount = WheelCount
      self.speed = speed
   
   def go(self):
     print "running at "+str(self.speed)+" KM per hour"

   def stop(self):
      print " engaging brakes on "+str(self.WheelCount)+ "wheel"

Train1 = Train(8, 280)
Train1.go()
Train1.stop()