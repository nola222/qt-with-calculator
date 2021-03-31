# -*- coding: utf-8 -*-
"""PyQT实现计算器
时间: 2021/3/31 11:48

作者: nola

更改记录:

重要说明:
    MVC模式
"""
import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


__version__ = '0.1'
__author__ = 'nola'

ERROR_MSG = 'ERROR'


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
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget()
        # 设置一个中心组件，作为其他组件的parent
        self.setCentralWidget(self._centralWidget)
        # 设置通用布局
        self._centralWidget.setLayout(self.generalLayout)
        # 创建布局和按钮
        self._create_display()
        self._create_button()

    def _create_display(self):
        """创建display组件
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # display添加到通用布局
        self.generalLayout.addWidget(self.display)

    def _create_button(self):
        """创建按钮

        Returns:
            None

        """
        self.buttons = {}
        buttons_layout = QGridLayout()
        # 按钮文字和位置
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }
        # 创建按钮 添加到网格布局
        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(40, 40)
            buttons_layout.addWidget(self.buttons[btn_text], pos[0], pos[1])
        # 添加按钮到通用布局
        self.generalLayout.addLayout(buttons_layout)

    def set_display_text(self, text):
        """设置按钮显示文本

        Args:
            text(str): 设置的文本

        Returns:
            None

        """
        self.display.setText(text)
        self.display.setFocus()  # 聚焦

    def get_display_text(self):
        """获取按钮文本

        Returns:
            text(str): 显示的文本

        """
        return self.display.text()

    def clear_display(self):
        """清除显示文字
        """
        self.set_display_text('')


class CalculatorCtl(object):
    """控制器
    """
    def __init__(self, view, model):
        """init

        Args:
            view(CalculatorGUI): CalculatorGUI 实例
            model(evaluate_expression): model
        """
        self._view = view
        self._connect_signal()
        self._evaluate = model

    def _build_expression(self, sub_exp):
        """构造数学运算表达式 更新输入显示

        Args:
            sub_exp(str): text

        Returns:
            None

        """
        expression = self._view.get_display_text() + sub_exp
        self._view.set_display_text(expression)

    def _connect_signal(self):
        """连接信号和槽 点击按钮生成数学运算表达式 点击C清空输入
        """
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._build_expression, btn_text))

        self._view.buttons['C'].clicked.connect(self._view.clear_display)
        self._view.buttons['='].clicked.connect(self._calculate_result)
        self._view.display.returnPressed.connect(self._calculate_result)  # hits Enter

    def _calculate_result(self):
        """计算结果
        """
        result = self._evaluate(expression=self._view.get_display_text())
        self._view.set_display_text(result)


def evaluate_expression(expression):
    """计算数学运算表达式

    Args:
        expression(str): 表达式

    Returns:
        result(int,float): 运算结果

    """
    try:
        result = str(eval(expression, {}, {}))
    except (SyntaxError, TypeError):
        result = ERROR_MSG

    return result


def main():
    """main
    """
    # 实例计算器应用
    cal = QApplication(sys.argv)
    # 显示GUI
    view = CalculatorGUI()
    view.show()
    # 创建model和controller
    model = evaluate_expression
    CalculatorCtl(view=view, model=model)
    # loop
    sys.exit(cal.exec_())


if __name__ == '__main__':
    main()
