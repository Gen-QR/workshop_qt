import sys

from PySide2.QtWidgets import (
    QApplication, 
    QComboBox, 
    QDialog, 
    QDialogButtonBox, 
    QGridLayout, 
    QGroupBox, 
    QFormLayout, 
    QHBoxLayout, 
    QLabel, 
    QLineEdit, 
    QMenu, 
    QMenuBar, 
    QPushButton, 
    QSpinBox, 
    QTextEdit, 
    QVBoxLayout,
)


class Dialog(QDialog):
    num_grid_rows = 3
    num_buttons = 4

    def __init__(self):
        # this init method does not need to be modified
        # make your changes only in the methods below
        super().__init__()

        self.create_horizontal_group_box()
        self.create_grid_group_box()
        self.create_form_group_box()

        big_editor = QTextEdit()
        big_editor.setPlainText("This widget takes up all the remaining space "
                "in the top-level layout.")

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self._horizontal_group_box)
        main_layout.addWidget(self._grid_group_box)
        main_layout.addWidget(self._form_group_box)
        main_layout.addWidget(big_editor)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

        self.setWindowTitle("Basic Layouts")

    def create_horizontal_group_box(self):
        self._horizontal_group_box = QGroupBox("Horizontal layout")
        layout = QHBoxLayout()

        # create buttons like this:
        # button_1 = QPushButton("Button 1")

        self._horizontal_group_box.setLayout(layout)

    def create_grid_group_box(self):
        self._grid_group_box = QGroupBox("Grid layout")
        layout = QGridLayout()

        # helping tip: to add a widget that spans multiple rows or columns,
        # use the QGridLayout.addWidget() overload that takes rowSpan and
        # columnSpan as additional arguments.
        # layout.addWidget(some_widget, row, column, rowSpan, columnSpan)

        self._grid_group_box.setLayout(layout)

    def create_form_group_box(self):
        self._form_group_box = QGroupBox("Form layout")
        layout = QGridLayout()

        # helping tip: this are the kind of widgets you may need:
        # label = QLabel("Line 1:")
        # edit = QLineEdit()
        # combo = QComboBox()
        # spin = QSpinBox()
        # layout.addWidget(label, 0, 0)

        self._form_group_box.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec())
