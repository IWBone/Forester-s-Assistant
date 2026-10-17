from PyQt6.QtWidgets import QListWidgetItem
from ModuleDB import get_db

class Branches:
    def __init__(self, ui):
        self.ui = ui
        self.ui.branch_lineEdit_1.setPlaceholderText('Филиал')
        self.ui.branch_lineEdit_2.setPlaceholderText('Код филиала')
        # self.ui.branch_lineEdit_2.setMaxLength(2)

        # Вставка пустых строк
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM branches WHERE branch = ? AND code_branch = ?", ['', ''])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO branches(branch, code_branch) VALUES (?, ?)", ['', ''])
                db.commit()

    # Филиалы
    # Вывод списков
    def branch_initData_1(self):
        # Интеграция в вкладку Приемка
        self.ui.acceptance_branch.clear()
        # Интеграция в вкладку Заказы
        self.ui.orders_comboBox_1.clear()
        self.ui.orders_comboBox_2.clear()
        self.ui.orders_comboBox_3.clear()
        self.ui.orders_comboBox_4.clear()
        self.ui.orders_archive_comboBox_1.clear()
        # Интеграция в вкладку Филиалы и приемка
        self.ui.branch_listWidget_1.clear()
        self.ui.branch_listWidget_2.clear()
        self.ui.acceptance_archive_comboBox_2.clear()

        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT branch FROM branches ORDER BY branch")
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(elements[0]), self.ui.branch_listWidget_1)
                # Интеграция в вкладку заказы
                self.ui.orders_comboBox_1.addItem(elements[0])
                self.ui.orders_comboBox_2.addItem(elements[0])
                self.ui.orders_comboBox_3.addItem(elements[0])
                self.ui.orders_comboBox_4.addItem(elements[0])

            cursor.execute("SELECT code_branch FROM branches ORDER BY branch")
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(elements[0]), self.ui.branch_listWidget_2)
                # Интеграция в вкладку Приемка
                self.ui.acceptance_branch.addItem(elements[0])
                # Интеграция в вкладку Филиалы и приемка
                self.ui.acceptance_archive_comboBox_2.addItem(elements[0])
                # Интеграция в вкладку Заказы
                self.ui.orders_archive_comboBox_1.addItem(elements[0])

    # Запись новых данных
    def branch_write_1(self):
        if self.ui.branch_lineEdit_1.text() != '' and self.ui.branch_lineEdit_2.text() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM branches WHERE branch = ? AND code_branch = ?", [self.ui.branch_lineEdit_1.text(), self.ui.branch_lineEdit_2.text().upper()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO branches(branch, code_branch) VALUES (?, ?)", [self.ui.branch_lineEdit_1.text(), self.ui.branch_lineEdit_2.text().upper()])
                    db.commit()
            self.ui.branch_lineEdit_1.setText('')
            self.ui.branch_lineEdit_2.setText('')
            self.branch_initData_1()

    # Удаление данных
    def branches_delete_item_1(self, item):
        if item.text() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM branches WHERE branch = ?", [item.text()])
                db.commit()
            self.branch_initData_1()

    def branches_delete_item_2(self, item):
        if item.text() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM branches WHERE code_branch = ?", [item.text()])
                db.commit()
            self.branch_initData_1()

    # Архив приемок
    # Инициализация списка тем архива приемок
    def init_archive_acceptance(self):
        self.ui.acceptance_archive_listWidget_1.clear()
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance ORDER BY rowid DESC")
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)

    # Вывод содержимого приемки по теме
    def load_body_acceptance(self, item):
        if ', ' not in item.text():
            return
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        with get_db() as db:
            cursor = db.cursor()
            theme = item.text().split(', ')
            cursor.execute("SELECT provider_acceptance FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [theme[0], theme[1]])
            provider = cursor.fetchone()
            cursor.execute("SELECT body_acceptance FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [theme[0], theme[1]])
            body = cursor.fetchone()
            s = f'{provider[0]}\n{"".join(str(x) for x in body[0])}'
            self.ui.acceptance_archive_plainTextEdit_2.setPlainText(s)
        self.ui.acceptance_archive_label_1.setText(item.text())

    # Удаление данных
    def acceptance_archive_delete_item(self):
        if self.ui.acceptance_archive_label_1.text() == '' or ', ' not in self.ui.acceptance_archive_label_1.text():
            return
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        with get_db() as db:
            cursor = db.cursor()
            theme = self.ui.acceptance_archive_label_1.text().split(', ')
            cursor.execute("DELETE FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [theme[0], theme[1]])
            db.commit()
        self.acceptance_archive_selection()
        self.ui.acceptance_archive_label_1.setText('')

    # Отбор данных
    def acceptance_archive_selection(self):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        with get_db() as db:
            cursor = db.cursor()
            if self.ui.acceptance_archive_comboBox_2.currentText() != '' and self.ui.acceptance_archive_comboBox_1.currentText() != '':
                self.ui.acceptance_archive_listWidget_1.clear()
                cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE branch_acceptance = ? AND provider_acceptance = ? ORDER BY rowid DESC", 
                                                   [self.ui.acceptance_archive_comboBox_2.currentText(), self.ui.acceptance_archive_comboBox_1.currentText()])
                items = cursor.fetchall()
                for elements in items:
                    QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
            elif self.ui.acceptance_archive_comboBox_2.currentText() == '' and self.ui.acceptance_archive_comboBox_1.currentText() != '':
                self.ui.acceptance_archive_listWidget_1.clear()
                cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE provider_acceptance = ? ORDER BY rowid DESC",
                                                   [self.ui.acceptance_archive_comboBox_1.currentText()])
                items = cursor.fetchall()
                for elements in items:
                    QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
            elif self.ui.acceptance_archive_comboBox_2.currentText() != '' and self.ui.acceptance_archive_comboBox_1.currentText() == '':
                self.ui.acceptance_archive_listWidget_1.clear()
                cursor.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE branch_acceptance = ? ORDER BY rowid DESC",
                                                   [self.ui.acceptance_archive_comboBox_2.currentText()])
                items = cursor.fetchall()
                for elements in items:
                    QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
            else:
                self.init_archive_acceptance()
