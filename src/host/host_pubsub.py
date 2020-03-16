#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def talker():
    rospy.init_node('host_pub_sub', anonymous=True)
    pub = rospy.Publisher('/host_msg', String, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = "From host %s" % rospy.get_time()
        rospy.loginfo("Host msg sent")
        pub.publish(hello_str)
        # listener()
        rate.sleep()

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

# def listener():
#     rospy.init_node('host_pub_sub', anonymous=True)
#     rospy.Subscriber("/pi_msg", String, callback)
#     talker()
#     rospy.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
