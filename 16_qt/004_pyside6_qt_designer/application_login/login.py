import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.mon_login import Ui_w_LoginForm

class LoginForm(qtw.QWidget, Ui_w_LoginForm):
  
  login_success = qtc.Signal()
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    
    self.pb_cancel.clicked.connect(self.close)
    self.pb_ok.clicked.connect(self.process_login)
  
  @qtc.Slot()
  def process_login(self):
    print('login marche')
    print('mot de passe', self.le_Password)
    if self.le_UserID.text() == 'lapinragnar' and self.le_Password.text() == 'password':
      self.login_success.emit()
      self.close()
    else:
      self.lb_message.setText('Mauvais identifiant ou mot de passe')

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)
  window = LoginForm()
  window.show()
  
  app.exec()