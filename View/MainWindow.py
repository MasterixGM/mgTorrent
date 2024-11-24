import sys
sys.path.append(r'mgTorrent')
from Model.ViewFunctions import ViewFunctions as vf
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QWidget
from Controller.MainWindowController import MainController as MC
from View.DownloadBar import Ui_Form as DownloadBar
class MainWindow(QMainWindow):
    def __init__(self, mainController):
        super().__init__()
        self.mainController = mainController
        self.mainController.set_main_view(self)
        self.initUi(self)
        self.setWindowTitle("mgTorrent")
        self.init_controller_connections()
        
    def initUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1470, 1043)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # Elimina los márgenes exteriores
        self.gridLayout.setSpacing(0)  # Elimina el espaciado entre widgets
        
        
        self.TopBar = QtWidgets.QFrame(self.centralwidget)
        self.TopBar.setMaximumSize(QtCore.QSize(16777215, 41))
        self.TopBar.setObjectName("TopBar")
        
        self.TopBarLayout = QtWidgets.QHBoxLayout(self.TopBar)
        self.TopBarLayout.setObjectName("TopBarLayout")
        
        self.SearchIcon = QtWidgets.QLabel(self.TopBar)
        self.SearchIcon.setEnabled(True)
        self.SearchIcon.setMinimumSize(QtCore.QSize(25, 35))
        self.SearchIcon.setMaximumSize(QtCore.QSize(25, 35))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.SearchIcon.setFont(font)
        self.SearchIcon.setText("")
        self.SearchIcon.setPixmap(QtGui.QPixmap("View\Material Icons\search.png"))
        self.SearchIcon.setScaledContents(True)
        self.SearchIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.SearchIcon.setObjectName("SearchIcon")
        
        self.TopBarLayout.addWidget(self.SearchIcon)
        
        self.SearchBar = QtWidgets.QLineEdit(self.TopBar)
        self.SearchBar.setMinimumHeight(35)
        self.SearchBar.setToolTip("")
        self.SearchBar.setObjectName("SearchBar")
        self.SearchBar.setFrame(False)
        
        self.TopBarLayout.addWidget(self.SearchBar)
        
        self.HelpSupportIcon = QtWidgets.QLabel(self.TopBar)
        self.HelpSupportIcon.setMinimumSize(QtCore.QSize(25, 35))
        self.HelpSupportIcon.setMaximumSize(QtCore.QSize(25, 35))
        self.HelpSupportIcon.setText("")
        self.HelpSupportIcon.setPixmap(QtGui.QPixmap("View\Material Icons\support.png"))
        self.HelpSupportIcon.setScaledContents(True)
        self.HelpSupportIcon.setObjectName("HelpSupportIcon")
        
        self.TopBarLayout.addWidget(self.HelpSupportIcon)
        
        self.HelpSupport = QtWidgets.QLabel(self.TopBar)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.HelpSupport.setFont(font)
        self.HelpSupport.setObjectName("HelpSupport")
        
        self.TopBarLayout.addWidget(self.HelpSupport)
        
        self.gridLayout.addWidget(self.TopBar, 0, 1, 1, 2)
        
        self.DownloadsFrame = QtWidgets.QFrame(self.centralwidget)
        self.DownloadsFrame.setMinimumSize(QtCore.QSize(1351, 461))
        self.DownloadsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.DownloadsFrame.setObjectName("DownloadsFrame")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.DownloadsFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.DownloadsLayout = QtWidgets.QVBoxLayout()
        self.DownloadsLayout.setObjectName("DownloadsLayout")
        
        self.NoDownloadsLabel = QtWidgets.QLabel(self.DownloadsFrame)
        self.NoDownloadsLabel.setMinimumSize(QtCore.QSize(1000, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.NoDownloadsLabel.setFont(font)
        self.NoDownloadsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NoDownloadsLabel.setObjectName("NoDownloadsLabel")
        
        self.DownloadsLayout.addWidget(self.NoDownloadsLabel)
        
        self.verticalLayout_2.addLayout(self.DownloadsLayout)
        
        self.gridLayout.addWidget(self.DownloadsFrame, 6, 1, 1, 2)
        
        self.SideBar = QtWidgets.QFrame(self.centralwidget)
        self.SideBar.setMinimumSize(QtCore.QSize(100, 0))
        self.SideBar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SideBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SideBar.setObjectName("SideBar")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SideBar)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.HomeLayout_2 = QtWidgets.QFrame(self.SideBar)
        self.HomeLayout_2.setMinimumSize(QtCore.QSize(0, 50))
        self.HomeLayout_2.setObjectName("HomeLayout_2")
        
        self.HomeLayout = QtWidgets.QVBoxLayout(self.HomeLayout_2)
        self.HomeLayout.setObjectName("HomeLayout")
        
        self.HomeBTTN = QtWidgets.QPushButton(self.HomeLayout_2)
        self.HomeBTTN.setMinimumSize(QtCore.QSize(35, 35))
        self.HomeBTTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.HomeBTTN.setFont(font)
        self.HomeBTTN.setAutoFillBackground(False)
        self.HomeBTTN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("View\Material Icons\home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeBTTN.setIcon(icon)
        self.HomeBTTN.setIconSize(QtCore.QSize(35, 35))
        self.HomeBTTN.setFlat(True)
        self.HomeBTTN.setObjectName("HomeBTTN")
        
        self.HomeLayout.addWidget(self.HomeBTTN)
        
        self.HomeLABEL = QtWidgets.QLabel(self.HomeLayout_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.HomeLABEL.setFont(font)
        self.HomeLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.HomeLABEL.setObjectName("HomeLABEL")
        
        self.HomeLayout.addWidget(self.HomeLABEL)
        
        self.verticalLayout.addWidget(self.HomeLayout_2)
        
        self.torrentsLayout = QtWidgets.QFrame(self.SideBar)
        self.torrentsLayout.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(3)
        self.torrentsLayout.setFont(font)
        self.torrentsLayout.setObjectName("torrentsLayout")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.torrentsLayout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.TorrentsBTTN = QtWidgets.QPushButton(self.torrentsLayout)
        self.TorrentsBTTN.setMinimumSize(QtCore.QSize(35, 35))
        self.TorrentsBTTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(3)
        self.TorrentsBTTN.setFont(font)
        self.TorrentsBTTN.setAutoFillBackground(False)
        self.TorrentsBTTN.setText("")
        TorrentLabel = QtGui.QIcon()
        TorrentLabel.addPixmap(QtGui.QPixmap("View\Material Icons\hard_drive_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TorrentsBTTN.setIcon(TorrentLabel)
        self.TorrentsBTTN.setIconSize(QtCore.QSize(35, 35))
        self.TorrentsBTTN.setFlat(True)
        self.TorrentsBTTN.setObjectName("TorrentsBTTN")
        
        self.verticalLayout_3.addWidget(self.TorrentsBTTN)
        
        self.TorrentsLABEL = QtWidgets.QLabel(self.torrentsLayout)
        self.TorrentsLABEL.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.TorrentsLABEL.setFont(font)
        self.TorrentsLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.TorrentsLABEL.setObjectName("TorrentsLABEL")
        
        self.verticalLayout_3.addWidget(self.TorrentsLABEL)
        
        self.verticalLayout.addWidget(self.torrentsLayout)
        
        self.verticalFrame_2 = QtWidgets.QFrame(self.SideBar)
        self.verticalFrame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.UploadsBTTN = QtWidgets.QPushButton(self.verticalFrame_2)
        self.UploadsBTTN.setMinimumSize(QtCore.QSize(35, 35))
        self.UploadsBTTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.UploadsBTTN.setFont(font)
        self.UploadsBTTN.setAutoFillBackground(False)
        self.UploadsBTTN.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("View\Material Icons\cloud_upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UploadsBTTN.setIcon(icon2)
        self.UploadsBTTN.setIconSize(QtCore.QSize(35, 35))
        self.UploadsBTTN.setFlat(True)
        self.UploadsBTTN.setObjectName("UploadsBTTN")
        
        self.verticalLayout_4.addWidget(self.UploadsBTTN)
        
        self.UploadLABEL = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.UploadLABEL.setFont(font)
        self.UploadLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.UploadLABEL.setObjectName("UploadLABEL")
        
        self.verticalLayout_4.addWidget(self.UploadLABEL)
        
        self.verticalLayout.addWidget(self.verticalFrame_2)
        
        self.settingsLayout = QtWidgets.QFrame(self.SideBar)
        self.settingsLayout.setMinimumSize(QtCore.QSize(50, 50))
        self.settingsLayout.setObjectName("settingsLayout")
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settingsLayout)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.SettingsBTTN = QtWidgets.QPushButton(self.settingsLayout)
        self.SettingsBTTN.setMinimumSize(QtCore.QSize(35, 35))
        self.SettingsBTTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.SettingsBTTN.setFont(font)
        self.SettingsBTTN.setAutoFillBackground(False)
        self.SettingsBTTN.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("View\Material Icons\settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsBTTN.setIcon(icon3)
        self.SettingsBTTN.setIconSize(QtCore.QSize(35, 35))
        self.SettingsBTTN.setFlat(True)
        self.SettingsBTTN.setObjectName("SettingsBTTN")
        
        self.verticalLayout_5.addWidget(self.SettingsBTTN)
        
        self.SettingsLABEL = QtWidgets.QLabel(self.settingsLayout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SettingsLABEL.setFont(font)
        self.SettingsLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.SettingsLABEL.setObjectName("SettingsLABEL")
        
        self.verticalLayout_5.addWidget(self.SettingsLABEL)
        
        self.verticalLayout.addWidget(self.settingsLayout)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        
        self.LogoutFrame = QtWidgets.QFrame(self.SideBar)
        self.LogoutFrame.setMinimumSize(QtCore.QSize(50, 50))
        self.LogoutFrame.setObjectName("LogoutFrame")
        
        self.logoutLayout = QtWidgets.QVBoxLayout(self.LogoutFrame)
        self.logoutLayout.setObjectName("logoutLayout")
        
        self.LogoutBTTN = QtWidgets.QPushButton(self.LogoutFrame)
        self.LogoutBTTN.setMinimumSize(QtCore.QSize(35, 35))
        self.LogoutBTTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.LogoutBTTN.setFont(font)
        self.LogoutBTTN.setAutoFillBackground(False)
        self.LogoutBTTN.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("View\Material Icons\logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LogoutBTTN.setIcon(icon4)
        self.LogoutBTTN.setIconSize(QtCore.QSize(35, 35))
        self.LogoutBTTN.setFlat(True)
        self.LogoutBTTN.setObjectName("LogoutBTTN")
        
        self.logoutLayout.addWidget(self.LogoutBTTN)
        
        self.LogoutLABEL = QtWidgets.QLabel(self.LogoutFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.LogoutLABEL.setFont(font)
        self.LogoutLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoutLABEL.setObjectName("LogoutLABEL")
        
        self.logoutLayout.addWidget(self.LogoutLABEL)
        
        self.verticalLayout.addWidget(self.LogoutFrame)
        
        self.gridLayout.addWidget(self.SideBar, 0, 0, 7, 1)
        
        self.BoxFrame = QtWidgets.QFrame(self.centralwidget)
        self.BoxFrame.setMinimumSize(QtCore.QSize(1000, 480))
        self.BoxFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.BoxFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.BoxFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BoxFrame.setObjectName("BoxFrame")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.BoxFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.BytesUpBox = QtWidgets.QFrame(self.BoxFrame)
        self.BytesUpBox.setMaximumSize(QtCore.QSize(300, 300))
        self.BytesUpBox.setFrameShape(QtWidgets.QFrame.Box)
        self.BytesUpBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BytesUpBox.setObjectName("BytesUpBox")
        
        self.UploadLabel = QtWidgets.QLabel(self.BytesUpBox)
        self.UploadLabel.setGeometry(QtCore.QRect(20, 20, 77, 77))
        self.UploadLabel.setText("")
        self.UploadLabel.setPixmap(QtGui.QPixmap("View\Material Icons\cloud_upload.png"))
        self.UploadLabel.setScaledContents(True)
        self.UploadLabel.setObjectName("UploadLabel")
        
        self.UploadSizeLabel = QtWidgets.QLabel(self.BytesUpBox)
        self.UploadSizeLabel.setGeometry(QtCore.QRect(30, 200, 169, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.UploadSizeLabel.setFont(font)
        self.UploadSizeLabel.setObjectName("UploadSizeLabel")
        
        self.UpLabel = QtWidgets.QLabel(self.BytesUpBox)
        self.UpLabel.setGeometry(QtCore.QRect(30, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UpLabel.setFont(font)
        self.UpLabel.setObjectName("UpLabel")
        
        self.horizontalLayout_2.addWidget(self.BytesUpBox)
        
        self.BytesDownBox = QtWidgets.QFrame(self.BoxFrame)
        self.BytesDownBox.setMaximumSize(QtCore.QSize(300, 300))
        self.BytesDownBox.setFrameShape(QtWidgets.QFrame.Box)
        self.BytesDownBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BytesDownBox.setObjectName("BytesDownBox")
        
        self.DownloadLabel_2 = QtWidgets.QLabel(self.BytesDownBox)
        self.DownloadLabel_2.setGeometry(QtCore.QRect(20, 20, 77, 77))
        self.DownloadLabel_2.setText("")
        self.DownloadLabel_2.setPixmap(QtGui.QPixmap("View\Material Icons\cloud_download.png"))
        self.DownloadLabel_2.setScaledContents(True)
        self.DownloadLabel_2.setObjectName("DownloadLabel_2")
        
        self.DownloadSizeLabel = QtWidgets.QLabel(self.BytesDownBox)
        self.DownloadSizeLabel.setGeometry(QtCore.QRect(30, 200, 169, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.DownloadSizeLabel.setFont(font)
        self.DownloadSizeLabel.setObjectName("DownloadSizeLabel")
        
        self.DownLabel = QtWidgets.QLabel(self.BytesDownBox)
        self.DownLabel.setGeometry(QtCore.QRect(30, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DownLabel.setFont(font)
        self.DownLabel.setObjectName("DownLabel")
        
        self.horizontalLayout_2.addWidget(self.BytesDownBox)
        
        self.TotalDownBox = QtWidgets.QFrame(self.BoxFrame)
        self.TotalDownBox.setMaximumSize(QtCore.QSize(300, 300))
        self.TotalDownBox.setFrameShape(QtWidgets.QFrame.Box)
        self.TotalDownBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TotalDownBox.setObjectName("TotalDownBox")
        
        self.HardDriveLabel = QtWidgets.QLabel(self.TotalDownBox)
        self.HardDriveLabel.setGeometry(QtCore.QRect(20, 20, 77, 77))
        self.HardDriveLabel.setText("")
        self.HardDriveLabel.setPixmap(QtGui.QPixmap("View\Material Icons\hard_drive_2.png"))
        self.HardDriveLabel.setScaledContents(True)
        self.HardDriveLabel.setObjectName("HardDriveLabel")
        
        self.TotalDownloadLabel = QtWidgets.QLabel(self.TotalDownBox)
        self.TotalDownloadLabel.setGeometry(QtCore.QRect(30, 200, 169, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.TotalDownloadLabel.setFont(font)
        self.TotalDownloadLabel.setObjectName("TotalDownloadLabel")
        
        self.TotalLabel = QtWidgets.QLabel(self.TotalDownBox)
        self.TotalLabel.setGeometry(QtCore.QRect(30, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TotalLabel.setFont(font)
        self.TotalLabel.setObjectName("TotalLabel")
        
        self.horizontalLayout_2.addWidget(self.TotalDownBox)
        
        self.TorrentDownBox = QtWidgets.QFrame(self.BoxFrame)
        self.TorrentDownBox.setMaximumSize(QtCore.QSize(300, 300))
        self.TorrentDownBox.setFrameShape(QtWidgets.QFrame.Box)
        self.TorrentDownBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TorrentDownBox.setObjectName("TorrentDownBox")
        
        self.TorrentLabel = QtWidgets.QLabel(self.TorrentDownBox)
        self.TorrentLabel.setGeometry(QtCore.QRect(110, 20, 77, 77))
        self.TorrentLabel.setText("")
        self.TorrentLabel.setPixmap(QtGui.QPixmap("View\Material Icons\download.png"))
        self.TorrentLabel.setScaledContents(True)
        self.TorrentLabel.setObjectName("TorrentLabel")
        
        self.TorrentDownSizeLabel = QtWidgets.QLabel(self.TorrentDownBox)
        self.TorrentDownSizeLabel.setGeometry(QtCore.QRect(73, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TorrentDownSizeLabel.setFont(font)
        self.TorrentDownSizeLabel.setObjectName("TorrentDownSizeLabel")
        
        self.TorrentDownHintLabel = QtWidgets.QLabel(self.TorrentDownBox)
        self.TorrentDownHintLabel.setGeometry(QtCore.QRect(60, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TorrentDownHintLabel.setFont(font)
        self.TorrentDownHintLabel.setObjectName("TorrentDownHintLabel")
        
        self.TorrentDownORLabel = QtWidgets.QLabel(self.TorrentDownBox)
        self.TorrentDownORLabel.setGeometry(QtCore.QRect(135, 180, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TorrentDownORLabel.setFont(font)
        self.TorrentDownORLabel.setObjectName("TorrentDownORLabel")
        
        self.BrowseBTTN = QtWidgets.QPushButton(self.TorrentDownBox)
        self.BrowseBTTN.setGeometry(QtCore.QRect(45, 220, 210, 50))
        self.BrowseBTTN.setMinimumSize(QtCore.QSize(70, 50))
        self.BrowseBTTN.setMaximumSize(QtCore.QSize(210, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseBTTN.setFont(font)
        self.BrowseBTTN.setObjectName("BrowseBTTN")
        
        self.horizontalLayout_2.addWidget(self.TorrentDownBox)
        
        self.gridLayout.addWidget(self.BoxFrame, 1, 1, 1, 2)
        
        self.RecentTorrentShowAllFrame = QtWidgets.QFrame(self.centralwidget)
        self.RecentTorrentShowAllFrame.setMinimumSize(QtCore.QSize(1000, 0))
        self.RecentTorrentShowAllFrame.setObjectName("RecentTorrentShowAllFrame")
        
        self.RecentTorrentShowAllLayout = QtWidgets.QHBoxLayout(self.RecentTorrentShowAllFrame)
        self.RecentTorrentShowAllLayout.setObjectName("RecentTorrentShowAllLayout")
        
        self.RecentTorrents = QtWidgets.QLabel(self.RecentTorrentShowAllFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.RecentTorrents.setFont(font)
        self.RecentTorrents.setObjectName("RecentTorrents")
        
        self.RecentTorrentShowAllLayout.addWidget(self.RecentTorrents)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.RecentTorrentShowAllLayout.addItem(spacerItem2)
        
        self.SeeAllTorrentsBTTN = QtWidgets.QLabel(self.RecentTorrentShowAllFrame)
        self.SeeAllTorrentsBTTN.setMinimumSize(QtCore.QSize(10, 21))
        self.SeeAllTorrentsBTTN.setMaximumSize(QtCore.QSize(115, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SeeAllTorrentsBTTN.setFont(font)
        self.SeeAllTorrentsBTTN.setCursor(QtCore.Qt.PointingHandCursor)
        self.SeeAllTorrentsBTTN.setObjectName("SeeAllTorrentsBTTN")
        
        self.RecentTorrentShowAllLayout.addWidget(self.SeeAllTorrentsBTTN)
        
        self.gridLayout.addWidget(self.RecentTorrentShowAllFrame, 3, 1, 3, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NoDownloadsLabel.setText(_translate("MainWindow", "Looks like there is nothing here, Start Downloading!"))
        self.LogoutLABEL.setText(_translate("MainWindow", "LOGOUT"))
        self.HomeLABEL.setText(_translate("MainWindow", "HOME"))
        self.TorrentsLABEL.setText(_translate("MainWindow", "TORRENTS"))
        self.UploadLABEL.setText(_translate("MainWindow", "UPLOAD"))
        self.SettingsLABEL.setText(_translate("MainWindow", "SETTINGS"))
        self.SearchBar.setPlaceholderText(_translate("MainWindow", " SEARCH FOR A TORRENT"))
        self.HelpSupport.setText(_translate("MainWindow", "HELP AND SUPPORT"))
        self.UploadSizeLabel.setText(_translate("MainWindow", "0 Gb"))
        self.UpLabel.setText(_translate("MainWindow", "Bytes Uploaded"))
        self.DownloadSizeLabel.setText(_translate("MainWindow", "0 Gb"))
        self.DownLabel.setText(_translate("MainWindow", "Bytes Downloaded"))
        self.TotalDownloadLabel.setText(_translate("MainWindow", "0 Gb"))
        self.TotalLabel.setText(_translate("MainWindow", "Total Downloaded on APP"))
        self.TorrentDownSizeLabel.setText(_translate("MainWindow", ".TORRENT, MAX SIZE 2MB"))
        self.TorrentDownHintLabel.setText(_translate("MainWindow", "Drag & Drop torrent files here"))
        self.TorrentDownORLabel.setText(_translate("MainWindow", "OR"))
        self.BrowseBTTN.setText(_translate("MainWindow", "Browse"))
        self.RecentTorrents.setText(_translate("MainWindow", "Recent Torrents"))
        self.SeeAllTorrentsBTTN.setText(_translate("MainWindow", "SEE ALL TORRENTS"))

        vf.load_stylesheet(self, "View\Styles\Main.css")
        
    #This method connects the UI components to the controller methods.    
    def init_controller_connections(self):
        # Connecting sidebar buttons to controller methods
        self.LogoutBTTN.clicked.connect(self.mainController.logout)
        self.BrowseBTTN.clicked.connect(self.mainController.browse) 
      
    def center(self):
        self.showMaximized()
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    download_controller = MC(DownloadBar)
    window = MainWindow(download_controller)
    window.show()
    window.center()
    sys.exit(app.exec_())