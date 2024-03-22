# Only needed for access to command line arguments
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")
    self.label = QLabel("Click in this window")

    # Set the central widget of the Window.
    self.setCentralWidget(self.label)

  def mouseMoveEvent(self, e):
    self.label.setText("mouseMoveEvent")

  def mousePressEvent(self, e):
    self.label.setText("mousePressEvent")

  def mouseReleaseEvent(self, e):
    self.label.setText("mouseReleaseEvent")

  def mouseDoubleClickEvent(self, e):
    self.label.setText("mouseDoubleClickEvent")

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
