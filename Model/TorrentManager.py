import logging, os
import libtorrent as lt
from PyQt5.QtCore import QThread, pyqtSignal 
from Model.MessageHandler import MessageHandler as mh
class TorrentManager:
    
    def __init__(self): 
        self.session = lt.session()
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        
    # Method to download torrent files
    def download_torrent(self, torrent_file, save_path = './downloads'):
        try:
            info = lt.torrent_info(torrent_file)
            handle = self.session.add_torrent({'ti': info, 'save_path': save_path}) # This should be a user choice.  
            return handle
        except:
            print("Error downloading torrent")
            
    def is_torrent_downloaded(self, torrent_file, save_path):
        try:
            # Load the torrent file information
            info = lt.torrent_info(torrent_file)

            # Get the list of files from the torrent
            file_storage = info.files()
            num_files = file_storage.num_files()

            # Verify each file in the directory
            for index in range(num_files):
                file_path = os.path.join(save_path, file_storage.file_path(index))
                expected_size = file_storage.file_size(index)

                # If the file doesn't exist or its size is incorrect, the torrent is not fully downloaded
                if not os.path.exists(file_path):
                    logging.info(f"File {file_path} not found. Torrent is not fully downloaded.")
                    return False
                elif os.path.getsize(file_path) != expected_size:
                    logging.info(f"The file {file_path} has an incorrect size. Expected: {expected_size}, Actual: {os.path.getsize(file_path)}.")
                    return False

            logging.info("All torrent files are present and the correct size.")
            return True
        except Exception as e:
            logging.error(f"Error checking if the torrent is downloaded: {str(e)}")
            return False

    # Method to Check the status of a torrent
    def get_torrent_status(self, handle):
        try:
            return handle.status()
        except:
            print("Error getting torrent status")
            
class TorrentDownloadThread(QThread):
    progress_updated = pyqtSignal(int, str, str, str)  # Señal para actualizar la interfaz
    finished = pyqtSignal()  # Señal para indicar que la descarga finalizó
    
    def __init__(self, torrent_file, save_path):
        super().__init__()
        self.torrent_file = torrent_file
        self.save_path = save_path
        self.manager = TorrentManager()
        self.handle = None
        self.is_downloading = True
        self.progress_data = (0, "0.00 MB/s", "0.00 MB/s", "N/A")
    
    def run(self):
        try:
            if self.manager.is_torrent_downloaded(self.torrent_file, self.save_path):
                logging.info("Torrent is already downloaded.")
                self.finished.emit()
                return

            # Inicia la descarga
            self.handle = self.manager.download_torrent(self.torrent_file, self.save_path)
            logging.info("Download started.")

            while self.is_downloading and not self.handle.is_seed():
                # Obtener el estado del torrent
                status = self.manager.get_torrent_status(self.handle)
                progress = int(status.progress * 100)
                download_rate = f"{status.download_rate / 1000:.2f} MB/s"
                upload_rate = f"{status.upload_rate / 1000:.2f} MB/s"
                remaining_time = (status.total_wanted - status.total_wanted_done) / status.download_rate if status.download_rate > 0 else 0
                remaining_time_str = f"{int(remaining_time // 60)} min {int(remaining_time % 60)} sec"

                # Actualiza los datos de progreso
                self.progress_data = (progress, download_rate, upload_rate, remaining_time_str)
                self.emit_progress_signal()

                # Pausa para no sobrecargar la interfaz
                self.msleep(200)
            
            # Si se convierte en semilla, indica que la descarga terminó
            if self.handle.is_seed():
                self.progress_data = (100, "0.00 MB/s", "0.00 MB/s", "0 min 0 sec")
                self.emit_progress_signal()
                logging.info("Download completed. Torrent is now a seed.")
                self.finished.emit()

        except Exception as e:
            logging.error(f"Error in TorrentDownloadThread: {e}")
        finally:
            self.is_downloading = False  # Marca la descarga como detenida
            logging.info("TorrentDownloadThread has finished.")

    def stop(self):
        """Solicita detener el hilo."""
        logging.info("Stopping TorrentDownloadThread...")
        self.is_downloading = False
        self.quit()  # Finaliza el bucle de eventos del hilo
        self.wait()  # Espera a que el hilo termine antes de continuar

    def emit_progress_signal(self):
        """Emite la señal de progreso."""
        self.progress_updated.emit(*self.progress_data)
        logging.debug(f"Progress: {self.progress_data}")

        