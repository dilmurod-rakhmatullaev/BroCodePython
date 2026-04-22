import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 .QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(r"C:\Users\SB\BackendProjects\BroCodePython\lesson10\gui_logo.jpg"))

        image_label = QLabel(self)
        image_label.setGeometry(0, 250, 250, 250)

        pixmap = QPixmap(r"C:\Users\SB\BackendProjects\BroCodePython\lesson10\gui_logo.jpg")
        image_label.setPixmap(pixmap)

        image_label.setScaledContents(True)
        image_label.setGeometry((self.width()- image_label.width()) // 2,
                           (self.height() - image_label.height()) // 2,
                          image_label.width(),
                          image_label.height())

        text_label = QLabel("Hello", self)
        text_label.setFont(QFont("Times New Roman", 40))
        text_label.setGeometry(0, 0, 500, 100)
        text_label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # text_label.setAlignment(Qt.AlignTop)   # Vertically top
        # text_label.setAlignment(Qt.AlignBottom)  # Vertically bottom
        # text_label.setAlignment(Qt.AlignVCenter) # Vertically Center

        # text_label.setAlignment(Qt.AlignRight) # Horizontally Right
        # text_label.setAlignment(Qt.AlignLeft) # Horizontally Left
        # text_label.setAlignment(Qt.AlignHCenter) # # Horizontally Center

        # text_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
        # text_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
        # text_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
        text_label.setAlignment(Qt.AlignCenter)   # Center & Center


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()