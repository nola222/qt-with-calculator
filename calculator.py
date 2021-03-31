# -*- coding: utf-8 -*-
"""PyQT实现计算器
时间: 2021/3/31 11:48

作者: nola

更改记录:

重要说明:
    MVC模式
"""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget


__version__ = '0.1'
__author__ = 'nola'


class CalculatorGUI(QMainWindow):
    """View
    """
    def __init__(self):
        """init

        """
        super(CalculatorGUI, self).__init__()
        # 设置main Window属性
        self.setWindowTitle('Calculator')
        # 设置固定大小，避免用户随意更改大小
        self.setFixedSize(235, 235)
        self._centralWidget = QWidget()
        # 设置一个中心组件，作为其他组件的parent
        self.setCentralWidget(self._centralWidget)


def main():
    """main
    """
    # 实例计算器应用
    cal = QApplication(sys.argv)
    # 显示GUI
    view = CalculatorGUI()
    view.show()
    # loop
    sys.exit(cal.exec_())


if __name__ == '__main__':
    main()
