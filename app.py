# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.button_is_checked = True

    self.setWindowTitle("My App")

    self.button = QPushButton("Press Me!")
    self.setFixedSize(QSize(400, 300))
    self.button.setCheckable(True)
    self.button.released.connect(self.the_button_was_released)
    self.button.setChecked(self.button_is_checked)

    # Set the central widget of the Window.
    self.setCentralWidget(self.button)

  def the_button_was_released(self):
    self.button_is_checked = self.button.isChecked()

    print(self.button_is_checked)

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
