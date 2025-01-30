import sys
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # Cria nossa Aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

