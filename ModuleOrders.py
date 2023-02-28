import sqlite3
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtWidgets import QApplication
from ModuleProviders import providers
from ModuleBranches import branches

class orders:
    def __init__(self, ui):
        self.ui = ui
        self.providers = providers(ui)
        self.branches = branches(ui)
        self.clipboard = QApplication.clipboard()

    # Видимость строк
    def order_changeVisibility_1(self):
        if self.ui.orders_checkBox_1.isChecked() == True:
            self.ui.orders_comboBox_2.setVisible(True)
            self.ui.orders_comboBox_6.setVisible(True)
            self.ui.orders_comboBox_10.setVisible(True)
            self.ui.orders_spinBox_2.setVisible(True)
        else:
            self.ui.orders_comboBox_2.setVisible(False)
            self.ui.orders_comboBox_6.setVisible(False)
            self.ui.orders_comboBox_10.setVisible(False)
            self.ui.orders_spinBox_2.setVisible(False)
    def order_changeVisibility_2(self):
        if self.ui.orders_checkBox_2.isChecked() == True:
            self.ui.orders_comboBox_3.setVisible(True)
            self.ui.orders_comboBox_7.setVisible(True)
            self.ui.orders_comboBox_11.setVisible(True)
            self.ui.orders_spinBox_3.setVisible(True)
        else:
            self.ui.orders_comboBox_3.setVisible(False)
            self.ui.orders_comboBox_7.setVisible(False)
            self.ui.orders_comboBox_11.setVisible(False)
            self.ui.orders_spinBox_3.setVisible(False)
    def order_changeVisibility_3(self):
        if self.ui.orders_checkBox_3.isChecked() == True:
            self.ui.orders_comboBox_4.setVisible(True)
            self.ui.orders_comboBox_8.setVisible(True)
            self.ui.orders_comboBox_12.setVisible(True)
            self.ui.orders_spinBox_4.setVisible(True)
        else:
            self.ui.orders_comboBox_4.setVisible(False)
            self.ui.orders_comboBox_8.setVisible(False)
            self.ui.orders_comboBox_12.setVisible(False)
            self.ui.orders_spinBox_4.setVisible(False)
    # Генерация заказа
    def order(self):
        if self.ui.orders_comboBox_13.currentText() != '' and (self.ui.orders_comboBox_1.currentText() != '' or (self.ui.orders_comboBox_2.currentText() != '' or (self.ui.orders_comboBox_3.currentText() != '' or self.ui.orders_comboBox_4.currentText() != ''))):
            db_branches = sqlite3.connect('Database/branches.db')
            cursor_branches = db_branches.cursor()
            # Заполнение темы
            cursor_branches.execute("SELECT code_branch FROM branches WHERE branch = ?", [self.ui.orders_comboBox_1.currentText()])
            code_branch_1 = cursor_branches.fetchone()[0]
            cursor_branches.execute("SELECT code_branch FROM branches WHERE branch = ?", [self.ui.orders_comboBox_2.currentText()])
            code_branch_2 = cursor_branches.fetchone()[0]
            cursor_branches.execute("SELECT code_branch FROM branches WHERE branch = ?", [self.ui.orders_comboBox_3.currentText()])
            code_branch_3 = cursor_branches.fetchone()[0]
            cursor_branches.execute("SELECT code_branch FROM branches WHERE branch = ?", [self.ui.orders_comboBox_4.currentText()])
            code_branch_4 = cursor_branches.fetchone()[0]
            if code_branch_2 != '':
                branch_2 = f' + {code_branch_2}'
            else: branch_2 = ''
            if code_branch_3 != '':
                branch_3 = f' + {code_branch_3}'
            else: branch_3 = ''
            if code_branch_4 != '':
                branch_4 = f' + {code_branch_4}'
            else: branch_4 = ''
            if code_branch_2 == code_branch_1:
                branch_2 = ''
            if code_branch_3 == code_branch_1:
                branch_3 = ''
            if code_branch_4 == code_branch_1:
                branch_4 = ''
            if code_branch_3 == code_branch_2:
                branch_3 = ''
            if code_branch_4 == code_branch_2:
                branch_4 = ''
            if code_branch_4 == code_branch_3:
                branch_4 = ''
            code_branch_for_archive = ", ".join([code_branch_1, branch_2, branch_3, branch_4])
            self.ui.orders_pushButton_2.setText(f"""Заказ лес {code_branch_1}{branch_2}{branch_3}{branch_4} на {self.ui.orders_calendarWidget.selectedDate().toString('dd.MM.yyyy')}""")
            # Заполнение тела
            if code_branch_1 != '':
                body_1 = f'{self.ui.orders_comboBox_1.currentText()} - {self.ui.orders_comboBox_5.currentText()} {self.ui.orders_comboBox_9.currentText()}м {self.ui.orders_spinBox_1.text()}м3, на {self.ui.orders_calendarWidget.selectedDate().toString("dd.MM.yyyy")}\n'
            else: body_1 = ''
            if code_branch_2 != '':
                body_2 = f'{self.ui.orders_comboBox_2.currentText()} - {self.ui.orders_comboBox_6.currentText()} {self.ui.orders_comboBox_10.currentText()}м {self.ui.orders_spinBox_2.text()}м3, на {self.ui.orders_calendarWidget.selectedDate().toString("dd.MM.yyyy")}\n'
            else: body_2 = ''
            if code_branch_3 != '':
                body_3 = f'{self.ui.orders_comboBox_3.currentText()} - {self.ui.orders_comboBox_7.currentText()} {self.ui.orders_comboBox_11.currentText()}м {self.ui.orders_spinBox_3.text()}м3, на {self.ui.orders_calendarWidget.selectedDate().toString("dd.MM.yyyy")}\n'
            else: body_3 = ''
            if code_branch_4 != '':
                body_4 = f'{self.ui.orders_comboBox_4.currentText()} - {self.ui.orders_comboBox_8.currentText()} {self.ui.orders_comboBox_12.currentText()}м {self.ui.orders_spinBox_4.text()}м3, на {self.ui.orders_calendarWidget.selectedDate().toString("dd.MM.yyyy")}\n'
            else: body_4 = ''
            body = f'{body_1}{body_2}{body_3}{body_4}'
            self.ui.orders_pushButton_3.setText(f'Добрый день\n{body}\n')

            # Занесение заказа в архив
            db_archive_orders = sqlite3.connect('Database/archive_orders.db')
            cursor_archive_orders = db_archive_orders.cursor()
            cursor_archive_orders.execute("SELECT * FROM archive_orders WHERE theme_order = ? AND body_order = ? AND provider_order = ?",
                                        [self.ui.orders_pushButton_2.text(), self.ui.orders_pushButton_3.text(), self.ui.orders_comboBox_13.currentText()])
            if cursor_archive_orders.fetchone() is None:
                cursor_archive_orders.execute("INSERT INTO archive_orders(theme_order, body_order, provider_order, branch_order, date_order) VALUES (?, ?, ?, ?, ?)",
                                            [self.ui.orders_pushButton_2.text(), self.ui.orders_pushButton_3.text(), self.ui.orders_comboBox_13.currentText(), code_branch_for_archive, self.ui.orders_calendarWidget.selectedDate().toString('dd.MM.yyyy')])
                db_archive_orders.commit()
            cursor_branches.close()
            db_branches.close()
            cursor_archive_orders.close()
            db_archive_orders.close()
            self.order_archive_selection()

    # Копирование темы в буфер обмена
    def order_copytheme(self):
        self.clipboard.setText(self.ui.orders_pushButton_2.text())
    # Копирование тела в буфер обмена
    def order_copybody(self):
        self.clipboard.setText(self.ui.orders_pushButton_3.text())

    # Очистка полей
    def order_clear(self):
        self.branches.branch_initData_1()
        self.providers.init_data_providers_2()
        self.ui.orders_spinBox_1.setValue(0)
        self.ui.orders_spinBox_2.setValue(0)
        self.ui.orders_spinBox_3.setValue(0)
        self.ui.orders_spinBox_4.setValue(0)
        self.ui.orders_pushButton_2.setText('')
        self.ui.orders_pushButton_3.setText('')

    # Архив заказов
    # Инициализация списка тем архива приемок
    def init_archive_order(self):
        self.ui.orders_archive_listWidget_1.clear()
        db_archive_orders = sqlite3.connect('Database/archive_orders.db')
        cursor_archive_orders = db_archive_orders.cursor()
        cursor_archive_orders.execute("SELECT theme_order, rowid FROM archive_orders ORDER BY rowid DESC")
        items = cursor_archive_orders.fetchall()
        for elements in items:
            QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
        cursor_archive_orders.close()
        db_archive_orders.close()

    # Вывод содержимого приемки по теме
    def load_body_order_achive(self, item):
        self.ui.orders_archive_plainTextEdit_1.setPlainText('')
        db_archive_orders = sqlite3.connect('Database/archive_orders.db')
        cursor_archive_orders = db_archive_orders.cursor()
        substring = item.text().split(', ')[1]
        cursor_archive_orders.execute("SELECT provider_order FROM archive_orders WHERE rowid = ?", [substring])
        provider = cursor_archive_orders.fetchone()
        cursor_archive_orders.execute("SELECT body_order FROM archive_orders WHERE rowid = ?", [substring])
        themes = cursor_archive_orders.fetchone()
        s = f'{provider[0]}\n{"".join(str(x) for x in themes[0])}'
        self.ui.orders_archive_plainTextEdit_1.setPlainText(s)
        cursor_archive_orders.close()
        db_archive_orders.close()
        self.ui.orders_archive_label_1.setText(substring)

    # Удаление данных
    def order_archive_delete_item(self):
        self.ui.orders_archive_plainTextEdit_1.setPlainText('')
        db_archive_orders = sqlite3.connect('Database/archive_orders.db')
        cursor_archive_orders = db_archive_orders.cursor()
        cursor_archive_orders.execute("DELETE FROM archive_orders WHERE rowid = ?", [self.ui.orders_archive_label_1.text()])
        db_archive_orders.commit()
        cursor_archive_orders.close()
        db_archive_orders.close()
        self.ui.orders_archive_label_1.setText('')
        self.order_archive_selection()

    # Отбор данных
    def order_archive_selection(self):
        self.ui.orders_archive_plainTextEdit_1.setPlainText('')
        db_archive_orders = sqlite3.connect('Database/archive_orders.db')
        cursor_archive_orders = db_archive_orders.cursor()
        if self.ui.orders_archive_comboBox_1.currentText() != '' and self.ui.orders_archive_comboBox_2.currentText() != '':
            self.ui.orders_archive_listWidget_1.clear()
            cursor_archive_orders.execute("SELECT theme_order, rowid FROM archive_orders WHERE theme_order LIKE ? AND provider_order = ? ORDER BY rowid DESC", ['%' + self.ui.orders_archive_comboBox_1.currentText() + '%', self.ui.orders_archive_comboBox_2.currentText()])
            items = cursor_archive_orders.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
        elif self.ui.orders_archive_comboBox_1.currentText() == '' and self.ui.orders_archive_comboBox_2.currentText() != '':
            self.ui.orders_archive_listWidget_1.clear()
            cursor_archive_orders.execute("SELECT theme_order, rowid FROM archive_orders WHERE provider_order = ? ORDER BY rowid DESC", [self.ui.orders_archive_comboBox_2.currentText()])
            items = cursor_archive_orders.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
        elif self.ui.orders_archive_comboBox_1.currentText() != '' and self.ui.orders_archive_comboBox_2.currentText() == '':
            self.ui.orders_archive_listWidget_1.clear()
            cursor_archive_orders.execute("SELECT theme_order, rowid FROM archive_orders WHERE theme_order LIKE ? ORDER BY rowid DESC", ['%' + self.ui.orders_archive_comboBox_1.currentText() + '%'])
            items = cursor_archive_orders.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
        else:
            self.init_archive_order()
        cursor_archive_orders.close()
        db_archive_orders.close()