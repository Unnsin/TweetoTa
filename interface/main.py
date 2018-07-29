import sys
from PyQt5.QtWidgets import (
    QWidget, 
    QApplication, 
    QMessageBox, 
    QToolTip,
    QDesktopWidget)  
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class TweetoTa(QWidget):
    def __init__(self):
      super().__init__()

      self.initUI()

    def initUI(self):
      QToolTip.setFont(QFont('SansSerif', 10))

      self.setToolTip('This is a main frame')

      self.setGeometry(650, 450, 650, 450)
      self.setWindowTitle('TweetoTa')
      self.center()
      self.show()
    
    def closeEvent(self, event):
      reply = QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)

      if reply == QMessageBox.Yes:
        event.accept()
      else:
        event.ignore()

    def center(self):
      qr = self.frameGeometry()
      cp = QDesktopWidget().availableGeometry().center()
      qr.moveCenter(cp)
      self.move(qr.topLeft())
    

app = QApplication(sys.argv)
main = TweetoTa()
sys.exit(app.exec_())