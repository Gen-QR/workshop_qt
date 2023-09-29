# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys
import time
from PySide2.QtCore import QObject, QThread, Signal, Slot
from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Form")
        self.layout = QVBoxLayout()
        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.start_thread)

        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def start_thread(self):
        instanced_thread = WorkerThread(self)
        instanced_thread.signals.result.connect(self.print_result)
        instanced_thread.signals.progress.connect(self.print_progress)
        instanced_thread.start()

    @Slot(str)
    def print_result(self, result):
        print(result)

    @Slot(str)
    def print_progress(self, progress):
        print(progress)


class MySignals(QObject):
    result = Signal(int)
    progress = Signal(str)


# Create the Worker Thread
class WorkerThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.signals = MySignals()

    def run(self):
        result = 0
        for i in range(1, 10):
            self.signals.progress.emit(f"Work in Progress: {i}/10")
            time.sleep(1)
            result += i
        self.signals.result.emit(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())
