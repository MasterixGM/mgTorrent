import sys, os, logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication
from Util.MessageHandler import MessageHandler
from View.Register import Register
from View.MainWindow import MainWindow
from Controller.RegisterController import RegisterController
from Util.DBHandler import DBManager

class ControladorLogin:
    def __init__(self):
        self.app = QApplication(sys.argv)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        self.MessageHandler = MessageHandler
        self.RegisterController = RegisterController
        self.db_handler = DBManager()  # Initialize the DBHandler instance
        self.main_window = None
        self.register_view = None
        
    def set_login_view(self, login_view):
        self.login_view = login_view
        self.message_Handler = MessageHandler(self.login_view)  # Pass the parent widget to MessageHandler

    def login(self, user_or_email, password):
        from View.MainWindow import MainWindow
        try:
            # Log para verificar los valores de entrada
            self.logger.debug(f"Attempting login for: {user_or_email}")
        
            if self.db_handler.user_exists(user_or_email):
                if self.db_handler.check_password(user_or_email, password):
                    self.logger.info(f"Login successful for user: {user_or_email}")
                    self.login_view.hide()
                    self.main_window = MainWindow()
                    self.main_window.show()
                else:
                    self.logger.warning(f"Incorrect password for user: {user_or_email}")
                    self.message_Handler.showErrorMessage(message="User or password is incorrect, please try again.")
            else:
                self.logger.warning(f"User or email not found: {user_or_email}")
                self.message_Handler.showErrorMessage(message="User or password is incorrect, please try again.")
        except Exception as e:
            self.logger.error(f"Login error for user {user_or_email}: {str(e)}")
            self.message_Handler.showErrorMessage(message=f"An error occurred, please try again later. Error: {str(e)}")
            
    def registerClick(self):
        if self.register_view is None:
            self.logger.debug("Initializing and centering the register view.")
            self.register_view = Register(RegisterController)
            self.register_view.show_and_center()
        if self.login_view:
            self.login_view.hide()
            self.register_view.show_and_center()    

    def login_as_guest(self):
        try:
            self.login_view.hide()
            self.main_window = MainWindow()
            self.main_window.show()
            # Need to Apply something to block options
        except:
            self.message_Handler.showErrorMessage(message="An error occurred, please try again later.")
        
    def rememberMe(self):  # Pending on Implementation
        try:
            # Something to remember the choice of the user
            pass
        except:
            self.message_Handler.showErrorMessage(message="An error occurred, please try again later.")
            
    def run(self):
        self.login_view.show()
        sys.exit(self.app.exec_())
        
if __name__ == "__main__":
    ControladorLogin().run()