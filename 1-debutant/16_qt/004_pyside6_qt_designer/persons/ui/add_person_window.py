# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
# import icons.rc_icons

class Ui_d_person(object):
    def setupUi(self, d_person):
        if not d_person.objectName():
            d_person.setObjectName(u"d_person")
        d_person.setWindowModality(Qt.ApplicationModal)
        d_person.resize(400, 300)
        font = QFont()
        font.setPointSize(12)
        d_person.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        d_person.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_person)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_submit = QPushButton(d_person)
        self.pb_submit.setObjectName(u"pb_submit")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_submit.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_submit, 2, 1, 1, 1)

        self.pb_close = QPushButton(d_person)
        self.pb_close.setObjectName(u"pb_close")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_close.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_close, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.gb_person = QGroupBox(d_person)
        self.gb_person.setObjectName(u"gb_person")
        self.gb_person.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.gb_person)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_person)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_firstName = QLineEdit(self.gb_person)
        self.le_firstName.setObjectName(u"le_firstName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_firstName)

        self.label_2 = QLabel(self.gb_person)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_lastName = QLineEdit(self.gb_person)
        self.le_lastName.setObjectName(u"le_lastName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_lastName)


        self.gridLayout.addWidget(self.gb_person, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.lb_message = QLabel(d_person)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 3)


        self.retranslateUi(d_person)

        QMetaObject.connectSlotsByName(d_person)
    # setupUi

    def retranslateUi(self, d_person):
        d_person.setWindowTitle(QCoreApplication.translate("d_person", u"Mon super application", None))
        self.pb_submit.setText(QCoreApplication.translate("d_person", u"Submit", None))
        self.pb_close.setText(QCoreApplication.translate("d_person", u"Close", None))
        self.gb_person.setTitle(QCoreApplication.translate("d_person", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("d_person", u"First Name :", None))
        self.label_2.setText(QCoreApplication.translate("d_person", u"Last Name :", None))
        self.lb_message.setText(QCoreApplication.translate("d_person", u"Message", None))
    # retranslateUi

