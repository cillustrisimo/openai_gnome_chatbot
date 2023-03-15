from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QLabel, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtCore
from playsound import playsound
import sys
import qdarktheme
from backend import Chatbot
import threading
from nltk.sentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


class ChatbotWindow(QMainWindow, QWidget):
    keyPressed = QtCore.pyqtSignal()

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
        self.mood_normal()

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

        self.mood = ""
        self.sound = ""

        self.show()

    def send_message(self):
        self.user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#bdc3c8'>Me: {self.user_input}</p>")
        self.input_field.clear()
        print(self.user_input)

        threading.Thread(target=self.get_bot_response, args=(self.user_input, )).start()

    def get_bot_response(self, user_input):
        self.response = self.chatbot.get_response(user_input)
        self.update_chat()

    def update_chat(self):
        self.chat_area.append(f"<p style='color:#bdc3c8'>Mr. Sneed: {self.response}</p>")
        print(self.response)
        threading.Thread(target=self.analyze()).start()

    def mood_normal(self):
        normal_pixmap = QPixmap("sneeds/sneed-small.png")
        self.label.setPixmap(normal_pixmap)
        self.label.resize(190, 170)
        self.label.move(500, 12)

    def mood_happy(self):
        happy_pixmap = QPixmap('sneeds/sneed-happy-small.png')
        self.label.setPixmap(happy_pixmap)
        threading.Timer(1.5, self.reset_emotion).start()

    def mood_fear(self):
        angry_pixmap = QPixmap('sneeds/sneed-fear-small.png')
        self.label.setPixmap(angry_pixmap)
        threading.Timer(3, self.reset_emotion).start()

    def mood_neutral(self):
        neutral_pixmap = QPixmap('sneeds/sneed-neutral-small.png')
        self.label.setPixmap(neutral_pixmap)
        threading.Timer(1.5, self.reset_emotion).start()

    def reset_emotion(self):
        normal_pixmap = QPixmap("sneeds/sneed-small.png")
        self.label.setPixmap(normal_pixmap)

    def analyze(self):
        user_mood = self.user_input
        scores = analyzer.polarity_scores(user_mood)

        if scores['neg'] > scores['pos']:
            self.mood = "sad"
        elif scores['pos'] > scores['neg']:
            self.mood = 'happy'
        else:
            self.mood = "neutral"

        thread2 = threading.Thread(target=self.mood_change())
        thread2.start()

    def mood_change(self):
        if self.mood == "sad":
            self.sound = "sounds/angry.mp3"
            self.mood_fear()
        elif self.mood == "happy":
            self.sound = "sounds/laugh.mp3"
            self.mood_happy()
        elif self.mood == "neutral":
            self.sound = "sounds/neutral.mp3"
            self.mood_neutral()
        self.play_sound()

    def play_sound(self):
        sound = self.sound
        playsound(sound)


app = QApplication(sys.argv)
qdarktheme.setup_theme()
main_window = ChatbotWindow()
main_window.setWindowTitle("Mr. Sneed Messenger")
playsound("sounds/welcome-redux.mp3")
sys.exit(app.exec())
