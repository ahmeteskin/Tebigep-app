import sys
from PyQt5.QtWidgets import *
from tebigep_py import *
import sqlite3
from datetime import date
import matplotlib.pyplot as plt
from sayac import sayacWindow_tyt, sayacWindow_ayt


uygulama = QApplication(sys.argv)
pencere = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()
#saat.pencere2.show()
window_tyt = sayacWindow_tyt()
window_ayt = sayacWindow_ayt()


# Veritabanı işlemleri


baglanti_tyt = sqlite3.connect("tebigep_tyt.db")
islem_tyt = baglanti_tyt.cursor()

table_tyt = islem_tyt.execute("CREATE TABLE IF NOT EXISTS Tebigep_tyt (tytNet FLOAT)")

baglanti_ayt = sqlite3.connect("tebigep_ayt.db")
islem_ayt = baglanti_ayt.cursor()
baglanti_ayt.commit()

table_ayt = islem_ayt.execute("CREATE TABLE IF NOT EXISTS Tebigep_ayt (aytNet FLOAT)")
baglanti_ayt.commit()

s = sqlite3.connect("calisma_programi.db")
c = s.cursor()

#c.execute("DROP TABLE IF EXISTS cp")
c.execute("""CREATE TABLE IF NOT EXISTS cp(
pzt TEXT,
sal TEXT,
crs TEXT,
per TEXT,
cum TEXT,
cmt TEXT,
paz TEXT)""")
s.commit()

ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
sor = "select * from cp"
c.execute(sor)

for indexSatir, kayitNumarasi in enumerate(c):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))



# netler

def net_hesapla_tyt_trk():
    tyt_trk_d = ui.lineEdit.text()
    tyt_trk_y = ui.lineEdit_2.text()
    tyt_trk_b = ui.lineEdit_3.text()
    tyt_trk_d_int = int(tyt_trk_d)
    tyt_trk_y_int = int(tyt_trk_y)

    tyt_net_trk = tyt_trk_d_int - tyt_trk_y_int/4
    ui.lineEdit_16.setText(str(tyt_net_trk))

def net_hesapla_tyt_mat():

    tyt_mat_d = (ui.lineEdit_6.text())
    tyt_mat_y = (ui.lineEdit_4.text())
    tyt_mat_b = (ui.lineEdit_5.text())
    tyt_mat_d_int = int(tyt_mat_d)
    tyt_mat_y_int = int(tyt_mat_y)

    tyt_net_mat = float(tyt_mat_d_int - tyt_mat_y_int/4)
    ui.lineEdit_15.setText(str(tyt_net_mat))

def net_hesapla_tyt_sos():
    
    tyt_sos_d = int(ui.lineEdit_7.text())
    tyt_sos_y = int(ui.lineEdit_8.text())
    tyt_sos_b = int(ui.lineEdit_9.text())

    tyt_sos_d_int = int(tyt_sos_d)
    tyt_sos_y_int = int(tyt_sos_y)

    tyt_net_sos = float(tyt_sos_d_int - tyt_sos_y_int/4)
    ui.lineEdit_13.setText(str(tyt_net_sos))

def net_hesapla_tyt_fen():

    tyt_fen_d = int(ui.lineEdit_12.text())
    tyt_fen_y = int(ui.lineEdit_10.text())
    tyt_fen_b = int(ui.lineEdit_11.text())

    tyt_fen_d_int = int(tyt_fen_d)
    tyt_fen_y_int = int(tyt_fen_y)

    tyt_net_fen = float(tyt_fen_d_int - tyt_fen_y_int/4)
    ui.lineEdit_14.setText(str(tyt_net_fen)) 

def tyt_net_yaz():
    ayt_trk_net = float(ui.lineEdit_16.text())
    ayt_mat_net = float(ui.lineEdit_15.text())
    ayt_sos_net = float(ui.lineEdit_13.text())
    ayt_fen_net = float(ui.lineEdit_14.text())

    tyt_net = ayt_trk_net + ayt_mat_net + ayt_sos_net + ayt_fen_net
    ui.lineEdit_34.setText(str(tyt_net))
    kayit_ekle_tyt(tyt_net)
    

