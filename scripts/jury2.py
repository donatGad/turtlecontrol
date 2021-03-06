#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import *


class kornjaca():

    def pose_calculate(self, data):
        self.x = data.x
        self.y = data.y
        
        try:
            self.razlika = sqrt(pow(turtle1.x-turtle2.x,2)+pow(turtle1.y-turtle2.y,2))
            if self.razlika < 1:
                rospy.loginfo(" You win!!")        
        except:
            pass
        
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    rospy.init_node('jury', anonymous=True)
    
    turtle1 = kornjaca('turtle1')
    turtle2 = kornjaca('turtle2')   
     
        
    while not rospy.is_shutdown():
        rospy.Subscriber('/turtle1/pose', Pose, turtle1.pose_calculate)
        rospy.Subscriber('/turtle2/pose', Pose, turtle2.pose_calculate)
        rospy.spin()
    #rospy.sleep(1.0)


