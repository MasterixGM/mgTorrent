import sys

sys.path.append(r'mgTorrent')
from Util.ViewFunctions import ViewFunctions as vf
from Controller.LoginController import ControladorLogin as LC
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QHBoxLayout, QPushButton, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Login(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setFixedSize(1440, 1024)  # Fixed Window Size
        self.setWindowTitle("SIGN IN") # Window title
        
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        mainLayout = QHBoxLayout(self.centralwidget)

        # Left Widget
        leftWidget = QWidget(self.centralwidget)
        leftLayout = QVBoxLayout(leftWidget)
        leftLayout.setContentsMargins(150, 245, 200, 245) # Left, Top, Right, Bottom 
        mainLayout.addWidget(leftWidget, 2)

        # Welcome message
        MensajeSIGN = QVBoxLayout()
        MensajeSIGN.setSpacing(0)
        
        #SIGN IN text
        SIGNIN = QLabel()
        SIGNIN.setFont(QFont("Segoe UI", 24))
        SIGNIN.setText("SIGN IN")
        SIGNIN.setAlignment(Qt.AlignCenter)
        SIGNIN.setObjectName('SignInLabel')
        MensajeSIGN.addWidget(SIGNIN)

        #SIGN IN SubText
        SIGNINtext = QLabel()
        SIGNINtext.setFont(QFont("Segoe UI", 13))
        SIGNINtext.setText("sign in to your account or register")
        SIGNINtext.setAlignment(Qt.AlignHCenter)
        SIGNINtext.setObjectName('SignInText')
        MensajeSIGN.addWidget(SIGNINtext)
        
        leftLayout.addLayout(MensajeSIGN)

        # Text Field for User and Password
        
        UsernameText = QLineEdit(self)
        UsernameText.setPlaceholderText('Username or Email.')
        UsernameText.setFont(QFont("Segoe UI"))
        UsernameText.setObjectName('UsernameText')
        UsernameText.setFixedHeight(60)
        UsernameText.setFixedWidth(360)
        UsernameText.setStyleSheet("""
                QLineEdit {
                    border-radius: 25px;
                    padding-left: 20px;
                    background: rgba(255, 255, 255, 0.8);
                    border: 2px solid lightgrey;
                }
                QLineEdit:focus {
                    border: 2px solid #00e9c2;
                }
            """)
        
        leftLayout.addWidget(UsernameText)

        PasswordText = QLineEdit(self)
        PasswordText.setPlaceholderText('Password.')
        PasswordText.setEchoMode(QLineEdit.Password)
        PasswordText.setFont(QFont("Segoe UI"))
        PasswordText.setObjectName('PasswordText')
        PasswordText.setFixedHeight(60)
        PasswordText.setFixedWidth(360)
        PasswordText.setStyleSheet("""
                QLineEdit {
                    border-radius: 25px;
                    padding-left: 20px;
                    background: rgba(255, 255, 255, 0.8);
                    border: 2px solid lightgrey;
                }
                QLineEdit:focus {
                    border: 2px solid #00e9c2;
                }
            """)
        
        leftLayout.addWidget(PasswordText)

        # Checkbox and "Forgot password" layout
        Remember_ForgetLayout = QHBoxLayout()
        
        # Remember Me CheckBox
        RememberCheck = QCheckBox()
        RememberCheck.setFont(QFont("Segoe UI"))
        RememberCheck.setText("Remember me.")
        RememberCheck.setObjectName("RememberCheck")
        Remember_ForgetLayout.addWidget(RememberCheck)

        # Forgot Password Text and Link
        ForgotLabel = QLabel()
        ForgotLabel.setFont(QFont("Segoe UI"))
        ForgotLabel.setText('<html><head/><body><p><a href="#" style="color: #0055ff;">Forgot password?</a></p></body></html>')
        ForgotLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        ForgotLabel.setObjectName('ForgotLabel')
        Remember_ForgetLayout.addWidget(ForgotLabel)
        leftLayout.addLayout(Remember_ForgetLayout)

        # Sign In Button
        SignInBttn = QPushButton()
        SignInBttn.setFont(QFont("Segoe UI", 14, QFont.Bold))
        SignInBttn.setText("SIGN IN")
        SignInBttn.setCursor(Qt.PointingHandCursor)
        SignInBttn.setFixedHeight(60)
        SignInBttn.setFixedWidth(270)
        SignInBttn.setObjectName('SignInBttn')
        SignInBttn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 rgba(0, 233, 194, 1),
                                            stop: 1 rgba(0, 131, 109, 1));
                color: white;
                font-size: 18px;
                border-radius: 30px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 rgba(0, 131, 109, 1),
                                            stop: 1 rgba(0, 233, 194, 1));
            }
        """)
        SignInBttn.clicked.connect(lambda: self.controller.login(UsernameText.text(), PasswordText.text()))
        leftLayout.addWidget(SignInBttn, alignment=Qt.AlignCenter)

        #Guest Button and 'OR' text
        
        #OR Label
        orlabel = QLabel()
        orlabel.setFont(QFont("Segoe UI", 13))
        orlabel.setText("OR")
        orlabel.setObjectName("orLabel")
        orlabel.setAlignment(Qt.AlignCenter)
        leftLayout.addWidget(orlabel)

        #Enter as Guest Button
        EnterGuestbttn = QPushButton()
        EnterGuestbttn.setFont(QFont("Segoe UI", 14, QFont.Bold))
        EnterGuestbttn.setText("ENTER AS GUEST")
        EnterGuestbttn.setCursor(Qt.PointingHandCursor)
        EnterGuestbttn.setObjectName('EnterGuestBttn')
        EnterGuestbttn.setFixedHeight(60)
        EnterGuestbttn.setFixedWidth(270)
        EnterGuestbttn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 rgba(0, 233, 194, 1),
                                            stop: 1 rgba(0, 131, 109, 1));
                color: white;
                font-size: 18px;
                border-radius: 30px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 rgba(0, 131, 109, 1),
                                            stop: 1 rgba(0, 233, 194, 1));
            }
        """)
        EnterGuestbttn.clicked.connect(self.controller.login_as_guest)
        leftLayout.addWidget(EnterGuestbttn, alignment=Qt.AlignCenter)

        # Register Label
        RegisterLabel = QLabel()
        RegisterLabel.setText("<html><head/><body><p>Don't have an account? <a href='#'><span style=\" color:#0055ff;\">Register</span></a></p></body></html>")
        RegisterLabel.setAlignment(Qt.AlignCenter)
        leftLayout.addWidget(RegisterLabel)

        # Right Widget (Welcome Message)
        rightWidget = QWidget(self.centralwidget)
        rightWidget.setObjectName('rightWidget') 
        # I don't like this solution but the css doesn't recognise qlineargradient
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
        WelcomeLabel.setAlignment(Qt.AlignCenter)
        WelcomeLabel.setObjectName("WelcomeLabel")
        rightLayout.addWidget(WelcomeLabel)
        
        # Right Welcome Subtext
        PlatformLabel = QLabel(rightWidget)
        PlatformLabel.setFont(QFont("Segoe UI", 13, QFont.Bold))
        PlatformLabel.setText("A Torrent Platform\nBy Dragos.")
        PlatformLabel.setAlignment(Qt.AlignCenter)
        PlatformLabel.setObjectName("PlatformLabel")
        rightLayout.addWidget(PlatformLabel)

        # CSS Stylesheet loading
        vf.load_stylesheet(self,'mgTorrent\View\Styles\Login.css')
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

if __name__ == "__main__": #View Load
    app = QApplication(sys.argv)
    controller = LC()
    window = Login(controller)
    controller.set_login_view(window)
    window.center()
    window.show()
    sys.exit(app.exec_())
