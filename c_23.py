# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QMainWindow,
  QApplication,
  QLineEdit,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My App")

    widget = QLineEdit()
    widget.setMaxLength(10)
    widget.setPlaceholderText("Enter your text")

    #widget.setReadOnly(True) # uncomment this to make readonly

    widget.returnPressed.connect(self.enter_pressed) #IDK why returnPressed catch Enter key
    widget.selectionChanged.connect(self.selection_changed)
    widget.textChanged.connect(self.text_changed)
    widget.textEdited.connect(self.text_edited)

    # Set the central widget of the Window.
    self.setCentralWidget(widget)

  def enter_pressed(self):
    print("Return pressed!")
    self.centralWidget().setText("BOOM!")

  def selection_changed(self):
    print("Selection changed")
    print(self.centralWidget().selectedText())

  def text_changed(self, s):
    print("Text changed...")
    print(s)

  def text_edited(self, s):
    print("Text edited...")
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
