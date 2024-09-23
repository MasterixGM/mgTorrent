import sys, os, logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QFileDialog
from Controller.DownloadBarController import DownloadBarController
from Util.MessageHandler import MessageHandler as mh

class MainController:
    def __init__(self, ui):
        # Basic logger configuration
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        self.ui = ui
        self.download_bar_controller = DownloadBarController(self.ui)  # Download bar controller
        self.active_Downloads = [] # List of active Downloads
        self.main_view = None # Initial initialization of the view
        
    # Set the main view and connect the signals
    def set_main_view(self, main_view):
        self.main_view = main_view # Asignation of the Main View
        self.main_view.show()
        
    #Called when the 'Browse' button is clicked.
    def browse(self):
        from View.DownloadBar import Ui_Form  # Import the UI class for the download bar
        from Util.TorrentManager import TorrentManager as tm
        
        self.logger.info("Browse button clicked")
        
        # Open file dialog to select a .torrent file
        browseFile = QFileDialog.getOpenFileName(self.main_view, 'Select a file to download', '.', 'Torrent Files (*.torrent)')
        
        if browseFile[0]:  # If a file is selected
            torrent_file = browseFile[0]
            
            if tm.is_torrent_downloaded(self, torrent_file, "./Downloads"):
                mh.showInfoMessage(self, "Torrent already downloaded")
                return
            else:
                self.main_view.NoDownloadsLabel.hide()
                # Create a new widget for the download
                downloadBar = Ui_Form()
                self.main_view.DownloadsLayout.addWidget(downloadBar)

                # Create a controller to manage the download
                controller = DownloadBarController(downloadBar)
                controller.start_download(torrent_file, "./Downloads") # Start the download process
            
    #Starts the download of a torrent file.
    def start_download(self, torrent_file, save_path):
        try:
            download_instance = DownloadBarController(self.ui)
            self.active_Downloads.append(download_instance)
            
             # Call the method to start the download from the download bar controller
            download_instance.start_download(torrent_file, save_path)
            self.logger.info(f"Started download: {torrent_file}")
            download_instance.download_thread.finished.connect(download_instance.deleteLater)
        except Exception as e:
            self.handle_error(e)  # Handle errors that may occur during the download
            
    # Update the progress bar in the UI
    def update_progress_bar(self, progress):
        self.logger.info(f"Updating progress bar: {progress}%")
        self.download_bar_controller.ui.progressBar.setValue(progress) 
        
    # Show the "No Downloads" label when all downloads are complete
    def on_download_finished(self):
        self.logger.info("Download finished!")
        self.main_view.NoDownloadsLabel.show()  
   
    # Display an error message in the UI and Logger
    def handle_error(self, error):
        """Handles any error that occurs during the download."""
        self.logger.error(f"Error during download: {error}")
        mh.showErrorMessage(self, "An Error Ocurred During the Download.")

    #Logs out the current user and shows the login screen.
    def logout(self):
        from View.Login import Login
        from Controller.LoginController import ControladorLogin
        self.login_view = Login(ControladorLogin)
        self.login_view.show()
