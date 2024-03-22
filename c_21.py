# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QMainWindow,
  QApplication,
  QComboBox,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My App")

    widget = QComboBox()
    widget.setEditable(True)
    widget.setMaxCount(2)
    widget.addItems(["One", "Two", "Three"])

    # Sends the current index (position) of the selected item.
    widget.currentIndexChanged.connect( self.index_changed )

    # There is an alternate signal to send the text.
    widget.currentTextChanged.connect( self.text_changed )

    # Set the central widget of the Window.
    self.setCentralWidget(widget)

  def index_changed(self, i): # i is an int
    print(i)

  def text_changed(self, s): # s is a str
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
