import sqlite3
from PyQt6.QtWidgets import QListWidgetItem

class branches:
    def __init__(self, ui):
        self.ui = ui
        self.ui.branch_lineEdit_1.setPlaceholderText('Филиал')
        self.ui.branch_lineEdit_2.setPlaceholderText('Код филиала')

        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM branches WHERE branches = ? AND code_branches = ?", ['', ''])
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO branches(branches, code_branches) VALUES (?, ?)", ['', ''])
            db.commit()
        cursor.close()
        db.close()

    # Вывод списков
    def branch_initData_1(self):
        # Интеграция в вкладку Приемка
        self.ui.acceptance_branch.clear()
        # 
        self.ui.orders_comboBox_1.clear()
        self.ui.orders_comboBox_2.clear()
        self.ui.orders_comboBox_3.clear()
        self.ui.orders_comboBox_4.clear()
        self.ui.branch_listWidget_1.clear()
        self.ui.branch_listWidget_2.clear()
        # Интеграция в вкладку Филиалы и приемка
        self.ui.acceptance_archive_comboBox_2.clear()
        # Интеграция в вкладку Заказы
        self.ui.orders_archive_comboBox_1.clear()
        # 
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT branches FROM branches ORDER BY branches")
        items = cursor.fetchall()
        for elements in items:
            QListWidgetItem(format(elements[0]), self.ui.branch_listWidget_1)
            # Интеграция в вкладку заказы
            self.ui.orders_comboBox_1.addItem(elements[0])
            self.ui.orders_comboBox_2.addItem(elements[0])
            self.ui.orders_comboBox_3.addItem(elements[0])
            self.ui.orders_comboBox_4.addItem(elements[0])
            # 
        cursor.execute("SELECT code_branches FROM branches ORDER BY branches")
        items = cursor.fetchall()
        for elements in items:
            QListWidgetItem(format(elements[0]), self.ui.branch_listWidget_2)
            # Интеграция в вкладку Приемка
            self.ui.acceptance_branch.addItem(elements[0])
            # Интеграция в вкладку Филиалы и приемка
            self.ui.acceptance_archive_comboBox_2.addItem(elements[0])
            # Интеграция в вкладку Заказы
            self.ui.orders_archive_comboBox_1.addItem(elements[0])
        db.commit()
        db.close()

    # Запись новых данных
    def branch_write_1(self):
        if (self.ui.branch_lineEdit_1.text() == '' and self.ui.branch_lineEdit_2.text() != '') or (self.ui.branch_lineEdit_1.text() != '' and self.ui.branch_lineEdit_2.text() == ''):
            None
        else:
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM branches WHERE branches = ? AND code_branches = ?", [self.ui.branch_lineEdit_1.text(), self.ui.branch_lineEdit_2.text()])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO branches(branches, code_branches) VALUES (?, ?)", [self.ui.branch_lineEdit_1.text(), self.ui.branch_lineEdit_2.text()])
                db.commit()
            self.ui.branch_lineEdit_1.setText('')
            self.ui.branch_lineEdit_2.setText('')
            self.branch_initData_1()
            cursor.close()
            db.close()
    # Удаление данных
    def branches_delete_item_1(self, item):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        if item.text() != '':
            cursor.execute("DELETE FROM branches WHERE branches = ?", [item.text()])
            self.ui.branch_listWidget_1.clear()
            self.ui.branch_listWidget_2.clear()
            db.commit()
            db.close()
            self.branch_initData_1()
    def branches_delete_item_2(self, item):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        if item.text() != '':
            cursor.execute("DELETE FROM branches WHERE code_branches = ?", [item.text()])
            self.ui.branch_listWidget_1.clear()
            self.ui.branch_listWidget_2.clear()
            db.commit()
            db.close()
            self.branch_initData_1()

    # Архив приемок
    # Инициализация списка тем архива приемок
    def init_archive_acceptance(self):
        self.ui.acceptance_archive_listWidget_1.clear()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance ORDER BY rowid DESC")
        items = cursor.fetchall()
        for elements in items:
            QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        db.close()
    # Вывод содержимого приемки по теме
    def load_body_acceptance(self, item):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT provider_acceptance FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [item.text()[:21], item.text()[23:]])
        provider = cursor.fetchone()
        cursor.execute("SELECT body_acceptance FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [item.text()[:21], item.text()[23:]])
        themes = cursor.fetchone()
        s = f'{provider[0]}\n{"".join(str(x) for x in themes[0])}'
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText(s)
        db.commit()
        db.close()
        self.ui.acceptance_archive_label_1.setText(item.text())
    # Удаление данных
    def acceptance_archive_delete_item(self):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("DELETE FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [self.ui.acceptance_archive_label_1.text()[:21], self.ui.acceptance_archive_label_1.text()[23:]])
        db.commit()
        db.close()
        self.acceptance_archive_selection()
    # Отбор данных
    def acceptance_archive_selection(self):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        if self.ui.acceptance_archive_comboBox_2.currentText() != '' and self.ui.acceptance_archive_comboBox_1.currentText() != '':
            self.ui.acceptance_archive_listWidget_1.clear()
            cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE branch_acceptance = ? AND provider_acceptance = ? ORDER BY rowid DESC", [self.ui.acceptance_archive_comboBox_2.currentText(), self.ui.acceptance_archive_comboBox_1.currentText()])
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        elif self.ui.acceptance_archive_comboBox_2.currentText() == '' and self.ui.acceptance_archive_comboBox_1.currentText() != '':
            self.ui.acceptance_archive_listWidget_1.clear()
            cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE provider_acceptance = ? ORDER BY rowid DESC", [self.ui.acceptance_archive_comboBox_1.currentText()])
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        elif self.ui.acceptance_archive_comboBox_2.currentText() != '' and self.ui.acceptance_archive_comboBox_1.currentText() == '':
            self.ui.acceptance_archive_listWidget_1.clear()
            cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE branch_acceptance = ? ORDER BY rowid DESC", [self.ui.acceptance_archive_comboBox_2.currentText()])
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        else:
            self.init_archive_acceptance()
        db.close()