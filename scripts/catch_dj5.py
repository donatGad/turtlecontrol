#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from numpy import random
import turtlesim.srv
from math import *
import std_srvs.srv

def ubij(name):
    rospy.wait_for_service('kill')
    killer = rospy.ServiceProxy('kill', turtlesim.srv.Kill)
    try:
        killer(name)
    except:
        pass

def stvori(x,y,theta,name):
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(x, y, theta, name)

def obrisi():
    rospy.wait_for_service('clear')
    cleaner = rospy.ServiceProxy('clear', std_srvs.srv.Empty)
    cleaner()
    
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

class NodeExample():

    def random_control(self):
        """ potprogram za random ponasanje kornjace """
        v = 2
        w = random.random_integers(-5,5)
        vel = Twist()
        vel.linear.x = v
        vel.angular.z = w
        return vel
            
    def __init__(self):
        rospy.init_node('jury', anonymous=True)        
        pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)    #definiranje poruke
        self.vel_cmd = Twist()
        while not rospy.is_shutdown():
            #objava poruke(slijeca brzina kornjace)
            self.vel_cmd = self.random_control()
            pub.publish(self.vel_cmd)
            rospy.Subscriber('/turtle1/pose', Pose, turtle1.pose_calculate) #pretplata na pozicije kornjaca
            rospy.Subscriber('/turtle2/pose', Pose, turtle2.pose_calculate)
            rospy.sleep(1.0)


if __name__ == '__main__':
    """ubijanje nepotrebnih i stvaranje potrebnih kornjaca"""
    ubij('turtle1')
    ubij('turtle2')    
    stvori(1, 1, -pi/4, 'turtle1')    
    stvori(10, 10, 3*pi/4, 'turtle2')  
    obrisi()  
    
    turtle1 = kornjaca('turtle1')
    turtle2 = kornjaca('turtle2')   
    
    try:    #pokretanje
        ne = NodeExample()
    except rospy.ROSInterruptException: pass
        


