#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

def callback(data):
    # rospy.loginfo("callback")
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def talker():
    rospy.init_node('host_pub_sub', anonymous=True)
    pub = rospy.Publisher('/host_msg', String, queue_size=10)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        hello_str = "From host %s" % rospy.get_time()
        rospy.loginfo("host msg sent")
        pub.publish(hello_str)
        rospy.Subscriber('/pi_msg', String, callback)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
