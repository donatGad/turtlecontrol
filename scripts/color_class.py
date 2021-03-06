#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color

class NodeExample():

    def color_callback(self,data):
        rospy.loginfo(rospy.get_caller_id()+" Color I see"+" is r=%d g=%d b=%d", data.r,data.g,data.b)
        if data.r > data.b:
            self.cmd_vel.angular.z = 0.1
        else:
            self.cmd_vel.angular.z = -0.1
            
        

    def __init__(self):
        
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 0.1
        self.cmd_vel.angular.z = 0.1    
        rospy.Subscriber("color",Color, self.color_callback)
        while not rospy.is_shutdown():
            pub.publish(self.cmd_vel)
            rospy.sleep(1.0)

if __name__ == '__main__':

    rospy.init_node('pyclass')

    try:
        ne = NodeExample()
    except rospy.ROSInterruptException: pass
