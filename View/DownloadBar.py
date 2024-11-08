import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from Controller.DownloadBarController import DownloadBarController
from Util.ViewFunctions import ViewFunctions as vf
class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.downloadController = DownloadBarController(self)
        if self.downloadController.download_thread:
            self.downloadController.download_thread.progress_updated.connect(self.update_ui)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)    

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1302, 98)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1301, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")

        # Interface elements such as Download labels, progress bar, etc...
        self.Icon = QtWidgets.QLabel(self.frame)
        self.Icon.setGeometry(QtCore.QRect(30, 10, 80, 80))
        self.Icon.setFrameShape(QtWidgets.QFrame.Box)
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("mgTorrent/View/Material Icons/download.png"))
        self.Icon.setScaledContents(True)
        self.Icon.setObjectName("Icon")

        self.TorrentNameLabel = QtWidgets.QLabel(self.frame)
        self.TorrentNameLabel.setGeometry(QtCore.QRect(138, 15, 280, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TorrentNameLabel.setFont(font)
        self.TorrentNameLabel.setObjectName("TorrentNameLabel")

        self.DownloadIcon = QtWidgets.QLabel(self.frame)
        self.DownloadIcon.setGeometry(QtCore.QRect(138, 45, 31, 31))
        self.DownloadIcon.setText("")
        self.DownloadIcon.setPixmap(QtGui.QPixmap("mgTorrent/View/Material Icons/cloud_download.png"))
        self.DownloadIcon.setScaledContents(True)
        self.DownloadIcon.setObjectName("DownloadIcon")

        self.CurrentDownloadLabel = QtWidgets.QLabel(self.frame)
        self.CurrentDownloadLabel.setGeometry(QtCore.QRect(175, 55, 85, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.CurrentDownloadLabel.setFont(font)
        self.CurrentDownloadLabel.setObjectName("CurrentDownloadLabel")

        self.CurrentUploadLabel = QtWidgets.QLabel(self.frame)
        self.CurrentUploadLabel.setGeometry(QtCore.QRect(325, 55, 85, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.CurrentUploadLabel.setFont(font)
        self.CurrentUploadLabel.setObjectName("CurrentUploadLabel")

        self.UploadIcon = QtWidgets.QLabel(self.frame)
        self.UploadIcon.setGeometry(QtCore.QRect(290, 45, 31, 31))
        self.UploadIcon.setText("")
        self.UploadIcon.setPixmap(QtGui.QPixmap("mgTorrent/View/Material Icons/cloud_upload.png"))
        self.UploadIcon.setScaledContents(True)
        self.UploadIcon.setObjectName("UploadIcon")

        self.DownloadTimeLabel = QtWidgets.QLabel(self.frame)
        self.DownloadTimeLabel.setGeometry(QtCore.QRect(455, 55, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.DownloadTimeLabel.setFont(font)
        self.DownloadTimeLabel.setObjectName("DownloadTimeLabel")

        self.TimeIcon = QtWidgets.QLabel(self.frame)
        self.TimeIcon.setGeometry(QtCore.QRect(420, 45, 31, 31))
        self.TimeIcon.setText("")
        self.TimeIcon.setPixmap(QtGui.QPixmap("mgTorrent/View/Material Icons/time.png"))
        self.TimeIcon.setScaledContents(True)
        self.TimeIcon.setObjectName("TimeIcon")

        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(140, 87, 825, 5))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.PercentageProgressBar = QtWidgets.QLabel(self.frame)
        self.PercentageProgressBar.setGeometry(QtCore.QRect(910, 68, 23, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.PercentageProgressBar.setFont(font)
        self.PercentageProgressBar.setObjectName("PercentageProgressBar")

        self.InfoBTTN = QtWidgets.QPushButton(self.frame)
        self.InfoBTTN.setEnabled(True)
        self.InfoBTTN.setGeometry(QtCore.QRect(944, -10, 181, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.InfoBTTN.setFont(font)
        self.InfoBTTN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.InfoBTTN.setAutoFillBackground(False)
        self.InfoBTTN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mgTorrent/View/Material Icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InfoBTTN.setIcon(icon)
        self.InfoBTTN.setIconSize(QtCore.QSize(24, 24))
        #self.InfoBTTN.clicked.connect(self.downloadController.show_info)
        self.InfoBTTN.setObjectName("InfoBTTN")

        self.PauseBTTN = QtWidgets.QPushButton(self.frame)
        self.PauseBTTN.setEnabled(True)
        self.PauseBTTN.setGeometry(QtCore.QRect(1120, -10, 181, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.PauseBTTN.setFont(font)
        self.PauseBTTN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PauseBTTN.setAutoFillBackground(False)
        self.PauseBTTN.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("mgTorrent/View/Material Icons/pause_circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PauseBTTN.setIcon(icon1)
        self.PauseBTTN.setIconSize(QtCore.QSize(24, 24))
        #self.PauseBTTN.clicked.connect(self.downloadController.pause_download)
        self.PauseBTTN.setObjectName("PauseBTTN")

        self.InfoLabel = QtWidgets.QLabel(self.frame)
        self.InfoLabel.setGeometry(QtCore.QRect(1021, 60, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setObjectName("InfoLabel")

        self.PauseLabel = QtWidgets.QLabel(self.frame)
        self.PauseLabel.setGeometry(QtCore.QRect(1193, 60, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.PauseLabel.setFont(font)
        self.PauseLabel.setObjectName("PauseLabel")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        vf.load_stylesheet(self, "mgTorrent\View\Styles\DownloadBar.css")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.TorrentNameLabel.setText(_translate("Form", "Torrent Ejemplo"))
        self.CurrentDownloadLabel.setText(_translate("Form", "0 MB/S"))
        self.CurrentUploadLabel.setText(_translate("Form", "0 MB/S"))
        self.DownloadTimeLabel.setText(_translate("Form", "0 mins 0 sec"))
        self.PercentageProgressBar.setText(_translate("Form", "0%"))
        self.InfoLabel.setText(_translate("Form", "INFO"))
        self.PauseLabel.setText(_translate("Form", "PAUSE"))
    
    def update_ui(self, progress, download_rate, upload_rate, remaining_time):
        # Here the UI updates with the download info
        logging.info(f"UI updated with progress: {progress}, download_rate: {download_rate}, upload_rate: {upload_rate}, remaining_time: {remaining_time}")
        
        try:
            self.progressBar.setValue(progress)
            self.CurrentDownloadLabel.setText(download_rate)
            self.CurrentUploadLabel.setText(upload_rate)
            self.DownloadTimeLabel.setText(remaining_time)
            self.PercentageProgressBar.setText(f"{progress}%")
            
        except Exception as e:
            logging.error("Error at download updating ui: " + str(e))