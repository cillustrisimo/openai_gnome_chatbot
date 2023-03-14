from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QPixmap
import sys
import qdarktheme


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 440)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 455, 680, 35)

        self.button = QPushButton(QIcon("icons/send.png"), "", self)
        self.button.setGeometry(650, 456, 35, 30)

        self.label = QLabel(self)
        self.sneed = QPixmap("icons/sneed.png")
        self.label.setPixmap(self.sneed)
        self.label.resize(190, 170)
        self.label.move(500, 12)

        self.label2 = QLabel(self)
        self.stats = QPixmap("icons/sneed_stats_small.png")
        self.label2.setPixmap(self.stats)
        self.label2.resize(self.stats.width(), self.stats.height())
        self.label2.move(493, 230)
        self.label2.setStyleSheet("border 10px solid grey;" "border-top-left-radius :10px;" 
                                  "border-top-right-radius :10px;" "border-bottom-left-radius :10px;"
                                  "border-bottom-right-radius :10px")

        self.label3 = QLabel(self)
        self.notice = QPixmap("icons/notice_dark.png")
        self.label3.setPixmap(self.notice)
        self.label3.resize(self.notice.width(), self.notice.height())
        self.label3.move(500, 190)

        self.show()


app = QApplication(sys.argv)
qdarktheme.setup_theme()
main_window = ChatbotWindow()
sys.exit(app.exec())