import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import datetime
from sensor_msgs.msg import Image
import time
import requests
from playsound import playsound
import requests
from playsound import playsound

#from timeout_decorator import timeout, TimeoutError


# Sring型メッセージをサブスクライブして端末に表示するだけの簡単なクラス
class HscrSub(Node):
    def __init__(self): # コンストラクタ
        super().__init__('HSCR_Robot_sub_node')
        # サブスクライバの生成
        self.sub = self.create_subscription(String,'topic', self.callback, 10)#topicっていう名前の箱のサブスクライブ、Stringは形　受け取る
        self.publisher = self.create_publisher(Image,'result',10)#大事！resultっていう名前の箱にパブリッシュしてる。送ってる。rqtは通信を見えるようにする。動画をresultに送ってrqtでみてる。

    def callback(self, msg):  # コールバック関数 送られたときに起動
        self.get_logger().info(f'サブスクライブ: {msg.data}')


    
    def movie_start(self):#main４４行目の中で動作してる　この中変える　28〜39ロスで動画流すルール
        msg = String()
	

    # VOICEVOX EngineのURL
    VOICEVOX_URL = "http://localhost:50021"
	
    def text_to_speech(text):
	# 音声合成のためのクエリを生成
        response = requests.post(
        f"{VOICEVOX_URL}/audio_query",
        params={
                "text": text,
                "speaker": 58,
                },
            )

        audio_query = response.json()

	    # 音声合成を行う
        response = requests.post(
            f"{VOICEVOX_URL}/synthesis",
		headers={
		    "Content-Type": "application/json",
		},
		params={
		    "speaker": 58,
		},
		json=audio_query,
            )
            
	    # ステータスコードが200以外の場合はエラーメッセージを表示
        if response.status_code != 200:
            print("エラーが発生しました。ステータスコード: {}".format(response.status_code))
            print(response.text)
        else:
	# 音声データを取得
            audio = response.content
	# 音声データをファイルに保存
            with open("output.wav", "wb") as f:
                f.write(audio)
	# 音声データを再生
            playsound("output.wav")
            
    if __name__ == "__main__":
	    # 音声に変換したいテキスト
            text = "かつおぶしが好きにゃ。"
            sub_speech(text)
                            
            print("end")
            
def main(args=None): # main¢p
    try:
        rclpy.init()#初期化
        node = HscrSub()#nodeにHscrを
        msg=String()#stringは文字列いれれる 
        while True:           
            rclpy.spin_once(node)#一回ノードを起動する？
            node.movie_start()#movie_startを実行する
    except KeyboardInterrupt:
        pass#ctl+C(KeyboardInterrupt) node finish

    """
    while True:       
        if msg.data==True:
            
            i = i+1
            print(i)
        else:
            print("wait_time")
            time.sleep(1)
    """
    
    """
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されました')
    finally:
        rclpy.shutdown()
    """
