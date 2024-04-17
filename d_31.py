import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

  def __init__(self, color):
    super(Color, self).__init__()
    self.setAutoFillBackground(True)

    palette = self.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(color))
    self.setPalette(palette)

class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My App")

    main_layout = QHBoxLayout()
    layout_left = QVBoxLayout()
    layout_right = QVBoxLayout()

    main_layout.setContentsMargins(70, 30, 10, 0)
    main_layout.setSpacing(5)

    layout_left.addWidget(Color('red'))
    layout_left.addWidget(Color('yellow'))
    layout_left.addWidget(Color('purple'))

    main_layout.addLayout( layout_left )

    main_layout.addWidget(Color('green'))

    layout_right.addWidget(Color('red'))
    layout_right.addWidget(Color('purple'))

    main_layout.addLayout( layout_right )

    widget = QWidget()
    widget.setLayout(main_layout)
    self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.setGeometry(100, 100, 500, 800)
window.show()

app.exec()