#!/usr/bin/env python

import rospy
from darwin_gazebo.darwin import Darwin


if __name__=="__main__":
    rospy.init_node("walker_demo")
    
    rospy.loginfo("Instantiating Darwin Client")
    darwin=Darwin()
    rospy.sleep(1)
 
    rospy.loginfo("Darwin Walker Demo Starting")

    darwin.set_angles({"j_high_arm_l":0.5})
    darwin.set_angles({"j_high_arm_r":0.5})
    rospy.sleep(2)
    darwin.set_angles({"j_high_arm_l":0.8})
    darwin.set_angles({"j_high_arm_r":0.8})
    rospy.sleep(2)

    darwin.set_walk_velocity(0.2,0,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(1,0,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(0,1,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(0,-1,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(-1,0,0)
    rospy.sleep(3)
    darwin.set_walk_velocity(1,1,0)
    rospy.sleep(5)
    darwin.set_walk_velocity(0,0,0)
    
    rospy.loginfo("Darwin Walker Demo Finished")
