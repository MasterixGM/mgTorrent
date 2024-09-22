import logging
from Util.TorrentManager import TorrentDownloadThread as tdt
from PyQt5.QtCore import QObject

class DownloadBarController(QObject):
    def __init__(self, ui):
        super().__init__()
        
        #Instance of UI
        self.ui = ui
        
        #Initialization of the Thread
        self.download_thread = tdt(None, None) #Default Inicialization
        
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        
    def start_download(self, torrent_file, save_path):
        
        try:
            # Start the download Thread
            self.download_thread = tdt(torrent_file, save_path)
        
            #Connect the proggress signal with the ui updato method
            self.download_thread.progress_updated.connect(self.update_progress)
            logging.info("Signal Connected.")
        
            self.download_thread.start()
            logging.info("Thread Iniciated.")
            
        except Exception as e:
            logging.error(f"ERROR AT DOWNLOAD: " + str(e))
            
    def update_progress(self, progress, download_rate, upload_rate, remaining_time):
        # Update the UI with the Torrent Information
        try:
            if hasattr(self.ui, 'progressBar'):
                self.ui.progressBar.setValue(progress)
            logging.info(f"Download Rate: {download_rate}")
            logging.info(f"Upload Rate: {upload_rate}")
            logging.info(f"Remaining Time: {remaining_time}")
            logging.info(f"Progress: {progress}%")    
            
            # TODO : Update the UI with the Torrent Information (DownloadBar Doesn't connect properly that's why this doesn't update, i do receive the data as shown in logging info)

            """self.ui.PercentageProgressBar.setText(f"{progress}%")
            self.ui.CurrentDownloadLabel.setText(download_rate)
            self.ui.CurrentUploadLabel.setText(upload_rate)
            self.ui.DownloadTimeLabel.setText(remaining_time)
            logging.info("Progress Updated.")"""
        except Exception as e:
            logging.error("Error Updating Progress: " + str(e))    
            
    def pause_download(self):
        # Pause the download
        if self.download_thread:
            self.download_thread.stop()

    def show_info(self):
        print("Torrent Info") # Temporal solution will do a separate window for this