import rospy
from std_msgs.msg import Float64

def main():
    rospy.init_node('robot')

    # 目標角度指令をSubscribeする
    target_angle_sub = rospy.Subscriber('target_angle', Float64, target_angle_callback)

    # サーボモータの制御
    def target_angle_callback(data):
        # 目標角度指令に応じて、サーボモータの角度を決定する
        arm_angle = data.data

        # サーボモータの角度をPublishする
        arm_angle_pub.publish(arm_angle)

    arm_angle_pub = rospy.Publisher('arm_angle', Float64, queue_size=1)

    while True:
        rospy.spin()

if __name__ == '__main__':
    main()
