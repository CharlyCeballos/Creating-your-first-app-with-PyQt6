# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")
    self.label = QLabel("Test right button please")

    # Set the central widget of the Window.
    self.setCentralWidget(self.label)

  def contextMenuEvent(self, e):
    context = QMenu(self)
    context.addAction(QAction("test 1", self))
    context.addAction(QAction("test 2", self))
    context.addAction(QAction("test 3", self))
    context.exec(e.globalPos())

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
