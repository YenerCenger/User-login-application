import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table if not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")

        self.baglanti.commit()
    def init_ui(self):

        self.kullanici = QtWidgets.QLabel("Kullanıcı Adı : ")
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLabel("       Parola : ")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        self.clear = QtWidgets.QPushButton("Temizle")
        self.sign = QtWidgets.QPushButton("Kayıt Ol")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.kullanici)
        h_box1.addWidget(self.kullanici_adi)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.sifre)
        h_box2.addWidget(self.parola)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.yazi_alani)
        h_box3.addStretch()

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.clear)
        h_box4.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.sign)
        h_box5.addWidget(self.giris)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addStretch()
        v_box.addLayout(h_box5)

        self.setLayout(v_box)

        self.setWindowTitle("Kullanıcı Giriş Uygulaması")

        self.clear.clicked.connect(self.click)
        self.giris.clicked.connect(self.login)
        self.sign.clicked.connect(self.sign_in)
        self.show()

    def sign_in(self):
        user_name = self.kullanici_adi.text()
        password = self.parola.text()

        self.cursor.execute("Insert into üyeler Values(?,?)",(user_name,password))

        self.yazi_alani.setText("Başarıyla Kayıt Olundu.")

        self.baglanti.commit()

    def login(self):

        adı = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * from üyeler where kullanıcı_adı = ? and parola = ?",(adı,par))
        data = self.cursor.fetchall()
        if (len(data) == 0):
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen Tekrar Deneyin...")

        else:
            self.yazi_alani.setText("Giriş Yapılıyor...\nHoşgeldiniz " + adı)

    def click(self):

        sender = self.sender()

        if (sender.text() == "Temizle"):
            self.kullanici_adi.clear()
            self.parola.clear()


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())