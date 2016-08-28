#encoding: utf-8
import pybursts

# 系列を表現する数値配列
offsets = [4., 17., 23., 27., 33., 35., 37., 76., 77., 82., 84., 88., 90., 92.]

# s: 指数分布の底
# gamma: 状態を変更する際のコスト係数
print pybursts.kleinberg(offsets, s=2, gamma=0.1)
