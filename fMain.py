import datetime
import gc
import os
import random
import shutil
import subprocess
import threading
from time import sleep
import typing
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, Qt
from Ui_fTiktok import Ui_MainWindow
from Ui_fSettings import Ui_fSettings
from Ui_fSettingUpload import Ui_fUpload
from Ui_fProxy import Ui_fProxy
from Ui_fSeeding import Ui_fSeeding
from gologin import Gologin
from mainTikTok import TikTok
from omocaptcha import Omocaptcha
from config import Config
from postionChrome import setPositionChrome
from proxy import Proxy
from typing import Union, Dict
from datetime import datetime
import traceback
from seedingTiktok import SeedingTiktok
# import shutil
import requests
import logging
import sys
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
sema = None
globalCssMenu = """
QMenu {
    border: 1px solid rgb(40, 44, 90);
    border-radius: 4px;
    padding: 4px;
    background-color: rgb(40, 44, 52);
    color: white;
    
}
QMenu::item:selected {
    background-color: rgba(196, 167, 231, 0.5);
    color: white;
}         """
globalCssButton = '''QPushButton {
	border: 2px solid %s;
	border-radius: 5px;	
	background-color: %s;
}
 QPushButton:hover {
	background-color: %s;
	border: 2px solid %s;
}
 QPushButton:pressed {	
	background-color: %s;
	border: 2px solid %s;
}'''

