# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QMainWindow,
  QApplication,
  QSpinBox,
  # QDoubleSpinBox,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My App")

    widget = QSpinBox()
    # Or: widget = QDoubleSpinBox()

    widget.setMinimum(-10)
    widget.setMaximum(3)
    # Or: widget.setRange(-10,3)

    widget.setPrefix("$")
    widget.setSuffix("c")
    widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
    widget.valueChanged.connect(self.value_changed)
    widget.textChanged.connect(self.value_changed_str)

    widget.lineEdit().setReadOnly(True)

    # Set the central widget of the Window.
    self.setCentralWidget(widget)

  def value_changed(self, i):
    print(i)

  def value_changed_str(self, s):
    print(s)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event loop has stopped.
