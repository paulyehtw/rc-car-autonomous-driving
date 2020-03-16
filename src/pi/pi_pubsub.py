#!/usr/bin/env python
import rospy
from std_msgs.msg import String
# def talker():
#     pub = rospy.Publisher('/pi_msg', String, queue_size=10)
#     rate = rospy.Rate(1) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "From pi %s" % rospy.get_time()
#         # rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         listener()
#         rate.sleep()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('pi_pub_sub', anonymous=True)
    rospy.Subscriber("/host_msg", String, callback)
    talker()
    rospy.sleep(1)

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
