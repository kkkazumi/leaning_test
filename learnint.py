import rospy
from std_msgs.msg import Float64
from gym import Env

class EmotionRecognitionEnv(Env):
    def __init__(self):
        self.action_space = [0, 1, 2, 3]
        self.observation_space = [0, 1, 2, 3]

    def step(self, action):
        # 表情認識データを取得する
        emotion_data = rospy.wait_for_message('emotion_data', Image)

        # 報酬を計算する
        reward = emotion_data.data[action]

        # 次の状態を決定する
        next_state = action

        return next_state, reward, False, {}

    def reset(self):
        # 初期状態を決定する
        next_state = 0
        return next_state

    def render(self):
        # 画面に描画する
        pass

def main():
    rospy.init_node('learning')

    # 環境を作成
    env = EmotionRecognitionEnv()

    # Q学習のアルゴリズムを定義
    q_table = np.zeros((4, 4))
    alpha = 0.1
    gamma = 0.9

    # 学習を開始
    for i in range(10000):
        # 状態を取得する
        state = env.reset()

        # 行動を決定する
        action = np.argmax(q_table[state])

        # 次の状態と報酬を取得する
        next_state, reward, done, _ = env.step(action)

        # Q表を更新する
        q_table[state][action] = q_table[state][action] + alpha * (reward + gamma * np.max(q_table[next_state]))

        # 終了条件
        if done:
            break

    # 次ステップの目標角度指令をPublishする
    pub = rospy.Publisher('target_angle', Float64, queue_size=1)
    while True:
        # 行動を決定する
        action = np.argmax(q_table[state])

        # 目標角度指令をPublishする
        pub.publish(action)
        rospy.sleep(0.1)

if __name__ == '__main__':
    main()
