import sys, os
sys.path.append(os.path.join(sys.path[0], './interface/'))
import Interface
from PyQt5.QtWidgets import ( QApplication )  

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Interface.TweetoTa()
    w.resize(650, 450)
    w.center()
    w.setWindowTitle('TweetoTa')
    w.show()

    sys.exit(app.exec_()) 