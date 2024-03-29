# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QMainWindow,
  QApplication,
  QDial,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My App")

    widget = QDial()

    widget.setRange(-10, 100)
    widget.setSingleStep(5)

    widget.valueChanged.connect(self.value_changed)
    widget.sliderMoved.connect(self.slider_position)
    widget.sliderPressed.connect(self.slider_pressed)
    widget.sliderReleased.connect(self.slider_released)

    # Set the central widget of the Window.
    self.setCentralWidget(widget)

  def value_changed(self, i):
    print(i)

  def slider_position(self, p):
    print("position", p)

  def slider_pressed(self):
    print("Pressed!")

  def slider_released(self):
    print("Released")

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
