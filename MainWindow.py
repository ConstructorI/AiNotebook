# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 710)
        MainWindow.setBaseSize(QSize(780, 710))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	font: 10pt \"Bahnschrift\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(15, 15, 15);\n"
"}\n"
"\n"
"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 10);\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(255, 192, 133);\n"
"	border-radius: 3px;\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(161, 204, 210);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgba(255, 192, 133, 70);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(255, 192, 133);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	color: rgb(15, 15, 15);\n"
"	background-color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	color: rgb(15, 15, 15);\n"
"	background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	font: 12pt "
                        "\"Bahnschrift\";\n"
"	color: rgb(60, 66, 92);\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color:rgba(255, 255, 255, 10);\n"
"	color:rgb(255, 255, 255);\n"
"	border-style:solid;\n"
"	border-color:rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"	background-color:rgba(255, 255, 255, 20);\n"
"	color:rgb(255, 255, 255);\n"
"	border:1px;\n"
"	border-style:solid;\n"
"	border-color:rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	font: 10pt \"Bahnschrift\";\n"
"    background-color:rgba(255, 255, 255, 10);color:rgb(255, 255, 255);border-style:solid;border-color:rgb(255, 255, 255);border-radius: 3px;padding: 5px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"	font: 10pt \"Bahnschrift\";\n"
"    background-color:rgba(255, 255, 255, 30);color:rgb(255, 255, 255);border:1px;border-style:solid;border-color:rgb(255, 255, 255);border-radius: 3px;p"
                        "adding: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_new = QPushButton(self.centralwidget)
        self.pushButton_new.setObjectName(u"pushButton_new")
        self.pushButton_new.setMinimumSize(QSize(0, 24))
        self.pushButton_new.setStyleSheet(u"image: url(:/icons/icons/new.ico);")

        self.horizontalLayout_5.addWidget(self.pushButton_new)

        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setMinimumSize(QSize(0, 24))
        self.pushButton_open.setStyleSheet(u"image: url(:/icons/icons/open.ico);")

        self.horizontalLayout_5.addWidget(self.pushButton_open)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 24))
        self.pushButton_save.setStyleSheet(u"image: url(:/icons/icons/save.ico);")

        self.horizontalLayout_5.addWidget(self.pushButton_save)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_alignleft = QPushButton(self.centralwidget)
        self.pushButton_alignleft.setObjectName(u"pushButton_alignleft")
        self.pushButton_alignleft.setMinimumSize(QSize(20, 20))
        self.pushButton_alignleft.setMaximumSize(QSize(20, 20))
        self.pushButton_alignleft.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_alignleft.setStyleSheet(u"image: url(:/icons/icons/left.ico);")

        self.horizontalLayout_4.addWidget(self.pushButton_alignleft)

        self.pushButton_aligncenter = QPushButton(self.centralwidget)
        self.pushButton_aligncenter.setObjectName(u"pushButton_aligncenter")
        self.pushButton_aligncenter.setMinimumSize(QSize(20, 20))
        self.pushButton_aligncenter.setMaximumSize(QSize(20, 20))
        self.pushButton_aligncenter.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_aligncenter.setStyleSheet(u"image: url(:/icons/icons/center.ico);")

        self.horizontalLayout_4.addWidget(self.pushButton_aligncenter)

        self.pushButton_alignright = QPushButton(self.centralwidget)
        self.pushButton_alignright.setObjectName(u"pushButton_alignright")
        self.pushButton_alignright.setMinimumSize(QSize(20, 20))
        self.pushButton_alignright.setMaximumSize(QSize(20, 20))
        self.pushButton_alignright.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_alignright.setStyleSheet(u"image: url(:/icons/icons/right.ico);")

        self.horizontalLayout_4.addWidget(self.pushButton_alignright)

        self.pushButton_alignjust = QPushButton(self.centralwidget)
        self.pushButton_alignjust.setObjectName(u"pushButton_alignjust")
        self.pushButton_alignjust.setMinimumSize(QSize(20, 20))
        self.pushButton_alignjust.setMaximumSize(QSize(20, 20))
        self.pushButton_alignjust.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_alignjust.setStyleSheet(u"image: url(:/icons/icons/justified.ico);")

        self.horizontalLayout_4.addWidget(self.pushButton_alignjust)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_bold = QPushButton(self.centralwidget)
        self.pushButton_bold.setObjectName(u"pushButton_bold")
        self.pushButton_bold.setMinimumSize(QSize(20, 20))
        self.pushButton_bold.setMaximumSize(QSize(20, 20))
        self.pushButton_bold.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_bold.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.pushButton_bold)

        self.pushButton_italic = QPushButton(self.centralwidget)
        self.pushButton_italic.setObjectName(u"pushButton_italic")
        self.pushButton_italic.setMinimumSize(QSize(20, 20))
        self.pushButton_italic.setMaximumSize(QSize(20, 20))
        self.pushButton_italic.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_italic.setStyleSheet(u"font: italic 10pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.pushButton_italic)

        self.pushButton_underline = QPushButton(self.centralwidget)
        self.pushButton_underline.setObjectName(u"pushButton_underline")
        self.pushButton_underline.setMinimumSize(QSize(20, 20))
        self.pushButton_underline.setMaximumSize(QSize(20, 20))
        self.pushButton_underline.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_underline.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"text-decoration: underline;")

        self.horizontalLayout_3.addWidget(self.pushButton_underline)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_font = QComboBox(self.centralwidget)
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.setObjectName(u"comboBox_font")
        self.comboBox_font.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.comboBox_font)

        self.comboBox_size = QComboBox(self.centralwidget)
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.setObjectName(u"comboBox_size")
        self.comboBox_size.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.comboBox_size)

        self.pushButton_textcolor = QPushButton(self.centralwidget)
        self.pushButton_textcolor.setObjectName(u"pushButton_textcolor")
        self.pushButton_textcolor.setMinimumSize(QSize(20, 20))
        self.pushButton_textcolor.setMaximumSize(QSize(20, 20))
        self.pushButton_textcolor.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_textcolor)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_AI = QPushButton(self.centralwidget)
        self.pushButton_AI.setObjectName(u"pushButton_AI")
        self.pushButton_AI.setMinimumSize(QSize(176, 20))
        self.pushButton_AI.setMaximumSize(QSize(176, 20))

        self.horizontalLayout_7.addWidget(self.pushButton_AI)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(480, 16777215))
        self.textEdit.setBaseSize(QSize(0, 0))
        self.textEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(300, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit_AI = QTextEdit(self.centralwidget)
        self.textEdit_AI.setObjectName(u"textEdit_AI")
        self.textEdit_AI.setMinimumSize(QSize(0, 0))
        self.textEdit_AI.setMaximumSize(QSize(300, 16777215))
        self.textEdit_AI.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout.addWidget(self.textEdit_AI)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(300, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(300, 100))
        self.plainTextEdit.setStyleSheet(u"font: 12pt \"Arial\";")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.pushButton_gen = QPushButton(self.centralwidget)
        self.pushButton_gen.setObjectName(u"pushButton_gen")
        self.pushButton_gen.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_gen)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(300, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AiNotebook", None))
        self.pushButton_new.setText("")
        self.pushButton_open.setText("")
        self.pushButton_save.setText("")
        self.pushButton_alignleft.setText("")
        self.pushButton_aligncenter.setText("")
        self.pushButton_alignright.setText("")
        self.pushButton_alignjust.setText("")
        self.pushButton_bold.setText(QCoreApplication.translate("MainWindow", u" \u0416 ", None))
        self.pushButton_italic.setText(QCoreApplication.translate("MainWindow", u" \u041a ", None))
        self.pushButton_underline.setText(QCoreApplication.translate("MainWindow", u"\u041f", None))
        self.comboBox_font.setItemText(0, QCoreApplication.translate("MainWindow", u"Arial", None))
        self.comboBox_font.setItemText(1, QCoreApplication.translate("MainWindow", u"Arial Unicode MS", None))
        self.comboBox_font.setItemText(2, QCoreApplication.translate("MainWindow", u"Artifakt Element", None))
        self.comboBox_font.setItemText(3, QCoreApplication.translate("MainWindow", u"Bahnschrift", None))
        self.comboBox_font.setItemText(4, QCoreApplication.translate("MainWindow", u"Book Antiqua", None))
        self.comboBox_font.setItemText(5, QCoreApplication.translate("MainWindow", u"Bookman Old Style", None))
        self.comboBox_font.setItemText(6, QCoreApplication.translate("MainWindow", u"Calibri", None))
        self.comboBox_font.setItemText(7, QCoreApplication.translate("MainWindow", u"Cambria", None))
        self.comboBox_font.setItemText(8, QCoreApplication.translate("MainWindow", u"Cambria Math", None))
        self.comboBox_font.setItemText(9, QCoreApplication.translate("MainWindow", u"Candara", None))
        self.comboBox_font.setItemText(10, QCoreApplication.translate("MainWindow", u"Cascadia Code", None))
        self.comboBox_font.setItemText(11, QCoreApplication.translate("MainWindow", u"Century", None))
        self.comboBox_font.setItemText(12, QCoreApplication.translate("MainWindow", u"Century Gothic", None))
        self.comboBox_font.setItemText(13, QCoreApplication.translate("MainWindow", u"Century Schoolbook", None))
        self.comboBox_font.setItemText(14, QCoreApplication.translate("MainWindow", u"Comic Sans MS", None))
        self.comboBox_font.setItemText(15, QCoreApplication.translate("MainWindow", u"Complex", None))
        self.comboBox_font.setItemText(16, QCoreApplication.translate("MainWindow", u"Consolas", None))
        self.comboBox_font.setItemText(17, QCoreApplication.translate("MainWindow", u"Constantia", None))
        self.comboBox_font.setItemText(18, QCoreApplication.translate("MainWindow", u"Corbel", None))
        self.comboBox_font.setItemText(19, QCoreApplication.translate("MainWindow", u"Courier", None))
        self.comboBox_font.setItemText(20, QCoreApplication.translate("MainWindow", u"Courier New", None))
        self.comboBox_font.setItemText(21, QCoreApplication.translate("MainWindow", u"Fixedsys", None))
        self.comboBox_font.setItemText(22, QCoreApplication.translate("MainWindow", u"Franklin Gothic", None))
        self.comboBox_font.setItemText(23, QCoreApplication.translate("MainWindow", u"Franklin Gothic Book", None))
        self.comboBox_font.setItemText(24, QCoreApplication.translate("MainWindow", u"Gabriola", None))
        self.comboBox_font.setItemText(25, QCoreApplication.translate("MainWindow", u"Garamond", None))
        self.comboBox_font.setItemText(26, QCoreApplication.translate("MainWindow", u"GENISO", None))
        self.comboBox_font.setItemText(27, QCoreApplication.translate("MainWindow", u"Georgia", None))
        self.comboBox_font.setItemText(28, QCoreApplication.translate("MainWindow", u"GOST Common", None))
        self.comboBox_font.setItemText(29, QCoreApplication.translate("MainWindow", u"GothicE", None))
        self.comboBox_font.setItemText(30, QCoreApplication.translate("MainWindow", u"GothicG", None))
        self.comboBox_font.setItemText(31, QCoreApplication.translate("MainWindow", u"GothicI", None))
        self.comboBox_font.setItemText(32, QCoreApplication.translate("MainWindow", u"GreekC", None))
        self.comboBox_font.setItemText(33, QCoreApplication.translate("MainWindow", u"GreekS", None))
        self.comboBox_font.setItemText(34, QCoreApplication.translate("MainWindow", u"Haettenschweiler", None))
        self.comboBox_font.setItemText(35, QCoreApplication.translate("MainWindow", u"Impact", None))
        self.comboBox_font.setItemText(36, QCoreApplication.translate("MainWindow", u"ISOCP", None))
        self.comboBox_font.setItemText(37, QCoreApplication.translate("MainWindow", u"ISOCP2", None))
        self.comboBox_font.setItemText(38, QCoreApplication.translate("MainWindow", u"ISOCP3", None))
        self.comboBox_font.setItemText(39, QCoreApplication.translate("MainWindow", u"ISOCPEUR", None))
        self.comboBox_font.setItemText(40, QCoreApplication.translate("MainWindow", u"ISOCT", None))
        self.comboBox_font.setItemText(41, QCoreApplication.translate("MainWindow", u"ISOCT2", None))
        self.comboBox_font.setItemText(42, QCoreApplication.translate("MainWindow", u"ISOCT3", None))
        self.comboBox_font.setItemText(43, QCoreApplication.translate("MainWindow", u"ISOCTEUR", None))
        self.comboBox_font.setItemText(44, QCoreApplication.translate("MainWindow", u"Italic", None))
        self.comboBox_font.setItemText(45, QCoreApplication.translate("MainWindow", u"ItalicC", None))
        self.comboBox_font.setItemText(46, QCoreApplication.translate("MainWindow", u"ItalicT", None))
        self.comboBox_font.setItemText(47, QCoreApplication.translate("MainWindow", u"Lucida Console", None))
        self.comboBox_font.setItemText(48, QCoreApplication.translate("MainWindow", u"Lucida Sans Unicode", None))
        self.comboBox_font.setItemText(49, QCoreApplication.translate("MainWindow", u"Malgun Gothic", None))
        self.comboBox_font.setItemText(50, QCoreApplication.translate("MainWindow", u"Microsoft JhengHei", None))
        self.comboBox_font.setItemText(51, QCoreApplication.translate("MainWindow", u"Microsoft JhengHei UI", None))
        self.comboBox_font.setItemText(52, QCoreApplication.translate("MainWindow", u"Microsoft Sans Serif", None))
        self.comboBox_font.setItemText(53, QCoreApplication.translate("MainWindow", u"Microsoft YaHei", None))
        self.comboBox_font.setItemText(54, QCoreApplication.translate("MainWindow", u"Mistral", None))
        self.comboBox_font.setItemText(55, QCoreApplication.translate("MainWindow", u"Monotxt", None))
        self.comboBox_font.setItemText(56, QCoreApplication.translate("MainWindow", u"Monotype Corsiva", None))
        self.comboBox_font.setItemText(57, QCoreApplication.translate("MainWindow", u"MS Gothic", None))
        self.comboBox_font.setItemText(58, QCoreApplication.translate("MainWindow", u"MS PGothic", None))
        self.comboBox_font.setItemText(59, QCoreApplication.translate("MainWindow", u"MS Reference Sans Serif", None))
        self.comboBox_font.setItemText(60, QCoreApplication.translate("MainWindow", u"MS Sans Serif", None))
        self.comboBox_font.setItemText(61, QCoreApplication.translate("MainWindow", u"MS Serif", None))
        self.comboBox_font.setItemText(62, QCoreApplication.translate("MainWindow", u"MS UI Gothic", None))
        self.comboBox_font.setItemText(63, QCoreApplication.translate("MainWindow", u"NSimSun", None))
        self.comboBox_font.setItemText(64, QCoreApplication.translate("MainWindow", u"Palatino Linotype", None))
        self.comboBox_font.setItemText(65, QCoreApplication.translate("MainWindow", u"Proxy 1", None))
        self.comboBox_font.setItemText(66, QCoreApplication.translate("MainWindow", u"Proxy 2", None))
        self.comboBox_font.setItemText(67, QCoreApplication.translate("MainWindow", u"Proxy 3", None))
        self.comboBox_font.setItemText(68, QCoreApplication.translate("MainWindow", u"Proxy 4", None))
        self.comboBox_font.setItemText(69, QCoreApplication.translate("MainWindow", u"Proxy 5", None))
        self.comboBox_font.setItemText(70, QCoreApplication.translate("MainWindow", u"Proxy 6", None))
        self.comboBox_font.setItemText(71, QCoreApplication.translate("MainWindow", u"Proxy 7", None))
        self.comboBox_font.setItemText(72, QCoreApplication.translate("MainWindow", u"Proxy 8", None))
        self.comboBox_font.setItemText(73, QCoreApplication.translate("MainWindow", u"Proxy 9", None))
        self.comboBox_font.setItemText(74, QCoreApplication.translate("MainWindow", u"Revit_HEB_DWG", None))
        self.comboBox_font.setItemText(75, QCoreApplication.translate("MainWindow", u"Revit_HEB_Key", None))
        self.comboBox_font.setItemText(76, QCoreApplication.translate("MainWindow", u"RomanC", None))
        self.comboBox_font.setItemText(77, QCoreApplication.translate("MainWindow", u"RomanD", None))
        self.comboBox_font.setItemText(78, QCoreApplication.translate("MainWindow", u"RomanS", None))
        self.comboBox_font.setItemText(79, QCoreApplication.translate("MainWindow", u"RomanT", None))
        self.comboBox_font.setItemText(80, QCoreApplication.translate("MainWindow", u"ScriptC", None))
        self.comboBox_font.setItemText(81, QCoreApplication.translate("MainWindow", u"ScriptS", None))
        self.comboBox_font.setItemText(82, QCoreApplication.translate("MainWindow", u"Segoe Print", None))
        self.comboBox_font.setItemText(83, QCoreApplication.translate("MainWindow", u"Segoe Sprint", None))
        self.comboBox_font.setItemText(84, QCoreApplication.translate("MainWindow", u"Segoe UI", None))
        self.comboBox_font.setItemText(85, QCoreApplication.translate("MainWindow", u"Simplex", None))
        self.comboBox_font.setItemText(86, QCoreApplication.translate("MainWindow", u"SimSun", None))
        self.comboBox_font.setItemText(87, QCoreApplication.translate("MainWindow", u"Sitka", None))
        self.comboBox_font.setItemText(88, QCoreApplication.translate("MainWindow", u"Small Fonts", None))
        self.comboBox_font.setItemText(89, QCoreApplication.translate("MainWindow", u"Syastro", None))
        self.comboBox_font.setItemText(90, QCoreApplication.translate("MainWindow", u"Sylfaen", None))
        self.comboBox_font.setItemText(91, QCoreApplication.translate("MainWindow", u"Symap", None))
        self.comboBox_font.setItemText(92, QCoreApplication.translate("MainWindow", u"Symath", None))
        self.comboBox_font.setItemText(93, QCoreApplication.translate("MainWindow", u"Symeteo", None))
        self.comboBox_font.setItemText(94, QCoreApplication.translate("MainWindow", u"Symusic", None))
        self.comboBox_font.setItemText(95, QCoreApplication.translate("MainWindow", u"System", None))
        self.comboBox_font.setItemText(96, QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.comboBox_font.setItemText(97, QCoreApplication.translate("MainWindow", u"Times New Roman", None))
        self.comboBox_font.setItemText(98, QCoreApplication.translate("MainWindow", u"Trebuchet MS", None))
        self.comboBox_font.setItemText(99, QCoreApplication.translate("MainWindow", u"Txt", None))
        self.comboBox_font.setItemText(100, QCoreApplication.translate("MainWindow", u"Vendana", None))
        self.comboBox_font.setItemText(101, QCoreApplication.translate("MainWindow", u"Yu Gothic", None))
        self.comboBox_font.setItemText(102, QCoreApplication.translate("MainWindow", u"Yu Gothic UI", None))

        self.comboBox_size.setItemText(0, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_size.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_size.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_size.setItemText(3, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_size.setItemText(4, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_size.setItemText(5, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_size.setItemText(6, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_size.setItemText(7, QCoreApplication.translate("MainWindow", u"20", None))

        self.pushButton_textcolor.setText("")
        self.pushButton_AI.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0432 \u0437\u0430\u043f\u0440\u043e\u0441", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441 \u0434\u043b\u044f \u043d\u0435\u0439\u0440\u043e\u0441\u0435\u0442\u0438:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c?", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_gen.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f, \u043f\u043e\u0434\u043e\u0436\u0434\u0438\u0442\u0435", None))
    # retranslateUi

