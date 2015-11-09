#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import *


class kornjaca():

    def pose_calculate(self, data):
        
        self.x = data.x
        self.y = data.y
        
        self.razlika = sqrt(pow(turtle1.x-turtle2.x,2)+pow(turtle1.y-turtle2.y,2))
        if self.razlika > 1:
            rospy.loginfo(" Udaljenost izmedu kornjaca je: %2.2f", self.razlika)
        else:
            rospy.loginfo(" Bravo!! Udaljenost je : %2.2f < 1m", self.razlika)
        
    def __init__(self, name):
        self.name = name
        #self.x = x
        #self.y = y        
        #self.adress = '/{0}/pose'.format(self.name)
        rospy.Subscriber('/{0}/pose'.format(self.name), Pose, self.pose_calculate)
        
        


if __name__ == '__main__':
    rospy.init_node('jury', anonymous=True)
    global turtle1
    global turtle2
    while not rospy.is_shutdown():
        try:
            turtle1 = kornjaca('turtle1')
        except:
            pass            
        turtle2 = kornjaca('turtle2')   
        rospy.sleep(1.0)
    
    rospy.spin()


