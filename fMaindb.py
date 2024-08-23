import datetime
import gc
import json
import os
import random
import shutil
import sqlite3
import subprocess
import threading
from time import sleep
import typing
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, Qt

from GUI.fAddAccounts_ui import Ui_fAddAccounts
from GUI.fProxy_ui import Ui_fProxy
from GUI.fSeeding_ui import Ui_fSeeding
from GUI.fSettingUpload_ui import Ui_fUpload
from GUI.fSettings_ui import Ui_fSettings
from GUI.fTiktok_ui import Ui_MainWindow
from GUI.fUpdate_ui import Ui_fUpdateInfo
from utils.databasehandle import DataBaseHandleTikTok
from utils.generatorName import GeneratorName
from utils.gologin import Gologin
from mainTikTok import TikTok
from utils.api_captcha.omocaptcha import Omocaptcha
from config import Config
from utils.postionChrome import setPositionChrome
from proxy import Proxy
from typing import Union, Dict
from datetime import datetime
import traceback
from seedingTiktok import SeedingTiktok

# import shutil
import requests
import logging
import sys
from stylesheet import StyleSheet

from updateInfo import UpdateInfo


# Thiết lập hàm ghi lỗi tự động
def log_unhandled_exception(exc_type, exc_value, exc_traceback):
    error_message = f"Unhandled exception: {str(exc_type)} - {str(exc_value)}"
    logging.error(error_message, exc_info=True)

    # Ghi traceback vào tệp tin log
    tb_text = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    logging.error(tb_text)


# Cài đặt hàm ghi lỗi tự động cho sys.excepthook
sys.excepthook = log_unhandled_exception

# Cấu hình logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)


