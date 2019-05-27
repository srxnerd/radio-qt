#!/usr/bin/env python3


from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
import colored
import requests
import bs4
import os
import string
from colored import fore, back, style
import sys
import wget
import requests
from bs4 import BeautifulSoup

import selenium.webdriver.opera
import pyfiglet
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
link = "https://www.radiojavan.com/playlists/playlist/mp3/854b87855624"
driver = webdriver.Chrome("/home/sti/down_git/chromedriver")
driver.get(link)
driver.set_window_size(800, 700)
elem = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[1]""")
actions = ActionChains(driver)
actions.click(elem).perform()
elem2 = driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
po = driver.find_element_by_class_name("artist").text
po1 = driver.find_element_by_class_name("song").text


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 630)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 621))
        self.frame.setStyleSheet("QFrame{\n"
"background:#000C29;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.popnew = QtWidgets.QPushButton(self.frame)
        self.popnew.setGeometry(QtCore.QRect(20, 70, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Gargi-1.2b")
        self.popnew.setFont(font)
        self.popnew.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-new-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.popnew.setIcon(icon)
        self.popnew.setIconSize(QtCore.QSize(23, 28))
        self.popnew.setObjectName("popnew")
        self.artist = QtWidgets.QPushButton(self.frame)
        self.artist.setGeometry(QtCore.QRect(20, 20, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Gargi-1.2b")
        self.artist.setFont(font)
        self.artist.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-micro-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.artist.setIcon(icon1)
        self.artist.setIconSize(QtCore.QSize(23, 23))
        self.artist.setObjectName("artist")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(20, 120, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Gargi-1.2b")
        font.setItalic(True)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-exit-sign-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setIconSize(QtCore.QSize(22, 25))
        self.exit.setObjectName("exit")
        self.name2 = QtWidgets.QPushButton(self.frame)
        self.name2.setGeometry(QtCore.QRect(20, 260, 161, 61))
        self.name2.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-guitar-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name2.setIcon(icon3)
        self.name2.setIconSize(QtCore.QSize(31, 33))
        self.name2.setObjectName("name2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 351, 51))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:25px;\n"
"}\n"
"*{\n"
"color:black;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}\n"
"")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-headphones-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setObjectName("pushButton")
        self.name6 = QtWidgets.QPushButton(self.frame)
        self.name6.setGeometry(QtCore.QRect(20, 330, 161, 61))
        self.name6.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        self.name6.setIcon(icon3)
        self.name6.setIconSize(QtCore.QSize(31, 33))
        self.name6.setObjectName("name6")
        self.name1 = QtWidgets.QPushButton(self.frame)
        self.name1.setGeometry(QtCore.QRect(20, 190, 161, 61))
        font = QtGui.QFont()
        font.setItalic(False)
        self.name1.setFont(font)
        self.name1.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        self.name1.setIcon(icon3)
        self.name1.setIconSize(QtCore.QSize(31, 33))
        self.name1.setObjectName("name1")
        self.name5 = QtWidgets.QPushButton(self.frame)
        self.name5.setGeometry(QtCore.QRect(190, 330, 161, 61))
        self.name5.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}\n"
"")
        self.name5.setIcon(icon3)
        self.name5.setIconSize(QtCore.QSize(31, 33))
        self.name5.setObjectName("name5")
        self.name8 = QtWidgets.QPushButton(self.frame)
        self.name8.setGeometry(QtCore.QRect(20, 400, 161, 61))
        self.name8.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        self.name8.setIcon(icon3)
        self.name8.setIconSize(QtCore.QSize(31, 33))
        self.name8.setObjectName("name8")
        self.name3 = QtWidgets.QPushButton(self.frame)
        self.name3.setGeometry(QtCore.QRect(190, 260, 161, 61))
        self.name3.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        self.name3.setIcon(icon3)
        self.name3.setIconSize(QtCore.QSize(31, 33))
        self.name3.setObjectName("name3")
        self.play = QtWidgets.QPushButton(self.frame)
        self.play.setGeometry(QtCore.QRect(170, 540, 49, 45))
        self.play.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        self.play.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-play-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon5)
        self.play.setIconSize(QtCore.QSize(35, 35))
        self.play.setObjectName("play")
        self.download = QtWidgets.QPushButton(self.frame)
        self.download.setGeometry(QtCore.QRect(300, 540, 49, 45))
        self.download.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:15px;\n"
"}\n"
"#Form{\n"
"        background:redl;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        self.download.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-downloading-updates-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download.setIcon(icon6)
        self.download.setIconSize(QtCore.QSize(35, 35))
        self.download.setObjectName("download")
        self.name7 = QtWidgets.QPushButton(self.frame)
        self.name7.setGeometry(QtCore.QRect(190, 400, 161, 61))
        self.name7.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        self.name7.setIcon(icon3)
        self.name7.setIconSize(QtCore.QSize(33, 31))
        self.name7.setObjectName("name7")
        self.Repeat = QtWidgets.QPushButton(self.frame)
        self.Repeat.setGeometry(QtCore.QRect(30, 540, 51, 45))
        self.Repeat.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        self.Repeat.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-sync-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Repeat.setIcon(icon7)
        self.Repeat.setIconSize(QtCore.QSize(35, 35))
        self.Repeat.setObjectName("Repeat")
        self.next = QtWidgets.QPushButton(self.frame)
        self.next.setGeometry(QtCore.QRect(240, 540, 49, 45))
        self.next.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        self.next.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-fast-forward-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon8)
        self.next.setIconSize(QtCore.QSize(35, 35))
        self.next.setAutoRepeat(False)
        self.next.setObjectName("next")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(100, 540, 49, 45))
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"background:#E60000;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#0fb9b1;\n"
"}")
        self.back.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("/home/sti/radiojavan-Qt/icon/icons8-rewind-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon9)
        self.back.setIconSize(QtCore.QSize(35, 35))
        self.back.setAutoRepeat(False)
        self.back.setAutoExclusive(False)
        self.back.setObjectName("back")
        self.name4 = QtWidgets.QPushButton(self.frame)
        self.name4.setGeometry(QtCore.QRect(190, 190, 161, 61))
        self.name4.setStyleSheet("QPushButton\n"
"{\n"
"background:#ff9f00;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#850101;\n"
"}")
        self.name4.setIcon(icon3)
        self.name4.setIconSize(QtCore.QSize(31, 33))
        self.name4.setObjectName("name4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.next.clicked.connect(self.next_c)
        self.play.clicked.connect(self.play_c)
        self.back.clicked.connect(self.back_c)
        self.Repeat.clicked.connect(self.Repeat_c)
        self.download.clicked.connect(self.download_c)
        self.exit.clicked.connect(self.exit_c)
        self.popnew.clicked.connect(self.pop_c)
        self.artist.clicked.connect(self.arti_c)
        self.name1.clicked.connect(self.name1_c)
        self.name2.clicked.connect(self.name2_c)
        self.name3.clicked.connect(self.name3_c)
        self.name4.clicked.connect(self.name4_c)
        self.name5.clicked.connect(self.name5_c)
        self.name6.clicked.connect(self.name6_c)
        self.name7.clicked.connect(self.name7_c)
        self.name8.clicked.connect(self.name8_c)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def name1_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[1]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name2_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[11]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name3_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[3]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name4_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[9]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name5_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[10]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name6_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[12]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name7_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[14]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def name8_c(self):
        dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[14]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
    def arti_c(self):
        artis = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[2]""")
        actions = ActionChains(driver)
        actions.click(artis).perform()
        time.sleep(3)
        cls = driver.find_element_by_xpath("""//*[@id="playlist_categories"]/div/a[9]""").click()
    def exit_c(self):
        driver.close()
        driver.close()
    def art_c(self):
        artis = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[2]""").click()
    def exit_c(self):
        sys.exit(app.exec_(driver.close()))
        driver.close()
    def pop_c(self):
        try:
            artis = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[2]""")
            actions = ActionChains(driver)
            actions.click(artis).perform()
            time.sleep(3)
            p =  driver.find_element_by_xpath("""//*[@id="playlist_categories"]/div/a[5]""")
            actions = ActionChains(driver)
            actions.click(p).perform()
            time.sleep(3)
            sd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[4]""")
            actions = ActionChains(driver)
            actions.click(sd).perform()
            time.sleep(3)
            sr = driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""")
            actions = ActionChains(driver)
            actions.click(sr).perform()
        except:
            print("oh no")
    def next_c(self):
        elem = driver.find_element_by_xpath("""//*[@id="mp3_next"]""")
        actions = ActionChains(driver)
        actions.click(elem).perform()
        time.sleep(3)
        img = driver.find_element_by_xpath("""//*[@id="mp3"]/div/div[3]/div[1]/div/div[1]/div[1]/img""")
        actions = ActionChains(driver)
        actions.click(img).perform()
    def play_c(self):
        elem = driver.find_element_by_xpath("""//*[@id="mp3_play"]""")
        actions = ActionChains(driver)
        actions.click(elem).perform()
    def back_c(self):
        elem = driver.find_element_by_xpath("""//*[@id="mp3_back"]""")
        actions = ActionChains(driver)
        actions.click(elem).perform()
    def Repeat_c(self):
        driver.find_element_by_xpath("""//*[@id="mp3_repeat"]""").click()
    def download_c(self):
        try:
            po = driver.find_element_by_class_name("artist").text
            po1 = driver.find_element_by_class_name("song").text
            link_rj="https://host2.rj-mw1.com/media/mp3/mp3-256/"
            ar = po
            ar = ar.replace(',', '')
            ar = ar.replace('&', '')
            ar = ar.replace('vs', '')
            ar = ar.replace('@', '')
            ar = ar.replace('*', '')
            ar = ar.replace('()', '')
            ar = ar.replace('(', '').replace(')', '')
            ar = ar.replace('[', '').replace(']', '')
            mp = "-".join(ar.split())
            song = po1
            song = song.replace(',', '')
            song = song.replace('(', '').replace(')', '')
            song = song.replace('[', '').replace(']', '')
            song = song.replace('{', '').replace('}', '')
            song = song.replace('*', '')
            song = song.replace('&', '')
            song = song.replace('vs', '')
            song = song.replace('@', '')
            md = "-".join(song.split())
            mp3=".mp3"
            newstr = "-".join((mp, md))
            ok=link_rj+newstr+mp3
            print(ok)
            time.sleep(1)
            os.system("mkdir radio-Qt")
            wget.download(ok ,"radio-Qt/"+str(po)+" "+str(po1)+".mp3")
            os.system("notify-send Downlaod-Done")
        except:
            try:
                po = driver.find_element_by_class_name("artist").text
                po1 = driver.find_element_by_class_name("song").text
                link_rja="https://host2.rj-mw1.com/media/mp3/mp3-256/"
                ss = po
                ss = ss.replace(',', '')
                ss = ss.replace('&', '')
                ss = ss.replace('vs', '')
                ss = ss.replace('@', '')
                ss = ss.replace('*', '')
                ss = ss.replace('[', '').replace(']', '')
                mp = "-".join(ss.split())
                songs = po1
                songs = songs.replace(',', '')
                songs = songs.replace('[', '').replace(']', '')
                songs = songs.replace('{', '').replace('}', '')
                songs = songs.replace('*', '')
                songs = songs.replace('&', '')
                songs = songs.replace("/" , "")
                songs = songs.replace('vs', '')
                songs = songs.replace('@', '')
                md = "-".join(songs.split())
                mp3=".mp3"
                newstr = "-".join((mp, md))
                newstr.replace(" ", "")
                ok=link_rja+newstr+mp3
                print(ok)
                time.sleep(2)
                wget.download(ok ,"radio-Qt/"+str(po)+" "+str(po1)+".mp3")
                os.system("notify-send Downlaod-Done")
                time.sleep(3)
                os.system("mkdir radio-Qt")
                os.system("mv *.mp3 radio-Qt")
                os.system("clear")
            except:
                po = driver.find_element_by_class_name("artist").text
                po1 = driver.find_element_by_class_name("song").text
                link_rja="https://host1.rj-mw1.com/media/mp3/mp3-256/"
                ss = po
                ss = ss.replace(',', '')
                ss = ss.replace('&', '')
                ss = ss.replace('vs', '')
                ss = ss.replace('@', '')
                ss = ss.replace('*', '')
                ss = ss.replace('[', '').replace(']', '')
                mp = "-".join(ss.split())
                songs = po1
                songs = songs.replace(',', '')
                songs = songs.replace('[', '').replace(']', '')
                songs = songs.replace('{', '').replace('}', '')
                songs = songs.replace('*', '')
                songs = songs.replace('&', '')
                songs = songs.replace("/" , "")
                songs = songs.replace('vs', '')
                songs = songs.replace('@', '')
                md = "-".join(songs.split())
                mp3=".mp3"
                newstr = "-".join((mp, md))
                newstr.replace(" ", "")
                ok=link_rja+newstr+mp3
                print(ok)
                wget.download(ok ,"radiojavan_music/"+str(po)+" "+str(po1)+".mp3")
                os.system("notify-send Downlaod-Done")
                time.sleep(3)
                os.system("mkdir radio-Qt")
                os.system("mv *.mp3 radio-Qt")
                os.system("clear")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "radiojavan-gui"))
        self.popnew.setText(_translate("MainWindow", "new pop"))
        self.artist.setText(_translate("MainWindow", "artist"))
        self.exit.setText(_translate("MainWindow", "exit"))
        self.name2.setText(_translate("MainWindow", "Sasy"))
        self.name6.setText(_translate("MainWindow", "Shadmehr Aghil"))
        self.name1.setText(_translate("MainWindow", "Arash"))
        self.name5.setText(_translate("MainWindow", "Mohsen Yegane"))
        self.name8.setText(_translate("MainWindow", "Moein"))
        self.name3.setText(_translate("MainWindow", "Dariush"))
        self.name7.setText(_translate("MainWindow", "Sirvan khosravi"))
        self.name4.setText(_translate("MainWindow", "Mohsen Chavoshi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
driver.close()
