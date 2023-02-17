import win32com.client
import sqlite3
from PyQt6.QtWidgets import QListWidgetItem, QApplication
from PyQt6.QtGui import QRegularExpressionValidator, QClipboard, QImage
from PyQt6.QtCore import QRegularExpression, QTimer, Qt
from ModuleAcceptance import acceptance
from ModuleOrders import orders
import os

class outlook:
    def __init__(self, ui):
        self.ui = ui
        self.acceptance = acceptance(ui)
        self.orders = orders(ui)

        self.ui.frame_8.setVisible(False)
        self.ui.label_18.setVisible(False)

        if not os.path.exists("signature.html"):
            with open("signature.html", "w") as file:
                file.write("<html><body></body></html>")

        # Валидаторы
        self.ui.outlook_input_email_c.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-z]+\.[a-z]+$")))
        self.ui.outlook_input_email_cc.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-z]+\.[a-z]+$")))

    # Переключатель видимости
    def outlook_change_visible_settings(self):
        if self.ui.frame_8.isVisible():
            self.ui.frame_8.setVisible(False)
        else:
            self.ui.frame_8.setVisible(True)
    
    # Инициализация списка email в копию
    def outlook_init_copy_emails(self):
        self.ui.outlook_list_email_c.clear()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT outlook_copy_emails FROM outlook_copy_emails")
        items = cursor.fetchall()
        for elements in items:
            QListWidgetItem(format(elements[0]), self.ui.outlook_list_email_c)
        self.ui.outlook_list_email_c.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.outlook_list_email_c.setFixedHeight(self.ui.outlook_list_email_c.sizeHintForRow(0) * self.ui.outlook_list_email_c.count() + 2 * self.ui.outlook_list_email_c.frameWidth())
        db.commit()
        db.close()

    # Запись email в копию в базу
    def outlook_save_copy_emails(self):
        if self.ui.outlook_input_email_c.text() != '':
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("SELECT outlook_copy_emails FROM outlook_copy_emails WHERE outlook_copy_emails = ?", [self.ui.outlook_input_email_c.text().lower()])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO outlook_copy_emails(outlook_copy_emails) VALUES (?)", [self.ui.outlook_input_email_c.text().lower()])
                db.commit()
            self.ui.outlook_input_email_c.setText('')
            self.outlook_init_copy_emails()
            cursor.close()
            db.close()

    # Удаление записи email в копию по клику
    def outlook_delete_copy_emails(self, item):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("DELETE FROM outlook_copy_emails WHERE outlook_copy_emails = ?", [item.text()])
        db.commit()
        db.close()
        self.outlook_init_copy_emails()

    # Инициализация списка email в скрытую копию
    def outlook_init_ccopy_emails(self):
        self.ui.outlook_list_email_cc.clear()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("SELECT outlook_ccopy_emails FROM outlook_ccopy_emails")
        items = cursor.fetchall()
        for elements in items:
            QListWidgetItem(format(elements[0]), self.ui.outlook_list_email_cc)
        self.ui.outlook_list_email_cc.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.outlook_list_email_cc.setFixedHeight(self.ui.outlook_list_email_cc.sizeHintForRow(0) * self.ui.outlook_list_email_cc.count() + 2 * self.ui.outlook_list_email_cc.frameWidth())
        db.commit()
        db.close()

    # Запись email в скрытую копию в базу
    def outlook_save_ccopy_emails(self):
        if self.ui.outlook_input_email_cc.text() != '':
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("SELECT outlook_ccopy_emails FROM outlook_ccopy_emails WHERE outlook_ccopy_emails = ?", [self.ui.outlook_input_email_cc.text().lower()])
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO outlook_ccopy_emails(outlook_ccopy_emails) VALUES (?)", [self.ui.outlook_input_email_cc.text().lower()])
                db.commit()
            self.ui.outlook_input_email_cc.setText('')
            self.outlook_init_ccopy_emails()
            cursor.close()
            db.close()

    # Удаление записи email в скрытую копию по клику
    def outlook_delete_ccopy_emails(self, item):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("DELETE FROM outlook_ccopy_emails WHERE outlook_ccopy_emails = ?", [item.text()])
        db.commit()
        db.close()
        self.outlook_init_ccopy_emails()

    # Инициализация подписи
    def outlook_init_email_signature(self):
        with open("signature.html", "r") as file:
            html = file.read()
            self.ui.outlook_input_signature.setHtml(html)

    # Вставка изображения из буфера обмена
    def outlook_paste_signature_image(self):
        # self.ui.outlook_input_signature.insertHtml(QApplication.clipboard().text())
        clipboard = QApplication.clipboard()
        # if clipboard.mimeData().hasImage():
        #     image = clipboard.pixmap().toImage()
        #     cursor = self.ui.outlook_input_signature.textCursor()
        #     cursor.insertImage(image)
        if clipboard.mimeData().hasImage():
            self.ui.outlook_input_signature.insertHtml('<br>')
            image = QImage(clipboard.mimeData().imageData())
            image.save("signature.png")
            self.ui.outlook_input_signature.insertHtml('<img src="signature.png"/>')
        # elif clipboard.mimeData().hasHtml():
        #     html = clipboard.mimeData().html()
        #     self.ui.outlook_input_signature.insertHtml(html)
        # else:
        #     text = clipboard.mimeData().text()
        #     self.ui.outlook_input_signature.insertPlainText(text)

    # Запись подписи в базу
    def outlook_save_email_signature(self):
        if self.ui.outlook_input_signature.toPlainText() != '':
            with open("signature.html", "w") as file:
                file.write(self.ui.outlook_input_signature.toHtml())
            with open("signature.html", "r") as file:
                signature = file.read()
            signature = signature.replace("margin-top:12px;", "margin-top:0px;")
            signature = signature.replace("margin-bottom:12px;", "margin-bottom:0px;")
            with open("signature.html", "w") as file:
                file.write(signature)
            self.outlook_init_email_signature()
            self.ui.label_18.setVisible(True)
            QTimer.singleShot(3000, self.ui.label_18.hide)


    # Удаление подписи
    def outlook_delete_email_signature(self):
        with open("signature.html", "w") as file:
            file.write("")
        self.outlook_init_email_signature()

    # os.environ["Outlook_VSTO_PowerPoint_Add-In_Path"] = "C:\Program Files\Microsoft Office\root\Office16"
    # Отправка приемки
    def outlook_send_acceptance(self):
        if not (self.ui.acceptance_btn_copy_1.text() == '' and (self.ui.acceptance_btn_copy_2.text() == '' and self.ui.acceptance_comboBox_2.currentText() == '')):
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("SELECT outlook_copy_emails FROM outlook_copy_emails")
            cc_emails = cursor.fetchall()
            cc = "; ".join([email[0] for email in cc_emails])
            cursor.execute("SELECT outlook_ccopy_emails FROM outlook_ccopy_emails")
            bcc_emails = cursor.fetchall()
            bcc = "; ".join([email[0] for email in bcc_emails])
            cursor.execute("SELECT providers_email_acceptances FROM providers where providers = ?", [self.ui.acceptance_comboBox_2.currentText()])
            providers_email_acceptances = cursor.fetchone()[0]
            outlook = win32com.client.Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)
            mail.To = providers_email_acceptances
            mail.CC = cc
            mail.BCC = bcc
            mail.Subject = self.ui.acceptance_btn_copy_1.text()
            text = self.ui.acceptance_btn_copy_2.text().replace("\n", "<br>")
            with open("signature.html", "r") as file:
                signature = file.read()
            signature = signature.replace('<img src="signature.png" />', "")
            mail.HTMLBody = '<html><body>' + text + signature + "<br>" + "<img src='" + os.path.abspath("signature.png") + "'>" + '</body></html>'
            mail.Send()
            self.acceptance.acceptance_clr()

    def outlook_send_order(self):
        if not (self.ui.orders_pushButton_2.text() == '' and (self.ui.orders_pushButton_3.text() == '' and self.ui.orders_comboBox_13.currentText() == '')):
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("SELECT outlook_copy_emails FROM outlook_copy_emails")
            cc_emails = cursor.fetchall()
            cc = "; ".join([email[0] for email in cc_emails])
            cursor.execute("SELECT outlook_ccopy_emails FROM outlook_ccopy_emails")
            bcc_emails = cursor.fetchall()
            bcc = "; ".join([email[0] for email in bcc_emails])
            cursor.execute("SELECT providers_email_orders FROM providers where providers = ?", [self.ui.orders_comboBox_13.currentText()])
            providers_email_acceptances = cursor.fetchone()[0]
            outlook = win32com.client.Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)
            mail.To = providers_email_acceptances
            mail.CC = cc
            mail.BCC = bcc
            mail.Subject = self.ui.orders_pushButton_2.text()
            text = self.ui.orders_pushButton_3.text().replace("\n", "<br>")
            with open("signature.html", "r") as file:
                signature = file.read()
            signature = signature.replace('<img src="signature.png" />', "")
            mail.HTMLBody = '<html><body>' + text + signature + "<br>" + "<img src='" + os.path.abspath("signature.png") + "'>" + '</body></html>'
            mail.Send()
            self.orders.order_clear()