class TiktokManager(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.config = Config()
        # self.createDatabase()
        DataBaseHandleTikTok.createDatabase()
        self.loadForm()
        self.setWidthColumnTableWidget()
        self.setStatusbar()
        self.oldEvent = self.tableWidget.keyPressEvent
        self.tableWidget.keyPressEvent = self.keyPressEvent
        # self.btnAddAccounts.clicked.connect(self.addAccounts)
        self.tableWidget.contextMenuEvent = self.contextMenuEvent
        self.loadAccounts()
        self.loadSettings()
        self.refreshCombobox()
        # self.tableWidget.itemDoubleClicked.connect(self.editItem)
        # self.tableWidget.itemChanged.connect(self.saveNote)
        self._listThread: Dict[int, MainThread] = {}
        self.textChangedConnect()
        self.nameGroups = []
        self.btnSearch.clicked.connect(self.searchItem)
        self.btnAddGroup.clicked.connect(self.addGroup)
        self.btnEditGroup.clicked.connect(self.editGroup)
        self.btnDeleteGroup.clicked.connect(self.deleteGroup)
        self.cbGroup.currentTextChanged.connect(self.refreshTable)

    def addGroup(self):
        name, chk = QtWidgets.QInputDialog().getText(
            None, "Tạo thư mục", "Tên thư mục:"
        )
        if chk:
            self.cbGroup.addItem(name)
            self.refreshCombobox()
            self.writeSettings()

    def editGroup(self):
        index = self.cbGroup.currentIndex()
        old = self.cbGroup.currentText()
        if index != 0:
            name, chk = QtWidgets.QInputDialog().getText(
                None, "Sửa tên thư mục", "Tên thư mục mới:", text=old
            )
            if chk:
                self.changeType(name)
                self.cbGroup.setItemText(index, name)
                self.refreshCombobox()
                self.writeSettings()

    def deleteGroup(self):
        index = self.cbGroup.currentIndex()
        if index != 0:
            button = self.MsgBox(
                "Bạn cho chắc chắn muốn xoá ?", QtWidgets.QMessageBox.Question
            )
            if button == 16384:  # 16384 là OK
                self.changeType("")
                self.cbGroup.removeItem(index)
                self.refreshCombobox()
                self.writeSettings()

    def searchItem(self):
        index = {
            "username": 1,
            "password": 2,
            "mail": 3,
            "passmail": 4,
            "cookie": 5,
            "note": self.col_note,
            "description": self.col_description,
        }
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.hideRow(r)
        textSearch = self.textSearch.text()
        items = self.tableWidget.findItems(textSearch, Qt.MatchContains)
        for item in items:
            if item.column() == index[self.cbTypeSearch.currentText()]:
                self.tableWidget.showRow(item.row())

    # def editItem(self, item):
    #     listColumn = [1, 2, 3, 4, 5, self.col_note, self.col_description]
    def refreshCombobox(self):
        self.fAddAccounts.cbGroup.clear()
        items = self.get_combo_box_items(self.cbGroup)
        self.fAddAccounts.cbGroup.addItems([""] + items)

    def changeType(self, nameType):
        for row in range(self.tableWidget.rowCount()):
            typeInTable = self.tableWidget.item(row, 7).text().strip()
            if typeInTable == self.cbGroup.currentText():
                username = self.tableWidget.item(row, 1).text().strip()
                DataBaseHandleTikTok.updateRow(username, "type", nameType)
                self.show(row, 7, nameType)

    def refreshTable(self):
        typeText = self.cbGroup.currentText()
        if typeText == "[Tất cả thư mục]":
            typeText = None
        self.removeItemTableWidget()
        self.loadAccounts(typeText)

    def getData(self, row):
        listColumn = [1, 2, 3, 4, 5, self.col_note, self.col_description]
        data = []
        for col in listColumn:
            item = self.tableWidget.item(row, col)
            if item is None:
                value = ""
            else:
                value = item.text()
            data.append(value)
        return data

    # def saveNote(self, item):
    #     listColumn = [1, 2, 3, 4, 5, self.col_note, self.col_description]
    #     if item.column() in listColumn:
    #         row = item.row()
    #         username = self.tableWidget.item(row, 1).text()
    #         values = self.getData(row)
    #         DataBaseHandleTikTok.updateRows(values, username)

    def textChangedConnect(self):

        varfSettings = vars(self.fSetting)
        varfSettings.update(vars(self.fSeeding))
        varfSettings.update(vars(self.fUpload))
        varfSettings.update(vars(self.fProxy))
        varfSettings.update(vars(self.fUpdateInfo))
        for value in varfSettings.values():
            if isinstance(value, QtWidgets.QLineEdit) or isinstance(
                value, QtWidgets.QPlainTextEdit
            ):
                value.textChanged.connect(self.writeSettings)
            elif isinstance(value, QtWidgets.QSpinBox):
                value.valueChanged.connect(self.writeSettings)
            elif (
                isinstance(value, QtWidgets.QRadioButton)
                or isinstance(value, QtWidgets.QCheckBox)
                or isinstance(value, QtWidgets.QGroupBox)
            ):
                value.clicked.connect(self.writeSettings)
        self.fSetting.cbAPICaptcha.currentTextChanged.connect(self.writeSettings)

    def get_combo_box_items(self, combo_box):
        items = []
        for index in range(1, combo_box.count()):
            items.append(combo_box.itemText(index))
        return items

    def writeSettings(self):
        data = {}
        data["cbAPICaptcha"] = self.fSetting.cbAPICaptcha.currentText()
        data["api_key"] = self.fSetting.api_key_captcha.text()
        data["threadCount"] = self.fSetting.threadCount.value()
        data["version_main"] = self.fSetting.version_main.value()
        data["locationVideo"] = self.fUpload.locationVideo.text()
        data["locationFolderVideo"] = self.fUpload.locationFolderVideo.text()
        data["cbDeleteVideo"] = self.fSetting.cbDeleteVideo.isChecked()
        data["rbHidenChrome"] = self.fSetting.rbHidenChrome.isChecked()
        data["rbOnlyVideo"] = self.fUpload.rbOnlyVideo.isChecked()
        data["rbRandomVideo"] = self.fUpload.rbRandomVideo.isChecked()
        data["rbContentLine"] = self.fUpload.rbContentLine.isChecked()
        data["rbOnlyContent"] = self.fUpload.rbOnlyContent.isChecked()
        data["rbNoProxy"] = self.fProxy.rbNoProxy.isChecked()
        data["rbIPNew"] = self.fProxy.rbIPNew.isChecked()
        data["rbIPOld"] = self.fProxy.rbIPOld.isChecked()
        data["rbUpload"] = self.fSetting.rbUpload.isChecked()
        data["rbLogin"] = self.fSetting.rbLogin.isChecked()
        data["rbSeeding"] = self.fSetting.rbSeeding.isChecked()
        data["rbUpdateInfo"] = self.fSetting.rbUpdateInfo.isChecked()
        data["countVideo"] = self.fSetting.countVideo.value()
        data["delayOpen"] = {
            "delay1": self.fSetting.delayOpenChrome.value(),
            "delay2": self.fSetting.delayOpenChrome_2.value(),
        }
        data["delayUpload"] = {
            "delay1": self.fSetting.delayUpload.value(),
            "delay2": self.fSetting.delayUpload_2.value(),
        }
        data["textContent"] = self.fUpload.textContent.toPlainText()
        data["vProxyer"] = {
            "checked": self.fProxy.rbVproxyer.isChecked(),
            "textDomain": self.fProxy.textDomain.text(),
            "textKey": self.fProxy.textKey.toPlainText(),
        }
        data["seeding"] = {
            "follow": {
                "checked": self.fSeeding.groupBoxFollow.isChecked(),
                "textLinkUser": self.fSeeding.textLinkUser.toPlainText(),
                "delay": {
                    "delay1": self.fSeeding.spinBoxDelayFollow.value(),
                    "delay2": self.fSeeding.spinBoxDelayFollow_2.value(),
                },
            },
            "linkVideo": {
                "checked": self.fSeeding.groupBoxLinkVideo.isChecked(),
                "textLinkVideo": self.fSeeding.textLinkVideo.toPlainText(),
                "textComment": self.fSeeding.textComment.toPlainText(),
                "comment": self.fSeeding.cbComment.isChecked(),
                "like": self.fSeeding.cbLike.isChecked(),
                "view": self.fSeeding.cbView.isChecked(),
                "save": self.fSeeding.cbSave.isChecked(),
                "copy": self.fSeeding.cbCopy.isChecked(),
                "timeView": {
                    "timeView1": self.fSeeding.spinBoxTimeView.value(),
                    "timeView2": self.fSeeding.spinBoxTimeView_2.value(),
                },
                "delay": {
                    "delay1": self.fSeeding.spinBoxDelay.value(),
                    "delay2": self.fSeeding.spinBoxDelay_2.value(),
                },
            },
            "stream": {
                "checked": self.fSeeding.groupBoxViewLive.isChecked(),
                "share": self.fSeeding.cbShareLive.isChecked(),
                "comment": self.fSeeding.cbCommentLive.isChecked(),
                "textCommentLive": self.fSeeding.textCommentLive.toPlainText(),
                "textLinkLive": self.fSeeding.textLinkLive.text(),
                "timeView": {
                    "timeView1": self.fSeeding.spinBoxDelayViewLive.value(),
                    "timeView2": self.fSeeding.spinBoxDelayViewLive_2.value(),
                },
            },
            "story": {
                "checked": self.fSeeding.groupBoxStory.isChecked(),
                "like": self.fSeeding.cbLikeStory.isChecked(),
                "save": self.fSeeding.cbSaveVideo.isChecked(),
                "timeView": {
                    "timeView1": self.fSeeding.spinBoxTimeStory.value(),
                    "timeView2": self.fSeeding.spinBoxTimeStory_2.value(),
                },
            },
        }
        data["updateinfo"] = {
            "gbAvatar": {
                "checked": self.fUpdateInfo.gbAvatar.isChecked(),
                "locationAvatar": self.fUpdateInfo.locationAvatar.text(),
            },
            "gbName": {
                "checked": self.fUpdateInfo.gbName.isChecked(),
                "locationName": self.fUpdateInfo.locationName.text(),
                "cbTiktokID": self.fUpdateInfo.cbTiktokID.isChecked(),
            },
            "gbBio": {
                "checked": self.fUpdateInfo.gbBio.isChecked(),
                "locationBio": self.fUpdateInfo.locationBio.text(),
            },
        }
        data["cbGroup"] = self.get_combo_box_items(self.cbGroup)

        self.config.writeDataFileJson("settings.json", data=data)
        self.iterApi_key = iter(self.fProxy.textKey.toPlainText().splitlines())

    def loadSettings(self):
        try:
            if os.path.exists("settings.json"):
                data = self.config.getDataFileJson("settings.json")
                self.fSetting.cbAPICaptcha.setCurrentText(data["cbAPICaptcha"])
                self.fSetting.api_key_captcha.setText(data["api_key"])
                self.fSetting.threadCount.setValue(data["threadCount"])
                self.fSetting.version_main.setValue(data["version_main"])
                self.fSetting.rbHidenChrome.setChecked(data["rbHidenChrome"])
                self.fProxy.textKey.setPlainText(data["vProxyer"]["textKey"])
                self.fProxy.textDomain.setText(data["vProxyer"]["textDomain"])
                self.fProxy.rbVproxyer.setChecked(data["vProxyer"]["checked"])
                self.fProxy.rbNoProxy.setChecked(data["rbNoProxy"])
                self.fProxy.rbIPNew.setChecked(data["rbIPNew"])
                self.fProxy.rbIPOld.setChecked(data["rbIPOld"])
                self.fSetting.delayUpload.setValue(data["delayUpload"]["delay1"])
                self.fSetting.delayUpload_2.setValue(data["delayUpload"]["delay2"])
                self.fSetting.delayOpenChrome.setValue(data["delayOpen"]["delay1"])
                self.fSetting.delayOpenChrome_2.setValue(data["delayOpen"]["delay2"])
                self.fSetting.countVideo.setValue(data["countVideo"])
                self.fSetting.cbDeleteVideo.setChecked(data["cbDeleteVideo"])
                self.fSetting.rbLogin.setChecked(data["rbLogin"])
                self.fSetting.rbUpload.setChecked(data["rbUpload"])
                self.fSetting.rbSeeding.setChecked(data["rbSeeding"])
                self.fUpload.rbOnlyVideo.setChecked(data["rbOnlyVideo"])
                self.fUpload.rbRandomVideo.setChecked(data["rbRandomVideo"])
                self.fUpload.rbContentLine.setChecked(data["rbContentLine"])
                self.fUpload.rbOnlyContent.setChecked(data["rbOnlyContent"])
                self.fUpload.rbContentLine.setChecked(data["rbContentLine"])
                self.fUpload.locationVideo.setText(data["locationVideo"])
                self.fUpload.locationFolderVideo.setText(data["locationFolderVideo"])
                self.fUpload.spinBoxDay.setValue(int(datetime.now().strftime("%d")))
                self.fUpload.spinBoxHours.setValue(int(datetime.now().strftime("%H")))
                # self.fUpload.spinBoxMinutes.setValue(int(datetime.now().strftime("%M")))
                self.fUpload.textContent.setPlainText(data["textContent"])
                follow = data["seeding"]["follow"]
                linkVideo = data["seeding"]["linkVideo"]
                stream = data["seeding"]["stream"]
                story = data["seeding"]["story"]

                self.fSeeding.groupBoxFollow.setChecked(follow["checked"])
                self.fSeeding.textLinkUser.setPlainText(follow["textLinkUser"])
                self.fSeeding.spinBoxDelayFollow.setValue(follow["delay"]["delay1"])
                self.fSeeding.spinBoxDelayFollow_2.setValue(follow["delay"]["delay2"])

                self.fSeeding.groupBoxLinkVideo.setChecked(linkVideo["checked"])
                self.fSeeding.textLinkVideo.setPlainText(linkVideo["textLinkVideo"])
                self.fSeeding.textComment.setPlainText(linkVideo["textComment"])
                self.fSeeding.cbComment.setChecked(linkVideo["comment"])
                self.fSeeding.cbLike.setChecked(linkVideo["like"])
                self.fSeeding.cbCopy.setChecked(linkVideo["copy"])
                self.fSeeding.cbSave.setChecked(linkVideo["save"])
                self.fSeeding.cbView.setChecked(linkVideo["view"])
                self.fSeeding.spinBoxTimeView.setValue(
                    linkVideo["timeView"]["timeView1"]
                )
                self.fSeeding.spinBoxTimeView_2.setValue(
                    linkVideo["timeView"]["timeView2"]
                )
                self.fSeeding.spinBoxDelay.setValue(linkVideo["delay"]["delay1"])
                self.fSeeding.spinBoxDelay_2.setValue(linkVideo["delay"]["delay2"])

                self.fSeeding.groupBoxViewLive.setChecked(stream["checked"])
                self.fSeeding.textLinkLive.setText(stream["textLinkLive"])
                self.fSeeding.textCommentLive.setPlainText(stream["textCommentLive"])
                self.fSeeding.cbShareLive.setChecked(stream["share"])
                self.fSeeding.cbCommentLive.setChecked(stream["comment"])
                self.fSeeding.spinBoxDelayViewLive.setValue(
                    stream["timeView"]["timeView1"]
                )
                self.fSeeding.spinBoxDelayViewLive_2.setValue(
                    stream["timeView"]["timeView2"]
                )

                self.fSeeding.groupBoxStory.setChecked(story["checked"])
                self.fSeeding.cbLikeStory.setChecked(story["like"])
                self.fSeeding.cbSaveVideo.setChecked(story["save"])
                self.fSeeding.spinBoxTimeStory.setValue(story["timeView"]["timeView1"])
                self.fSeeding.spinBoxTimeStory_2.setValue(
                    story["timeView"]["timeView2"]
                )

                gbAvatar = data["updateinfo"]["gbAvatar"]
                gbName = data["updateinfo"]["gbName"]
                gbBio = data["updateinfo"]["gbBio"]

                self.fUpdateInfo.gbAvatar.setChecked(gbAvatar["checked"])
                self.fUpdateInfo.gbName.setChecked(gbName["checked"])
                self.fUpdateInfo.cbTiktokID.setChecked(gbName["cbTiktokID"])
                self.fUpdateInfo.gbBio.setChecked(gbBio["checked"])

                self.fUpdateInfo.locationAvatar.setText(gbAvatar["locationAvatar"])
                self.fUpdateInfo.locationBio.setText(gbBio["locationBio"])
                self.fUpdateInfo.locationName.setText(gbName["locationName"])
                self.cbGroup.addItems(data["cbGroup"])
                # data["cbGroup"] = self.get_combo_box_items(self.cbGroup)
        except:
            return

    def checkValueMinute(self):
        minutes = self.fUpload.spinBoxMinutes.value()
        if minutes % 5 != 0:
            self.fUpload.spinBoxMinutes.setValue(minutes + (5 - (minutes % 5)))

    def Delay(self, s):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(s * 1000), loop.quit)
        loop.exec_()

    def MsgBox(
        self,
        text="",
        icon=QtWidgets.QMessageBox.Information,
        standar=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    ):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(icon)
        self.msg.setWindowTitle("Thông báo")
        self.msg.setText(text)
        self.msg.setStandardButtons(standar)
        return self.msg.exec_()

    def loadForm(self):
        self.widgetSettings = QtWidgets.QWidget()
        self.widgetAddAccounts = QtWidgets.QWidget()
        self.widgetUpload = QtWidgets.QWidget()
        self.widgetProxy = QtWidgets.QWidget()
        self.widgetSeeding = QtWidgets.QWidget()
        self.widgetUpdateInfo = QtWidgets.QWidget()
        self.fSetting = Ui_fSettings()
        self.fAddAccounts = Ui_fAddAccounts()
        self.fUpload = Ui_fUpload()
        self.fProxy = Ui_fProxy()
        self.fSeeding = Ui_fSeeding()
        self.fUpdateInfo = Ui_fUpdateInfo()
        self.fSetting.setupUi(self.widgetSettings)
        self.fAddAccounts.setupUi(self.widgetAddAccounts)
        self.fUpload.setupUi(self.widgetUpload)
        self.fProxy.setupUi(self.widgetProxy)
        self.fSeeding.setupUi(self.widgetSeeding)
        self.fUpdateInfo.setupUi(self.widgetUpdateInfo)
        self.fSeeding.frame_3.setVisible(False)
        self.fSeeding.frame_4.setVisible(False)

        self.fSetting.btnSettingVideo.clicked.connect(self.widgetUpload.show)
        self.fSetting.btnSettingProxy.clicked.connect(self.widgetProxy.show)
        self.fSetting.btnSettingSeeding.clicked.connect(self.widgetSeeding.show)
        self.fSetting.btnSettingInfo.clicked.connect(self.widgetUpdateInfo.show)

        self.fUpload.btnOpenFileVideo.clicked.connect(self.OpenFileVideo)
        self.fUpload.btnOpenFolderVideo.clicked.connect(self.OpenFolderVideo)
        self.fUpload.btnOpenContent.clicked.connect(self.OpenFileContent)

        self.fUpdateInfo.btnFileBio.clicked.connect(self.OpenFileBio)
        self.fUpdateInfo.btnFileName.clicked.connect(self.OpenFileName)
        self.fUpdateInfo.btnFolderAvatar.clicked.connect(self.OpenFolderAvatar)

        self.btnSettings.clicked.connect(self.widgetSettings.show)
        self.btnAddAccounts.clicked.connect(self.widgetAddAccounts.show)
        self.fAddAccounts.btnAddAccounts.clicked.connect(self.addAccounts)

    def OpenFileVideo(self):
        file = QtWidgets.QFileDialog().getOpenFileName(None, "Mở file video", "./")
        if file[0] != "":
            self.fUpload.locationVideo.setText(file[0])

    def OpenFileContent(self):
        file = QtWidgets.QFileDialog.getOpenFileName(None, "Mở file content", "./")
        if file[0] != "":
            with open(file[0], encoding="utf-8") as file:
                self.fUpload.textContent.setPlainText(file.read())

    def OpenFileName(self):
        file = QtWidgets.QFileDialog().getOpenFileName(None, "Mở file tên", "./")
        if file[0] != "":
            self.fUpdateInfo.locationName.setText(file[0])

    def OpenFileBio(self):
        file = QtWidgets.QFileDialog().getOpenFileName(None, "Mở file tiểu sử", "./")
        if file[0] != "":
            self.fUpdateInfo.locationBio.setText(file[0])

    def OpenFolderVideo(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Mở folder chứa video", "./"
        )
        if folder != "":
            self.fUpload.locationFolderVideo.setText(folder)

    def OpenFolderAvatar(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Mở folder chứa ảnh", "./"
        )
        if folder != "":
            self.fUpdateInfo.locationAvatar.setText(folder)

    def setWidthColumnTableWidget(self):
        self.col_btn = self.tableWidget.columnCount() - 1
        self.col_status = self.tableWidget.columnCount() - 2
        self.col_description = self.tableWidget.columnCount() - 3
        self.col_note = self.tableWidget.columnCount() - 4
        self.col_group = self.tableWidget.columnCount() - 5

        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.col_status, QtWidgets.QHeaderView.Stretch
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            self.col_btn, QtWidgets.QHeaderView.Fixed
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Fixed
        )

        self.tableWidget.setColumnWidth(0, 25)

        self.tableWidget.setColumnWidth(self.col_btn, 100)
        self.tableWidget.setColumnWidth(self.col_status, 300)
        self.tableWidget.setColumnWidth(self.tableWidget.columnCount() - 3, 150)

    def removeItemTableWidget(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def show(self, row, col, text):
        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(text))

    def description(self, row, col, text):
        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(text))

    def setStatusbar(self):
        self.stringCountAcc = "Tổng tài khoản tiktok: %s"
        self.stringCountSelect = "Đã chọn: %s"

        self.labelCountAcc = QtWidgets.QLabel(self.stringCountAcc % 0)
        self.labelCountSelect = QtWidgets.QLabel(self.stringCountSelect % 0)

        css = 'color: rgb(221, 221, 221);\nfont: 10pt "Segoe UI";'
        self.labelCountAcc.setStyleSheet(css)
        self.labelCountSelect.setStyleSheet(css)
        self.statusbar.addWidget(self.labelCountAcc)
        self.statusbar.addWidget(self.labelCountSelect)

    def addAccounts(self):
        # self.tableWidget.itemChanged.connect(lambda: print("Tắt itemchanged"))
        conn = sqlite3.connect("data\\data.db")
        cursor = conn.cursor()
        data = self.fAddAccounts.plainTextData.toPlainText().splitlines()
        if data != 0:
            self.fAddAccounts.plainTextData.clear()
            self.widgetAddAccounts.close()
            for data in data:
                cookie = ""
                dt = data.split("|")
                if len(dt) == 2:
                    value = (
                    dt[0],
                    dt[1],
                    "",
                    "",
                    "",
                    "",
                    "",
                    self.fAddAccounts.cbGroup.currentText(),
                )
                else:
                # if len(dt) < 4:
                #     continue
                    if len(dt) == 5:
                        cookie = dt[-1]
                    value = (
                        dt[0],
                        dt[1],
                        dt[2],
                        dt[3],
                        cookie,
                        "",
                        "",
                        self.fAddAccounts.cbGroup.currentText(),
                    )
                (
                    username,
                    password,
                    mail,
                    passmail,
                    cookie,
                    note,
                    description,
                    nameType,
                ) = value
                sql_add_query = (
                    'INSERT INTO accounts (username, password, mail, passmail, cookie, note, description, type) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
                    % (
                        username,
                        password,
                        mail,
                        passmail,
                        cookie,
                        note,
                        description,
                        nameType,
                    )
                )
                try:
                    conn.execute(sql_add_query)
                    self.addItemAddAccounts(value, True)
                except:
                    pass
            conn.commit()
            cursor.close()
            conn.close()
        # self.tableWidget.itemChanged.connect(self.saveNote)

    def loadAccounts(self, type=None):
        output = DataBaseHandleTikTok.getTableAccounts(type)
        for value in output:
            self.addItemAddAccounts(value)
            self.Delay(0.01)
        self.labelCountAcc.setText(self.stringCountAcc % self.tableWidget.rowCount())

    def addItemAddAccounts(self, value, add=False):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        username, password, mail, passmail, cookie, note, description, nameType = value
        if (
            nameType != self.cbGroup.currentText()
            and self.cbGroup.currentText() != "[Tất cả thư mục]"
            and add
        ):
            self.tableWidget.hideRow(row)
        checkbox = QtWidgets.QTableWidgetItem()
        checkbox.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        checkbox.setCheckState(Qt.Unchecked)
        self.tableWidget.itemClicked.connect(self.eventSelected)
        self.tableWidget.setItem(row, 0, checkbox)
        proxy = ""
        profile = os.path.abspath(os.path.join("profile", username))
        if os.path.exists(profile):

            data = json.loads(
                open(profile + "\\Default\\Preferences", encoding="utf-8").read()
            )

            prr = data["gologin"]["proxy"]
            if "host" in prr:
                if prr["host"] != "":
                    proxy = "%s:%s" % (prr["host"], prr["port"])
        self.show(row, 1, username)
        self.show(row, 2, password)
        self.show(row, 3, mail)
        self.show(row, 4, passmail)
        self.show(row, 5, cookie)
        self.show(row, 6, proxy)
        self.show(row, self.col_group, nameType)
        self.show(row, self.col_note, note)
        self.show(row, self.col_description, description)
        self.createButton(row)

    def eventSelected(self):
        count = 0
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item.checkState() == Qt.Checked:
                count += 1
        self.labelCountSelect.setText(self.stringCountSelect % count)

    def createButton(self, row: int):

        button = QtWidgets.QPushButton("Bắt đầu")
        button.setStyleSheet(
            StyleSheet.QPushButton
            % ("#2E8B57", "#2E8B57", "#90EE90", "#90EE90", "#00FA9A", "#00FA9A")
        )
        button.clicked.connect(
            lambda _, r=row: self.buttonClicked(r)
        )  # lưu row bằng cách sử dụng lambda, để lấy lại row được thêm vào lúc trước khi bấm click
        self.tableWidget.setCellWidget(row, self.col_btn, button)

    def buttonClicked(self, row):

        if (
            self.fUpload.rbRandomVideo.isChecked()
            and self.fSetting.rbUpload.isChecked()
        ):
            location = self.fUpload.locationFolderVideo.text()
            if location != "" or os.path.exists(location):
                self.dirsVideo = os.listdir(location)
            else:
                return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        elif (
            self.fUpload.rbOnlyVideo.isChecked() and self.fSetting.rbUpload.isChecked()
        ):
            location = self.fUpload.locationVideo.text()
            if location == "" or not os.path.exists(location):
                return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        self.iterContent = iter(self.fUpload.textContent.toPlainText().splitlines())
        button = self.tableWidget.cellWidget(row, self.col_btn)
        if button.text() == "Bắt đầu":
            button.setText("Kết thúc")
            button.setStyleSheet(
                StyleSheet.QPushButton
                % ("#FF6347", "#FF6347", "#FF0000", "#FF0000", "#FF0000", "#FF0000")
            )
            iterRowSelect = iter([row])
            if self.fProxy.rbVproxyer.isChecked():

                keys = self.fProxy.textKey.toPlainText().splitlines()
                if keys == []:
                    self.show(row, self.col_status, "Vui lòng thêm key proxy!")
                    return
                try:
                    key = next(self.iterApi_key)
                except:
                    self.iterApi_key = iter(keys)
                    key = next(self.iterApi_key)
            else:
                key = ""
            self._listThread[row] = MainThread(self, iterRowSelect, key, 0, 0)
            self._listThread[row].show.connect(self.show)
            self._listThread[row].setButton.connect(self.setButton)
            self._listThread[row].start()
        else:
            button.setText("Bắt đầu")
            button.setStyleSheet(
                StyleSheet.QPushButton
                % ("#2E8B57", "#2E8B57", "#90EE90", "#90EE90", "#00FA9A", "#00FA9A")
            )
            # self._threads[row].stop()
            self._listThread[row].stop()

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu()
        openProfile_menu = QtWidgets.QMenu()
        openProfile_menu.setTitle("Mở profile")
        delete_menu = QtWidgets.QMenu()
        delete_menu.setTitle("Xoá")
        editItemTable_menu = QtWidgets.QMenu()
        editItemTable_menu.setTitle("Cập nhật thông tin")
        export_menu = QtWidgets.QMenu()
        export_menu.setTitle("Xuất file")
        move_group_menu = QtWidgets.QMenu()
        move_group_menu.setTitle("Chuyển sang thư mục")
        for value in vars().values():
            if isinstance(value, QtWidgets.QMenu):
                value.setStyleSheet(StyleSheet.QMenu)
        select_all_action = QtWidgets.QAction("Chọn tất cả")
        select_all_action.triggered.connect(self.selectAllChecked)
        unselect_all_action = QtWidgets.QAction("Bỏ chọn tất cả")
        unselect_all_action.triggered.connect(self.unselectAllChecked)
        start_select_action = QtWidgets.QAction("Bắt đầu")
        start_select_action.triggered.connect(self.startSelect)
        stop_action = QtWidgets.QAction("Kết thúc")
        stop_action.triggered.connect(self.stopAll)
        open_profile_action = QtWidgets.QAction("Mở profile")
        open_profile_action.triggered.connect(self.OpenProfile)
        open_profile_proxy_action = QtWidgets.QAction(
            "Mở profile(theo số lượng key proxy)"
        )
        open_profile_proxy_action.triggered.connect(lambda: self.OpenProfile(True))
        close_chrome_action = QtWidgets.QAction("Đóng tất cả chrome")
        close_chrome_action.triggered.connect(self.closeChrome)
        delete_profile_action = QtWidgets.QAction("Xoá profile")
        delete_profile_action.triggered.connect(self.DeleteProfile)
        delete_account_action = QtWidgets.QAction("Xoá tài khoản")
        delete_account_action.triggered.connect(self.DeleteAcc)
        add_proxy = QtWidgets.QAction("Thêm proxy")
        add_proxy.triggered.connect(self.AddProxy)
        delete_proxy = QtWidgets.QAction("Xoá proxy")
        delete_proxy.triggered.connect(self.DeleteProxy)
        export_account_action = QtWidgets.QAction("Xuất file username|password|cookie")
        export_account_action.triggered.connect(self.ExportData)
        exports_account_action = QtWidgets.QAction(
            "Xuất file username|password|mail|passmail|cookie"
        )
        exports_account_action.triggered.connect(lambda: self.ExportData(True))
        actions = []
        for item in self.get_combo_box_items(self.cbGroup):
            action = QtWidgets.QAction(item)
            action.triggered.connect(lambda _, i=item: self.moveGroupAccounts(i))
            actions.append(action)
        items = []
        for col in range(1, 10):
            if col == 7 or col == 6:
                continue
            col_name = self.tableWidget.horizontalHeaderItem(col).text()
            action = QtWidgets.QAction(col_name)
            action.triggered.connect(
                lambda _, c=col, c_n=col_name: self.editItemAction(c, c_n)
            )
            items.append(action)
        editItemTable_menu.addActions(items)
        move_group_menu.addActions(actions)
        menu.addAction(start_select_action)
        menu.addAction(stop_action)
        menu.addAction(select_all_action)
        menu.addAction(unselect_all_action)
        menu.addAction(add_proxy)
        menu.addAction(delete_proxy)
        openProfile_menu.addAction(open_profile_action)
        openProfile_menu.addAction(open_profile_proxy_action)
        menu.addAction(close_chrome_action)
        delete_menu.addAction(delete_profile_action)
        delete_menu.addAction(delete_account_action)
        export_menu.addAction(export_account_action)
        export_menu.addAction(exports_account_action)

        menu.addMenu(openProfile_menu)
        menu.addMenu(delete_menu)
        menu.addMenu(editItemTable_menu)
        menu.addMenu(export_menu)
        menu.addMenu(move_group_menu)

        menu.exec_(event.globalPos())

    def editItemAction(self, col, col_name):
        row = self.tableWidget.currentRow()
        usename = self.tableWidget.item(row, 1).text()
        valueNew, chk = QtWidgets.QInputDialog().getText(
            None,
            "Cập nhật thông tin " + col_name,
            col_name + " mới: ",
            text=self.tableWidget.item(row, col).text(),
        )
        if chk:
            self.show(row, col, valueNew)
            DataBaseHandleTikTok.updateRow(usename, col_name, valueNew)

    def moveGroupAccounts(self, nameType):
        # print(nameType)

        for row in sorted(self.getRowSelected(), reverse=True):
            username = self.tableWidget.item(row, 1).text().strip()
            DataBaseHandleTikTok.updateRow(username, "type", nameType)
            # self.refreshTable()
            self.show(row, 7, nameType)

            if self.cbGroup.currentIndex() != 0:
                self.tableWidget.item(row, 0).setCheckState(Qt.Unchecked)

                self.tableWidget.hideRow(row)

    def selectAllChecked(self):
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.item(r, 0).setCheckState(Qt.Checked)
        self.eventSelected()

    def unselectAllChecked(self):
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.item(r, 0).setCheckState(Qt.Unchecked)
        self.eventSelected()

    def getRowSelected(self):
        rows = []
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)

            if item.checkState() == Qt.Checked:
                rows.append(row)
        return rows

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            selected_rows = self.tableWidget.selectionModel().selectedRows()
            for index in selected_rows:
                item = self.tableWidget.item(index.row(), 0)
                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
            self.eventSelected()
        else:
            self.oldEvent(event)

    def ExportData(self, full=False):
        datas = []
        for r in range(self.tableWidget.rowCount()):
            data = []
            for c in range(1, 6):
                item = self.tableWidget.item(r, c)
                if item:
                    data.append(item.text())
            if not full:
                # xoá bỏ mail và passmail nếu không chọn full
                data.pop(2)
                data.pop(3)
            datas.append("|".join(data))
            # string += data[:-1]+"\n"
        file = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file data")
        if file[0]:
            with open(file[0], "w", encoding="utf-8") as file:
                file.write(str("\n".join(datas)))

    def startSelect(self):
        for value in self._listThread.values():
            if value.isRunning():
                return self.MsgBox("Không được spam bắt đầu!")
        if self.fSetting.rbUpload.isChecked():
            self.iterContent = iter(self.fUpload.textContent.toPlainText().splitlines())
        if (
            self.fUpload.rbRandomVideo.isChecked()
            and self.fSetting.rbUpload.isChecked()
        ):
            location = self.fUpload.locationFolderVideo.text()
            if location != "" or os.path.exists(location):
                self.dirsVideo = os.listdir(location)
            else:
                return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        elif (
            self.fUpload.rbOnlyVideo.isChecked() and self.fSetting.rbUpload.isChecked()
        ):
            location = self.fUpload.locationVideo.text()
            if location == "" or not os.path.exists(location):
                return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        if self.fProxy.rbVproxyer.isChecked():
            keys = self.fProxy.textKey.toPlainText().splitlines()
            countKey = len(keys)
            if countKey < self.fSetting.threadCount.value():
                self.fSetting.threadCount.setValue(countKey)

        rowSelect = self.getRowSelected()
        iterRowSelect = iter(rowSelect)
        self._list: Dict[int, Union[MainThread, None]] = {}
        self.countLinks = {}
        for t in self.fSeeding.textLinkVideo.toPlainText().splitlines():
            self.countLinks[t] = {
                "count": 0,
                "index": random.randint(
                    self.fSeeding.reactLink.value(), self.fSeeding.reactLink_2.value()
                ),
            }
        i = 0
        for x, y in setPositionChrome(300, 500, self.fSetting.threadCount.value()):
            if self.fProxy.rbVproxyer.isChecked():
                key = keys[i]
            else:
                key = ""
            self._list[i] = MainThread(self, iterRowSelect, key, x, y)
            self._list[i].show.connect(self.show)
            # self._list[i].newUsername.connect(lambda row, username: self.tableWidget.item(row, 1).setData(2, username))
            self._list[i].setButton.connect(self.setButton)
            self._list[i].start()
            i += 1
            self.Delay(0.1)

    def stopAll(self):
        try:
            for value in self._listThread.values():
                value.stop()
        except:
            pass

    def setButton(self, row, text):
        button = self.tableWidget.cellWidget(row, self.col_btn)
        if text == "start":
            button.setText("Bắt đầu")
            button.setStyleSheet(
                StyleSheet.QPushButton
                % ("#2E8B57", "#2E8B57", "#90EE90", "#90EE90", "#00FA9A", "#00FA9A")
            )
        else:
            button.setText("Kết thúc")
            button.setStyleSheet(
                StyleSheet.QPushButton
                % ("#FF6347", "#FF6347", "#FF0000", "#FF0000", "#FF0000", "#FF0000")
            )

    def DeleteProfile(self):
        usernames = []
        for row in self.getRowSelected():
            username = self.tableWidget.item(row, 1).text().strip()
            profile = os.path.abspath(os.path.join("profile", username))
            try:
                usernames.append(username)
                shutil.rmtree(profile)
                self.show(row, self.col_status, "Xoá profile thành công!")
                self.show(row, 5, "")
                self.show(row, 8, "")
                DataBaseHandleTikTok.updateRow(username, "cookie", "")
                DataBaseHandleTikTok.updateRow(username, "description", "")
            except:
                self.show(row, self.col_status, "Xoá profile thất bại!")

    def DeleteAcc(self):
        usernames = []
        for row in sorted(self.getRowSelected(), reverse=True):
            username = self.tableWidget.item(row, 1).text()
            usernames.append(username)
            try:
                profile = os.path.abspath(os.path.join("profile", username))
                shutil.rmtree(profile)
            except:
                pass
            self.tableWidget.removeRow(row)
        self.labelCountSelect.setText(
            self.stringCountSelect % self.tableWidget.rowCount()
        )
        DataBaseHandleTikTok.deleteRow(usernames)

    def OpenProfile(self, proxy=False):

        keys = self.fProxy.textKey.toPlainText().splitlines()
        # for index, row in enumerate(self.tableWidget.selectionModel().selectedRows()):
        for index, row in enumerate(self.getRowSelected()):
            if index >= len(keys) and proxy:
                break
            # row = row.row()
            if proxy:
                key = keys[index]
            else:
                key = ""
            self.open = OpenChrome(self, proxy, row, key)
            self.open.show.connect(self.show)
            self.open.start()
            self.Delay(0.1)

    def closeChrome(self):
        subprocess.Popen(
            'taskkill /F /IM "chrome.exe"', creationflags=subprocess.CREATE_NO_WINDOW
        )

    def AddProxy(self):
        file = QtWidgets.QFileDialog().getOpenFileName(None, "Mở file video", "./")
        if file[0] != "":
            data = open(file[0], errors="ignore").read().splitlines()
        index = 0
        for row in self.getRowSelected():
            if index >= len(data):
                index = 0
            proxy = data[index]
            username = self.tableWidget.item(row, 1).text()
            profile = os.path.abspath(os.path.join("profile", username))
            if not os.path.exists(profile):
                gologin = Gologin()
                gologin.createProfile(username)
            if Gologin().changeProxy(profile, proxy):
                self.show(row, self.col_status, "Thêm proxy thành công!")
                one = proxy.find(":")
                two = proxy.find(":", one + 1)
                self.show(row, 6, proxy[:two])
            else:
                self.show(row, self.col_status, "Thêm proxy thất bại!")
            index += 1

    def DeleteProxy(self):
        for row in self.getRowSelected():
            username = self.tableWidget.item(row, 1).text()
            profile = os.path.abspath(os.path.join("profile", username))
            if not os.path.exists(profile):
                gologin = Gologin()
                gologin.createProfile(username)
            if Gologin().changeProxy(profile, None):
                self.show(row, self.col_status, "Xoá proxy thành công!")
                self.show(row, 6, "")
            else:
                self.show(row, self.col_status, "xoá proxy thất bại!")


