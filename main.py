from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QTextEdit, QLineEdit, QPushButton,QApplication
import sys
from backend import Chatbot

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.chatbot = Chatbot()

        self.setMinimumSize(700,500)

        # Add the Chat ARea widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)

        # Input Field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,480,40)

        # Add the button
        self.button = QPushButton("Send",self)
        self.button.setGeometry(500, 340, 100,40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me: {user_input}")
        self.input_field.clear()

        try:
            response = self.chatbot.get_response(user_input)
            if response:
                # If response is in dict format, extract the message content
                response_text = response.get('message', "No message in response")
                self.chat_area.append(f"Bot: {response_text}")
                print(response_text)  # Print response to CLI for debugging
            else:
                self.chat_area.append("Bot: No response received.")
                print("Error: No response from chatbot.")
        except Exception as e:
            self.chat_area.append(f"Error: {str(e)}")
            print(f"Error in send_message: {e}")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
main_window.show()
sys.exit(app.exec())