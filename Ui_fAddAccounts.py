# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Tiktok\fAddAccounts.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fAddAccounts(object):
    def setupUi(self, fAddAccounts):
        fAddAccounts.setObjectName("fAddAccounts")
        fAddAccounts.resize(1070, 452)
        fAddAccounts.setStyleSheet("QWidget{\n"
"    background-color: rgb(40, 44, 52);\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 121, 198);    \n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QPlainTextEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
" QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
" QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(fAddAccounts)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextData = QtWidgets.QPlainTextEdit(fAddAccounts)
        self.plainTextData.setObjectName("plainTextData")
        self.verticalLayout.addWidget(self.plainTextData)
        self.frame_3 = QtWidgets.QFrame(fAddAccounts)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frameSearch = QtWidgets.QFrame(self.frame_3)
        self.frameSearch.setMinimumSize(QtCore.QSize(200, 0))
        self.frameSearch.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frameSearch.setStyleSheet("")
        self.frameSearch.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSearch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSearch.setObjectName("frameSearch")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameSearch)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frameSearch)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbGroup = QtWidgets.QComboBox(self.frameSearch)
        self.cbGroup.setMinimumSize(QtCore.QSize(150, 0))
        self.cbGroup.setObjectName("cbGroup")
        self.horizontalLayout.addWidget(self.cbGroup)
        self.horizontalLayout_3.addWidget(self.frameSearch)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frameButton = QtWidgets.QFrame(self.frame_3)
        self.frameButton.setStyleSheet("")
        self.frameButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButton.setObjectName("frameButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddAccounts = QtWidgets.QPushButton(self.frameButton)
        self.btnAddAccounts.setMinimumSize(QtCore.QSize(120, 30))
        self.btnAddAccounts.setObjectName("btnAddAccounts")
        self.horizontalLayout_2.addWidget(self.btnAddAccounts)
        self.btnClose = QtWidgets.QPushButton(self.frameButton)
        self.btnClose.setMinimumSize(QtCore.QSize(50, 30))
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.horizontalLayout_3.addWidget(self.frameButton)
        self.frameButton.raise_()
        self.frameSearch.raise_()
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(fAddAccounts)
        QtCore.QMetaObject.connectSlotsByName(fAddAccounts)

    def retranslateUi(self, fAddAccounts):
        _translate = QtCore.QCoreApplication.translate
        fAddAccounts.setWindowTitle(_translate("fAddAccounts", "Thêm tài khoản"))
        self.plainTextData.setPlaceholderText(_translate("fAddAccounts", "username|password|mail|passmail|cookie"))
        self.label.setText(_translate("fAddAccounts", "Thư mục:"))
        self.btnAddAccounts.setText(_translate("fAddAccounts", "Thêm tài khoản"))
        self.btnClose.setText(_translate("fAddAccounts", "Thoát"))
