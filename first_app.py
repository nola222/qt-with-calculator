# -*- coding: utf-8 -*-
"""创建第一个qt应用
时间: 2021/3/31 10:41

作者: nola

更改记录:

重要说明:
"""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 创建一个应用实例
first_app = QApplication(sys.argv)

# 为应用创建一个GUI实例
window = QWidget()
window.setWindowTitle('First PyQT5 APP')
window.setGeometry(100, 100, 400, 80)  # 设置位置和窗口大小x,y,w,h
window.move(60, 15)
# 避免内存泄露，每个QWidget对象都应该设置一个parent，主窗口或顶层的窗口没有parent；parent删除，child会自动删除
msg = QLabel('<h1>code change the world！', parent=window)
msg.move(60, 15)

# 显示GUI,从queue调起paint事件
window.show()

# loop应用，关闭终端，程序退出，释放资源
sys.exit(first_app.exec_())





