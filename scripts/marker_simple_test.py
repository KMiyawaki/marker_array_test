#!/usr/bin/env python

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math

def make_marker(x, y, z, r, g, b, a):
    marker_array = MarkerArray()
    marker = Marker()
    marker.header.frame_id = "base_link"
    marker.id = 0
    marker.ns = "test_marker"
    marker.lifetime = rospy.Duration(0.01)
    marker.type = marker.SPHERE
    marker.action = marker.ADD
    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.a = a
    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = x
    marker.pose.position.y = y
    marker.pose.position.z = z

    # We add the new marker to the MarkerArray, removing the oldest marker from it when necessary
    marker_array.markers.append(marker)
    return marker_array

topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray, queue_size=10)

rospy.init_node('marker_array_test')

count = 0
MARKERS_MAX = 1

while not rospy.is_shutdown():
    rad = math.radians(count % 360)
    x = math.cos(rad) * 2.0
    y = math.sin(rad) * 2.0
    a = math.cos(rad) / 2.0 + 0.5
    rospy.loginfo("%f, %f, %f", x, y, a)

    # Publish the MarkerArray
    publisher.publish(make_marker(x, y, 0, 1, 1, 0, a))

    count += 1
    rospy.sleep(0.01)
