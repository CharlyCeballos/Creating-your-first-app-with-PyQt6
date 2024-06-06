import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel

def main():

  app = QApplication(sys.argv)

  font = QFont("Fira Code", pointSize=12, italic=True)

  label = QLabel()
  label.setFont(font)
  label.setText("Hello world!! >= == <=")
  label.resize(640, 480)
  label.setAlignment(Qt.AlignmentFlag.AlignCenter)
  label.show()

  sys.exit(app.exec())


if __name__ == "__main__":
  main()

"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QLabel

def main():

  app = QApplication(sys.argv)

  # db = QFontDatabase()
  # font = db.font("RAVIE", "Medium Italic", 12)
  ## OR
  font = QFont("Fira Code", pointSize=12, weight=QFont.Medium, italic=True)

  label = QLabel(alignment=Qt.AlignCenter)
  label.setFont(font)
  label.setText("Hello world!! >= == <=")
  label.resize(640, 480)
  label.show()

  sys.exit(app.exec_())


if __name__ == "__main__":
  main()

"""