def net_hesapla_ayt_trk():
    ayt_trk_d = ui.lineEdit_22.text()
    ayt_trk_y = ui.lineEdit_17.text()
    ayt_trk_b = ui.lineEdit_18.text()
    ayt_trk_d_int = int(ayt_trk_d)
    ayt_trk_y_int = int(ayt_trk_y)

    ayt_net_trk = ayt_trk_d_int - ayt_trk_y_int/4
    ui.lineEdit_19.setText(str(ayt_net_trk))

def net_hesapla_ayt_mat():

    ayt_mat_d = (ui.lineEdit_25.text())
    ayt_mat_y = (ui.lineEdit_30.text())
    ayt_mat_b = (ui.lineEdit_32.text())
    ayt_mat_d_int = int(ayt_mat_d)
    ayt_mat_y_int = int(ayt_mat_y)

    ayt_net_mat = float(ayt_mat_d_int - ayt_mat_y_int/4)
    ui.lineEdit_21.setText(str(ayt_net_mat))

def net_hesapla_ayt_sos():
    
    ayt_sos_d = int(ui.lineEdit_26.text())
    ayt_sos_y = int(ui.lineEdit_29.text())
    ayt_sos_b = int(ui.lineEdit_27.text())

    ayt_sos_d_int = int(ayt_sos_d)
    ayt_sos_y_int = int(ayt_sos_y)

    ayt_net_sos = float(ayt_sos_d_int - ayt_sos_y_int/4)
    ui.lineEdit_31.setText(str(ayt_net_sos))

def net_hesapla_ayt_fen():

    ayt_fen_d = int(ui.lineEdit_28.text())
    ayt_fen_y = int(ui.lineEdit_20.text())
    ayt_fen_b = int(ui.lineEdit_23.text())

    ayt_fen_d_int = int(ayt_fen_d)
    ayt_fen_y_int = int(ayt_fen_y)

    ayt_net_fen = float(ayt_fen_d_int - ayt_fen_y_int/4)
    ui.lineEdit_24.setText(str(ayt_net_fen)) 
    
def ayt_net_yaz():
    ayt_trk_net = float(ui.lineEdit_19.text())
    ayt_mat_net = float(ui.lineEdit_21.text())
    ayt_sos_net = float(ui.lineEdit_31.text())
    ayt_fen_net = float(ui.lineEdit_24.text())

    ayt_net = ayt_trk_net + ayt_mat_net + ayt_sos_net + ayt_fen_net
    ui.lineEdit_33.setText(str(ayt_net))
    kayit_ekle_ayt(ayt_net)
    #baglanti_ayt.commit()
    

def kayit_ekle_tyt(tyt_net):
    
    ekle = "insert into Tebigep_tyt (tytNet) values (?)"
    islem_tyt.execute(ekle,(tyt_net,))
   
    baglanti_tyt.commit()
    ui.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı",10000)

def kayit_ekle_ayt(ayt_net):
    
    ekle = "insert into Tebigep_ayt (aytNet) values (?)"
    islem_ayt.execute(ekle, (ayt_net,))
    baglanti_ayt.commit()
    
    ui.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı",10000)


def kayit_listele_tyt():
    #ui.tableWidget_2.clear()
    #ui.tableWidget_2.setHorizontalHeaderLabels(("TY"))
    ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from Tebigep_tyt"
    islem_tyt.execute(sorgu)
    """for i in islem_tyt:
        ui.tableWidget_2.setItem(QTableWidgetItem(str(i)))"""
    #ui.tableWidget_2.setRowCount(0)
    for indexSatir, kayitNumarasi in enumerate(islem_tyt):
        #print(indexSatir,kayitNumarasi)
        ui.tableWidget_2.insertRow(indexSatir)
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            print(indexSutun)
            ui.tableWidget_2.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kayit_listele_ayt():
    #ui.tableWidget_3.clear()
    #ui.tableWidget_3.setHorizontalHeaderLabels(("AYT"))
    ui.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgu = "select * from Tebigep_ayt"
    islem_ayt.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem_ayt):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tableWidget_3.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

