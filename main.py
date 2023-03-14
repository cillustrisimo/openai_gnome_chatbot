from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QPixmap
import sys
import qdarktheme
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 440)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 455, 680, 35)
        self.input_field.returnPressed.connect(self.send_message)

        self.button = QPushButton(QIcon("icons/send.png"), "", self)
        self.button.setGeometry(650, 456, 35, 30)
        self.button.clicked.connect(self.send_message)

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

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#bdc3c8'>Me: {user_input}</p>")
        self.input_field.clear()
        print(user_input)

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#bdc3c8'>Mr. Sneed: {response}</p>")
        print(response)


app = QApplication(sys.argv)
qdarktheme.setup_theme()
main_window = ChatbotWindow()
sys.exit(app.exec())