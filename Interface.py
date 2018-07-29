import sys
from PyQt5.QtWidgets import (
    QWidget, QMessageBox, QToolTip,
    QPushButton, QDesktopWidget, QApplication,
    QLabel, QLineEdit)  
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class TweetoTa(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        btn = QPushButton('Start', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget for Start')
        btn.resize(btn.sizeHint())
        btn.move(560, 10)

        exbtn = QPushButton('Quit', self)
        exbtn.setToolTip('This is a <b>QPushButton</b> widget for Exit')
        exbtn.clicked.connect(QCoreApplication.instance().quit)
        exbtn.resize(exbtn.sizeHint())
        exbtn.move(560, 410)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
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

    def onChanged(self, text):
      self.lbl.setText(text)
      self.lbl.adjustSize()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = TweetoTa()
    w.resize(650, 450)
    w.center()
    w.setWindowTitle('TweetoTa')
    w.show()

    sys.exit(app.exec_())