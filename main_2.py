from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtCore

#from ds import Ui_MainWindow
import sys
#from PyQt5 import QtCore, QtGui
#from PyQt5.QtCore import QSize,QDateTime
import sqlite3
from threading import Thread
import time

import datetime
import pygame
from PyQt5.QtGui import QFont
import re
from PyQt5.QtGui import QPixmap

########################

class MainWindow(QMainWindow):
    def __init__(self,name,start_time,tybe_pc,time_in,user_name):
        super(MainWindow, self).__init__()
        

        

        ######################
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        ########################
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_timer2)
        self.minutes2 = 0
        ########################
        self.name = name
        self.start_time = start_time
        self.user_name = user_name
        self.tybe_pc = tybe_pc

        self.DS()
        
        if time_in.isdigit():
            self.time_in = int(time_in)
            self.lb_too.hide()
            self.start_timer()
            self.start_timer2()
        elif isinstance(time_in, str):
            self.input_mint = time_in 

            if self.input_mint == "ساعه":
                self.lb_too.hide()
                self.time_in = 60
                self.start_timer()
                self.start_timer2()
            elif self.input_mint  == "ساعتين":
                self.lb_too.hide()
                self.time_in = 120
                self.start_timer()
                self.start_timer2()
            elif self.input_mint == "مفتوح":
                #self.timer.stop()
                self.start_timer2()
                self.bt_set_Time.hide()
                self.lb_time_in.hide()
                self.lb_too.hide()
                
            else:
                pass
        else:
            pass

        ###################################
       
        #self.minutes = int(self.time_in)
        
        ##################
        
    def DS(self):
        
        ##################
        self.tootl = 0
        self.food = ""
        
        #.setStyleSheet(color)
        
        ############################
        self.color_bt = """
                    font-size: 17px;
                    font-family: 'Segoe UI', Semibold;
                """
    
        self.color = """
                background-color:#073763;
                color:#fff;
                font-size: 18px;
                font-family: 'Segoe UI', Semibold;
                text-align: center;
                border: 1px solid black;
                """    
        layout = QVBoxLayout()
        self.Lb_name_pc = QLabel(f"{self.name}")
        self.Lb_name_pc.setStyleSheet(self.color)
        self.Lb_name_pc.setAlignment(Qt.AlignCenter)
        #self.Lb_name_pc.setFont(QFont('Times New Roman', 20))

        #self.lb_start_time = QLabel(f"تم البدء: {self.start_time}")
        
        self.lb_time_mosthlk = QLabel("")
        self.lb_time_mosthlk.setAlignment(Qt.AlignCenter)
        self.lb_time_mosthlk.setStyleSheet(self.color)

        self.lb_tybe_pc = QLabel(f"نوع اللعب: {self.tybe_pc}")
        self.lb_tybe_pc.setAlignment(Qt.AlignCenter)
        self.lb_tybe_pc.setStyleSheet(self.color)

        self.lb_time_in = QLabel("")
        self.lb_time_in.setAlignment(Qt.AlignCenter)
        self.lb_time_in.setStyleSheet(self.color)

        

        #self.lb_add_time = QLabel("")
        self.lb_too = QLabel("")
        self.lb_too.setAlignment(Qt.AlignCenter)
        self.lb_too.setStyleSheet(self.color)

        #self.lb_1 = QLabel("********************")
        self.bt_end = QPushButton("إنهاء")
        self.bt_end.clicked.connect(self.exit)
        self.bt_end.setStyleSheet(self.color_bt)

        self.bt_add_food = QPushButton("أوردر")
        self.bt_add_food.clicked.connect(self.Add_food)
        self.bt_add_food.setStyleSheet(self.color_bt)

        self.bt_set_Time = QPushButton("إضافة وقت")
        self.bt_set_Time.clicked.connect(self.SET_TIME)
        self.bt_set_Time.setStyleSheet(self.color_bt)

       
        ###########################
        

        #for w in widgets:
            #layout.addWidget(w)

        layout.addWidget(self.Lb_name_pc)
        layout.addWidget(self.lb_tybe_pc)
        layout.addWidget(self.lb_time_mosthlk)
        
        layout.addWidget(self.lb_time_in)
       
        #layout.addWidget(self.lb_add_time)
        #layout.addWidget(self.lb_1)
        layout.addWidget(self.lb_too)

        layout.addWidget(self.bt_set_Time)
        layout.addWidget(self.bt_add_food)
        layout.addWidget(self.bt_end)

        




        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)






    ############################################
    #time
    def start_timer(self):
        print(">>>>>>>>>>>>>" + str(self.time_in) )
        self.minutes = int(self.time_in)

        self.remaining_time = int(self.minutes) * 60
        self.timer.start(1000)
            
        

    def update_timer(self):
        #جلب الساعات وضربها
        self.remaining_time -= 1
        self.format_time(self.remaining_time)        
        self.lb_time_in.setText(f"الوقت المتبقي: {str(self.format_time(self.remaining_time))}")
        if self.remaining_time <= 0:
            self.timer.stop()
            self.timer2.stop()
            #self.setStyleSheet("background:red")

        
            #self.lb_time_in.setText("انتهى الوقت!")
            self.exit()
            self.ADD_DATA_IN_DATABESE()
            self.close()
            #QMessageBox.information(self,"نفذ وقت الجهاز","")
    def format_time(self, seconds):
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02}:{secs:02}"
    ###########################################

















    ##########################################
    #time 2
    #time
    def start_timer2(self):
        try:
            #self.minutes = int(1)
            self.remaining_time2 = self.minutes2 * 60
            self.timer2.start(1000)
        except ValueError:
            #self.timer_label.setText("الرجاء إدخال رقم صحيح.")
            pass

    def update_timer2(self):
        #########
        self.remaining_time2 += 1
        self.format_time2(self.remaining_time2)
        self.lb_time_mosthlk.setText(f"الوقت المستهلك: {str(self.format_time2(self.remaining_time2))}")
        
        #if self.remaining_time <= 0:
            #self.timer.stop()
            #self.lb_tybe_pc.setText("انتهى الوقت!")
            

    def format_time2(self, seconds):
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02}:{secs:02}"
    

    ##########################################
    def exit(self):
        print("إنهاء")
        self.timer.stop()
        self.timer2.stop()
        #self.lb_time_in.setText("انتهى الوقت!")
        
        #self.close()
        
        ##################################
        #get info tybe in data
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        dd = cr.execute(f"select * from new_pc where name_pc = '{str(self.name)}'")
        for key, data in enumerate(dd):
            ##############
            pass
        fardy = int(data[4])
        zawgy = int(data[5])
        #####################
        #[جلب الوقت المسنهاك]
        ##########################
        test = str(self.lb_time_mosthlk.text())
        numbers = re.findall(r'\d+', test)
        self.time_get = int(numbers[0])
        #######################
        if str(self.tybe_pc) == "فردي":
            self.tootl += self.time_get * fardy
            print("tootl fardy: " + str(self.tootl))
            self.lb_too.show()
            self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")

        elif str(self.tybe_pc) == "زوجي":
            
            self.tootl += self.time_get * zawgy
            print("tootl zawgy: " + str(self.tootl))
            self.lb_too.show()
            self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")


        #########################
        text_info=f""""
        اسم الجهاز: {self.name}
        *******************
        وقت البدء: {self.start_time}
        *******************
        نوع اللعب: {self.tybe_pc}
        *******************
        الحاس الكلي: {str(self.tootl)}
        """
        QMessageBox.information(self,"إنهاء الفاتوره", text_info)
        ##########################
        #self.ADD_DATA_IN_DATABESE()
        
        
        self.close()

        
    def Add_food(self):
        print("اضافه اكل")

        listt = ["ادنومي","شاي","بيبسي"]
        item , ok = QInputDialog.getItem(self,"اضافه مشروبات","أدخل إسم المشروب",listt,0,False)
        if ok:
            self.food = str(str(item))
            print(item)


    def SET_TIME(self):
        
        print("اضافه وقت")
        
        num, ok = QInputDialog.getInt(self,"إضافه وقت","أدخل عدد الدقائق",60,True)
        if ok:
            print(f"[[[[ {num} {ok}]]]]")
            #print(self.minutes)
            try:
                self.time_in += num
                self.start_timer()
            except Exception as e:
                print(e)
            #self.start_timer()
        #self.update_timer()

            #print(get)
            #self.lb_time_in.setText("10")
            #self.time_get = int(numbers[0])
            
            
            
            #self.minutes += str(int(self.minutes) + int(num))
            #self.lb_time_in.setText(f"{str(num)}")


        #self.lb_add_time.setText(str(f"الوقت المضاف: {str(self.tootl)}"))
        #set tootl time
        #self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")
        
    
    def ADD_DATA_IN_DATABESE(self):
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #set time in var
        time_now= str(formatted_time)

        #add data in databise
        try:
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"""insert into start_pc(
            person,
            name_pc,
            total,
            type_pc,
            time,
            end_time,
            food) values(
            '{self.user_name}',
            '{self.name}',
            '{str(self.tootl)}',
            '{self.tybe_pc}',
            '{self.time_in}',
            '{str(time_now)}',
            '{self.food}') """)
            #######################
            db.commit()
            db.close()
            #
            print("Done The information has been successfully saved in the Database. ")

            #refresh window
            #self.close()
        except Exception as e:
            print(e)
        

    
