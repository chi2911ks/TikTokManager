# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Tiktok\fSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fSettings(object):
    def setupUi(self, fSettings):
        fSettings.setObjectName("fSettings")
        fSettings.resize(533, 600)
        fSettings.setMaximumSize(QtCore.QSize(600, 600))
        fSettings.setStyleSheet("/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"QGroupBox{\n"
"\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(255, 255, 255);}\n"
"QWidget{\n"
"    background-color: rgb(40, 44, 52);\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(255, 121, 198);\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border: none;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"\n"
"}\n"
"QTableWidget {    \n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: rgb(33, 37, 43);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView {\n"
"    qproperty-defaultAlignment: AlignHCenter AlignVCenter;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {    \n"
"    color: rgb(255, 121, 198);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {    \n"
"    color: rgb(255, 170, 255);\n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {    \n"
"    color: rgb(189, 147, 249);\n"
"    background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
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
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(fSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_7 = QtWidgets.QFrame(fSettings)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.delayOpenChrome = QtWidgets.QSpinBox(self.frame_7)
        self.delayOpenChrome.setMaximum(9999)
        self.delayOpenChrome.setProperty("value", 5)
        self.delayOpenChrome.setObjectName("delayOpenChrome")
        self.horizontalLayout_3.addWidget(self.delayOpenChrome)
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.delayOpenChrome_2 = QtWidgets.QSpinBox(self.frame_7)
        self.delayOpenChrome_2.setMaximum(9999)
        self.delayOpenChrome_2.setProperty("value", 10)
        self.delayOpenChrome_2.setObjectName("delayOpenChrome_2")
        self.horizontalLayout_3.addWidget(self.delayOpenChrome_2)
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame_7, 5, 0, 1, 2)
        self.frame_6 = QtWidgets.QFrame(fSettings)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.delayUpload = QtWidgets.QSpinBox(self.frame_6)
        self.delayUpload.setMaximum(9999)
        self.delayUpload.setProperty("value", 5)
        self.delayUpload.setObjectName("delayUpload")
        self.horizontalLayout_2.addWidget(self.delayUpload)
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.delayUpload_2 = QtWidgets.QSpinBox(self.frame_6)
        self.delayUpload_2.setMaximum(9999)
        self.delayUpload_2.setProperty("value", 10)
        self.delayUpload_2.setObjectName("delayUpload_2")
        self.horizontalLayout_2.addWidget(self.delayUpload_2)
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(fSettings)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbAPICaptcha = QtWidgets.QComboBox(self.frame_2)
        self.cbAPICaptcha.setMinimumSize(QtCore.QSize(150, 0))
        self.cbAPICaptcha.setObjectName("cbAPICaptcha")
        self.cbAPICaptcha.addItem("")
        self.cbAPICaptcha.addItem("")
        self.horizontalLayout_6.addWidget(self.cbAPICaptcha)
        self.api_key_captcha = QtWidgets.QLineEdit(self.frame_2)
        self.api_key_captcha.setObjectName("api_key_captcha")
        self.horizontalLayout_6.addWidget(self.api_key_captcha)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(fSettings)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.countVideo = QtWidgets.QSpinBox(self.frame_5)
        self.countVideo.setProperty("value", 1)
        self.countVideo.setObjectName("countVideo")
        self.horizontalLayout.addWidget(self.countVideo)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_5)
        self.cbDeleteVideo = QtWidgets.QCheckBox(self.frame_4)
        self.cbDeleteVideo.setObjectName("cbDeleteVideo")
        self.verticalLayout.addWidget(self.cbDeleteVideo)
        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(fSettings)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 2)
        self.frame_8 = QtWidgets.QFrame(fSettings)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnSettingSeeding = QtWidgets.QPushButton(self.frame_8)
        self.btnSettingSeeding.setMinimumSize(QtCore.QSize(0, 30))
        self.btnSettingSeeding.setObjectName("btnSettingSeeding")
        self.horizontalLayout_5.addWidget(self.btnSettingSeeding)
        self.btnSettingInfo = QtWidgets.QPushButton(self.frame_8)
        self.btnSettingInfo.setMinimumSize(QtCore.QSize(0, 30))
        self.btnSettingInfo.setObjectName("btnSettingInfo")
        self.horizontalLayout_5.addWidget(self.btnSettingInfo)
        self.btnSettingVideo = QtWidgets.QPushButton(self.frame_8)
        self.btnSettingVideo.setMinimumSize(QtCore.QSize(0, 30))
        self.btnSettingVideo.setObjectName("btnSettingVideo")
        self.horizontalLayout_5.addWidget(self.btnSettingVideo)
        self.btnSettingProxy = QtWidgets.QPushButton(self.frame_8)
        self.btnSettingProxy.setMinimumSize(QtCore.QSize(0, 30))
        self.btnSettingProxy.setObjectName("btnSettingProxy")
        self.horizontalLayout_5.addWidget(self.btnSettingProxy)
        self.gridLayout.addWidget(self.frame_8, 9, 0, 1, 1)
        self.frame = QtWidgets.QFrame(fSettings)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.threadCount = QtWidgets.QSpinBox(self.frame)
        self.threadCount.setMinimum(1)
        self.threadCount.setMaximum(99)
        self.threadCount.setProperty("value", 3)
        self.threadCount.setObjectName("threadCount")
        self.horizontalLayout_4.addWidget(self.threadCount)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame, 4, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(fSettings)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.version_main = QtWidgets.QSpinBox(self.frame_3)
        self.version_main.setMaximum(999)
        self.version_main.setProperty("value", 103)
        self.version_main.setObjectName("version_main")
        self.horizontalLayout_7.addWidget(self.version_main)
        self.rbHidenChrome = QtWidgets.QRadioButton(self.frame_3)
        self.rbHidenChrome.setObjectName("rbHidenChrome")
        self.horizontalLayout_7.addWidget(self.rbHidenChrome)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.gridLayout.addWidget(self.frame_3, 7, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(fSettings)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbUpdateInfo = QtWidgets.QRadioButton(self.groupBox)
        self.rbUpdateInfo.setObjectName("rbUpdateInfo")
        self.gridLayout_2.addWidget(self.rbUpdateInfo, 3, 0, 1, 1)
        self.rbLogin = QtWidgets.QRadioButton(self.groupBox)
        self.rbLogin.setChecked(True)
        self.rbLogin.setObjectName("rbLogin")
        self.gridLayout_2.addWidget(self.rbLogin, 0, 0, 1, 1)
        self.rbSeeding = QtWidgets.QRadioButton(self.groupBox)
        self.rbSeeding.setChecked(False)
        self.rbSeeding.setObjectName("rbSeeding")
        self.gridLayout_2.addWidget(self.rbSeeding, 0, 1, 1, 1)
        self.rbUpload = QtWidgets.QRadioButton(self.groupBox)
        self.rbUpload.setObjectName("rbUpload")
        self.gridLayout_2.addWidget(self.rbUpload, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(fSettings)
        QtCore.QMetaObject.connectSlotsByName(fSettings)

    def retranslateUi(self, fSettings):
        _translate = QtCore.QCoreApplication.translate
        fSettings.setWindowTitle(_translate("fSettings", "Cài đặt"))
        self.label_9.setText(_translate("fSettings", "Độ trễ mở chrome giữa các luồng từ:"))
        self.label_10.setText(_translate("fSettings", "đến"))
        self.label_11.setText(_translate("fSettings", "giây"))
        self.label_6.setText(_translate("fSettings", "Độ trễ đăng video từ:"))
        self.label_7.setText(_translate("fSettings", "đến"))
        self.label_8.setText(_translate("fSettings", "giây"))
        self.cbAPICaptcha.setItemText(0, _translate("fSettings", "Omocaptcha"))
        self.cbAPICaptcha.setItemText(1, _translate("fSettings", "Captcha.guru"))
        self.label_4.setText(_translate("fSettings", "Số video đăng của một tiktok:"))
        self.label_5.setText(_translate("fSettings", "video"))
        self.cbDeleteVideo.setText(_translate("fSettings", "Xoá video sau khi đăng"))
        self.btnSettingSeeding.setText(_translate("fSettings", "Cài đặt tương tác"))
        self.btnSettingInfo.setText(_translate("fSettings", "Cài đặt thông tin nick"))
        self.btnSettingVideo.setText(_translate("fSettings", "Cài đặt video"))
        self.btnSettingProxy.setText(_translate("fSettings", "Cài đặt proxy"))
        self.label.setText(_translate("fSettings", "Số luồng chạy trong một lần:"))
        self.label_3.setText(_translate("fSettings", "Verion chrome:"))
        self.rbHidenChrome.setText(_translate("fSettings", "Ẩn chrome"))
        self.groupBox.setTitle(_translate("fSettings", "Action"))
        self.rbUpdateInfo.setText(_translate("fSettings", "Cập nhật thông tin nick"))
        self.rbLogin.setText(_translate("fSettings", "Đăng nhập"))
        self.rbSeeding.setText(_translate("fSettings", "Tương tác"))
        self.rbUpload.setText(_translate("fSettings", "Tải video lên"))