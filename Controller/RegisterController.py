import sys, logging
from PyQt5.QtWidgets import QApplication
from Model.MessageHandler import MessageHandler
from Model.DBHandler import DBManager

class RegisterController:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        self.message_handler = MessageHandler(self)
        self.db_manager = DBManager()
        self.login_window = None
        self.register_view = None

    def set_login_window(self, login_window):
        self.login_window = login_window

    def set_register_view(self, register_view):
        self.register_view = register_view
        self.message_handler = MessageHandler(self.register_view)

    def register(self, user, password, email):
        try:
            # Verifies if Username or Email are available
            if self.db_manager.user_exists(user) or self.db_manager.user_exists(email):
                self.message_handler.showWarningMessage("Username or Email already exists")
                return
            
            # If both are available then procceed to register
            self.db_manager.add_user(user, password, email)
            self.message_handler.showInfoMessage("Registration successful")

            if self.login_window:
                self.login_window.show()
                
            if self.register_view:
                self.register_view.hide()
                
        except Exception as e:
            self.message_handler.showErrorMessage("An error occurred: {}".format(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = RegisterController()
    sys.exit(app.exec_())
