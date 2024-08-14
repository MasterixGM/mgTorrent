# Class that handles torrent files.

import libtorrent as lt

class TorrentManager:
    
    def __init__(self): 
        self.session = lt.session()
        
    # Method to download torrent files
    def download_torrent(self, torrent_file, save_path = './downloads'):
        try:
            info = lt.torrent_info(torrent_file)
            handle = self.session.add_torrent({'ti': info, 'save_path': save_path}) # Esto es de ejemplo la de ./downloads deberia cambiarlo a la decision del usuario    
            return handle
        except:
            print("Error downloading torrent")
            
    # Method to Check the status of a torrent
    def get_torrent_status(self, handle):
        try:
            return handle.status()
        except:
            print("Error getting torrent status")