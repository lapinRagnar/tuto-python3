# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mon_login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
# import Icons_rc
import UI.rc_icons

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(557, 323)
        font = QFont()
        font.setPointSize(12)
        w_LoginForm.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        w_LoginForm.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_cancel = QPushButton(w_LoginForm)
        self.pb_cancel.setObjectName(u"pb_cancel")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_cancel.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_cancel, 2, 1, 1, 1)

        self.lb_message = QLabel(w_LoginForm)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 1)

        self.pb_ok = QPushButton(w_LoginForm)
        self.pb_ok.setObjectName(u"pb_ok")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_ok.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_ok, 2, 0, 1, 1)

        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_UserID = QLineEdit(self.groupBox)
        self.le_UserID.setObjectName(u"le_UserID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_UserID)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"Mon super application", None))
        self.pb_cancel.setText(QCoreApplication.translate("w_LoginForm", u"Cancel", None))
        self.lb_message.setText(QCoreApplication.translate("w_LoginForm", u"Message", None))
        self.pb_ok.setText(QCoreApplication.translate("w_LoginForm", u"Ok", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Bienvenue, Se connecter!", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"Password", None))
    # retranslateUi

