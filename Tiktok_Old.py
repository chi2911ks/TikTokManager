import datetime
import os
import sqlite3
from time import sleep
import typing
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, Qt
from Ui_tiktok import Ui_MainWindow
from omocaptcha import Omocaptcha
from config import Config
from mainOld import TikTok
from postionChrome import setPositionChrome
from uploadVideo import UploadVideoTiktok
import traceback
import requests
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
class NuoiTiktok(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.config = Config()
        self.createDatabase()
        self.setStatusbar()
        self.loadAccounts()
        self.loadSettings()
        self.tableWidget.contextMenuEvent = self.contextMenuEvent
        self.threadNew = CreateThread(self)
        self.threadNew.show.connect(self.show)
        self.threadCount.valueChanged.connect(self.writeSettings)
        self.api_key_captcha.textChanged.connect(self.writeSettings)
        self.locationVideo.textChanged.connect(self.writeSettings)
        self.locationCookie.textChanged.connect(self.writeSettings)
        self.version_main.valueChanged.connect(self.writeSettings)
        self.btnAddAccounts.clicked.connect(self.addAccounts)
        self.btnFolderVideo.clicked.connect(self.openFolderVideo)
        self.btnFolderCookie.clicked.connect(self.openFolderCookie)
        self.btnExportCookie.clicked.connect(self.ExportCookie)
        self.btnStart.clicked.connect(self.start)
        self.btnStop.clicked.connect(self.stop)
    def createDatabase(self):
        conn = sqlite3.connect('account.db')
        cursor = conn.cursor()
        sql_create_accounts_table = """ CREATE TABLE IF NOT EXISTS accounts (
                                        username text PRIMARY KEY,
                                        password text NOT NULL,
                                        cookie text
                                    ); """
        cursor.execute(sql_create_accounts_table)
        cursor.close()
        conn.close()
    def writeSettings(self):
        data = {}
        data["api_key"] = self.api_key_captcha.text()
        data["threadCount"] = self.threadCount.value()
        data["locationVideo"] = self.locationVideo.text()
        data["locationCookie"] = self.locationCookie.text()
        data["version_main"] = self.version_main.value()
        self.config.writeDataFileJson("settings.json", data=data)
    def loadSettings(self):
        try:
            if os.path.exists("settings.json"):
                data = self.config.getDataFileJson("settings.json")
                self.api_key_captcha.setText(data["api_key"])
                self.threadCount.setValue(data["threadCount"])
                self.locationVideo.setText(data["locationVideo"])
                self.version_main.setValue(data["version_main"])
                self.locationCookie.setText(data["locationCookie"])
        except: return
    def removeItemTableWidget(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
    def show(self, row, col, text):
        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(text))
    def setStatusbar(self):
        self.stringCountAcc = "Tổng tài khoản tiktok: %s"
        
        self.labelCountAcc = QtWidgets.QLabel(self.stringCountAcc%0)
        
        css = "color: rgb(221, 221, 221);\nfont: 10pt \"Segoe UI\";"
        self.labelCountAcc.setStyleSheet(css)
       
        self.statusbar.addWidget(self.labelCountAcc)
    def addAccounts(self):
        conn = sqlite3.connect('account.db')
        cursor = conn.cursor()
        file = QtWidgets.QFileDialog.getOpenFileName(None, "Mở file chứa tài khoản tiktok", "./")
        
        if (file[0] != ""):
            self.removeItemTableWidget()
            
            with open(file[0], encoding="utf-8") as file:
                data = file.read().splitlines()
                for data in data:
                    dt = data.split("|")
                    if len(dt) > 2:
                        cookie = dt[-1]
                    else: cookie = ""
                    try: conn.execute(
    """INSERT INTO accounts (username, password, cookie) VALUES ("%s", "%s", "%s")"""%(dt[0], dt[1], cookie))
                    except: pass
            conn.commit()
        
            cursor.close()
            conn.close()
            self.loadAccounts()
    def loadAccounts(self):
        
        if not os.path.exists("account.db"): return
        conn = sqlite3.connect('account.db')
        cursor = conn.cursor()
        statement = '''SELECT * FROM accounts'''

        cursor.execute(statement)


        output = cursor.fetchall()
        for row in output:
            username, password, cookie = row
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.show(row, 0, username)
            self.show(row, 1, password)
            self.show(row, 2, cookie)
        self.labelCountAcc.setText(self.stringCountAcc%self.tableWidget.rowCount())

        conn.commit()
        cursor.close()
        conn.close()
    def deleteRow(self, usernames):
        conn = sqlite3.connect('account.db')
        cursor = conn.cursor()
        record_users_to_delete = usernames
        placeholders = ",".join("?" * len(record_users_to_delete))
        delete_query = f"DELETE FROM accounts WHERE username IN ({placeholders})"
        cursor.execute(delete_query, tuple(record_users_to_delete))
        conn.commit()
        cursor.close()
        conn.close()
        
    def updateRow(self, username, column, value):
        conn = sqlite3.connect('account.db')
        cursor = conn.cursor()
        update_query = "UPDATE accounts SET %s = ? WHERE username = ?"%column
        cursor.execute(update_query, (value, username))
        conn.commit()
        cursor.close()
        conn.close()
    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(globalCssMenu)
        delete_account_action = QtWidgets.QAction("Xoá tài khoản")
        delete_account_action.triggered.connect(self.DeleteAcc)
        menu.addAction(delete_account_action)
        menu.exec_(event.globalPos())
    def DeleteAcc(self):
        usernames = []
        for row in self.tableWidget.selectionModel().selectedRows():
            username = self.tableWidget.item(row.row(), 0).text()
            usernames.append(username)
        self.removeItemTableWidget()
        self.deleteRow(usernames)
        self.loadAccounts()
    def start(self):
        global sema
        self.threadNew.createJ2Team = False
        sema = QtCore.QSemaphore(self.threadCount.value())
        if not self.threadNew.isRunning(): self.threadNew.start()
    def stop(self):
        self.threadNew.stop()
    def openFolderVideo(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Mở folder chứa video", "./")
        if folder != "": self.locationVideo.setText(folder)
    def openFolderCookie(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Mở folder chứa j2team cookie", "./")
        if folder != "": self.locationCookie.setText(folder)
    def ExportCookie(self):
        global sema
        self.threadNew.createJ2Team = True
        sema = QtCore.QSemaphore(self.threadCount.value())
        if not self.threadNew.isRunning(): self.threadNew.start()
class CreateThread(QtCore.QThread):
    show = QtCore.pyqtSignal(int, int, str)
    createJ2Team = False
    def __init__(self, this: NuoiTiktok) -> None:
        super().__init__()
        self.this = this
    def stop(self):
        try:
            for v in self.listThread.values(): 

                v.stop()
        except: pass
    def run(self):
        self.listThread = {}
        row_selected = self.this.tableWidget.selectionModel().selectedRows()
        index = 0
        for x, y in setPositionChrome(500, 700, len(row_selected)):
            row = row_selected[index].row()
            username = self.this.tableWidget.item(row, 0).text()
            password = self.this.tableWidget.item(row, 1).text()
            try:
                cookie = self.this.tableWidget.item(row, 2).text()
            except: cookie = ""
            self.listThread[row] = LoginAndUpload(self, row, username, password, cookie, x, y, self.createJ2Team)
            self.listThread[row].start()
            sleep(0.1)
            index += 1
            
class LoginAndUpload(QtCore.QThread):
    def __init__(self, this: CreateThread, row, username, password, cookie, x, y, createJ2Team=False) -> None:
        super().__init__()
        self.this = this
        self.row = row
        self.username = username
        self.password = password
        self.cookie = cookie
        self.x = x
        self.y = y
        self.createJ2Team = createJ2Team
    def stop(self):
        try: 
            self.quit()
            self.this.show.emit(self.row, 3, "Đã dừng!")
        except: pass
        self.terminate()
    def quit(self):
        try:
            self.login.driver.quit()
            self.login.stop(self.login.driver.user_data_dir)
            self.login.deleteProfile()
        except: pass
    def run(self):
        sema.acquire()
        pathVideo = self.this.this.locationVideo.text()
        if self.this.this.rdUpload.isChecked() and not os.path.exists(pathVideo):
            self.this.show.emit(self.row, 3, "Không tìm thấy thư mực video!")
            sema.release()
            return
        api_key = self.this.this.api_key_captcha.text()
        omocaptcha = Omocaptcha(api_key)
        if not omocaptcha.checkValidKey() and self.this.this.rdLogin.isChecked():
            self.this.show.emit(self.row, 3, "Sai api key captcha!")
            return
        if omocaptcha.getBalance() < 0.00060:
            self.this.show.emit(self.row, 3, "Hết tiền captcha!")
            return
        try:

            self.login = TikTok(self.this, self.row, self.username, self.password, self.cookie, api_key, self.x, self.y, "")

            
            if not self.createJ2Team:
                # if self.login.checkLogin():
                if self.this.this.rdLogin.isChecked():
                    if not self.login.checkLogin():
                        self.login.loginByUsername()
                elif self.this.this.rdJ2Team.isChecked():
                    if not self.login.checkLogin():
                        self.login.addCookieJ2Team()
                elif self.this.this.rdUpload.isChecked():
                    if self.cookie != "": 
                        if not self.login.checkLogin():
                            self.login.addCookie()
                        for path in os.listdir(pathVideo):
                            if path.endswith(".mp4"):
                                self.login.uploadVideo(os.path.join(pathVideo, path), "")
                    else:
                        if self.login.checkLogin():
                            for path in os.listdir(pathVideo):
                                if path.endswith(".mp4"):
                                    self.login.uploadVideo(os.path.join(pathVideo, path), "")
            
                
            self.login.createJ2Team()
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            self.this.show.emit(self.row, 3, "Lỗi bất định!")

        self.quit()
        sema.release()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    nuoitiktok = NuoiTiktok()
    MainWindow.show()
    sys.exit(app.exec_())
