import rospy
from sensor_msgs.msg import Image

def main():
    rospy.init_node('sensor_sender')
    pub = rospy.Publisher('emotion_data', Image, queue_size=1)

    while True:
        # 表情認識データを生成する
        data = Image()
        data.header.stamp = rospy.Time.now()
        data.data = np.ones((100, 100, 3), dtype=np.uint8)

        # データをPublishする
        pub.publish(data)
        rospy.sleep(0.1)

if __name__ == '__main__':
    main()