#Grafikler

def grafik_tyt():
    sorgu = 'SELECT * FROM Tebigep_tyt'
    islem_tyt.execute(sorgu)
    kayit = islem_tyt.fetchall()
    plt.plot(kayit,
        color="blue",
         linewidth=3,
         linestyle=":",
         marker="o",
         markerfacecolor="yellow",
         markeredgewidth=1, 
         markeredgecolor="blue")
    plt.xlim((1,ui.tableWidget_2.rowCount()))
    plt.title("Tyt Netleri")
    plt.xlabel("Deneme Sayısı")
    plt.ylabel("Netler")
    plt.show()

def grafik_ayt():
    sorgu = 'SELECT * FROM Tebigep_ayt'
    islem_ayt.execute(sorgu)
    kayit = islem_ayt.fetchall()
    plt.plot(kayit,
         color="blue",
         linewidth=3,
         linestyle=":",
         marker="o",
         markerfacecolor="yellow",
         markeredgewidth=2, 
         markeredgecolor="blue")
    plt.xlim((1,ui.tableWidget_3.rowCount()))
    plt.title("Ayt Netleri")
    plt.xlabel("Deneme Sayısı")
    plt.ylabel("Netler")
    plt.show()

#kalan gün
sinav = date(2023, 6, 17)
bugun = date.today()
kalan = sinav - bugun
gun = kalan.days
ui.lcdNumber.display(gun)

#sınavi başlatma

def sayaci_ac():

    if ui.comboBox.currentText() == "TYT":
        window_tyt.showWid()
    elif ui.comboBox.currentText() == "AYT":
        window_ayt.showWid()


def calisma_programi_ekle(row_data):

    print(row_data)
    c.execute("insert into cp(pzt,sal,crs,per,cum,cmt,paz) values (?,?,?,?,?,?,?)",(row_data))
    s.commit()


def calisma_programi_data():
    satir_sayi = ui.tableWidget.rowCount()
    sutun_sayi = ui.tableWidget.columnCount()

    for satir in range(satir_sayi):
        satir_data = list()
        for sutun in range(sutun_sayi):
            widget_item = ui.tableWidget.item(satir,sutun)
            if widget_item and widget_item.text():
                satir_data.append(widget_item.text())
            else:
                satir_data.append("none")

        calisma_programi_ekle(satir_data)
        s.commit()

def calisma_programi_guncelle_tablo_drop():
    c.execute("DROP TABLE IF EXISTS cp")
    c.execute("""CREATE TABLE IF NOT EXISTS cp(
    pzt TEXT,
    sal TEXT,
    crs TEXT,
    per TEXT,
    cum TEXT,
    cmt TEXT,
    paz TEXT)""")

    s.commit()

ui.pushButton_3.clicked.connect(net_hesapla_tyt_trk)
ui.pushButton_3.clicked.connect(net_hesapla_tyt_mat)
ui.pushButton_3.clicked.connect(net_hesapla_tyt_sos)
ui.pushButton_3.clicked.connect(net_hesapla_tyt_fen)
ui.pushButton_3.clicked.connect(tyt_net_yaz)
ui.pushButton_2.clicked.connect(kayit_listele_tyt)


ui.pushButton_11.clicked.connect(net_hesapla_ayt_trk)
ui.pushButton_11.clicked.connect(net_hesapla_ayt_mat)
ui.pushButton_11.clicked.connect(net_hesapla_ayt_sos)
ui.pushButton_11.clicked.connect(net_hesapla_ayt_fen)
ui.pushButton_11.clicked.connect(ayt_net_yaz)
ui.pushButton_2.clicked.connect(kayit_listele_ayt)

ui.pushButton.clicked.connect(grafik_tyt)
ui.pushButton_4.clicked.connect(grafik_ayt)
ui.pushButton_5.clicked.connect(calisma_programi_data)

ui.pushButton_7.clicked.connect(calisma_programi_guncelle_tablo_drop)
ui.pushButton_7.clicked.connect(calisma_programi_data)

ui.bt_sinavi_baslat.clicked.connect(sayaci_ac)

sys.exit(uygulama.exec_())
