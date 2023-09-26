import sys
from PySide2.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()

        my_label = QLabel("Look at all of these cool widgets!")
        my_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(my_label)

        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

        # Create a label
        self.label = QLabel('Welcome to PySide2 Workshop!', self)
        self.label.setGeometry(10, 10, 380, 30)  # Set the label's position and size

        # Create a button
        self.button = QPushButton('Click Me', self)
        self.button.setGeometry(10, 50, 100, 30)  # Set the button's position and size

        # Connect the button click event to a function
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        self.label.setText('Button Clicked!')


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
