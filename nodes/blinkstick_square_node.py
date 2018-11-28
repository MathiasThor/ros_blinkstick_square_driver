#!/usr/bin/env python
from __future__ import print_function, division

import rospy
from std_msgs.msg import Int16, String, ColorRGBA
from blinkstick import blinkstick


class blinkstickDriver(object):

    def __init__(self):

        try:
            self.bstick = blinkstick.find_first()
        except:
            rospy.logerr('unable to find BlinkStick Square')
            sys.exit(-1)
	
	rospy.loginfo('connected to BlinkStick Square')

	rospy.Subscriber("set_all_led", ColorRGBA, self.set_all)
        rospy.Subscriber("set_single_led", ColorRGBA, self.set_single)

	self.bstick.morph(channel=0, index=0, red=0, green=40, blue=0)

    def set_all(self,data):
	self.bstick.morph(channel=0, index=0, red=data.r, green=data.g, blue=data.b)

    def set_single(self,data):
	self.bstick.morph(channel=0, index=int(data.a), red=data.r, green=data.g, blue=data.b)


def main():
    rospy.init_node('blinkstick_square')
    node = blinkstickDriver()
    rospy.spin()

if __name__ == '__main__':
    main()
