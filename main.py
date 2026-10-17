import os
import sys
import ctypes  # Добавляем для работы с Windows API
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon  # Добавляем для глобальной иконки
from PyQt6 import uic
from ModuleConnect import Connect

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

class CalcWood(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = uic.loadUi(get_resource_path("Calc_wood.ui"), self)
        self.connect = Connect(ui)
        self.show()

if __name__ == '__main__':
    # Явно указываем Windows наш собственный App ID
    myappid = 'wbone.forester_assistant.app.4_2' 
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except AttributeError:
        pass  # Защита от ошибок на других ОС

    app = QApplication(sys.argv)
    
    # Устанавливаем глобальную иконку для всего приложения
    app.setWindowIcon(QIcon(get_resource_path("icon.ico")))
    
    window = CalcWood()
    sys.exit(app.exec())