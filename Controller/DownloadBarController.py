import logging
from Util.TorrentManager import TorrentDownloadThread as tdt
from PyQt5.QtCore import QObject

class DownloadBarController(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui #Instance of UI
        self.download_thread = tdt(None, None) #Initialization of the Thread
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        
    def start_download(self, torrent_file, save_path):
        if self.download_thread and self.download_thread.isRunning():
            logging.warning("Download thread is already running. Aborting new download.")
            return

        try:
            # Start the download Thread
            self.download_thread = tdt(torrent_file, save_path)
        
            # Connect the progress signal with the ui updated method
            self.download_thread.progress_updated.connect(self.ui.update_ui)
            logging.info("Signal Connected.")
        
            self.download_thread.start()
            logging.info("Thread Iniciated.")
        
        except Exception as e:
            logging.error(f"ERROR AT DOWNLOAD: " + str(e))
            
    def pause_download(self):
        # Pause the download
        if self.download_thread:
            self.download_thread.stop()

    def on_Download_Finished(self):
        self.download_thread.stop()
        self.download_thread.wait()
        self.download_thread.deleteLater()
        self.download_thread = None

    def show_info(self):
        print("Torrent Info") # Temporal solution will do a separate window for this