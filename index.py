import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from main import Ui_MainWindow


class MainApp (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
         super (MainApp, self).__init__(parent)
         self.setupUi(self)
         self.pushButton_2.clicked.connect(self.prin)

    def prin(self):
        self.lineEdit_2.setText("hello haasasa")










def main():

   app = QApplication(sys.argv)
   myWin = MainApp()
   myWin.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
    main()

