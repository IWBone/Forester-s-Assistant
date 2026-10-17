from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from ModuleDB import get_db
import re

class Providers:
    def __init__(self, ui):
        self.ui = ui

        # Вставка пустых строк
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM providers WHERE provider = ? and provider_email_acceptance = ? and provider_email_order = ?", ['', '', ''])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO providers(provider, provider_email_acceptance, provider_email_order) VALUES (?, ?, ?)", ['', '', ''])
                db.commit()
            cursor.execute("SELECT car_number, provider FROM car_numbers WHERE car_number = ? AND provider = ?", ['', ''])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO car_numbers(car_number, provider) VALUES (?, ?)", ['', ''])
                db.commit()

        self.ui.info_lineEdit_1.setPlaceholderText('Номер машины')
        self.ui.info_lineEdit_3.setPlaceholderText('Добавление поставщика')
        self.ui.info_lineEdit_4.setPlaceholderText('Почта для приемок')
        self.ui.info_lineEdit_5.setPlaceholderText('Почта для заказов')
        self.ui.info_lineEdit_4.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-z-]+\.[a-z-]+$")))
        self.ui.info_lineEdit_5.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-z-]+\.[a-z-]+$")))

    # Таблица с номерами машин
    # Вывод номеров из базы
    def init_data_providers(self):
        self.ui.info_listWidget_1.clear()
        # Интеграция во вкладку Приемка
        self.ui.acceptance_number.clear()
        # Вывод данных
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT DISTINCT car_number FROM car_numbers ORDER BY car_number")
            numbers = cursor.fetchall()
            for elements in numbers:
                self.ui.info_listWidget_1.addItem(elements[0])
                # Интеграция во вкладку приемка
                self.ui.acceptance_number.addItem(elements[0])

    # Запись новых данных в БД номеров машин
    def write_data_providers(self):
        if self.ui.info_lineEdit_1.text() != '' and self.ui.info_comboBox_1.currentText() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT car_number, provider FROM car_numbers WHERE car_number = ? AND provider = ?", [self.ui.info_lineEdit_1.text().upper(), self.ui.info_comboBox_1.currentText()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO car_numbers(car_number, provider) VALUES (?, ?)", [self.ui.info_lineEdit_1.text().upper(), self.ui.info_comboBox_1.currentText()])
                    db.commit()
            self.ui.info_lineEdit_1.setText('')
            self.init_data_providers()

    # Вывод из столбца с поставщиками по клику на номер машины
    def load_providers(self, item):
        self.ui.info_listWidget_2.clear()
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT provider FROM car_numbers WHERE car_number = ? ORDER BY provider", [item.text()])
            providers = cursor.fetchall()
            for elements in providers:
                QListWidgetItem(format(elements[0]), self.ui.info_listWidget_2)
        self.ui.info_label_2.setText(item.text())

    # Удаление данных по клику на поставщика
    def delete_item(self, item):
        with get_db() as db:
            cursor = db.cursor()
            if item.text() != '':
                cursor.execute("DELETE FROM car_numbers WHERE car_number = ? AND provider = ?", [self.ui.info_label_2.text(), item.text()])
                self.ui.info_listWidget_2.clear()
                cursor.execute("SELECT provider FROM car_numbers WHERE car_number = ? ORDER BY provider", [self.ui.info_label_2.text()])
                providers = cursor.fetchall()
                for elements in providers:
                    QListWidgetItem(format(elements[0]), self.ui.info_listWidget_2)
            db.commit()
        self.init_data_providers()

    # Таблица с поставщиками
    # Вывод списка поставщиков
    def init_data_providers_2(self):
        # Интеграция в вкладку Приемка
        self.ui.acceptance_comboBox_2.clear()
        # Интеграция в вкладку Заказы
        self.ui.orders_comboBox_13.clear()
        self.ui.orders_archive_comboBox_2.clear()
        # Интеграция в вкладку Филиалы и приемка
        self.ui.acceptance_archive_comboBox_1.clear()
        # Вывод данных
        self.ui.info_comboBox_1.clear()
        self.ui.info_listWidget_3.clear()
        self.ui.info_listWidget_4.clear()
        self.ui.info_listWidget_5.clear()
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM providers ORDER BY provider")
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

    # Запись новых данных
    def write_data_providers_2(self):
        with get_db() as db:
            cursor = db.cursor()
            pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-z-]+\.[a-z-]+$")

            if (self.ui.info_lineEdit_3.text() != '' and (self.ui.info_lineEdit_4.text() == '' and self.ui.info_lineEdit_5.text() != '')) and pattern.match(self.ui.info_lineEdit_5.text()):
                cursor.execute("SELECT * FROM providers WHERE provider = ? and provider_email_acceptance = ? and provider_email_order = ?",
                                          [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_5.text(), self.ui.info_lineEdit_5.text()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO providers(provider, provider_email_acceptance, provider_email_order) VALUES (?, ?, ?)",
                                              [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_5.text(), self.ui.info_lineEdit_5.text()])
                    db.commit()
                    self.ui.info_lineEdit_3.setText('')
                    self.ui.info_lineEdit_4.setText('')
                    self.ui.info_lineEdit_5.setText('')
            else:
                self.ui.info_label_15.setText("Неверный адрес электронной почты")

            if (self.ui.info_lineEdit_3.text() != '' and (self.ui.info_lineEdit_4.text() != '' and self.ui.info_lineEdit_5.text() == '')) and pattern.match(self.ui.info_lineEdit_4.text()):
                cursor.execute("SELECT * FROM providers WHERE provider = ? and provider_email_acceptance = ? and provider_email_order = ?",
                                          [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_4.text()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO providers(provider, provider_email_acceptance, provider_email_order) VALUES (?, ?, ?)",
                                              [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_4.text()])
                    db.commit()
                    self.ui.info_lineEdit_3.setText('')
                    self.ui.info_lineEdit_4.setText('')
                    self.ui.info_lineEdit_5.setText('')
            else:
                self.ui.info_label_15.setText("Неверный адрес электронной почты")

            if (self.ui.info_lineEdit_3.text() != '' and (self.ui.info_lineEdit_4.text() != '' and self.ui.info_lineEdit_5.text() != '')) and (pattern.match(self.ui.info_lineEdit_4.text()) and pattern.match(self.ui.info_lineEdit_5.text())):
                cursor.execute("SELECT * FROM providers WHERE provider = ? and provider_email_acceptance = ? and provider_email_order = ?",
                                          [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_5.text()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO providers(provider, provider_email_acceptance, provider_email_order) VALUES (?, ?, ?)",
                                              [self.ui.info_lineEdit_3.text(), self.ui.info_lineEdit_4.text(), self.ui.info_lineEdit_5.text()])
                    db.commit()
                    self.ui.info_lineEdit_3.setText('')
                    self.ui.info_lineEdit_4.setText('')
                    self.ui.info_lineEdit_5.setText('')
            else:
                self.ui.info_label_15.setText("Неверный адрес электронной почты")

        self.init_data_providers_2()

    # Удаление данных по клику
    def delete_item_2(self, item):
        if item.text() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM providers WHERE provider = ?", [item.text()])
                db.commit()
            self.init_data_providers_2()
