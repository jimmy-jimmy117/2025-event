import pyshark
import plotly_express as px

# import plotly.express as px
import pandas as pd

# キャプチャするインターフェースの指定
cap = pyshark.LiveCapture(interface="any")

# パケットデータを格納するリスト
data = []

# パケットキャプチャの開始
for packet in cap.sniff_continuously(packet_count=500):  # 100パケットだけキャプチャ
    try:
        # IPソースアドレスを抽出
        src_ip = packet.ip.src
        data.append(src_ip)
    except AttributeError:
        pass  # IPアドレスが無いパケットもあるため、その場合はスキップ

# データをDataFrameに変換
df = pd.DataFrame(data, columns=["Source IP"])

# IPアドレスごとのパケット数をカウント
df_count = df["Source IP"].value_counts().reset_index()
df_count.columns = ["Source IP", "Packet Count"]

# Plotlyでグラフ作成
fig = px.bar(
    df_count, x="Source IP", y="Packet Count", title="Packet Count by Source IP"
)
fig.show()

import json

# データをJSON形式で保存
with open("packet_data.json", "w") as json_file:
    json.dump(df_count.to_dict(orient="records"), json_file)
