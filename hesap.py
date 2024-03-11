# -- coding: utf-8 --

# Form implementation generated from reading ui file 'hesap.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 30, 431, 561))
        self.groupBox.setObjectName("groupBox")
        self.btn2 = QtWidgets.QPushButton(self.groupBox)
        self.btn2.setGeometry(QtCore.QRect(170, 230, 101, 71))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.groupBox)
        self.btn3.setGeometry(QtCore.QRect(290, 230, 101, 71))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.groupBox)
        self.btn4.setGeometry(QtCore.QRect(50, 310, 101, 71))
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.groupBox)
        self.btn5.setGeometry(QtCore.QRect(172, 307, 101, 71))
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.groupBox)
        self.btn6.setGeometry(QtCore.QRect(290, 310, 101, 71))
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.groupBox)
        self.btn7.setGeometry(QtCore.QRect(50, 390, 101, 71))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.groupBox)
        self.btn8.setGeometry(QtCore.QRect(172, 390, 101, 71))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.groupBox)
        self.btn9.setGeometry(QtCore.QRect(290, 390, 101, 71))
        self.btn9.setObjectName("btn9")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(50, 230, 101, 71))
        self.btn1.setObjectName("btn1")
        self.btn0 = QtWidgets.QPushButton(self.groupBox)
        self.btn0.setGeometry(QtCore.QRect(172, 470, 101, 71))
        self.btn0.setObjectName("btn0")
        self.temizle_btn = QtWidgets.QPushButton(self.groupBox)
        self.temizle_btn.setGeometry(QtCore.QRect(50, 470, 101, 71))
        self.temizle_btn.setObjectName("temizle_btn")
        self.esittir_btn = QtWidgets.QPushButton(self.groupBox)
        self.esittir_btn.setGeometry(QtCore.QRect(290, 470, 101, 71))
        self.esittir_btn.setObjectName("esittir_btn")
        self.toplam_btn = QtWidgets.QPushButton(self.groupBox)
        self.toplam_btn.setGeometry(QtCore.QRect(340, 20, 51, 41))
        self.toplam_btn.setObjectName("toplam_btn")
        self.cikarma_btn = QtWidgets.QPushButton(self.groupBox)
        self.cikarma_btn.setGeometry(QtCore.QRect(340, 70, 51, 41))
        self.cikarma_btn.setObjectName("cikarma_btn")
        self.carpma_btn = QtWidgets.QPushButton(self.groupBox)
        self.carpma_btn.setGeometry(QtCore.QRect(340, 120, 51, 41))
        self.carpma_btn.setObjectName("carpma_btn")
        self.bolme_btn = QtWidgets.QPushButton(self.groupBox)
        self.bolme_btn.setGeometry(QtCore.QRect(340, 170, 51, 41))
        self.bolme_btn.setObjectName("bolme_btn")
        self.ekran = QtWidgets.QTextBrowser(self.groupBox)
        self.ekran.setGeometry(QtCore.QRect(50, 20, 256, 192))
        self.ekran.setObjectName("ekran")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # İşlevleri bağla
        self.btn1.clicked.connect(lambda: self.on_button_click("1"))
        self.btn2.clicked.connect(lambda: self.on_button_click("2"))
        self.btn3.clicked.connect(lambda: self.on_button_click("3"))
        self.btn4.clicked.connect(lambda: self.on_button_click("4"))
        self.btn5.clicked.connect(lambda: self.on_button_click("5"))
        self.btn6.clicked.connect(lambda: self.on_button_click("6"))
        self.btn7.clicked.connect(lambda: self.on_button_click("7"))
        self.btn8.clicked.connect(lambda: self.on_button_click("8"))
        self.btn9.clicked.connect(lambda: self.on_button_click("9"))
        self.btn0.clicked.connect(lambda: self.on_button_click("0"))
        self.temizle_btn.clicked.connect(self.clear_screen)
        self.toplam_btn.clicked.connect(lambda: self.on_operator_click("+"))
        self.cikarma_btn.clicked.connect(lambda: self.on_operator_click("-"))
        self.carpma_btn.clicked.connect(lambda: self.on_operator_click("*"))
        self.bolme_btn.clicked.connect(lambda: self.on_operator_click("/"))
        self.esittir_btn.clicked.connect(self.calculate_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "HESAP MAKİNESİ"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.temizle_btn.setText(_translate("MainWindow", "C"))
        self.esittir_btn.setText(_translate("MainWindow", "="))
        self.toplam_btn.setText(_translate("MainWindow", "+"))
        self.cikarma_btn.setText(_translate("MainWindow", "-"))
        self.carpma_btn.setText(_translate("MainWindow", "x"))
        self.bolme_btn.setText(_translate("MainWindow", "/"))

    def on_button_click(self, value):
        current_text = self.ekran.toPlainText()
        self.ekran.setPlainText(current_text + value)

    def clear_screen(self):
        self.ekran.clear()

    def on_operator_click(self, operator):
        current_text = self.ekran.toPlainText()
        self.ekran.setPlainText(current_text + " " + operator + " ")

    def calculate_result(self):
        expression = self.ekran.toPlainText()
        try:
            result = eval(expression)
            self.ekran.setPlainText(str(result))
        except Exception as e:
            self.ekran.setPlainText("Hata")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())