##########################################################
    
            
###########################################################
###########################################################
































































#Ui_MainWindow
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        
        
        
        uic.loadUi('ui\\main_2.ui', self)

        
        


        self.user_name = ""
        #داله الازرار
        self.Button_DS()
        self.Pc_8_DS()
        #داله انشاء قاده البيانات
        self.create_all_db()
        #var Login
        self.time_start_user = ""
        self.var_time = 0

        self.DS_ALL()
        #set data in Login
        self.username.setText("admin")
        self.passwd.setText("admin")
        self.th_create_db()
        self.settings()
        self.hide_groupBox()
        self.show_data_settings()
        self.show_data_settings_billiaed()
        self.set_name_pc_in_combo()
        self.Live_time()
        self.deleted_items = []
        ########
        
        ########
        #self.cun: int = 0
        #self.gridLayout


        
        self.widg_DS()
        self.widg_Bil2()
        self.billiard_settings()
        self.DS_billiard_settings()
        self.food_settings()
        self.DS_food_settings()
       
        #self.setGeometry(100, 100, pixmap.width(), pixmap.height())

#############################################################
    def DS_ALL(self):

        self.lb_info_user = self.findChild(QLabel,"label")
        self.groupBox_main_window = self.findChild(QGroupBox,"groupBox_2")
        #self.groupBox_main_window.hide()
        #
        self.tabWidget = self.findChild(QTabWidget,"tabWidget")
        self.tabWidget.hide()
        #groupBox settings
        self.groupBox_settings = self.findChild(QGroupBox,"groupBox_4")
        #groupBox Login
        self.groupBox_Login = self.findChild(QGroupBox,"groupBox")
        
        self.box_add = self.findChild(QWidget,"groupBox_5")

        
        

        
        

        #self.gridLayout
        #layout.addWidget(self.widget_1,0,1)
        #layout.addWidget(self.widget_2,0,2)
        #layout.addWidget(self.widget_3,0,3)
        #self.setLayout(layout)

       

        






        #Combo Box
        self.list_name_pc = []
        self.comboBox_name = self.findChild(QComboBox,"comboBox_4")

        self.comboBox_time_1 = self.findChild(QComboBox,"comboBox_7")
        
        #self.comboBox_time.addItems(item)
        
        self.comboBox_type = self.findChild(QComboBox,"comboBox_6")

        #sttings
        self.name_pc = self.findChild(QLineEdit,"lineEdit_10")
        self.type_pc = self.findChild(QLineEdit,"lineEdit_11")
        self.price_fardy_pc = self.findChild(QLineEdit,"lineEdit_12")
        self.price_zawgy_pc = self.findChild(QLineEdit,"lineEdit_13")




        #widg login
        self.widget_login = self.findChild(QWidget,"widget_5")
        self.welcome_lb =  self.label_2
        self.widget_login.hide()
    
    #billiard
    #اعداادت البليارديو
    def billiard_settings(self):
        db3 = sqlite3.connect("app.db")
        db3.execute("""create table if not exists Billiard_sttings (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_pool_table Text,
                    price_matsh VARCHAR(10) DEFAULT 'Missed',
                    price_hour VARCHAR(10) DEFAULT 'Missed',
                    admin Text)
                    """)
        db3.close()

        self.list_name_billiard = []
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from Billiard_sttings order by id ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            self.list_name_billiard.append(str(data[1]))
        
        

            
        self.comboBox_10.addItems(self.list_name_billiard)
        self.comboBox_11.addItems(self.list_name_billiard)
        self.comboBox_9.addItems(self.list_name_billiard)

    #اعداادت البوفيه
    def food_settings(self):
        
        self.list_name_food = []
        db3 = sqlite3.connect("app.db")
        db3.execute("""create table if not exists food (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name Text,
                    price_sheraa VARCHAR(10) DEFAULT 'Missed',
                    price_pe3 VARCHAR(10) DEFAULT 'Missed',
                    El3dd VARCHAR(10) DEFAULT 'Missed',
                    admin Text)
                    """)
        db3.close()
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from food order by name ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            self.list_name_food.append(str(data[1]))

        self.comboBox_12.addItems(self.list_name_food)
        self.comboBox_13.addItems(self.list_name_food)


    def DS_food_settings(self):
        self.show_data_food()
        self.pushButton_29.clicked.connect(self.show_box_add_in_food)
        self.pushButton_31.clicked.connect(self.show_box_update_in_food)
        self.pushButton_30.clicked.connect(self.show_box_delete_in_food)
        ####
        self.pushButton_2.clicked.connect(self.add_name_in_food)
        self.pushButton_11.clicked.connect(self.update_name_in_food)
        self.pushButton_28.clicked.connect(self.delete_name_in_food)
        self.comboBox_12.activated.connect(self.setData_in_como_food)
        self.groupBox_17.show() #add
        self.groupBox_18.hide() #update
        self.groupBox_19.hide() #delete
    def show_box_add_in_food(self):
        self.groupBox_17.show() #add
        self.groupBox_18.hide() #update
        self.groupBox_19.hide() #delete
    def show_box_update_in_food(self):
        self.groupBox_17.hide() #add
        self.groupBox_18.show() #update
        self.groupBox_19.hide() #delete
    def show_box_delete_in_food(self):
        self.groupBox_17.hide() #add
        self.groupBox_18.hide() #update
        self.groupBox_19.show() #delete
    
    def add_name_in_food(self):
        if str(self.lineEdit_3.text()) != "" and str(self.lineEdit_4.text()) != "" and str(self.lineEdit_5.text()) != "" and str(self.lineEdit_6.text()) != "":
            #add in databise
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"""insert into food(
            name,
            price_sheraa,
            price_pe3,           
            El3dd,admin) values(
            '{str(self.lineEdit_3.text())}',
            '{str(self.lineEdit_5.text())}',
            '{str(self.lineEdit_6.text())}',
            '{str(self.lineEdit_4.text())}',
            '{str(self.user_name)}') """)
            #######################
            db.commit()
            db.close()
            #
            print("Done Add Data new ")
            QMessageBox.about(self,"تم الاضافه بنجاح","تم الاضافه  بنجاح")
            self.close()
            self.w3 = Ui()
            self.w3.show()
        else:
            QMessageBox.about(self,"الحقول فارغه"," الحقول فارغه")
    def update_name_in_food(self):
        print("Update")
        get_name_food = str(self.comboBox_12.currentText())
    
        #add in databise
        if str(self.lineEdit_24.text()) != "" and str(self.lineEdit_25.text()) != "" and str(self.lineEdit_23.text()) != "" and str(self.lineEdit_26.text()) != "":
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"update food set name = '{str(self.lineEdit_24.text())}' where name = '{get_name_food}'")
            cr.execute(f"update food set El3dd = '{str(self.lineEdit_25.text())}' where name = '{get_name_food}'")
            cr.execute(f"update food set price_sheraa = '{str(self.lineEdit_23.text())}' where name = '{get_name_food}'")
            cr.execute(f"update food set price_pe3 = '{str(self.lineEdit_26.text())}' where name = '{get_name_food}'")
            cr.execute(f"update food set admin = '{str(self.user_name)}' where name = '{str(get_name_food)}'")
            db.commit()
            db.close()

            
            QMessageBox.about(self,"التعديل","تم التعديل  بنجاح")
            self.close()
            self.wwq9 = Ui()
            self.wwq9.show()

        else:
            QMessageBox.about(self,"خطأ","الحقول فارغه")
    def delete_name_in_food(self):
        get_name_bil_food = str(self.comboBox_13.currentText())
        try:   
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            #self.edit_name_user
            cr.execute(f"delete from food where name = '{get_name_bil_food}' ")
            db.commit()
            db.close()
            QMessageBox.about(self,"تم الحذف","تم الحذف  بنجاح")
            
            self.close()
            self.wwr = Ui()
            self.wwr.show()
        except Exception:
            QMessageBox.critical(self,"خطا","خطا لم يتم الحذف")
    def setData_in_como_food(self):
        self.lineEdit_24.setText("") #name
        self.lineEdit_25.setText("") 
        self.lineEdit_23.setText("") 
        self.lineEdit_26.setText("") 
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute(f"select * from food where name = '{str(self.comboBox_12.currentText())}' ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            print(data)
        self.lineEdit_24.setText(data[1]) #name
        self.lineEdit_25.setText(data[4]) 
        self.lineEdit_23.setText(data[2]) 
        self.lineEdit_26.setText(data[3]) 


    def DS_billiard_settings(self):
        
        self.pushButton_23.clicked.connect(self.show_box_add_in_billiard)
        self.pushButton_25.clicked.connect(self.show_box_update_in_billiard)
        self.pushButton_12.clicked.connect(self.show_box_delete_in_billiard)
        self.pushButton_26.clicked.connect(self.add_name_in_billiard)
        self.pushButton_24.clicked.connect(self.update_name_in_billiard)
        self.pushButton_27.clicked.connect(self.delete_name_in_billiard)
        self.comboBox_10.activated.connect(self.setData_in_como)
        self.tash.clicked.connect(self.start_bile)
        
        #اخفاء البوكس
        self.groupBox_15.show()
        self.groupBox_14.hide()
        self.groupBox_16.hide()
    def show_box_add_in_billiard(self):
        print("Hi billiard")
        self.groupBox_15.show()
        self.groupBox_14.hide()
        self.groupBox_16.hide()

    def show_box_update_in_billiard(self):
        self.groupBox_14.show()
        self.groupBox_16.hide()
        self.groupBox_15.hide()

    def show_box_delete_in_billiard(self):
        self.groupBox_16.show()
        self.groupBox_15.hide()
        self.groupBox_14.hide()
    ###############################
    #اضافه و تحديث وحذف البيانات
    def add_name_in_billiard(self):
        if str(self.lineEdit_31.text()) != "" and str(self.lineEdit_32.text()) != "" and str(self.lineEdit_33.text()) != "":
            #add in databise
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"""insert into Billiard_sttings(
            name_pool_table,
            price_matsh,           
            price_hour,admin) values(
            '{str(self.lineEdit_31.text())}',
            '{str(self.lineEdit_32.text())}',
            '{str(self.lineEdit_33.text())}',
            '{str(self.user_name)}') """)
            #######################
            db.commit()
            db.close()
            #
            print("Done Add Data new ")
            QMessageBox.about(self,"تم الاضافه بنجاح","تم الاضافه  بنجاح")
            self.w3 = Ui()
            self.w3.show()
        else:
            QMessageBox.about(self,"الحقول فارغه"," الحقول فارغه")

        
    def update_name_in_billiard(self):
        print("Update")
        get_name_bil = str(self.comboBox_10.currentText())
    
        #add in databise
        if str(self.lineEdit_27.text()) != "" and str(self.lineEdit_28.text()) != "" and str(self.lineEdit_29.text()) != "":
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"update Billiard_sttings set name_pool_table = '{str(self.lineEdit_27.text())}' where name_pool_table = '{get_name_bil}'")
            cr.execute(f"update Billiard_sttings set price_matsh = '{str(self.lineEdit_28.text())}' where name_pool_table = '{get_name_bil}'")
            cr.execute(f"update Billiard_sttings set price_hour = '{str(self.lineEdit_29.text())}' where name_pool_table = '{get_name_bil}'")
            #cr.execute(f"update Billiard_sttings set admin = '{self.user_name}' where name_pool_table = '{get_name_bil}'")
            db.commit()
            db.close()

            
            QMessageBox.about(self,"التعديل","تم التعديل  بنجاح")
            self.close()
            self.wwq7 = Ui()
            self.wwq7.show()

        else:
            QMessageBox.about(self,"خطأ","الحقول فارغه")
        

        
        


    def delete_name_in_billiard(self):
        get_name_bil_dl = str(self.comboBox_11.currentText())
        try:   
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            #self.edit_name_user
            cr.execute(f"delete from Billiard_sttings where name_pool_table = '{get_name_bil_dl}' ")
            db.commit()
            db.close()
            QMessageBox.about(self,"تم الحذف","تم الحذف  بنجاح")
            
            self.close()
            self.wwr = Ui()
            self.wwr.show()
        except Exception:
            QMessageBox.critical(self,"خطا","خطا لم يتم الحذف")

    ##################################
    def setData_in_como(self):
        self.lineEdit_27.setText("") #name
        self.lineEdit_28.setText("") #price > matsh
        self.lineEdit_29.setText("") #price > hors
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute(f"select * from Billiard_sttings where name_pool_table = '{str(self.comboBox_10.currentText())}' ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            print(data)
        self.lineEdit_27.setText(data[1]) #name
        self.lineEdit_28.setText(data[2]) #price > matsh
        self.lineEdit_29.setText(data[3]) #price > hors
    def show_info_table_data(self):
        pass
    
    def widg_Bil2(self):
        self.scrollArea_2
        self.Grid2 = QGridLayout()
        
        self.home_Widget2 = QWidget()

        self.home_Widget2.setLayout(self.Grid2)
    def start_bile(self):
        print("START B")
        #get data in ui
        name_in_combo = str(self.comboBox_9.currentText())
        time_matsh = str(self.comboBox_8.currentText())
        if name_in_combo != "حدد الطاوله" and time_matsh != "حدد الوقت":
            #time_pc = str(self.comboBox_7.currentText())
            ##########################################
            #get time now
            dt = datetime.datetime.now()
            formatted_time = dt.strftime('%H:%M')
            #set time in var
            time_now= str(formatted_time)
            ###########################################
            if not "تحديد" in str(name_in_combo):
            
                
                self.Grid2.addWidget(BiLLiard(name_in_combo,time_matsh,self.user_name),0,self.Grid2.columnCount())
                print("count>"+str(self.Grid2.count()))
                #self.deleteItem()
            #else:
                #QMessageBox.critical(self,"خطأ","أدخل معلومات الجهاز المراد تشغيله")

            
            #######################################
            self.home_Widget2.setLayout(self.Grid2)
            self.scrollArea_2.setWidget(self.home_Widget2)
            # تمكين خاصية التمرير العمودي والأفقي
            self.scrollArea_2.setWidgetResizable(True)
        else:
            QMessageBox.critical(self,"خطأ","حدد الطاوله والوقت أولاً")



    #جميع الازرار هنا
    def Button_DS(self):
        #الاعدادات
        self.bt_stt = self.findChild(QPushButton,"pushButton_13")
        self.bt_stt.clicked.connect(self.test)
        ###
        
        #bt start user
        self.start_user_bt = self.findChild(QPushButton,"pushButton_8")
        self.start_user_bt.clicked.connect(self.start_user)
        ####
        self.exit_bt = self.findChild(QPushButton,"pushButton_3")
        self.exit_bt.clicked.connect(self.exit_user)
        #bt login
        self.seve_bt_1 = self.findChild(QPushButton,"pushButton_17")
        self.seve_bt_1.clicked.connect(self.Login_user)

        #bt login sittings
        self.bt_add_pc = self.findChild(QPushButton,"add")
        self.bt_edit_pc = self.findChild(QPushButton,"edit")
        self.bt_delete_pc = self.findChild(QPushButton,"delete_2")
        self.save_data_pc = self.findChild(QPushButton,"pushButton")



        self.update_7 = self.findChild(QPushButton,"update")
        #self.pushButton_14 = self.findChild(QPushButton,"pushButton_14")
        #self.update_7.clicked.connect(self.test_1)

        self.save_data_pc.clicked.connect(self.save_data)

        self.bt_add_pc.clicked.connect(self.show_widget_add_pc)
        self.bt_edit_pc.clicked.connect(self.show_widget_update_pc)
        self.bt_delete_pc.clicked.connect(self.show_widget_delete_pc)
        #############
        #home
        self.bt_home = self.findChild(QPushButton,"pushButton_14")
        self.bt_1 = self.findChild(QPushButton,"pushButton_15")
        self.bt_2 = self.findChild(QPushButton,"pushButton_16")
        self.bt_4 = self.findChild(QPushButton,"pushButton_21")
        self.bt_5 =self.findChild(QPushButton,"pushButton_22")
        
        

        self.bt_home.clicked.connect(self.Go_home)
        self.bt_1.clicked.connect(self.Go_start)
        self.bt_2.clicked.connect(self.Go_billiard)
        self.bt_4.clicked.connect(self.Go_register)
        self.bt_5.clicked.connect(self.Go_Settings)
        
        self.pushButton_19.clicked.connect(self.delete_name_pc)



        self.tabWidget.tabBar().setVisible(False)
        self.widget_add = self.findChild(QWidget,"widget")

        #######################################

        self.pushButton_18.clicked.connect(self.updata_settings_data_name_pc)
        self.comboBox.activated.connect(self.setDataUpdate_pc)
        



    #داله ال8 اجهزة هنا
    def Pc_8_DS(self):
        #[جهاز رقم 1]
        self.lb_name_pc = self.findChild(QLabel,"label_6")
        self.lb_time_pc = self.findChild(QLabel,"label_12")
        self.lb_type_pc = self.findChild(QLabel,"label_13")
        self.lb_time_motabky = self.findChild(QLabel,"label_15")
        #Login
        self.username = self.findChild(QLineEdit,"lineEdit")
        self.passwd = self.findChild(QLineEdit,"lineEdit_2")


    #show widg add new pc
    def show_widget_add_pc(self):
        print("add")
        self.groupBox_3.hide()
        self.groupBox_4.hide()
        self.groupBox.show()

    # show widg update pc
    def show_widget_update_pc(self):
        list_name_combo = []
        try:
            
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute("select * from new_pc order by id ")
            datas = cr.fetchall()
            for key, data in enumerate(datas):
                list_name_combo.append(str(data[2]))
            
            
            
            #list_name_combo.addItems(self.comboBox)
            unique_items = list(set(list_name_combo))  # تحويل القائمة إلى مجموعة ثم إلى قائمة لإزالة التكرار
            for item in unique_items:
                self.comboBox.addItem(item)



        except Exception as e:
            print(e)
        
        print("update")
        self.groupBox.hide()
        self.groupBox_4.hide()
        self.groupBox_3.show()

    # show widg delete pc
    def show_widget_delete_pc(self):
        #comboBox_2
        list_name = []
        #set data in combo box name
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from new_pc order by id ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            #print(data)
            list_name.append(data[2])
            #print("نواع: "+str(data[4] + str(data[5])))
        #set data in combo
        self.comboBox_2.addItems(list_name)
        # إزالة العناصر المكررة
        unique_items = []
        for index in range(self.comboBox_2.count()):
            item_text = self.comboBox_2.itemText(index)
            if item_text not in unique_items:
                unique_items.append(item_text)

        self.comboBox_2.clear()
        self.comboBox_2.addItems(unique_items)



        print("Delete")
        self.groupBox.hide()
        self.groupBox_3.hide()
        self.groupBox_4.show()


    #hide groupBox
    def hide_groupBox(self):
        self.groupBox.hide()
        self.groupBox_3.hide()
        self.groupBox_4.hide()


    def Login_user(self):


        self.widget_login.show()
        self.user_name = self.username.text()

        #set user in lb
        self.welcome_lb.setText(f"مرحبًا,{self.user_name}")

        print(self.user_name)
        #set time
        import datetime
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #cr.execute(f"insert into user(name,time) values('{str(self.username.text())}','{str(formatted_time)}' ) ")
        #db.commit()
        #db.close()
        if self.user_name != "":

            self.groupBox_main_window.hide()








    def settings(self):
        self.table = self.widget_stt
        self.table.setRowCount(6)
        ###########################
        self.table_bl = self.widget_stt_2
        self.table_bl.setRowCount(6)

        self.table_food = self.tableWidget_3
        self.table_food.setRowCount(6)
        
        
        


    def setDataUpdate_pc(self):
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        dd = cr.execute(f"select * from new_pc where name_pc = '{str(self.comboBox.currentText())}'")
        for key, data in enumerate(dd):
            ##############
            pass
        self.lineEdit_18.setText(str(data[2]))
        self.lineEdit_15.setText(str(data[3]))
        self.lineEdit_16.setText(str(data[4]))
        self.lineEdit_17.setText(str(data[5]))



    def set_name_pc_in_combo(self):
        list_name = []
        #set data in combo box name
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from new_pc order by id ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            #print(data)
            list_name.append(data[2])
            #print("نواع: "+str(data[4] + str(data[5])))
        #set data in combo
        self.comboBox_name.addItems(list_name)###
        ############################################



        #set data in combo box tybe
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        dd = cr.execute(f"select * from new_pc where name_pc = '{str(self.comboBox_name.currentText())}'")
        for key, data in enumerate(dd):
            ##############

            print(f"Fardy: {str(data[4])} Zawgy: {str(data[5])}")


    def updata_settings_data_name_pc(self):
        if str(self.lineEdit_18.text()) != "" and str(self.lineEdit_15.text()) != "" and str(self.lineEdit_16.text()) != "" and str(self.lineEdit_17.text()) != "":
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"update new_pc set name_pc = '{str(self.lineEdit_18.text())}' where name_pc = '{str(self.comboBox.currentText())}'")
            cr.execute(f"update new_pc set type_pc = '{self.lineEdit_15.text()}' where name_pc = '{str(self.comboBox.currentText())}'")
            cr.execute(f"update new_pc set price_hour_person1 = '{self.lineEdit_16.text()}' where name_pc = '{str(self.comboBox.currentText())}'")
            cr.execute(f"update new_pc set price_hour_person2 = '{self.lineEdit_17.text()}' where name_pc = '{str(self.comboBox.currentText())}'")
        
            db.commit()
            db.close()
            self.close()
            self.ws6 = Ui()
            self.ws6.show()
            QMessageBox.information(self,"تم تحديث البيانات","تم تحديث البيانات الان يمكنك مشاهدة البيانات الجديدة")
            #self.show_data_settings()

        
        else:
            QMessageBox.information(self,"خطأ","ليس هناك بيانات ليتم تعديلها حدد أولاً الصنف المراد تحديثه")




    def delete_name_pc(self):
        try:
            
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            #self.edit_name_user
            cr.execute(f"delete from new_pc where name_pc = '{str(self.comboBox_2.currentText())}' ")
            
            db.commit()
            db.close()
            QMessageBox.about(self,"تم الحذف","تم الحذف  بنجاح")
        
            
        except Exception:
            QMessageBox.critical(self,"خطا","خطا لم يتم الحذف")

    def show_data_settings(self):
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from new_pc order by id DESC")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            self.table.setRowCount(key+1)
            #print(data)
            self.table.setItem(key, 0, QTableWidgetItem(str(data[2])))
            self.table.setItem(key, 1, QTableWidgetItem(str(data[3])))
            self.table.setItem(key, 2, QTableWidgetItem(str(data[4])))
            self.table.setItem(key, 3, QTableWidgetItem(str(data[5])))
            self.table.setItem(key, 4, QTableWidgetItem(str(data[1])))

    def show_data_settings_billiaed(self):
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from Billiard_sttings order by id DESC")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            self.table_bl.setRowCount(key+1)
            #print(data)
            self.table_bl.setItem(key, 0, QTableWidgetItem(str(data[1])))
            self.table_bl.setItem(key, 1, QTableWidgetItem(str(data[3])))
            self.table_bl.setItem(key, 2, QTableWidgetItem(str(data[2])))
            self.table_bl.setItem(key, 3, QTableWidgetItem(str(data[4])))
            #self.table.setItem(key, 4, QTableWidgetItem(str(data[1])))


    def show_data_food(self):
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from food order by id DESC")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            self.table_food.setRowCount(key+1)
            #print(data)
            self.table_food.setItem(key, 0, QTableWidgetItem(str(data[1])))
            self.table_food.setItem(key, 1, QTableWidgetItem(str(data[4])))
            self.table_food.setItem(key, 2, QTableWidgetItem(str(data[2])))
            self.table_food.setItem(key, 3, QTableWidgetItem(str(data[3])))
            self.table_food.setItem(key, 4, QTableWidgetItem(str(data[0])))

    def create_db_sttings(self):
        db1 = sqlite3.connect("app.db")
        db1.execute("""create table if not exists new_pc (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person VARCHAR(10) DEFAULT 'Missed',
                    name_pc Text,
                    type_pc VARCHAR(10) DEFAULT 'Missed',
                    price_hour_person1 Text,
                    price_hour_person2 Text)
                    """)
        db1.close()
        # [جدول القفل والفتح فقط]
        db2 = sqlite3.connect("app.db")
        db2.execute("""create table if not exists start_pc (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person VARCHAR(10) DEFAULT 'Missed',
                    name_pc Text,
                    total Text,
                    type_pc VARCHAR(10) DEFAULT 'Missed',
                    time Text,
                    end_time,
                    food VARCHAR(10) DEFAULT 'Missed')
                    """)
        db2.close()


        


    def th_create_db(self):
        th = Thread(target=self.create_db_sttings)
        th.start()


    def widg_DS(self):
        self.scrollArea = self.scrollArea
        self.Grid = QGridLayout()
        
        self.home_Widget = QWidget()

        self.home_Widget.setWindowTitle("PyQt5")
        self.home_Widget.setLayout(self.Grid)



    def test(self):
        #get data in ui
        get_name_in_combo = str(self.comboBox_name.currentText())
        get_Index_in_combo = str(self.comboBox_name.currentIndex())
        name_pc = str(get_name_in_combo)
        tybe_pc = str(self.comboBox_type.currentText())
        time_pc = str(self.comboBox_7.currentText())
        ##########################################
        #get time now
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #set time in var
        time_now= str(formatted_time)
        ###########################################
        if not "تحديد" in str(get_name_in_combo) and time_pc != "الوقت" and tybe_pc != "نوع اللعب":
        
            print(f"index > {get_Index_in_combo}")
            self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
            print("count>"+str(self.Grid.count()))
            self.deleteItem()
        else:
            QMessageBox.critical(self,"خطأ","أدخل معلومات الجهاز المراد تشغيله")

        
        #######################################
        self.home_Widget.setLayout(self.Grid)
        self.scrollArea.setWidget(self.home_Widget)
        # تمكين خاصية التمرير العمودي والأفقي
        self.scrollArea.setWidgetResizable(True)

        
    
    def deleteItem(self):
        # احذف العنصر المحدد من QComboBox وأضفه إلى القائمة المحذوفة
        current_index = self.comboBox_name.currentIndex()
        if current_index >= 0:
            deleted_item = self.comboBox_name.itemText(current_index)
            self.deleted_items.append(deleted_item)
            self.comboBox_name.removeItem(current_index)
    def recoverItem(self):
        # استرجاع العناصر المحذوفة من القائمة وإضافتها مرة أخرى إلى QComboBox
        if self.deleted_items:
            recovered_item = self.deleted_items.pop()
            self.comboBox_name.addItem(recovered_item)
        


      
        
    def get_data_2(self):
        y = self.ui.lineEdit.text()
        self.label_4.setText(y)




        



    def Go_home(self):
        self.tabWidget.setCurrentIndex(0)
    def Go_start(self):
        self.tabWidget.setCurrentIndex(1)
    def Go_billiard(self):
        self.tabWidget.setCurrentIndex(2)
    
    def Go_register(self):
        self.tabWidget.setCurrentIndex(3)
    def Go_Settings(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(0)

    ##################################################
    def test_1(self):
        

        try:
            print("TEST")
            self.recoverItem()
            print(self.Grid.columnCount())
            #self.comboBox_name()
            self.set_name_pc_in_combo()
        except Exception:
            pass

    def update_countdown(self):
        self.time_left = self.time_left.addSecs(-1)  # تحديث الوقت المتبقي
        self.label.setText(self.time_left.toString())

        if self.time_left == QTime(0, 0):
            self.countdown1.stop()
            self.label.setText("انتهى الوقت!")
            #pygame.init()
            #pygame.mixer.music.load("end_1.mp3")  # قم بتعديل المسار إلى ملف الصوت الخاص بك
            #pygame.mixer.music.play()


    def Live_time(self):
        # creating a timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)


    def showTime(self):
        #font = QFont('Arial', 20, QFont.Bold)
        #self.label_3.setFont(font)

        # getting current time
        current_time = QTime.currentTime()
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        # showing it to the label
        self.label_3.setText(f"الساعه الان: {label_time}")

        
    
    def start_user(self):
        self.tabWidget.show()
        self.widget_login.hide()
        self.tabWidget.setCurrentIndex(0)

        #hi

        print("Hi, " + self.user_name)
        #get time
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')

        #set time in var
        self.time_start_user = str(formatted_time)
        self.lb_info_user.setText(f"مرحبًا يـ {self.user_name} , تم بدء الوردية الساعه: {self.time_start_user}")

        #self.start_user_bt.hide()
        #self.box_add.show()


    #set Data in var

    def exit_user(self):
        print(f"log out: {self.user_name}")
        self.name_user = ""


        self.tabWidget.hide()
        self.widget_5.hide()

        # show Login window
        self.groupBox_2.show()


        #clear bt data
        self.username.setText("admin")
        self.passwd.setText("admin")

    def create_all_db(self):
        db1 = sqlite3.connect("app.db")
        db1.execute("create table if not exists user (id INTEGER PRIMARY KEY AUTOINCREMENT,name Text,time VARCHAR(10) DEFAULT 'Missed' )")
        #db1.commit()
        db1.close()
        ####
        #الاصناف
        #db2 = sqlite3.connect("db\\new_data.db")
        #db2.execute("create table if not exists product_new (id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(20) DEFAULT 'Missed', parcode_defolt integer,parcode integer(20) DEFAULT 'Missed',eladd VARCHAR(20) DEFAULT 'Missed',price VARCHAR(20) DEFAULT 'Missed',date_now VARCHAR(20) DEFAULT 'Missed')")
        #db2.commit()
        #db2.close()
        #############
        #داتا البيع
        #db3 = sqlite3.connect("db\\info_day.db")
        #db3.execute("create table if not exists product (id INTEGER PRIMARY KEY AUTOINCREMENT,name Text, price integer,el3dd Text,time Text,date_now Text)")
        #db2.commit()
        #db3.close()

###########################################################
###########################################################


    def save_data(self):
        name_pc = str(self.name_pc.text())
        type_pc = str(self.type_pc.text())
        price_fardy_pc = str(self.price_fardy_pc.text())
        price_zawgy_pc = str(self.price_zawgy_pc.text())
        if name_pc != "" and type_pc != "" and price_fardy_pc != "" and price_zawgy_pc != "":
            try:
                # add Data in connect
                db = sqlite3.connect("app.db")
                cr = db.cursor()
                cr.execute(f"""insert into new_pc(
                person,
                name_pc,
                type_pc,
                price_hour_person1,
                price_hour_person2) values(
                '{self.user_name}',
                '{name_pc}',
                '{type_pc}',
                '{price_fardy_pc}',
                '{price_zawgy_pc}') """)
                #######################
                db.commit()
                db.close()
                #
                print("Don Data new pc ")

                #refresh window
                self.close()
                w = self.show()
                self.show_data_settings()

            except Exception as e:
                print(e)
        else:
            QMessageBox.information(self,"الحقول فارقه","أدخل البيانات أولاً")

############################################################
    






























































































class BiLLiard(QMainWindow):
    def __init__(self,name_in_combo,time_matsh,user_name) -> None:
        super(BiLLiard, self).__init__()
        self.name = name_in_combo
        self.time_matsh = time_matsh
        self.user_name = user_name
        self.totl_match = 1
        ##########################
        self.DS()
        self.info_data_time_match()
        
    def DS(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        ########################
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_timer2)
        ########################
        ##################
        self.tootl = 0
        self.food = ""
        #self.name = "Mohamed"
        #.setStyleSheet(color)
        
        ############################
        self.color_bt = """
                    font-size: 17px;
                    font-family: 'Segoe UI', Semibold;
                """
        self.color = """
                background-color:#1778f2;
                color:#fff;
                font-size: 20px;
                font-family: 'Segoe UI', Semibold;
                text-align: center;

                """    
        layout = QVBoxLayout()
        self.Lb_name_pc = QLabel(f"{self.name}")
        self.Lb_name_pc.setStyleSheet(self.color)
        self.Lb_name_pc.setAlignment(Qt.AlignCenter)
        #self.Lb_name_pc.setFont(QFont('Times New Roman', 20))

        #self.lb_start_time = QLabel(f"تم البدء: {self.start_time}")
        
        self.lb_time_mosthlk = QLabel("")
        self.lb_time_mosthlk.setAlignment(Qt.AlignCenter)
        self.lb_time_mosthlk.setStyleSheet(self.color)

        #self.lb_tybe_pc = QLabel(f"نوع اللعب: {self.tybe_pc}")
        #self.lb_tybe_pc.setAlignment(Qt.AlignCenter)
        #self.lb_tybe_pc.setStyleSheet(self.color)

        self.lb_time_in = QLabel("")
        self.lb_time_in.setAlignment(Qt.AlignCenter)
        self.lb_time_in.setStyleSheet(self.color)

        

        #self.lb_add_time = QLabel("")
        #self.lb_too = QLabel("")
        #self.lb_too.setAlignment(Qt.AlignCenter)
        #self.lb_too.setStyleSheet(self.color)

        #self.lb_1 = QLabel("********************")
        self.bt_end = QPushButton("إنهاء")
        self.bt_end.clicked.connect(self.exit)
        self.bt_end.setStyleSheet("background-color:#A60101;font-family: 'Segoe UI', Semibold;font-size: 17px;")


        self.bt_add_food = QPushButton("مشروبات")
        self.bt_add_food.clicked.connect(self.Add_food)
        self.bt_add_food.setStyleSheet(self.color_bt)
        self.bt_add_food.setStyleSheet("background-color:#426e8f;font-family: 'Segoe UI', Semibold;font-size: 17px;")

        self.bt_set_Time = QPushButton("إضافة وقت")
        self.bt_set_Time.clicked.connect(self.SET_TIME)
        #self.bt_set_Time.setStyleSheet(self.color_bt)
        self.bt_set_Time.setStyleSheet("background-color:#08ad08;font-family: 'Segoe UI', Semibold;font-size: 17px;")

        ###########################
        

        #for w in widgets:
            #layout.addWidget(w)

        layout.addWidget(self.Lb_name_pc)
        #layout.addWidget(self.lb_tybe_pc)
        layout.addWidget(self.lb_time_mosthlk)
        
        layout.addWidget(self.lb_time_in)
       
        #layout.addWidget(self.lb_add_time)
        #layout.addWidget(self.lb_1)
        #layout.addWidget(self.lb_too)

        layout.addWidget(self.bt_set_Time)
        layout.addWidget(self.bt_add_food)
        layout.addWidget(self.bt_end)

        




        self.widget = QWidget()
        self.widget.setLayout(layout)
        #self.widget.setStyleSheet("background:#000")
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(self.widget)
        
    def info_data_time_match(self):
        self.time_m = 0
        self.time_hour =  0
        #set data in combo box tybe
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        dd = cr.execute(f"select * from Billiard_sttings where name_pool_table = '{str(self.name)}'")
        
        for key, data in enumerate(dd):
            ##############
            self.time_hour += int(data[3]) #Hour 
            self.time_m    += int(data[2]) #Hour match


        
        if self.time_matsh == str("بالوقت"):
            self.minutes =  60 #self.time_hour
            self.start_timer()
            self.start_timer2()

        if self.time_matsh == str("بالمباراه"):
            print("بالوقت")
            self.bt_set_Time.setText("اضافه مباراة")
            self.lb_time_in.setText(f"عدد المباريات حتي الان [ {self.totl_match} ]")
            self.start_timer2()
            
        
    ############################################
    #time
    def start_timer(self):
        #print(">>>>>>>>>>>>>" + str(self.time_in) )
        #self.time_matsh = 10
        #self.minutes = int(time)

        self.remaining_time = int(self.minutes) * 60
        self.timer.start(1000)
    def update_timer(self):
        #جلب الساعات وضربها
        self.remaining_time -= 1
        self.format_time(self.remaining_time)        
        self.lb_time_in.setText(f"الوقت المتبقي: {str(self.format_time(self.remaining_time))}")
        if self.remaining_time <= 0:
            self.timer.stop()
            self.timer2.stop()
            #self.setStyleSheet("background:red")

        
            #self.lb_time_in.setText("انتهى الوقت!")
            self.exit()
            #self.ADD_DATA_IN_DATABESE()
            #self.close()
            #QMessageBox.information(self,"نفذ وقت الجهاز","")
    def format_time(self, seconds):
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02}:{secs:02}"
    ###########################################

    ##########################################
    #time 2
    #time
    def start_timer2(self):
        try:
            self.minutes2 = 0
            self.remaining_time2 = self.minutes2 * 60
            self.timer2.start(1000)
        except ValueError:
            #self.timer_label.setText("الرجاء إدخال رقم صحيح.")
            pass

    def update_timer2(self):
        #########
        self.remaining_time2 += 1
        self.format_time2(self.remaining_time2)
        self.lb_time_mosthlk.setText(f"الوقت المستهلك: {str(self.format_time2(self.remaining_time2))}")
        
        #if self.remaining_time <= 0:
            #self.timer.stop()
            #self.lb_tybe_pc.setText("انتهى الوقت!")
            

    def format_time2(self, seconds):
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02}:{secs:02}"
    
    
    ##########################################
    def exit(self):
        print("إنهاء")
        self.timer.stop()
        self.timer2.stop()

        if self.time_matsh == str("بالمباراه"):
            price_match = 0
            price_hour = 0
            print("بالمباراه")
    
            self.lb_time_in.setText(f"  إجمالي عدد المباريات هو [ {self.totl_match} ]")                     
            print(self.time_hour , self.time_m)
            ##################################
            #get info tybe in data
            text_info=f""""
            اسم الجهاز: {self.name}
            *******************

            *******************
            الحاسب الكلي: {str(int(self.totl_match) *  int(self.time_m))}
            """
            QMessageBox.information(self,"إنهاء الفاتوره", text_info)
            ##########################
        
        if self.time_matsh == str("بالوقت"):
            test = str(self.lb_time_mosthlk.text())
            numbers = re.findall(r'\d+', test)
            self.time_get = int(numbers[0])
            print(f"Time End : {str(self.time_get)}")
            ########################################
            #self.lb_time_in.show()
            #self.lb_time_in.setText(f" : إجمالي عدد الدقائق هو [ {self.totl_match} ]")                     
            text_info=f""""
            اسم الجهاز: {self.name}
            *******************

            *******************
            الحاسب الكلي: {str(int(self.time_get) *  int(self.time_hour))}
            """
            QMessageBox.information(self,"إنهاء الفاتوره", text_info)
            ##########################

        '''
        test = str(self.lb_time_mosthlk.text())
        numbers = re.findall(r'\d+', test)
        self.time_get = int(numbers[0])
        #######################
        if str(self.tybe_pc) == "فردي":
            self.tootl += self.time_get * fardy
            print("tootl fardy: " + str(self.tootl))
            self.lb_too.show()
            self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")

        elif str(self.tybe_pc) == "زوجي":
            
            self.tootl += self.time_get * zawgy
            print("tootl zawgy: " + str(self.tootl))
            self.lb_too.show()
            self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")


        #########################
        text_info=f""""
        اسم الجهاز: {self.name}
        *******************
        وقت البدء: {self.start_time}
        *******************
        نوع اللعب: {self.tybe_pc}
        *******************
        الحاس الكلي: {str(self.tootl)}
        """
        QMessageBox.information(self,"إنهاء الفاتوره", text_info)
        ##########################
        #self.ADD_DATA_IN_DATABESE()
        
        
        self.close()
        '''
        
    def Add_food(self):
        print("اضافه اكل")

        listt = ["ادنومي","شاي","بيبسي"]
        item , ok = QInputDialog.getItem(self,"اضافه مشروبات","أدخل إسم المشروب",listt,0,False)
        if ok:
            self.food = str(str(item))
            print(item)


    def SET_TIME(self):
        
        if self.time_matsh != "بالمباراه":        
            num, ok = QInputDialog.getInt(self,"إضافه وقت","أدخل عدد الدقائق",60,True)
            if ok:
                print(f"[[[[ {num} {ok}]]]]")
                #print(self.minutes)
                try:
                    self.minutes += num
                    self.start_timer()
                    self.start_timer2()
                    
                except Exception as e:
                    print(e)
                #self.start_timer()
            #self.update_timer()

                #print(get)
                #self.lb_time_in.setText("10")
                #self.time_get = int(numbers[0])
                
                
                
                #self.minutes += str(int(self.minutes) + int(num))
                #self.lb_time_in.setText(f"{str(num)}")


            #self.lb_add_time.setText(str(f"الوقت المضاف: {str(self.tootl)}"))
            #set tootl time
            #self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")
        else:
            num, ok = QInputDialog.getInt(self,"إضافه مباراه","أدخل العدد ",1,False)
            if ok:
                self.totl_match += num
                print(self.totl_match)
                self.lb_time_in.show()
                self.lb_time_in.setText(f"عدد المباريات حتي الان [ {self.totl_match} ]")
                #print(self.minutes)
                #try:
                    #self.time_in += num
                    #self.start_timer()
                #except Exception as e:
                    #print(e)
    '''
    def ADD_DATA_IN_DATABESE(self):
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #set time in var
        time_now= str(formatted_time)

        #add data in databise
        try:
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"""insert into start_pc(
            person,
            name_pc,
            total,
            type_pc,
            time,
            end_time,
            food) values(
            '{self.user_name}',
            '{self.name}',
            '{str(self.tootl)}',
            '{self.tybe_pc}',
            '{self.time_in}',
            '{str(time_now)}',
            '{self.food}') """)
            #######################
            db.commit()
            db.close()
            #
            print("Done The information has been successfully saved in the Database. ")

            #refresh window
            #self.close()
        except Exception as e:
            print(e)
'''
####################################################################



app = QtWidgets.QApplication(sys.argv)
#app.setStyleSheet(stylesheet)
window = Ui()
window.show()
app.exec_()

