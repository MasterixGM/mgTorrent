import sys
sys.path.append(r'mgTorrent')
from Util.ViewFunctions import ViewFunctions as vf
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1440, 1024)  # Fixed Window Size
        self.setWindowTitle("SIGN UP") # Window title
        
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
        MensajeSIGN.setSpacing(10) # Espaciado entre textos
        
        # SIGN UP text
        SIGNUP = QLabel()
        SIGNUP.setFont(QFont("Segoe UI", 28, QFont.Bold)) # Tamaño de fuente más grande
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
        fields = ["Email.", "Username.", "Password."]
        for placeholder in fields:
            textField = QLineEdit(self)
            textField.setPlaceholderText(placeholder)
            textField.setFont(QFont("Segoe UI", 12))
            textField.setObjectName("TextFields")
            textField.setFixedHeight(60)
            textField.setFixedWidth(360)
            
            if placeholder == "Password.":
                textField.setEchoMode(QLineEdit.Password)
            leftLayout.addWidget(textField)

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

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
                
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.center()
    window.show()
    sys.exit(app.exec_())