sema = None
class TiktokManager(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(MainWindow)

        self.config = Config()
        self.loadForm()
        self.setWidthColumnTableWidget()
        self.setStatusbar()
        self.oldEvent = self.tableWidget.keyPressEvent
        self.tableWidget.keyPressEvent = self.keyPressEvent
        self.btnAddAccounts.clicked.connect(self.addAccounts)
        self.tableWidget.contextMenuEvent = self.contextMenuEvent
        
        self.loadAccounts()
        self.loadSettings()
        self.tableWidget.itemDoubleClicked.connect(self.editItem)
        self.tableWidget.itemChanged.connect(self.saveNote)
        self._listThread: Dict[int, Union[MainThread, None]]= {}
        self.textChangedConnect()

    def saveNote(self, item):
        if item.column() == 5:
            cf = Config()
            data = cf.getDataFileJson("data.json")
            username = self.tableWidget.item(item.row(), 1).text().strip()
            data["accounts"][username]["note"] = item.text().strip() if item else item
            cf.writeDataFileJson("data.json", data)
    def editItem(self, item):
        if item.column() == 5:
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        else:
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
    def textChangedConnect(self):
        # self.fUpload.textContent.textChanged.connect(self.writeSettings)
        # self.fProxy.textKey.textChanged.connect(self.writeSettings)
        # self.fProxy.textDomain.textChanged.connect(self.writeSettings)
        # self.fProxy.groupBoxVporxyer.clicked.connect(self.writeSettings)
        # self.fProxy.rbIPOld.clicked.connect(self.writeSettings)
        # self.fProxy.rbIPNew.clicked.connect(self.writeSettings)

        varfSettings = vars(self.fSetting)
        varfSettings.update(vars(self.fSeeding))
        varfSettings.update(vars(self.fUpload))
        varfSettings.update(vars(self.fProxy))
        for value in varfSettings.values():
            if isinstance(value, QtWidgets.QLineEdit) or isinstance(value, QtWidgets.QPlainTextEdit):
                value.textChanged.connect(self.writeSettings)
            elif isinstance(value, QtWidgets.QSpinBox):
                value.valueChanged.connect(self.writeSettings)
            elif isinstance(value, QtWidgets.QRadioButton) or isinstance(value, QtWidgets.QCheckBox) or isinstance(value, QtWidgets.QGroupBox):
                value.clicked.connect(self.writeSettings)

            
    def writeSettings(self):
        data = {}
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
        data["rbIPNew"] = self.fProxy.rbIPNew.isChecked()
        data["rbIPOld"] = self.fProxy.rbIPOld.isChecked()
        data["rbUpload"] = self.fSetting.rbUpload.isChecked()
        data["rbLogin"] = self.fSetting.rbLogin.isChecked()
        data["rbSeeding"] = self.fSetting.rbSeeding.isChecked()
        data["countVideo"] = self.fSetting.countVideo.value()
        data["delayOpen"] = {"delay1": self.fSetting.delayOpenChrome.value(), "delay2": self.fSetting.delayOpenChrome_2.value()}
        data["delayUpload"] = {"delay1": self.fSetting.delayUpload.value(), "delay2": self.fSetting.delayUpload_2.value()}
        data["textContent"] = self.fUpload.textContent.toPlainText()
        data["vProxyer"] = {
            "checked": self.fProxy.groupBoxVporxyer.isChecked(),
            "textDomain": self.fProxy.textDomain.text(),
            "textKey": self.fProxy.textKey.toPlainText(),
        }
        data["seeding"] = {
            "follow": {
                "checked": self.fSeeding.groupBoxFollow.isChecked(),
                "textLinkUser": self.fSeeding.textLinkUser.toPlainText(),
                "delay": {"delay1": self.fSeeding.spinBoxDelayFollow.value(), "delay2": self.fSeeding.spinBoxDelayFollow_2.value()}
            },
            "linkVideo":{
                "checked": self.fSeeding.groupBoxLinkVideo.isChecked(),
                "textLinkVideo": self.fSeeding.textLinkVideo.toPlainText(),
                "textComment": self.fSeeding.textComment.toPlainText(),
                "comment": self.fSeeding.cbComment.isChecked(),
                "like": self.fSeeding.cbLike.isChecked(),
                "view": self.fSeeding.cbView.isChecked(),
                "save": self.fSeeding.cbSave.isChecked(),
                "copy": self.fSeeding.cbCopy.isChecked(),
                "timeView": {"timeView1": self.fSeeding.spinBoxTimeView.value(), "timeView2": self.fSeeding.spinBoxTimeView_2.value()},
                "delay": {"delay1": self.fSeeding.spinBoxDelay.value(), "delay2": self.fSeeding.spinBoxDelay_2.value()}

            },
            "stream":{
                "checked": self.fSeeding.groupBoxViewLive.isChecked(),
                "share": self.fSeeding.cbShareLive.isChecked(),
                "comment": self.fSeeding.cbCommentLive.isChecked(),
                "textCommentLive": self.fSeeding.textCommentLive.toPlainText(),
                "textLinkLive": self.fSeeding.textLinkLive.text(),
                "timeView": {"timeView1": self.fSeeding.spinBoxDelayViewLive.value(), "timeView2": self.fSeeding.spinBoxDelayViewLive_2.value()}
            },
            "story": {
                "checked": self.fSeeding.groupBoxStory.isChecked(),
                "like": self.fSeeding.cbLikeStory.isChecked(),
                "save": self.fSeeding.cbSaveVideo.isChecked(),
                "timeView": {"timeView1": self.fSeeding.spinBoxTimeStory.value(), "timeView2": self.fSeeding.spinBoxTimeStory_2.value()},

            }

        }
        self.config.writeDataFileJson("settings.json", data=data)
        self.iterApi_key = iter(self.fProxy.textKey.toPlainText().splitlines())
    def loadSettings(self):
        if os.path.exists("settings.json"):
            data = self.config.getDataFileJson("settings.json")
            self.fSetting.api_key_captcha.setText(data["api_key"])
            self.fSetting.threadCount.setValue(data["threadCount"])
            self.fSetting.version_main.setValue(data["version_main"])
            self.fSetting.rbHidenChrome.setChecked(data["rbHidenChrome"])
            self.fProxy.textKey.setPlainText(data["vProxyer"]["textKey"])
            self.fProxy.textDomain.setText(data["vProxyer"]["textDomain"])
            self.fProxy.groupBoxVporxyer.setChecked(data["vProxyer"]["checked"])
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
            self.fSeeding.spinBoxTimeView.setValue(linkVideo["timeView"]["timeView1"])
            self.fSeeding.spinBoxTimeView_2.setValue(linkVideo["timeView"]["timeView2"])
            self.fSeeding.spinBoxDelay.setValue(linkVideo["delay"]["delay1"])
            self.fSeeding.spinBoxDelay_2.setValue(linkVideo["delay"]["delay2"])

            self.fSeeding.groupBoxViewLive.setChecked(stream["checked"])
            self.fSeeding.textLinkLive.setText(stream["textLinkLive"])
            self.fSeeding.textCommentLive.setPlainText(stream["textCommentLive"])
            self.fSeeding.cbShareLive.setChecked(stream["share"])
            self.fSeeding.cbCommentLive.setChecked(stream["comment"])
            self.fSeeding.spinBoxDelayViewLive.setValue(stream["timeView"]["timeView1"])
            self.fSeeding.spinBoxDelayViewLive_2.setValue(stream["timeView"]["timeView2"])

            self.fSeeding.groupBoxStory.setChecked(story["checked"])
            self.fSeeding.cbLikeStory.setChecked(story["like"])
            self.fSeeding.cbSaveVideo.setChecked(story["save"])
            self.fSeeding.spinBoxTimeStory.setValue(story["timeView"]["timeView1"])
            self.fSeeding.spinBoxTimeStory_2.setValue(story["timeView"]["timeView2"])

    def checkValueMinute(self):
        minutes = self.fUpload.spinBoxMinutes.value()
        if minutes % 5 != 0:
            self.fUpload.spinBoxMinutes.setValue(minutes + (5 - (minutes % 5)))
    
    def Delay(self, s):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(s*1000), loop.quit)
        loop.exec_()
    
    def MsgBox(self, text="", icon=QtWidgets.QMessageBox.Information):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(icon)
        self.msg.setWindowTitle("Thông báo")
        self.msg.setText(text)
        self.msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msg.exec_()
    def loadForm(self):
        self.widgetSettings = QtWidgets.QWidget()
        self.widgetUpload = QtWidgets.QWidget()
        self.widgetProxy = QtWidgets.QWidget()
        self.widgetSeeding = QtWidgets.QWidget()
        self.fSetting = Ui_fSettings()
        self.fUpload = Ui_fUpload()
        self.fProxy = Ui_fProxy()
        self.fSeeding = Ui_fSeeding()
        self.fSetting.setupUi(self.widgetSettings)
        self.fUpload.setupUi(self.widgetUpload)
        self.fProxy.setupUi(self.widgetProxy)
        self.fSeeding.setupUi(self.widgetSeeding)
        self.fSeeding.frame_3.setVisible(False)
        self.fSeeding.frame_4.setVisible(False)
        self.fSetting.btnSettingVideo.clicked.connect(self.widgetUpload.show)
        self.fSetting.btnSettingProxy.clicked.connect(self.widgetProxy.show)
        self.fSetting.btnSettingSeeding.clicked.connect(self.widgetSeeding.show)
        self.fUpload.btnOpenFileVideo.clicked.connect(self.OpenFileVideo)
        self.fUpload.btnOpenFolderVideo.clicked.connect(self.OpenFolderVideo)
        self.fUpload.btnOpenContent.clicked.connect(self.OpenFileContent)

        self.btnSettings.clicked.connect(self.widgetSettings.show)
    def OpenFileVideo(self):
        file = QtWidgets.QFileDialog.getOpenFileName(None, "Mở file video", "./")
        if (file[0] != ""):
            self.fUpload.locationVideo.setText(file[0])
    def OpenFileContent(self):
        file = QtWidgets.QFileDialog.getOpenFileName(None, "Mở file content", "./")
        if (file[0] != ""):
            with open(file[0], encoding="utf-8") as file:
                self.fUpload.textContent.setPlainText(file.read())
    def OpenFolderVideo(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Mở folder chứa video", "./")
        if folder != "": self.fUpload.locationFolderVideo.setText(folder)
    def setWidthColumnTableWidget(self):
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.horizontalHeader().setSectionResizeMode(self.tableWidget.columnCount() - 2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(self.tableWidget.columnCount() - 1, QtWidgets.QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(self.tableWidget.columnCount() - 1, 100)
        self.tableWidget.setColumnWidth(self.tableWidget.columnCount() - 2, 300)
        self.tableWidget.setColumnWidth(self.tableWidget.columnCount() - 3, 150)
        self.tableWidget.setColumnWidth(0, 25)
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
        
        self.labelCountAcc = QtWidgets.QLabel(self.stringCountAcc%0)
        self.labelCountSelect = QtWidgets.QLabel(self.stringCountSelect%0)
        
        css = "color: rgb(221, 221, 221);\nfont: 10pt \"Segoe UI\";"
        self.labelCountAcc.setStyleSheet(css)
        self.labelCountSelect.setStyleSheet(css)
        self.statusbar.addWidget(self.labelCountAcc)
        self.statusbar.addWidget(self.labelCountSelect)
        
    def addAccounts(self):
        
        file = QtWidgets.QFileDialog.getOpenFileName(None, "Mở file chứa tài khoản tiktok", "./")
  
        if (file[0] != ""):
            self.removeItemTableWidget()
            dataOld = {"accounts": {}}
            if os.path.exists("data.json"): 
                dataOld = self.config.getDataFileJson("data.json")
            datas = {}
            with open(file[0], encoding="utf-8") as file:
                data = file.read().splitlines()
                for d in data:
                    d = d.split("|")
                    if len(d) == 3:
                        username, password, cookie = d[0], d[1], d[2]
                    else: 
                        username, password, cookie = d[0], d[1], None

                    datas.update({username: {"password": password, "cookie": cookie, "note": None, "description": None}})
                file.close()
            dataOld["accounts"].update(datas)
            
            
            self.config.writeDataFileJson("data.json", dataOld)
            self.loadAccounts()
    def loadAccounts(self):
        
        if not os.path.exists("data.json"): return
        dataOld = self.config.getDataFileJson("data.json")
        for value in dataOld["accounts"]:
            username, value = value, dataOld["accounts"][value]
            password, cookie, note, description =  value["password"], value["cookie"], value["note"], value["description"]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            checkbox = QtWidgets.QTableWidgetItem()
            checkbox.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox.setCheckState(Qt.Unchecked) 
            self.tableWidget.itemClicked.connect(self.eventSelected)
            self.tableWidget.setItem(row, 0, checkbox)
            self.show(row, 1, username)
            self.show(row, 2, password)
            self.show(row, 3, cookie)
            self.show(row, 5, note)
            self.show(row, 7, description)
            self.createButton(row)
        self.labelCountAcc.setText(self.stringCountAcc%self.tableWidget.rowCount())
    def eventSelected(self):
        count = 0
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item.checkState() == Qt.Checked: count += 1
        self.labelCountSelect.setText(self.stringCountSelect%count)
    def createButton(self, row: int):
        button = QtWidgets.QPushButton("Bắt đầu")
        button.setStyleSheet(globalCssButton%("#2E8B57", "#2E8B57", "#90EE90", "#90EE90", "#00FA9A", "#00FA9A"))
        button.clicked.connect(lambda _, r=row: self.buttonClicked(r)) #lưu row bằng cách sử dụng lambda, để lấy lại row được thêm vào lúc trước khi bấm click
        self.tableWidget.setCellWidget(row, 8, button)
    def buttonClicked(self, row):
        
        if self.fUpload.rbRandomVideo.isChecked() and self.fSetting.rbUpload.isChecked():
            location = self.fUpload.locationFolderVideo.text()
            if location != "" or os.path.exists(location):
                self.dirsVideo = os.listdir(location)
            else:
                return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        elif self.fUpload.rbOnlyVideo.isChecked() and self.fSetting.rbUpload.isChecked():
            location = self.fUpload.locationVideo.text()
            if location == "" or not os.path.exists(location): return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        self.iterContent = iter(self.fUpload.textContent.toPlainText().splitlines())
        button = self.tableWidget.cellWidget(row, 8)
        if button.text() == "Bắt đầu":
            button.setText("Kết thúc")
            button.setStyleSheet(globalCssButton%("#FF6347", "#FF6347", "#FF0000", "#FF0000", "#FF0000", "#FF0000"))
            
            iterRowSelect = iter([row])
            keys = self.fProxy.textKey.toPlainText().splitlines()
            if keys == []: 
                self.show(row, 7, "Vui lòng thêm key proxy!")
                return
            try:
                key = next(self.iterApi_key)
            except: 
                self.iterApi_key = iter(keys)
                key = next(self.iterApi_key)
            self._listThread[row] = MainThread(self, iterRowSelect, key, 0, 0)
            self._listThread[row].show.connect(self.show)
            self._listThread[row].setButton.connect(self.setButton)
            self._listThread[row].start()
        else:
            button.setText("Bắt đầu")
            button.setStyleSheet(globalCssButton%("#2E8B57", "#2E8B57", "#90EE90", "#90EE90", "#00FA9A", "#00FA9A"))
            # self._threads[row].stop()
            self._listThread[row].stop()
    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(globalCssMenu)
        select_all_action = QtWidgets.QAction("Chọn tất cả")
        select_all_action.triggered.connect(self.selectAllChecked)
        unselect_all_action = QtWidgets.QAction("Bỏ chọn tất cả")
        unselect_all_action.triggered.connect(self.unselectAllChecked)
        start_select_action = QtWidgets.QAction("Bắt đầu")
        start_select_action.triggered.connect(self.startSelect)
        stop_action = QtWidgets.QAction("Kết thúc")
        stop_action.triggered.connect(self.stopAll)
        open_profile_action = QtWidgets.QAction("Mở profile(no proxy)")
        open_profile_action.triggered.connect(self.OpenProfile)
        open_profile_proxy_action = QtWidgets.QAction("Mở profile(theo số lượng key proxy)")
        open_profile_proxy_action.triggered.connect(lambda: self.OpenProfile(True))
        close_chrome_action = QtWidgets.QAction("Đóng tất cả chrome")
        close_chrome_action.triggered.connect(self.closeChrome)
        delete_profile_action = QtWidgets.QAction("Xoá profile")
        delete_profile_action.triggered.connect(self.DeleteProfile)
        delete_account_action = QtWidgets.QAction("Xoá tài khoản")
        delete_account_action.triggered.connect(self.DeleteAcc)
        export_account_action = QtWidgets.QAction("Xuất file username|password|cookie")
        export_account_action.triggered.connect(self.ExportData)
        menu.addAction(start_select_action)
        menu.addAction(stop_action)
        menu.addAction(select_all_action)
        menu.addAction(unselect_all_action)
        menu.addAction(open_profile_action)
        menu.addAction(open_profile_proxy_action)
        menu.addAction(close_chrome_action)
        menu.addAction(delete_profile_action)
        menu.addAction(delete_account_action)
        menu.addAction(export_account_action)
        menu.exec_(event.globalPos())
    def selectAllChecked(self):
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.item(r, 0).setCheckState(Qt.Checked)
        self.eventSelected()
    def unselectAllChecked(self):
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.item(r, 0).setCheckState(Qt.Unchecked)
        self.eventSelected()
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
    def ExportData(self):
        string = ""
        for r in range(self.tableWidget.rowCount()):
            data = ""
            for c in range(1, 4):
                item = self.tableWidget.item(r, c)
                if item:
                    data += item.text()+"|"
            string += data[:-1]+"\n"
        file = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file data")
        if file[0]:
            with open(file[0], "w", encoding="utf-8") as file:
                file.write(string)
    def startSelect(self):
        for value in self._listThread.values():
            if value.isRunning(): return self.MsgBox("Không được spam bắt đầu!")
        if self.fSetting.rbUpload.isChecked(): self.iterContent = iter(self.fUpload.textContent.toPlainText().splitlines())
        if self.fUpload.rbRandomVideo.isChecked() and self.fSetting.rbUpload.isChecked():
            location = self.fUpload.locationFolderVideo.text()
            if location != "" or os.path.exists(location):
                self.dirsVideo = os.listdir(location)
            else:
                return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        elif self.fUpload.rbOnlyVideo.isChecked() and self.fSetting.rbUpload.isChecked():
            location = self.fUpload.locationVideo.text()
            if location == "" or not os.path.exists(location): return self.MsgBox("Vui lòng chọn đúng đường dẫn video!")
        if self.fProxy.groupBoxVporxyer.isChecked():
            keys = self.fProxy.textKey.toPlainText().splitlines()
            countKey = len(keys)
            if countKey < self.fSetting.threadCount.value():
                self.fSetting.threadCount.setValue(countKey)
            
        rowSelect = []
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item.checkState() == Qt.Checked: rowSelect.append(row)
        iterRowSelect = iter(rowSelect)
        self._list: Dict[int, Union[MainThread, None]]= {}
        i = 0
        for x, y in setPositionChrome(300, 500, self.fSetting.threadCount.value()):
            if self.fProxy.groupBoxVporxyer.isChecked(): key = keys[i]
            else: key = ""
            self._list[i] = MainThread(self, iterRowSelect, key, x, y)
            self._list[i].show.connect(self.show)
            self._list[i].setButton.connect(self.setButton)
            self._list[i].start()
            i += 1
            self.Delay(0.1)
    def stopAll(self):
        try:
            for value in self._listThread.values():
                value.stop()
        except: pass
    def setButton(self, row, text):
        button = self.tableWidget.cellWidget(row, 8)
        if text == "start":
            button.setText("Bắt đầu")
            button.setStyleSheet(globalCssButton%("#2E8B57", "#2E8B57", "#90EE90", "#90EE90", "#00FA9A", "#00FA9A"))
        else:
            button.setText("Kết thúc")
            button.setStyleSheet(globalCssButton%("#FF6347", "#FF6347", "#FF0000", "#FF0000", "#FF0000", "#FF0000"))
    def DeleteProfile(self):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item.checkState() == Qt.Checked:
                username = self.tableWidget.item(row, 1).text().strip()
                profile = os.path.abspath(os.path.join("profile", username))
                try:
                    shutil.rmtree(profile)
                    self.show(row, 7, "Xoá profile thành công!")
                    self.show(row, 5, "")
                    self.show(row, 3, "")
                    cf = Config()
                    data = cf.getDataFileJson("data.json")
                    data["accounts"][username]["cookie"] = ""
                    data["accounts"][username]["description"] = ""
                    cf.writeDataFileJson("data.json", data)
                except: self.show(row, 7, "Xoá profile thất bại!")
                
    def DeleteAcc(self):
        dataOld = self.config.getDataFileJson("data.json")
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if item.checkState() == Qt.Checked:
                username = self.tableWidget.item(row, 1).text()
                dataOld["accounts"].pop(username)
                try:
                    profile = os.path.abspath(os.path.join("profile", username))
                    shutil.rmtree(profile)
                except: pass
        self.config.writeDataFileJson("data.json", dataOld)
        self.removeItemTableWidget()
        self.loadAccounts()
        
    def OpenProfile(self, proxy=False):


        keys = self.fProxy.textKey.toPlainText().splitlines()
        for index, row in enumerate(self.tableWidget.selectionModel().selectedRows()):
            if index >= len(keys) and proxy: break
            row = row.row()
            if proxy: key = keys[index]
            else: key = ""
            self.open = OpenChrome(self, proxy, row, key)
            self.open.show.connect(self.show)
            self.open.start()
            self.Delay(0.1)
    def closeChrome(self):
        subprocess.Popen('taskkill /F /IM "chrome.exe"', creationflags=subprocess.CREATE_NO_WINDOW)
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
            self.show.emit(self._row, 7, "Đang đợi đổi ip...")
            vProxyer = Proxy(self._this.fProxy.textDomain.text(), self._key)
            ip = vProxyer.getIP()
            myip = vProxyer.changeIP(self._this.fProxy.rbIPNew.isChecked())
            if self._this.fProxy.rbIPOld.isChecked(): myip = vProxyer.checkProxy(ip)
            print(myip)
            self.show.emit(self._row, 4, myip)
        self.show.emit(self._row, 7, "Mở thành công!")

        args = [
            "chrome.exe",
            "--proxy-server="+ip,
            "--lang=en-US",
            "--no-first-run",
            "--no-sandbox",
            "--disable-web-security",
            '--password-store=basic'
            "--flag-switches-begin",
            "--flag-switches-end",
            "--no-default-browser-check",
            "--disable-popup-blocking",
            "--disable-extensions",
            # "--disable-gpu",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer",
            '--user-data-dir='+profile,
        ]
        subprocess.Popen(args, start_new_session=True, shell=True, cwd=os.path.abspath("Data\\orbita-browser"), creationflags=subprocess.CREATE_NO_WINDOW)
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
        try: self.runTiktok.stop()
        except: pass
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
            QtCore.QThread.sleep(random.randint(self._this.fSetting.delayOpenChrome.value(), self._this.fSetting.delayOpenChrome_2.value()))
            
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
        self.show.emit(self._row, 7, "Đã dừng!")
        print("Đã dừng...")
        self.close()
    def close(self):
        def c():
            try:
                self.login.driver.close()
                self.login.driver.quit()
                self.login.stop(self.login.profile)
            except: pass
        threading.Thread(target=c).start()
    def _getContent(self):
        if self._this.fUpload.rbContentLine.isChecked():
            try:
                content = next(self._this.iterContent)
            except: 
                self._this.iterContent = iter(self._this.fUpload.textContent.toPlainText().splitlines())
                content = next(self._this.iterContent)
        else:
            content = self._this.fUpload.textContent.toPlainText().splitlines()[0]
        return content
    @property
    def _delayUpload(self):
        return random.randint(self._this.fSetting.delayUpload.value(), self._this.fSetting.delayUpload_2.value())
    @property
    def _delayFollow(self):
        return random.randint(self._this.fSeeding.spinBoxDelayFollow.value(), self._this.fSeeding.spinBoxDelayFollow_2.value())
    @property
    def _timeViewStory(self):
        return random.randint(self._this.fSeeding.spinBoxTimeStory.value(), self._this.fSeeding.spinBoxTimeStory_2.value())
    
    @property
    def schedule(self):
        sche = None
        if self._this.fUpload.groupBoxSchedule.isChecked():
            self._this.checkValueMinute()
            sche = self._this.fUpload.spinBoxDay.value(), self._this.fUpload.spinBoxHours.value(), self._this.fUpload.spinBoxMinutes.value()
        return sche
    def _uploadVideo(self):
        if self.login.checkLogin(): 
            if self._this.fUpload.rbOnlyVideo.isChecked():
                location = self._this.fUpload.locationVideo.text()
                if location != "" or os.path.exists(location):
                    self.login.uploadVideo(location, self._getContent(), self.schedule)
                else:
                    self.show.emit(self._row, 7, "Không có đường dẫn này!")
            else:
                location = self._this.fUpload.locationFolderVideo.text()
                index = 0
                success = 0
                while index < self._this.fSetting.countVideo.value():
                    if not self._this.dirsVideo: 
                        self.show.emit(self._row, 7, "Hết video trong folder đó!")
                        break
                    path = random.choice(self._this.dirsVideo)
                    self._this.dirsVideo.remove(path)
                    if path.endswith(".mp4") or path.endswith(".webm"):
                        chkUp = self.login.uploadVideo(os.path.join(location, path), self._getContent(), self.schedule)
                        if chkUp: success += 1
                        if self._this.fSetting.cbDeleteVideo.isChecked() and chkUp:
                            self.show.emit(self._row, 7, "Đang xoá video...")
                            while True:
                                try: os.remove(os.path.join(location, path)); break
                                except:continue
                        index += 1
                        sleep(self._delayUpload)
                        
                self.show.emit(self._row, 7, "Upload thành công %s video!"%success)
        else: self.show.emit(self._row, 7, "Chưa đăng nhập!")
    
    def _follow(self):
        for link in self._this.fSeeding.textLinkUser.toPlainText().splitlines():
            self.seeding.followUser(link)
            self.show.emit(self._row, 7, "Theo dõi thành công %s !"%link)
            sleep(self._delayFollow)
    def _like(self):
        self.show.emit(self._row, 7, "Đang chuẩn bị like...")
        delay = random.randint(5, 10)
        self.seeding.likeVideo(delay)
        # sleep(self._delayLike)
        self.show.emit(self._row, 7, "Like hết video!")
    def _comment(self):
        
        nds = self._this.fSeeding.textComment.toPlainText().splitlines()
        if nds == []: 
            self.show.emit(self._row, 7, "Nội dung không có sẵn!")
            return
        nd = random.choice(nds)
        self.seeding.commentVideo(nd)
        self.show.emit(self._row, 7, "Bình luận thành công !")
        # sleep(self._delayComment)
    
    # def _viewVideo(self):
        
    #     self.show.emit(self._row, 7, "Đang xem video ...")
        
    #     self.show.emit(self._row, 7, "Xem xong video!")
    def _saveVideo(self):
        
        self.show.emit(self._row, 7, "Đang chuẩn bị lưu video...")
        self.seeding.saveVideo()
        # sleep(self._delayViewVideo)
        self.show.emit(self._row, 7, "Đã lưu video!")
    def _copyVideo(self):
        
        self.show.emit(self._row, 7, "Đang chuẩn bị share video...")
        self.seeding.shareVideo()
        # sleep(self._delayViewVideo)
        self.show.emit(self._row, 7, "Đã share video!")
    def _viewLive(self):
        link = self._this.fSeeding.textLinkLive.text()
        self.show.emit(self._row, 7, "Đang xem live...")
        nd = random.choice(self._this.fSeeding.textCommentLive.toPlainText().splitlines())
        print(nd)
        timeView = random.randint(self._this.fSeeding.spinBoxDelayViewLive.value(), self._this.fSeeding.spinBoxDelayViewLive_2.value())*60
        self.seeding.viewLive(link, nd, timeView, self._this.fSeeding.cbCommentLive.isChecked(), self._this.fSeeding.cbShareLive.isChecked())
        self.show.emit(self._row, 7, "Xem xong live!")
    def _viewStory(self):
        self.show.emit(self._row, 7, "Đang lướt bảng tin...")

        likeStory = self._this.fSeeding.cbLikeStory.isChecked()
        saveStory = self._this.fSeeding.cbSaveVideo.isChecked()
        self.seeding.story(self._timeViewStory, likeStory, saveStory)
        self.show.emit(self._row, 7, "Lướt bảng tin thành công!")

    def run(self):
        
        self.show.emit(self._row, 7, "Chờ đến lượt chạy...")
        omocaptcha = Omocaptcha(self._this.fSetting.api_key_captcha.text())
        if not omocaptcha.checkValidKey() and self._this.fSetting.rbLogin.isChecked():
            self.show.emit(self._row, 7, "Sai api key captcha!")
            return
        if omocaptcha.getBalance() < 0.00060:
            self.show.emit(self._row, 7, "Hết tiền captcha!")
            return
        if self._this.fProxy.groupBoxVporxyer.isChecked():
            self.show.emit(self._row, 7, "Đang đổi ip...")
            
            vProxyer = Proxy(self._this.fProxy.textDomain.text(), self._key)
            proxy = vProxyer.getIP()
            
            ip = vProxyer.changeIP(self._this.fProxy.rbIPNew.isChecked())
            if self._this.fProxy.rbIPOld.isChecked(): ip = vProxyer.checkProxy(proxy)
            self.show.emit(self._row, 4, ip)
        else: proxy = ""
        self.version_main =  self._this.fSetting.version_main.value()
        rbLogin = self._this.fSetting.rbLogin.isChecked
        rbUpload = self._this.fSetting.rbUpload.isChecked
        api_key = self._this.fSetting.api_key_captcha.text()
        username = self._this.tableWidget.item(self._row, 1).text()
        password = self._this.tableWidget.item(self._row, 2).text()
        cookie = self._this.tableWidget.item(self._row, 3)
        if cookie is None: cookie = ""
        else: cookie = cookie.text()
        try:
            self.login = TikTok(self, self._row, username, password, cookie, api_key, 0, 0, proxy)
            if rbLogin():
                if not self.login.checkLogin(): 
                    self.login.loginByUsername()
                else: self.show.emit(self._row, 7, "Đã đăng nhập!")
            elif rbUpload(): self._uploadVideo()
                
            else:
                if self.login.checkLogin(): 
                    self.seeding = SeedingTiktok(self.login.driver)
                    fSeeding = self._this.fSeeding
                    if fSeeding.groupBoxLinkVideo.isChecked():
                        for link in self._this.fSeeding.textLinkVideo.toPlainText().splitlines():
                            self.seeding.driver.get(link)
                            for i in range(random.randint(self._this.fSeeding.spinBoxTimeView.value(), self._this.fSeeding.spinBoxTimeView_2.value()), -1, -1):
                                self.show.emit(self._row, 7, "Xem video trong %s giây thì kết thúc..."%i)
                                sleep(1)
                            if fSeeding.cbView.isChecked(): self.show.emit(self._row, 7, "Xem xong video!")
                            
                            if fSeeding.cbComment.isChecked(): self._comment()
                            if fSeeding.cbLike.isChecked(): self._like()
                            
                            if fSeeding.cbSave.isChecked(): self._saveVideo()
                            if fSeeding.cbCopy.isChecked(): self._copyVideo()
                            for i in range(random.randint(self._this.fSeeding.spinBoxDelay.value(), self._this.fSeeding.spinBoxDelay_2.value()), -1, -1):
                                self.show.emit(self._row, 7, "Vui lòng đợi %s giây nữa..."%i)
                                sleep(1)
                    if fSeeding.groupBoxFollow.isChecked(): self._follow()
                    if fSeeding.groupBoxViewLive.isChecked(): self._viewLive()
                    if fSeeding.groupBoxStory.isChecked(): self._viewStory()
                else: self.show.emit(self._row, 7, "Chưa đăng nhập!")
                            
        except: 
            try: self.login.saveDescription("Lỗi bất định!")
            except: pass
            with open("error.txt", "a+", encoding="utf-8") as file:
                file.write(traceback.format_exc()+"\n")
            self.show.emit(self._row, 7, "Lỗi bất định!")
        self.close()
if __name__ == "__main__":
    import sys
    import resources_rc
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(":/logo/logo/tiktok.ico"))
    MainWindow = QtWidgets.QMainWindow()
    nuoitiktok = TiktokManager()
    MainWindow.show()
    sys.exit(app.exec_())