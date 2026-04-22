import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 .QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(r"C:\Users\SB\BackendProjects\BroCodePython\lesson10\gui_logo.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Times New Roman", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignTop)   # Vertically top
        # label.setAlignment(Qt.AlignBottom)  # Vertically bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically Center

        # label.setAlignment(Qt.AlignRight) # Horizontally Right
        # label.setAlignment(Qt.AlignLeft) # Horizontally Left
        # label.setAlignment(Qt.AlignHCenter) # # Horizontally Center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
        label.setAlignment(Qt.AlignCenter)   # Center & Center


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()