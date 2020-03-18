#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from picamera.array import PiRGBArray
import picamera
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import time

def capture_image(camera):
    image = np.empty((240*320*3,),dtype=np.uint8)
    camera.capture(image, 'bgr')
    time.sleep(1)
    image = image.reshape((240,320,3))
    return image

def talker():
    rospy.init_node('pi_pub_sub', anonymous=True)
    pub = rospy.Publisher('/pi_msg', String, queue_size=10)
    pub_image = rospy.Publisher('/cam_msg', Image, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    bridge = CvBridge()
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 24

    while not rospy.is_shutdown():
        hello_str = "From pi %s" % rospy.get_time()
        rospy.loginfo("pi msg sent")
        image_ros = bridge.cv2_to_imgmsg(capture_image(camera), encoding="bgr8")
        pub_image.publish(image_ros)
        pub.publish(hello_str)
        # listener()
        rate.sleep()

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

# def listener():
#     rospy.init_node('pi_pub_sub', anonymous=True)
#     rospy.Subscriber("/pi_msg", String, callback)
#     talker()
#     rospy.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
