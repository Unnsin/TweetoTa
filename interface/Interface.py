import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QMessageBox, QToolTip,
    QPushButton, QDesktopWidget, QApplication,
    QLabel, QLineEdit, QGridLayout, QTextEdit)  
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
sys.path.append(os.path.join(sys.path[0], '../parse/'))
import twitterpars
filename = "sysname.txt"
file = open(filename, encoding="UTF-8", mode="r")
files = []
for line in file: 
    files.append(line)

class TweetoTa(QWidget):
  def __init__(self):
    super().__init__()
    self.AccountText = ''
    self.initUI()
    self.parser = twitterpars.Parser(files)
    
  def initUI(self):
    QToolTip.setFont(QFont('SansSerif', 10))
    self.setToolTip('This is a <b>QWidget</b> widget')
    
    self.logOutput = QTextEdit(self)
    self.logOutput.setReadOnly(True)
    self.logOutput.resize(470,420)
    self.logOutput.move(10, 15)

    self.qle = QLineEdit(self)
    self.qle.move(500, 10)
    self.qle.textChanged[str].connect(self.onChanged)
    
    self.initButtons()

    self.setGeometry(300, 300, 300, 200)
    self.setWindowTitle('Tooltips')
    self.show()
    
  def initButtons(self):
    self.btn = QPushButton('Add Account', self)
    self.btn.setToolTip('This is a add acount button')
    self.btn.clicked.connect(self.AddButtonClicked)
    self.btn.resize(self.btn.sizeHint())
    self.btn.move(525, 40)

    self.exbtn = QPushButton('Quit', self)
    self.exbtn.setToolTip('This is a exit button')
    self.exbtn.clicked.connect(QCoreApplication.instance().quit)
    self.exbtn.resize(self.exbtn.sizeHint())
    self.exbtn.move(540, 410)

    self.startbtn = QPushButton('Start', self)
    self.startbtn.setToolTip('This is a start button')
    self.startbtn.clicked.connect(self.StartButtonClick)
    self.startbtn.resize(self.startbtn.sizeHint())
    self.startbtn.move(538, 70)

    self.editbtn = QPushButton('Edit', self)
    self.editbtn.setToolTip('This is a edit accounts button')
    self.editbtn.clicked.connect(self.EditButtonClick)
    self.editbtn.resize(self.editbtn.sizeHint())
    self.editbtn.move(540, 105)

    self.savebtn = QPushButton('Save', self)
    self.savebtn.setToolTip('This is a edit accounts button')
    self.savebtn.clicked.connect(self.SaveButtonClick)
    self.savebtn.resize(self.savebtn.sizeHint())
    self.savebtn.move(540, 370)
    self.savebtn.hide()

  def SaveButtonClick(self): 
    print(self.logOutput.toPlainText())

  def StartButtonClick(self):
    self.logOutput.setPlainText('')
    tweets = self.parser.getInitialTweets()
    for tweet in tweets: 
      self.logOutput.insertPlainText('Name: ' + tweet.Name + '\n')
      self.logOutput.insertPlainText('Tweet: ' + tweet.Text + '\n\n\n')
  
  def EditButtonClick(self):
    self.logOutput.setReadOnly(False)
    text = ''
    for line in files: 
        text = text + line
    self.logOutput.setPlainText(text)
    self.savebtn.show()

  def AddButtonClicked(self):
    account = 'https://twitter.com/' + self.AccountText
    self.parser.addAccount(account)

  def closeEvent(self, event):
    reply = QMessageBox.question(self, 'Message',
      "Are you sure to quit?", QMessageBox.Yes |
      QMessageBox.No, QMessageBox.No)

    if reply == QMessageBox.Yes:
      accounts = self.parser.getAccounts()
      filew = open(filename, encoding="UTF-8", mode="w")
      for acc in accounts: 
        filew.write(acc)
      event.accept()
    else:
      event.ignore()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def onChanged(self, text):
    self.AccountText = text

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = TweetoTa()
    w.resize(650, 450)
    w.center()
    w.setWindowTitle('TweetoTa')
    w.show()

    sys.exit(app.exec_())
    