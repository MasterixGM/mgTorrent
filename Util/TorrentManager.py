import libtorrent as lt
from PyQt5.QtCore import QThread, pyqtSignal 

class TorrentManager:
    
    def __init__(self): 
        self.session = lt.session()
        
    # Method to download torrent files
    def download_torrent(self, torrent_file, save_path = './downloads'):
        try:
            info = lt.torrent_info(torrent_file)
            handle = self.session.add_torrent({'ti': info, 'save_path': save_path}) # This should be a user choice.  
            return handle
        except:
            print("Error downloading torrent")
            
    # Method to Check the status of a torrent
    def get_torrent_status(self, handle):
        try:
            return handle.status()
        except:
            print("Error getting torrent status")
            
class TorrentDownloadThread(QThread):
    progress_updated = pyqtSignal(int, str, str, str)  # Signal to update the interface (Progress, Download Speed, Upload Speed, Remaining Time).
    
    def __init__(self, torrent_file, save_path):
        super().__init__()
        self.torrent_file = torrent_file
        self.save_path = save_path
        self.manager = TorrentManager()
        self.handle = None
        self.is_downloading = True

    def run(self):
        # Torrent Download Start
        self.handle = self.manager.download_torrent(self.torrent_file, self.save_path)
        
        while not self.handle.is_seed() and self.is_downloading:
            status = self.manager.get_torrent_status(self.handle)
            
            if  status.progress < 100:
                
                # Download Progress
                progress = int(status.progress * 100)
            
                # Download and Upload speeds
                download_rate = f"{status.download_rate / 1000:.2f} MB/s"
                upload_rate = f"{status.upload_rate / 1000:.2f} MB/s"
            
                # Remaining Time
                remaining_time = (status.total_wanted - status.total_wanted_done) / status.download_rate if status.download_rate > 0 else 0
                remaining_time_str = f"{int(remaining_time // 60)} min {int(remaining_time % 60)} sec"
            
                # We transmit the signal with the updated information
                self.progress_updated.emit(progress, download_rate, upload_rate, remaining_time_str)
            
                self.msleep(500)  # 0.5 sec pause to update regularly.
                
            else:
                self.finished.emit()
                self.stop()
                
    def stop(self):
        self.is_downloading = False  # This stops the Thread
        self.finished.connect(self.deleteLater)
        self.quit()   