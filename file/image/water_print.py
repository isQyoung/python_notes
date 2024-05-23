import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QFont, QColor


class WatermarkWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Watermark Window")
        self.setGeometry(100, 100, 800, 600)

        self.watermark_text = "Watermark"

    def paintEvent(self, event):
        painter = QPainter(self)

        # 设置水印文本的字体和大小
        font = QFont("Arial", 36)
        painter.setFont(font)

        # 设置水印文本的颜色和透明度
        text_color = QColor(255, 255, 255, 128)  # 白色，透明度128
        painter.setPen(text_color)

        # 计算水印文本的位置（居中）
        text_width = painter.fontMetrics().width(self.watermark_text)
        text_height = painter.fontMetrics().height()
        window_width = self.width()
        window_height = self.height()
        text_x = (window_width - text_width) // 2
        text_y = (window_height - text_height) // 2

        # 在窗口上绘制水印文本
        painter.drawText(text_x, text_y, self.watermark_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WatermarkWindow()
    window.show()
    sys.exit(app.exec_())