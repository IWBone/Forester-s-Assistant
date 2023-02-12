import sqlite3
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
import re

class providers:
    def __init__(self, ui):
        self.ui = ui

        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM providers WHERE providers = ? and providers_email_acceptances = ? and providers_email_orders = ?", ['', '', ''])
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO providers(providers, providers_email_acceptances, providers_email_orders) VALUES (?, ?, ?)", ['', '', ''])
            db.commit()
        cursor.execute("SELECT number_car, provider FROM base_nubers WHERE number_car = ? AND provider = ?", ['', ''])
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO base_nubers(number_car, provider) VALUES (?, ?)", ['', ''])
            db.commit()
        cursor.close()
        db.close()

        self.ui.info_lineEdit_1.setPlaceholderText('Номер машины')
        self.ui.info_lineEdit_3.setPlaceholderText('Добавление поставщика')
        self.ui.info_lineEdit_4.setPlaceholderText('Почта для приемок')
        self.ui.info_lineEdit_5.setPlaceholderText('Почта для заказов')
        self.ui.info_lineEdit_4.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-z]+\.[a-z]+$")))
        self.ui.info_lineEdit_5.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-z]+\.[a-z]+$")))

    # Вывод номеров из базы
    def init_data_providers(self):
        self.ui.info_listWidget_1.clear()
        # Интеграция во вкладку Приемка
        self.ui.acceptance_number.clear()
        # 
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT number_car FROM base_nubers ORDER BY number_car")
        numbers = cursor.fetchall()
        if numbers != []:
            for elements in numbers:
                QListWidgetItem(format(elements[0]), self.ui.info_listWidget_1)
            for i in numbers[0]:
                self.ui.info_listWidget_1.addItem(i)
            numbers = []
            for i in range(self.ui.info_listWidget_1.count()):
                numbers.append(self.ui.info_listWidget_1.item(i).text())
            unique_numbers_set = set(numbers)
            self.ui.info_listWidget_1.clear()
            for i in unique_numbers_set:
                self.ui.info_listWidget_1.addItem(i)
                # Интеграция во вкладку приемка
                self.ui.acceptance_number.addItem(i)
                # 
            self.ui.info_listWidget_1.sortItems()
        db.commit()
        db.close()
    # Запись новых данных в БД
    def write_data_providers(self):
        if (self.ui.info_lineEdit_1.text() == '' and self.ui.info_comboBox_1.currentText() != '') or (self.ui.info_lineEdit_1.text() != '' and self.ui.info_comboBox_1.currentText() == ''):
            None
        else:
            try:
                db = sqlite3.connect('database.db')
                cursor = db.cursor()
                cursor.execute("SELECT number_car, provider FROM base_nubers WHERE number_car = ? AND provider = ?", [self.ui.info_lineEdit_1.text().upper(), self.ui.info_comboBox_1.currentText()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO base_nubers(number_car, provider) VALUES (?, ?)", [self.ui.info_lineEdit_1.text().upper(), self.ui.info_comboBox_1.currentText()])
                    db.commit()
            finally:
                self.ui.info_lineEdit_1.setText('')
                self.init_data_providers()
                cursor.close()
                db.close()
    # Вывод из столбца с поставщиками по клику на номер машины
    def load_providers(self, item):
        self.ui.info_listWidget_2.clear()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT provider FROM base_nubers WHERE number_car = ? ORDER BY provider", [item.text()])
        providers = cursor.fetchall()
        for elements in providers:
            QListWidgetItem(format(elements[0]), self.ui.info_listWidget_2)
        db.commit()
        db.close()
        self.ui.info_label_2.setText(item.text())
    # Удаление данных по клику на поставщика
    def delete_item(self, item):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        if item.text() != '':
            cursor.execute("DELETE FROM base_nubers WHERE number_car = ? AND provider = ?", [self.ui.info_label_2.text(), item.text()])
            self.ui.info_listWidget_2.clear()
            cursor.execute("SELECT provider FROM base_nubers WHERE number_car = ? ORDER BY provider", [self.ui.info_label_2.text()])
            providers = cursor.fetchall()
            for elements in providers:
                QListWidgetItem(format(elements[0]), self.ui.info_listWidget_2)
        self.ui.info_label_2.setText('')
        db.commit()
        db.close()
        self.init_data_providers()

    # Таблица с поставщиками
    # Вывод списка поставщиков
    def init_data_providers_2(self):
        self.ui.info_comboBox_1.clear()
        # Интеграция в вкладку Приемка
        self.ui.acceptance_comboBox_2.clear()
        # Интеграция в вкладку Заказы
        self.ui.orders_comboBox_13.clear()
        self.ui.orders_archive_comboBox_2.clear()
        # Интеграция в вкладку Филиалы и приемка
        self.ui.acceptance_archive_comboBox_1.clear()
        # Вывод
        self.ui.info_listWidget_3.clear()
        self.ui.info_listWidget_4.clear()
        self.ui.info_listWidget_5.clear()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM providers ORDER BY providers")
        providers = cursor.fetchall()
        for elements in providers:
            QListWidgetItem(format(elements[0]), self.ui.info_listWidget_3)
            QListWidgetItem(format(elements[1]), self.ui.info_listWidget_4)
            QListWidgetItem(format(elements[2]), self.ui.info_listWidget_5)
            self.ui.info_comboBox_1.addItem(elements[0])
            # Интеграция в вкладку Приемка
            self.ui.acceptance_comboBox_2.addItem(elements[0])
            # Интеграция в вкладку Заказы
            self.ui.orders_comboBox_13.addItem(elements[0])
            self.ui.orders_archive_comboBox_2.addItem(elements[0])
            # Интеграция в вкладку Филиалы и приемка
            self.ui.acceptance_archive_comboBox_1.addItem(elements[0])
        db.commit()
        db.close()
    # Запись новых данных
    def write_data_providers_2(self):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-z]+\.[a-z]+$")

        if (self.ui.info_lineEdit_3.text() != '' and (self.ui.info_lineEdit_4.text() == '' and self.ui.info_lineEdit_5.text() != '')) and (pattern.match(self.ui.info_lineEdit_4.text()) and pattern.match(self.ui.info_lineEdit_5.text())):
            cursor.execute("SELECT * FROM providers WHERE providers = ? and providers_email_acceptances = ? and providers_email_orders = ?", [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_5.text(), self.ui.info_lineEdit_5.text()])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO providers(providers, providers_email_acceptances, providers_email_orders) VALUES (?, ?, ?)", [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_5.text(), self.ui.info_lineEdit_5.text()])
                db.commit()
                self.ui.info_lineEdit_3.setText('')
                self.ui.info_lineEdit_4.setText('')
                self.ui.info_lineEdit_5.setText('')
        else:
            self.ui.info_label_15.setText("Неверный адрес электронной почты")

        if (self.ui.info_lineEdit_3.text() != '' and (self.ui.info_lineEdit_4.text() != '' and self.ui.info_lineEdit_5.text() == '')) and pattern.match(self.ui.info_lineEdit_4.text()):
            cursor.execute("SELECT * FROM providers WHERE providers = ? and providers_email_acceptances = ? and providers_email_orders = ?", [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_4.text()])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO providers(providers, providers_email_acceptances, providers_email_orders) VALUES (?, ?, ?)", [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_4.text()])
                db.commit()
                self.ui.info_lineEdit_3.setText('')
                self.ui.info_lineEdit_4.setText('')
                self.ui.info_lineEdit_5.setText('')
        else:
            self.ui.info_label_15.setText("Неверный адрес электронной почты")

        if (self.ui.info_lineEdit_3.text() != '' and (self.ui.info_lineEdit_4.text() != '' and self.ui.info_lineEdit_5.text() != '')) and pattern.match(self.ui.info_lineEdit_5.text()):
            cursor.execute("SELECT * FROM providers WHERE providers = ? and providers_email_acceptances = ? and providers_email_orders = ?", [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_5.text()])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO providers(providers, providers_email_acceptances, providers_email_orders) VALUES (?, ?, ?)", [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_5.text()])
                db.commit()
                self.ui.info_lineEdit_3.setText('')
                self.ui.info_lineEdit_4.setText('')
                self.ui.info_lineEdit_5.setText('')
        else:
            self.ui.info_label_15.setText("Неверный адрес электронной почты")

        self.init_data_providers_2()
        cursor.close()
        db.close()

    # Удаление данных по клику
    def delete_item_2(self, item):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        if item.text() != '':
            cursor.execute("DELETE FROM providers WHERE providers = ?", [item.text()])
            self.ui.info_listWidget_3.clear()
            db.commit()
            db.close()
            self.init_data_providers_2()