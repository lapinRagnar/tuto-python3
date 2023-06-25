from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit

class Widget(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("QLabel et QLineEdit")
    self.resize(300, 300)

    # set a signals we can connect to
    label = QLabel("Fullname", self)
    self.line_edit = QLineEdit()
    
    # self.line_edit.textChanged.connect(self.text_changed)
    # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
    # self.line_edit.editingFinished.connect(self.editing_finished)
    # self.line_edit.returnPressed.connect(self.return_pressed)
    # self.line_edit.selectionChanged.connect(self.selection_changed)
    self.line_edit.textEdited.connect(self.text_edited)
    
    button = QPushButton("OK", self)
    button.clicked.connect(self.button_clicked) 
    self.text_holder_label = QLabel("I am here")
    
    h_layout = QHBoxLayout()
    h_layout.addWidget(label)
    h_layout.addWidget(self.line_edit)
    
    v_layout = QVBoxLayout()
    v_layout.addLayout(h_layout)
    v_layout.addWidget(button)
    v_layout.addWidget(self.text_holder_label)
    
    self.setLayout(v_layout)

  # slots
  def button_clicked(self):
    print('ca marche !')
    self.text_holder_label.setText(self.line_edit.text())
  
  def text_changed(self):
    self.text_holder_label.setText(self.line_edit.text())

  def cursor_position_changed(self, old, new):
    print(f"ancien position : {old} --> nouveau position : {new}")
    # self.text_holder_label.setText(self.line_edit.cursorPosition())
  
  def editing_finished(self):
    print("la ligne a été modifiée !")
  
  def return_pressed(self):
    print("le bouton a été appuyé !")
    
  def selection_changed(self):
    print("la sélection a été modifiée !", self.line_edit.selectedText())
  
  def text_edited(self, new_text):
    print("le texte a été modifié !", new_text)
  
  