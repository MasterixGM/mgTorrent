import sys
from PyQt5.QtWidgets import QApplication
from Controller.LoginController import ControladorLogin as LC
from View.Login import Login

def main():
    app = QApplication(sys.argv)
    
    # Crear instancia del controlador de login
    loginController = LC()
    
    # Crear e inicializar la ventana de login
    login_window = Login(loginController)
    loginController.set_login_view(login_window)
    login_window.center()
    login_window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