class OpenChrome(QtCore.QThread):
    show = QtCore.pyqtSignal(int, int, str)

    def __init__(self, this: TiktokManager, proxy, row, key) -> None:
        super().__init__()
        self._this = this
        self._proxy = proxy
        self._row = row
        self._key = key

    def run(self):
        username = self._this.tableWidget.item(self._row, 1).text()
        profile = os.path.abspath(os.path.join("profile", username))
        if not os.path.exists(profile):
            gologin = Gologin()
            gologin.createProfile(username)
        ip = ""
        if self._proxy:
            self.show.emit(self._row, self._this.col_status, "Đang đợi đổi ip...")
            vProxyer = Proxy(self._this.fProxy.textDomain.text(), self._key)
            ip = vProxyer.getIP()
            myip = vProxyer.changeIP(self._this.fProxy.rbIPNew.isChecked())
            if self._this.fProxy.rbIPOld.isChecked():
                myip = vProxyer.checkProxy(ip)
            print(myip)
            self.show.emit(self._row, 6, myip)
        else:
            data = json.loads(
                open(profile + "\\Default\\Preferences", encoding="utf-8").read()
            )

            proxy = data["gologin"]["proxy"]
            if "host" in proxy:
                if proxy["host"] != "":
                    ip = "%s:%s" % (proxy["host"], proxy["port"])

        self.show.emit(self._row, self._this.col_status, "Mở thành công!")

        args = [
            "chrome.exe",
            "--proxy-server=" + ip,
            "--lang=vi",
            "--no-first-run",
            "--no-sandbox",
            "--disable-web-security",
            "--password-store=basic" "--flag-switches-begin",
            "--flag-switches-end",
            "--no-default-browser-check",
            "--disable-popup-blocking",
            "--disable-extensions",
            # "--disable-gpu",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer",
            "--user-data-dir=" + profile,
        ]
        subprocess.Popen(
            args,
            start_new_session=True,
            shell=True,
            cwd=os.path.abspath("Data\\orbita-browser"),
            creationflags=subprocess.CREATE_NO_WINDOW,
        )


