# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QMainWindow,
  QApplication,
  QCheckBox,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My App")

    widget = QCheckBox()
    widget.setCheckState(Qt.CheckState.Checked)
    widget.setCheckState(Qt.CheckState.Unchecked)
    widget.setCheckState(Qt.CheckState.PartiallyChecked)

    # For tristate: widget.setCheckState(Qt.PartiallyChecked)
    # Or: widget.setTriState(True)
    widget.stateChanged.connect(self.show_state)

    # Set the central widget of the Window.
    self.setCentralWidget(widget)

  def show_state(self, s):
    print(s == Qt.CheckState.Checked.value)
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
