from PySide6.QtWidgets import QMessageBox, QVBoxLayout, QPushButton, QWidget

class Widget(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Mon super QMessageBox")
    
    button_hard = QPushButton("Hard")
    button_hard.clicked.connect(self.button_hard_clicked)

    button_critical = QPushButton("Critical")
    button_critical.clicked.connect(self.button_critical_clicked)

    button_info = QPushButton("Info")
    button_info.clicked.connect(self.button_info_clicked)
    
    button_warning = QPushButton("Warning")
    button_warning.clicked.connect(self.button_warning_clicked)

    button_question = QPushButton("Question")
    button_question.clicked.connect(self.button_question_clicked)

    button_about = QPushButton("About")
    button_about.clicked.connect(self.button_about_clicked)

    # layout
    layout = QVBoxLayout()
    layout.addWidget(button_hard)
    layout.addWidget(button_critical)
    layout.addWidget(button_info)
    layout.addWidget(button_warning)
    layout.addWidget(button_question)
    layout.addWidget(button_about)
    
    self.setLayout(layout)
  
  def button_hard_clicked(self):
    print("Hard clicked")
    message = QMessageBox()
    message.setMinimumSize(700, 200)
    message.setWindowTitle("Hard")
    message.setText('ceci est mon message text')
    message.setInformativeText('ceci est mon message informative')
    message.setIcon(QMessageBox.Critical)
    message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    message.setDefaultButton(QMessageBox.Ok)
    ret = message.exec()
    
    if ret == QMessageBox.Ok:
      print("Ok clicked")
    elif ret == QMessageBox.Cancel:
      print("Cancel clicked")
    
  
  
  def button_critical_clicked(self):
    print("Critical clicked")
    ret = QMessageBox.critical(
      self, 
      "Critical", "Are you sure?", 
      QMessageBox.Ok | QMessageBox.Cancel
    )
    if ret == QMessageBox.Ok:
      print("Ok clicked")
    elif ret == QMessageBox.Cancel:
      print("Cancel clicked")
  
  def button_info_clicked(self):
    print("Info clicked")
    ret = QMessageBox.information(
      self, 
      "Info", "Woah!!", 
      QMessageBox.Ok
    )
    
    if ret == QMessageBox.Ok:
      print("Ok clicked")
    elif ret == QMessageBox.Cancel:
      print("Cancel clicked")
  
  def button_warning_clicked(self):
    print("Warning clicked")
    ret = QMessageBox.warning(
      self, 
      "Warning", "Are you sure?",
      QMessageBox.Ok | QMessageBox.Cancel
    )
    if ret == QMessageBox.Ok:
      print("Ok clicked")
    elif ret == QMessageBox.Cancel:
      print("Cancel clicked")
  
  def button_question_clicked(self):
    print("Question clicked")
    ret = QMessageBox.question(
      self, 
      "Question", "Are you sure? (Yes/No) ",
      QMessageBox.Ok | QMessageBox.Cancel
    )
    if ret == QMessageBox.Ok:
      print("Ok clicked")
    elif ret == QMessageBox.Cancel:
      print("Cancel clicked")   
    
  
  def button_about_clicked(self):
    print("About clicked")
    ret = QMessageBox.about(
      self, 
      "About", 
      "This is the About message"
    )
    if ret == QMessageBox.Ok:
      print("Ok clicked")
   