from PyQt5.QtWidgets import QMessageBox

class MessageHandler:
    
    def __init__(self, parent):
        self.parent = parent
    
    def showErrorMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("ERROR")
        msg_box.setText(message)
        msg_box.exec_()
        
    def showInfoMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("INFO")
        msg_box.setText(message)
        msg_box.exec_()
        
    def showWarningMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("WARNING")
        msg_box.setText(message)
        msg_box.exec_()    