class MainThread(QtCore.QThread):
    show = QtCore.pyqtSignal(int, int, str)
    setButton = QtCore.pyqtSignal(int, str)

    def __init__(self, this: TiktokManager, iterRowSelect, key, *args) -> None:
        super().__init__()
        self._this = this
        self.iterRowSelect = iterRowSelect
        self._key = key
        self.x, self.y = args

    def stop(self):
        self.setButton.emit(self.row, "start")
        self.terminate()
        try:
            self.runTiktok.stop()
        except:
            pass

    def run(self):

        while True:
            try:
                self.row = next(self.iterRowSelect)
            except:
                return
            self._this._listThread[self.row] = self
            self.setButton.emit(self.row, "stop")
            self.runTiktok = RunTiktok(self, self.row, self._key)
            self.runTiktok.run()
            self.setButton.emit(self.row, "start")
            QtCore.QThread.sleep(
                random.randint(
                    self._this.fSetting.delayOpenChrome.value(),
                    self._this.fSetting.delayOpenChrome_2.value(),
                )
            )


class RunTiktok:
    # show = QtCore.pyqtSignal(int, int, str)
    def __init__(self, this: MainThread, row: int, key: str) -> None:
        super().__init__()
        self._this = this._this
        self.x, self.y = this.x, this.y
        self._row = row
        self._key = key
        self.show = this.show

    def stop(self):
        self.show.emit(self._row, self._this.col_status, "Đã dừng!")
        print("Đã dừng...")
        self.close()

    def close(self):
        def c():
            try:
                self.login.driver.close()
                self.login.driver.quit()
                self.login.stop(self.login.profile)
            except:
                pass

        threading.Thread(target=c).start()

    def _getContent(self):
        content = ""
        try:
            if self._this.fUpload.rbContentLine.isChecked():
                try:
                    content = next(self._this.iterContent)
                except:
                    self._this.iterContent = iter(
                        self._this.fUpload.textContent.toPlainText().splitlines()
                    )
                    content = next(self._this.iterContent)
            else:
                content = self._this.fUpload.textContent.toPlainText().splitlines()[0]
        except:
            pass
        return content

    @property
    def _delayUpload(self):
        return random.randint(
            self._this.fSetting.delayUpload.value(),
            self._this.fSetting.delayUpload_2.value(),
        )

    @property
    def _delayFollow(self):
        return random.randint(
            self._this.fSeeding.spinBoxDelayFollow.value(),
            self._this.fSeeding.spinBoxDelayFollow_2.value(),
        )

    @property
    def _timeViewStory(self):
        return random.randint(
            self._this.fSeeding.spinBoxTimeStory.value(),
            self._this.fSeeding.spinBoxTimeStory_2.value(),
        )

    @property
    def schedule(self):
        sche = ()
        if self._this.fUpload.groupBoxSchedule.isChecked():
            self._this.checkValueMinute()
            sche = (
                self._this.fUpload.spinBoxDay.value(),
                self._this.fUpload.spinBoxHours.value(),
                self._this.fUpload.spinBoxMinutes.value(),
            )
        return sche

    def _uploadVideo(self):
        # if self.login.checkLogin():
        if self._this.fUpload.rbOnlyVideo.isChecked():
            location = self._this.fUpload.locationVideo.text()
            if location != "" or os.path.exists(location):
                self.login.uploadVideo(location, self._getContent(), self.schedule)
            else:
                self.show.emit(
                    self._row, self._this.col_status, "Không có đường dẫn này!"
                )
        else:
            location = self._this.fUpload.locationFolderVideo.text()
            index = 0
            success = 0
            while index < self._this.fSetting.countVideo.value():
                if not self._this.dirsVideo:
                    self.show.emit(
                        self._row, self._this.col_status, "Hết video trong folder đó!"
                    )
                    break
                path = random.choice(self._this.dirsVideo)
                self._this.dirsVideo.remove(path)
                if path.endswith(".mp4") or path.endswith(".webm"):
                    chkUp = self.login.uploadVideo(
                        os.path.join(location, path), self._getContent(), self.schedule
                    )
                    if chkUp:
                        success += 1
                    if self._this.fSetting.cbDeleteVideo.isChecked() and chkUp:
                        self.show.emit(
                            self._row, self._this.col_status, "Đang xoá video..."
                        )
                        while True:
                            try:
                                os.remove(os.path.join(location, path))
                                break
                            except:
                                continue
                    index += 1
                    sleep(self._delayUpload)

            self.show.emit(
                self._row,
                self._this.col_status,
                "Upload thành công %s video!" % success,
            )

    # else: self.show.emit(self._row, self._this.col_status, "Chưa đăng nhập!")

    def _follow(self):
        for link in self._this.fSeeding.textLinkUser.toPlainText().splitlines():
            self.seeding.followUser(link)
            self.show.emit(
                self._row, self._this.col_status, "Theo dõi thành công %s !" % link
            )
            sleep(self._delayFollow)

    def _like(self):
        self.show.emit(self._row, self._this.col_status, "Đang chuẩn bị like...")
        delay = random.randint(5, 10)
        self.seeding.likeVideo(delay)
        # sleep(self._delayLike)
        self.show.emit(self._row, self._this.col_status, "Like hết video!")

    def _comment(self):

        nds = self._this.fSeeding.textComment.toPlainText().splitlines()
        if nds == []:
            self.show.emit(self._row, self._this.col_status, "Nội dung không có sẵn!")
            return
        nd = random.choice(nds)
        self.seeding.commentVideo(nd)
        self.show.emit(self._row, self._this.col_status, "Bình luận thành công !")
        # sleep(self._delayComment)

    # def _viewVideo(self):

    #     self.show.emit(self._row, self._this.col_status, "Đang xem video ...")

    #     self.show.emit(self._row, self._this.col_status, "Xem xong video!")
    def _saveVideo(self):

        self.show.emit(self._row, self._this.col_status, "Đang chuẩn bị lưu video...")
        self.seeding.saveVideo()
        # sleep(self._delayViewVideo)
        self.show.emit(self._row, self._this.col_status, "Đã lưu video!")

    def _copyVideo(self):

        self.show.emit(self._row, self._this.col_status, "Đang chuẩn bị share video...")
        self.seeding.shareVideo()
        # sleep(self._delayViewVideo)
        self.show.emit(self._row, self._this.col_status, "Đã share video!")

    def _viewLive(self):
        link = self._this.fSeeding.textLinkLive.text()
        self.show.emit(self._row, self._this.col_status, "Đang xem live...")
        nd = random.choice(
            self._this.fSeeding.textCommentLive.toPlainText().splitlines()
        )
        print(nd)
        timeView = (
            random.randint(
                self._this.fSeeding.spinBoxDelayViewLive.value(),
                self._this.fSeeding.spinBoxDelayViewLive_2.value(),
            )
            * 60
        )
        self.seeding.viewLive(
            link,
            nd,
            timeView,
            self._this.fSeeding.cbCommentLive.isChecked(),
            self._this.fSeeding.cbShareLive.isChecked(),
        )
        self.show.emit(self._row, self._this.col_status, "Xem xong live!")

    def _viewStory(self):
        self.show.emit(self._row, self._this.col_status, "Đang lướt bảng tin...")

        likeStory = self._this.fSeeding.cbLikeStory.isChecked()
        saveStory = self._this.fSeeding.cbSaveVideo.isChecked()
        self.seeding.story(self._timeViewStory, likeStory, saveStory)
        self.show.emit(self._row, self._this.col_status, "Lướt bảng tin thành công!")

    def run(self):
        username = self._this.tableWidget.item(self._row, 1).text()
        self.show.emit(self._row, self._this.col_status, "Chờ đến lượt chạy...")
        # omocaptcha = Omocaptcha(self._this.fSetting.api_key_captcha.text())
        # if not omocaptcha.checkValidKey() and self._this.fSetting.rbLogin.isChecked():
        #     self.show.emit(self._row, self._this.col_status, "Sai api key captcha!")
        #     return
        # if omocaptcha.getBalance() < 0.00060:
        #     self.show.emit(self._row, self._this.col_status, "Hết tiền captcha!")
        #     return
        if self._this.fProxy.rbVproxyer.isChecked():
            self.show.emit(self._row, self._this.col_status, "Đang đổi ip...")

            vProxyer = Proxy(self._this.fProxy.textDomain.text(), self._key)
            proxy = vProxyer.getIP()

            ip = vProxyer.changeIP(self._this.fProxy.rbIPNew.isChecked())
            if self._this.fProxy.rbIPOld.isChecked():
                ip = vProxyer.checkProxy(proxy)
            self.show.emit(self._row, 6, ip)
        else:
            proxy = ""
            profile = os.path.abspath(os.path.join("profile", username))
            if os.path.exists(profile):

                data = json.loads(
                    open(profile + "\\Default\\Preferences", encoding="utf-8").read()
                )

                prr = data["gologin"]["proxy"]
                if prr["host"] != "":
                    proxy = "%s:%s" % (prr["host"], prr["port"])

        self.version_main = self._this.fSetting.version_main.value()
        chkUpd = False
        rbLogin = self._this.fSetting.rbLogin.isChecked
        rbUpload = self._this.fSetting.rbUpload.isChecked
        rbUpdateInfo = self._this.fSetting.rbUpdateInfo.isChecked
        rbSeeding = self._this.fSetting.rbSeeding.isChecked
        api_key = self._this.fSetting.api_key_captcha.text()

        password = self._this.tableWidget.item(self._row, 2).text()
        cookie = self._this.tableWidget.item(self._row, 5)
        if cookie is None:
            cookie = ""
        else:
            cookie = cookie.text()
        try:
            self.login = TikTok(
                self, self._row, username, password, cookie, api_key, 0, 0, proxy
            )
            if rbLogin():
                if not self.login.checkLogin():
                    self.login.loginByUsername()
                else:
                    self.show.emit(self._row, self._this.col_status, "Đã đăng nhập!")
            else:
                chkContinue = True
                if not self.login.checkLogin():
                    if cookie != "":
                        chkContinue = self.login.addCookie()
                if chkContinue:
                    if rbUpload():
                        self._uploadVideo()
                    elif rbUpdateInfo():

                        # if self.login.checkLogin():
                        self.show.emit(
                            self._row,
                            self._this.col_status,
                            "Đang cập nhật thông tin nick...",
                        )

                        self.update = UpdateInfo()
                        self.update.setDiver(self.login.driver)
                        self.login.driver.get("https://www.tiktok.com/profile")
                        self.update.clickEditProfile()
                        if self._this.fUpdateInfo.gbAvatar.isChecked():
                            self.show.emit(
                                self._row,
                                self._this.col_status,
                                "Đang cập nhật ảnh đại diện...",
                            )

                            pathAvatar = self._this.fUpdateInfo.locationAvatar.text()
                            if os.path.exists(pathAvatar):
                                self.update.updateAvatar(pathAvatar)
                        if self._this.fUpdateInfo.gbBio.isChecked():
                            self.show.emit(
                                self._row,
                                self._this.col_status,
                                "Đang cập nhật tiểu sử...",
                            )

                            pathBio = self._this.fUpdateInfo.locationBio.text()
                            if os.path.exists(pathBio):
                                with open(pathBio, encoding="utf-8") as file:
                                    data = file.read().splitlines()
                                    for i in range(5):
                                        bio = random.choice(data)
                                        if len(bio) > 80:
                                            continue
                                        else:
                                            self.update.updateBio(bio)
                                            break

                        if self._this.fUpdateInfo.gbName.isChecked():
                            self.show.emit(
                                self._row,
                                self._this.col_status,
                                "Đang cập nhật tên và tiktokID...",
                            )

                            pathName = self._this.fUpdateInfo.locationName.text()
                            if os.path.exists(pathName):
                                name = GeneratorName(pathName)

                                self.update.updateName(name.fullname)
                                if self._this.fUpdateInfo.cbTiktokID.isChecked():
                                    self.usernameNew = name.username
                                    self.usernameNew = self.update.updateTikTokID(
                                        self.usernameNew
                                    )

                        sleep(5)
                        self.login.ClickJsWebElement("xpath", '//*[text()="Lưu" or text()="Save"]')
                        sleep(1)
                        try:
                            self.login.ClickJsWebElement(
                                "xpath",
                                '//button[@data-e2e="set-username-popup-confirm"]',
                                timeout=5,
                            )
                        except:
                            pass
                        sleep(10)
                        chkUpd = username not in self.login.driver.current_url
                        self.show.emit(
                            self._row,
                            self._this.col_description,
                            "Đã cập nhật thông tin nick!",
                        )
                        self.show.emit(
                            self._row,
                            self._this.col_status,
                            "Cập nhật thông tin nick thành công!",
                        )
                    elif rbSeeding():

                        # if self.login.checkLogin():
                        self.seeding = SeedingTiktok(self.login.driver)
                        fSeeding = self._this.fSeeding

                        if fSeeding.groupBoxLinkVideo.isChecked():
                            for (
                                link
                            ) in (
                                self._this.fSeeding.textLinkVideo.toPlainText().splitlines()
                            ):

                                if link in self._this.countLinks:
                                    if (
                                        self._this.countLinks[link]["count"]
                                        >= self._this.countLinks[link]["index"]
                                    ):
                                        self.show.emit(
                                            self._row,
                                            self._this.col_status,
                                            "Đủ %s lần cho link bỏ qua!"
                                            % self._this.countLinks[link]["index"],
                                        )
                                        continue
                                    self._this.countLinks[link]["count"] += 1

                                self.seeding.driver.get(link)
                                for i in range(
                                    random.randint(
                                        self._this.fSeeding.spinBoxTimeView.value(),
                                        self._this.fSeeding.spinBoxTimeView_2.value(),
                                    ),
                                    -1,
                                    -1,
                                ):
                                    self.show.emit(
                                        self._row,
                                        self._this.col_status,
                                        "Xem video trong %s giây thì kết thúc..." % i,
                                    )
                                    sleep(1)
                                if fSeeding.cbView.isChecked():
                                    self.show.emit(
                                        self._row,
                                        self._this.col_status,
                                        "Xem xong video!",
                                    )

                                if fSeeding.cbComment.isChecked():
                                    self._comment()
                                if fSeeding.cbLike.isChecked():
                                    self._like()

                                if fSeeding.cbSave.isChecked():
                                    self._saveVideo()
                                if fSeeding.cbCopy.isChecked():
                                    self._copyVideo()
                                for i in range(
                                    random.randint(
                                        self._this.fSeeding.spinBoxDelay.value(),
                                        self._this.fSeeding.spinBoxDelay_2.value(),
                                    ),
                                    -1,
                                    -1,
                                ):
                                    self.show.emit(
                                        self._row,
                                        self._this.col_status,
                                        "Vui lòng đợi %s giây nữa..." % i,
                                    )
                                    sleep(1)
                        if fSeeding.groupBoxFollow.isChecked():
                            self._follow()
                        if fSeeding.groupBoxViewLive.isChecked():
                            self._viewLive()
                        if fSeeding.groupBoxStory.isChecked():
                            self._viewStory()
                else:
                    self.show.emit(self._row, self._this.col_status, "Chưa đăng nhập!")

        except:
            try:
                self.login.saveDescription("Lỗi bất định!")
            except:
                pass
            with open("error.txt", "a+", encoding="utf-8") as file:
                file.write(traceback.format_exc() + "\n")
            self.show.emit(self._row, self._this.col_status, "Lỗi bất định!")
        self.close()

        # print(current_url)
        if self._this.fUpdateInfo.cbTiktokID.isChecked() and rbUpdateInfo() and chkUpd:
            values = self._this.getData(self._row)
            self.show.emit(self._row, 1, self.usernameNew)
            DataBaseHandleTikTok.updateRows(values, self.usernameNew)
            while True:
                try:
                    os.rename(
                        self.login.profile,
                        os.path.abspath(os.path.join("profile", self.usernameNew)),
                    )
                    break
                except:
                    pass

        # else:
        #     self.show.emit(self._row, self._this.col_description, "Đã cập nhật thông tin nick!")
        #     self.show.emit(self._row, self._this.col_status, "Cập nhật tiktokID thất bại!")


if __name__ == "__main__":
    import sys
    import resources_rc

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(":/logo/logo/tiktok.ico"))
    MainWindow = QtWidgets.QMainWindow()

    nuoitiktok = TiktokManager()
    MainWindow.show()
    sys.exit(app.exec_())
