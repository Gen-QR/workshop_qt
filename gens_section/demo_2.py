import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 200)  # Set the window geometry (x, y, width, height)
        self.setWindowTitle('PySide2 Workshop')


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
