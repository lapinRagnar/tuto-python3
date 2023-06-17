import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from ui.main_window import Ui_mw_main
from ..persons.add_person import AddPerson

class MainWindow(qtw.QMainWindow, Ui_mw_main):
  def __init__(self):
    super().__init__()

    self.setupUi(self)
    
    self.action_quit.triggered.connect(self.close)
    self.action_ajouter_person.triggered.connect(self.open_add_person)
  
  @qtc.Slot()
  def open_add_person(self):
    self.form = AddPerson()
    self.form.exec()

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)
  window = MainWindow()
  window.show()
  
  app.exec()