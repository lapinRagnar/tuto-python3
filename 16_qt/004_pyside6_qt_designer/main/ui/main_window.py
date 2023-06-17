# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
# import Icons_rc
# import Icons_rc
import main.ui.rc_icons

class Ui_mw_main(object):
    def setupUi(self, mw_main):
        if not mw_main.objectName():
            mw_main.setObjectName(u"mw_main")
        mw_main.resize(800, 600)
        font = QFont()
        font.setPointSize(12)
        mw_main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        mw_main.setWindowIcon(icon)
        self.action_quit = QAction(mw_main)
        self.action_quit.setObjectName(u"action_quit")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_quit.setIcon(icon1)
        self.action_quit.setFont(font)
        self.action_ajouter_person = QAction(mw_main)
        self.action_ajouter_person.setObjectName(u"action_ajouter_person")
        self.action_ajouter_person.setFont(font)
        self.centralwidget = QWidget(mw_main)
        self.centralwidget.setObjectName(u"centralwidget")
        mw_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 34))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuUser = QMenu(self.menubar)
        self.menuUser.setObjectName(u"menuUser")
        mw_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_main)
        self.statusbar.setObjectName(u"statusbar")
        mw_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())
        self.menuFile.addAction(self.action_quit)
        self.menuUser.addAction(self.action_ajouter_person)

        self.retranslateUi(mw_main)

        QMetaObject.connectSlotsByName(mw_main)
    # setupUi

    def retranslateUi(self, mw_main):
        mw_main.setWindowTitle(QCoreApplication.translate("mw_main", u"Mon super application", None))
        self.action_quit.setText(QCoreApplication.translate("mw_main", u"Quit", None))
        self.action_ajouter_person.setText(QCoreApplication.translate("mw_main", u"Ajouter User", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_main", u"File", None))
        self.menuUser.setTitle(QCoreApplication.translate("mw_main", u"User", None))
    # retranslateUi

