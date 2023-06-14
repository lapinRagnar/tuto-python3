from  PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QStatusBar, QPushButton, QMainWindow, QToolBar

class MainWindow(QMainWindow):
  def __init__(self, app):
    super().__init__()
    self.app = app
    self.setWindowTitle("Main Window")
    
    # menu bar and menus
    menu_bar = self.menuBar()
    file_menu = menu_bar.addMenu("File")
    quit_action = file_menu.addAction("Quitter")
    quit_action.triggered.connect(self.quit_app)
    
    # edit menu
    edit_menu = menu_bar.addMenu("Edit")
    edit_menu.addAction("Undo")
    edit_menu.addAction("Redo")
    edit_menu.addAction("Cut")
    edit_menu.addAction("Copy")
    edit_menu.addAction("Paste")
    
    # other menus just for fun
    menu_bar.addMenu('Options')
    menu_bar.addMenu('Help')
    
    # working with toolbars
    toolbar = QToolBar("Main")
    toolbar.setIconSize(QSize(32, 32))
    self.addToolBar(toolbar)
    
    # add quit action to toolbar
    toolbar.addAction(quit_action)
    
    # some actions
    action1 = QAction("Action 1", self)
    action1.setStatusTip('mon super status message')
    action1.triggered.connect(self.toolbar_button_click)
    toolbar.addAction(action1)
    
    # action 2
    action2 = QAction(QIcon("mon_icon.png"), "Action 2", self)
    action2.setStatusTip('mon super action message 2')
    action2.triggered.connect(self.toolbar_button_click)
    action2.setCheckable(True)
    toolbar.addAction(action2) 
    
    # add separator to toolbar
    toolbar.addSeparator()
    toolbar.addWidget(QPushButton("Mon super bouton"))
    
    # working with status bar
    self.setStatusBar(QStatusBar(self))
    
    # bouton be
    button1 = QPushButton("Mon super bouton 1")
    button1.clicked.connect(self.button1_clicked)
    self.setCentralWidget(button1)
    
  def button1_clicked(self):
    print("button 1 clicked")
    
  def quit_app(self):
    self.app.quit()
  
  def toolbar_button_click(self):
    print("toolbar button clicked")
    self.statusBar().showMessage("toolbar button clicked")
    
