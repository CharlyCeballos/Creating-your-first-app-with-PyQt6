# Only needed for access to command line arguments
import sys

from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QComboBox,
  QDateEdit,
  QDateTimeEdit,
  QDial,
  QDoubleSpinBox,
  QFontComboBox,
  QLabel,
  QLCDNumber,
  QLineEdit,
  QMainWindow,
  QProgressBar,
  QPushButton,
  QRadioButton,
  QSlider,
  QSpinBox,
  QTimeEdit,
  QVBoxLayout,
  QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.show()

    self.setWindowTitle("Widgets App")

    layout = QVBoxLayout()
    widgets = [
      QCheckBox,
      QComboBox,
      QDateEdit,
      QDateTimeEdit,
      QDial,
      QDoubleSpinBox,
      QFontComboBox,
      QLCDNumber,
      QLabel,
      QLineEdit,
      QProgressBar,
      QPushButton,
      QRadioButton,
      QSlider,
      QSpinBox,
      QTimeEdit,
    ]

    for w in widgets:
      layout.addWidget(w())

    widget = QWidget()
    widget.setLayout(layout)

    # Set the central widget of the Window. Widget will expand
    # to take up all the space in the window by default.
    self.setCentralWidget(widget)

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
###################################################################################
# Lets have a look at all the example widgets, from top to bottom:
'''
Widget 	        ||  What it does
____________________________________
QCheckbox 	    ||  A checkbox
QComboBox 	    ||  A dropdown list box
QDateEdit 	    ||  For editing dates and datetimes
QDateTimeEdit 	||  For editing dates and datetimes
QDial 	        ||  Rotatable dial
QDoubleSpinBox 	||  A number spinner for floats
QFontComboBox 	||  A list of fonts
QLCDNumber 	    ||  A quite ugly LCD display
QLabel 	        ||  Just a label, not interactive
QLineEdit 	    ||  Enter a line of text
QProgressBar 	  ||  A progress bar
QPushButton 	  ||  A button
QRadioButton 	  ||  A toggle set, with only one active item
QSlider 	      ||  A slider
QSpinBox 	      ||  An integer spinner
QTimeEdit 	    ||  For editing times
'''
