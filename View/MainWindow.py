import sys
sys.path.append(r'mgTorrent')
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from Util.TorrentManager import TorrentManager as tm
from Util.DBHandler import DBHandler as dbh

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Establishes the window name
        self.setWindowTitle("mgTorrent")
        
        layout = QVBoxLayout()
        self.label = QLabel("Welcome to mgTorrent")
        layout.addWidget(self.label)
        
        self.add_button = QPushButton("Add a Torrent")
        self.add_button.clicked.connect(self.download_torrent_bttn)
        layout.addWidget(self.add_button)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.torrent_manager = tm()
        self.db_handler = dbh()
        
        #Executes the download variable when hitting the button
    def download_torrent_bttn(self):
        file_dialog = QFileDialog()
        torrent_file, _ = file_dialog.getOpenFileName(self, "Choose a Torrent", "", "Torrent Files (*.torrent)")
        if torrent_file:
            handle = self.torrent_manager.download_torrent(torrent_file)
            self.db_handler.download_torrent(handle.name(), "Uploading", 0)
            self.label.setText(f"Torrent Added: {handle.name()}") 