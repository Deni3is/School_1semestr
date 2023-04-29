from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from sad_ui import Ui_MainWindow
class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.lineEdit1.text()
        self.lineEdit2.text()
        self.lineEdit3.text()
        self.lineEdit4.text()
        self.lineEdit5.text()
        self.lineEdit6.text()
        self.output()

    def output(self):
        b = 1
        n = [self.lineEdit1,self.lineEdit2,self.lineEdit3,self.lineEdit4,self.lineEdit5,self.lineEdit6]
        with open('text.txt', 'r') as cod:
            str=cod.read()
            for i in str:
                if b < 7:
                    n[b-1].setText(i)
                    b+=1
                else:
                    break


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
