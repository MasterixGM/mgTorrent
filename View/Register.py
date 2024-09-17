import sys, re
sys.path.append(r'mgTorrent')
from Util.ViewFunctions import ViewFunctions as vf
from Controller.RegisterController import RegisterController as RC
from Util.MessageHandler import MessageHandler
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Register(QMainWindow):
    def __init__(self, registerController):
        super().__init__()
        self.registerController = registerController()
        self.message_handler = MessageHandler(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(1440, 1024)  # Fixed Window Size
        self.setWindowTitle("SIGN UP")  # Window title
        
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        mainLayout = QHBoxLayout(self.centralwidget)

        # Left Widget
        leftWidget = QWidget(self.centralwidget)
        leftLayout = QVBoxLayout(leftWidget)
        leftLayout.setContentsMargins(150, 245, 200, 245)  # Left, Top, Right, Bottom 
        mainLayout.addWidget(leftWidget, 2)

        # Welcome message
        MensajeSIGN = QVBoxLayout()
        MensajeSIGN.setSpacing(10)
        
        # SIGN UP text
        SIGNUP = QLabel()
        SIGNUP.setFont(QFont("Segoe UI", 28, QFont.Bold))
        SIGNUP.setText("SIGN UP")
        SIGNUP.setObjectName("SignUpLabel")
        SIGNUP.setAlignment(Qt.AlignCenter)
        MensajeSIGN.addWidget(SIGNUP)

        # SIGN UP SubText
        SIGNUPtext = QLabel()
        SIGNUPtext.setFont(QFont("Segoe UI", 14))
        SIGNUPtext.setObjectName("SignUpSubLabel")
        SIGNUPtext.setText("Please fill the fields below.")
        SIGNUPtext.setAlignment(Qt.AlignCenter)
        MensajeSIGN.addWidget(SIGNUPtext)
        
        leftLayout.addLayout(MensajeSIGN)

        # Text Fields for Email, Username and Password
        self.emailField = QLineEdit(self)
        self.emailField.setPlaceholderText("Email.")
        self.emailField.setFont(QFont("Segoe UI", 12))
        self.emailField.setObjectName("TextFields")
        self.emailField.setFixedHeight(60)
        self.emailField.setFixedWidth(360)
        leftLayout.addWidget(self.emailField)

        self.usernameField = QLineEdit(self)
        self.usernameField.setPlaceholderText("Username.")
        self.usernameField.setFont(QFont("Segoe UI", 12))
        self.usernameField.setObjectName("TextFields")
        self.usernameField.setFixedHeight(60)
        self.usernameField.setFixedWidth(360)
        leftLayout.addWidget(self.usernameField)

        self.passwordField = QLineEdit(self)
        self.passwordField.setPlaceholderText("Password.")
        self.passwordField.setFont(QFont("Segoe UI", 12))
        self.passwordField.setObjectName("TextFields")
        self.passwordField.setFixedHeight(60)
        self.passwordField.setFixedWidth(360)
        self.passwordField.setEchoMode(QLineEdit.Password)
        leftLayout.addWidget(self.passwordField)

        # Sign Up Button
        SignUpBttn = QPushButton()
        SignUpBttn.setFont(QFont("Segoe UI", 18, QFont.Bold))
        SignUpBttn.setText("SIGN UP")
        SignUpBttn.setCursor(Qt.PointingHandCursor)
        SignUpBttn.setFixedHeight(60)
        SignUpBttn.setFixedWidth(270)
        SignUpBttn.setObjectName("SignUpButton")
        SignUpBttn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 rgba(0, 233, 194, 1),
                                            stop: 1 rgba(0, 131, 109, 1));
                color: white;
                font-size: 18px;
                border-radius: 25px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 rgba(0, 131, 109, 1),
                                            stop: 1 rgba(0, 233, 194, 1));
            }
        """)
        SignUpBttn.clicked.connect(self.handle_register)
        leftLayout.addWidget(SignUpBttn, alignment=Qt.AlignCenter)

        # Terms and Conditions
        TermsLabel = QLabel()
        TermsLabel.setText("<html><head/><body><p>By signing up you accept our <a href='#'><span style=\" color:#0055ff;\">terms and conditions.</span></a></p></body></html>")
        TermsLabel.setAlignment(Qt.AlignCenter)
        TermsLabel.setObjectName("TermsLabel")
        leftLayout.addWidget(TermsLabel)

        # Right Widget (Welcome Message)
        rightWidget = QWidget(self.centralwidget)
        rightWidget.setObjectName('rightWidget')
        rightWidget.setStyleSheet("""
                                  #rightWidget { 
                                    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                                                stop: 0 rgba(0, 233, 194, 1),
                                                                stop: 1 rgba(0, 131, 109, 1)); 
                                    }
                                """)
        rightLayout = QVBoxLayout(rightWidget)
        rightLayout.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(rightWidget, 3)

        # Right Welcome label
        WelcomeLabel = QLabel(rightWidget)
        WelcomeLabel.setFont(QFont("Segoe UI", 28, QFont.Bold))
        WelcomeLabel.setText("WELCOME TO MGTORRENT")
        WelcomeLabel.setObjectName("WelcomeLabel")
        WelcomeLabel.setAlignment(Qt.AlignCenter)
        rightLayout.addWidget(WelcomeLabel)
        
        # Right Welcome Subtext
        PlatformLabel = QLabel(rightWidget)
        PlatformLabel.setFont(QFont("Segoe UI", 13, QFont.Bold))
        PlatformLabel.setText("A Torrent platform\nby Dragos.")
        PlatformLabel.setObjectName("PlatformLabel")
        PlatformLabel.setAlignment(Qt.AlignCenter)
        rightLayout.addWidget(PlatformLabel)
        
        vf.load_stylesheet(self, "mgTorrent\View\Styles\Register.css")

    def handle_register(self):
        # This Way i Get the Data on the TextField Fields
        email = self.emailField.text()
        username = self.usernameField.text()
        password = self.passwordField.text()

        # This way i check for Blanks on the fields
        if not username:
            self.message_handler.showErrorMessage("Username is required")
            return

        if not password:
            self.message_handler.showErrorMessage("Password is required")
            return

        if not email:
            self.message_handler.showErrorMessage("Email is required")
            return
        
        # Validate email format
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            self.message_handler.showErrorMessage("Invalid email format")
            return
        
        self.registerController.register(username, password, email)
       
    def show_and_center(self):
        self.show()
        qtRectangle = self.frameGeometry()  # Obtains the Window Rectangle Geometry
        centerPoint = QDesktopWidget().availableGeometry().center()  # Finds the center of the screen
        qtRectangle.moveCenter(centerPoint)  # Moves the rectangle to the center
        self.move(qtRectangle.topLeft())  # Moves the window to top-Left to Center it.   
                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    registerController = RC()
    sys.exit(app.exec_())
