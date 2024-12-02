import logging
from Model.TorrentManager import TorrentDownloadThread as tdt
from PyQt5.QtCore import QObject, QThread

class DownloadBarController(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Instancia de la interfaz de usuario
        self.download_thread = None  # No inicializamos hasta que se necesite
        logging.basicConfig(level=logging.DEBUG, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                            handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        
    def start_download(self, torrent_file, save_path):
        # Verifica si ya hay un hilo en ejecución
        if self.download_thread and self.download_thread.isRunning():
            self.logger.warning("Download thread is already running. Aborting new download.")
            return

        try:
            # Crea e inicializa el hilo de descarga
            self.download_thread = tdt(torrent_file, save_path)
            
            # Conecta señales para gestionar la interfaz y la finalización del hilo
            self.download_thread.progress_updated.connect(self.ui.update_ui)
            self.download_thread.finished.connect(self.on_download_finished)
            self.download_thread.start()
            self.logger.info("Download thread started successfully.")
        
        except Exception as e:
            self.logger.error(f"Error starting download: {str(e)}")
            
    def pause_download(self):
        # Pausa la descarga de manera segura
        if self.download_thread:
            self.download_thread.stop()

    def on_download_finished(self):
        # Lógica cuando la descarga finaliza
        if self.download_thread:
            self.logger.info("Download finished. Cleaning up thread.")
            self.download_thread.wait()  # Asegúrate de que el hilo termine completamente
            self.download_thread.deleteLater()
            self.download_thread = None  # Limpia la referencia al hilo

    def stop_all(self):
        # Método para detener el hilo antes de salir de la aplicación
        if self.download_thread and self.download_thread.isRunning():
            self.logger.info("Stopping all active downloads.")
            self.download_thread.stop()
            self.download_thread.wait()  # Espera a que termine

    def close(self):
        # Método a invocar al cerrar la aplicación o ventana
        self.logger.info("Closing DownloadBarController. Stopping threads if needed.")
        self.stop_all()
