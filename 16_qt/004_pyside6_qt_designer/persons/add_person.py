import sys
from typing import Optional

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import PySide6.QtCore
import PySide6.QtWidgets

from persons.ui.add_person_window import Ui_d_person

class AddPerson(qtw.QDialog, Ui_d_person):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    
    self.gb_person.setTitle('Ajouter un utilisateur')
    self.lb_message.clear()
    self.le_firstName.setFocus()
    self.pb_close.clicked.connect(self.reject)
    self.pb_submit.clicked.connect(self.process_entry)
  
  @qtc.Slot()
  def process_entry(self):
    self.lb_message.setText('un nouveau utilisateur a été ajouté')
    self.le_firstName.clear()
    self.le_lastName.clear()
    self.le_firstName.setFocus()

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)
  window = AddPerson()
  window.show()
  
  app.exec()