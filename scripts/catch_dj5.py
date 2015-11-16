#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from numpy import random
import turtlesim.srv
from math import *
import std_srvs.srv

""" slijedece dvije funkcije stvaraju i brisu kornjace koristeci ROS service turtlesim paketa"""
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

def obrisi():   #f-ja za ciscenje ekrana
    rospy.wait_for_service('clear')
    cleaner = rospy.ServiceProxy('clear', std_srvs.srv.Empty)
    cleaner()
    
class kornjaca():   """definiranje klase """

    def pose_calculate(self, data):  #(sve metode obavezno imaju kao prvi argument 'self', ili samo njega)
        self.x = data.x
        self.y = data.y
        
        try:
            """računanje udaljenosti izmedju kornjaca"""
            self.razlika = sqrt(pow(turtle1.x-turtle2.x,2)+pow(turtle1.y-turtle2.y,2))
            if self.razlika < 1:
                rospy.loginfo(" You win!!")  
                
        except:
            pass
        
    def __init__(self, ime):    #kao selfse prenosi trutle1 ili turtle2, ovisi koja se instanca napravila
        self.name = ime         #lijevo je varijabla instance(njena lokalna), a desno se prenosi argument iz poziva iz 79 reda

class NodeSubPub():

    def random_control(self):
        """ potprogram za random ponasanje kornjace """
        v = 2
        w = random.random_integers(-5,5)
        vel = Twist()           #definiranje oblika varijable
        vel.linear.x = v
        vel.angular.z = w
        return vel
            
    def __init__(self):         #kad se dolje(u redu  82) stvori instanca klase, pokrene se ova metoda
        rospy.init_node('jury', anonymous=True)        
        pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)    #definiranje poruke
        self.vel_cmd = Twist()   #definiranje varijable koja ce se objavljivati
        while not rospy.is_shutdown():
            #objava poruke(slijeca brzina kornjace)
            self.vel_cmd = self.random_control()        #brzina u ovom nodu je random vrijednost izracunata u metodi ove insance klase Node
            pub.publish(self.vel_cmd)                   #i onda se objavljuje
            rospy.Subscriber('/turtle1/pose', Pose, turtle1.pose_calculate) #pretplata na pozicije kornjaca
            rospy.Subscriber('/turtle2/pose', Pose, turtle2.pose_calculate) #za svaku kornjacupoziva se njezina pose_calculate metoda(nema razlike
            rospy.sleep(1.0)


if __name__ == '__main__':
    """ubijanje nepotrebnih i stvaranje potrebnih kornjaca"""
    ubij('turtle1')
    #ubij('turtle2')  - nema smisla ako koristimo launch  
    stvori(1, 1, -pi/4, 'turtle1')    #stvanjanje kornjaca na dijagonali ekrana
    stvori(10, 10, 3*pi/4, 'turtle2')  
    obrisi()                            #brisanje ekrana
    
    turtle1 = kornjaca('turtle1')  #stvaranje instanci klase kornjaca
    turtle2 = kornjaca('turtle2')   
    
    try:    #pokretanje
        nsp = NodeSubPub()          #stvaranjeinstance klase node
    except rospy.ROSInterruptException: pass
        


