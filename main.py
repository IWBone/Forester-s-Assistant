import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from ModuleConnect import connect
import tracemalloc
tracemalloc.start()

class CalcWood(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = uic.loadUi("Calc_wood.ui", self)
        self.connect = connect(ui)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcWood()
    sys.exit(app.exec())