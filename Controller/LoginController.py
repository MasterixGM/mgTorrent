import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication
from Util.MessageHandler import MessageHandler
from View.MainWindow import MainWindow

class ControladorLogin:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.MessageHandler = MessageHandler
        self.main_window = None

    def set_login_view(self, login_view):
        self.login_view = login_view
        self.message_Handler = MessageHandler(self.login_view)  # Pass the parent widget to MessageHandler

    def login(self, user, password):
        try:
            if (user == "Juan" and password == "1234"): #Test
                self.login_view.hide()
                self.main_window = MainWindow()
                self.main_window.show()
            else: 
                self.message_Handler.showErrorMessage(message = "User or password is incorrect, please try again.")
        except:
                self.message_Handler.showErrorMessage(message = "An error occurred, please try again later.")

    def login_as_guest(self):
        try:
            self.login_view.hide()
            self.main_window = MainWindow()
            self.main_window.show()
            # Need to Apply something to block options
        except:
            self.message_Handler.showErrorMessage(message = "An error occurred, please try again later.")
        
    def rememberMe(self):
        try:
            # Something to remember the choice of the user
            pass
        except:
            self.message_Handler.showErrorMessage(message = "An error occurred, please try again later.")
            
    def run(self):
        self.login_view.show()
        sys.exit(self.app.exec_())
        
if __name__ == "__main__":
    ControladorLogin().run()