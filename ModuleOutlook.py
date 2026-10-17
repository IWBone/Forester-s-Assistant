import win32com.client
from PyQt6.QtWidgets import QListWidgetItem, QApplication
from PyQt6.QtGui import QRegularExpressionValidator, QClipboard, QImage
from PyQt6.QtCore import QRegularExpression, QTimer, Qt, QByteArray, QBuffer, QIODevice
from ModuleAcceptance import Acceptance
from ModuleOrders import Orders

from ModuleDB import get_db, get_app_dir
import os
import base64

class Outlook:
    def __init__(self, ui):
        self.ui = ui
        self.acceptance = Acceptance(ui)
        self.orders = Orders(ui)

        self.ui.frame_8.setVisible(False)
        self.ui.label_18.setVisible(False)




        # Пути к файлам подписи в директории приложения
        self.html_path = os.path.join(get_app_dir(), "signature.html")
        self.png_path = os.path.join(get_app_dir(), "signature.png")

        # Создание signature.html, если его нет
        if not os.path.exists(self.html_path):
            with open(self.html_path, "w") as file:
                file.write("<html><body><p>С уважением,</p><br><img src=\"signature.png\"></body></html>")

        # Создание пустого signature.png, если его нет
        if not os.path.exists(self.png_path):
            empty_png = b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
            with open(self.png_path, "wb") as file:
                file.write(base64.b64decode(empty_png))

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
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email_pref = 'cc'")
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(elements[0]), self.ui.outlook_list_email_c)
            self.ui.outlook_list_email_c.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            self.ui.outlook_list_email_c.setFixedHeight(self.ui.outlook_list_email_c.sizeHintForRow(0) * self.ui.outlook_list_email_c.count() + 2 * self.ui.outlook_list_email_c.frameWidth())

    # Запись email в копию в базу
    def outlook_save_copy_emails(self):
        if self.ui.outlook_input_email_c.text() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email = ? AND outlook_email_pref = 'cc'", [self.ui.outlook_input_email_c.text().lower()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO outlook_email(outlook_email, outlook_email_pref) VALUES (?, 'cc')", [self.ui.outlook_input_email_c.text().lower()])
                    db.commit()
            self.ui.outlook_input_email_c.setText('')
            self.outlook_init_copy_emails()

    # Удаление записи email в копию по клику
    def outlook_delete_copy_emails(self, item):
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM outlook_email WHERE outlook_email = ? AND outlook_email_pref = 'cc'", [item.text()])
            db.commit()
        self.outlook_init_copy_emails()

    # Инициализация списка email в скрытую копию
    def outlook_init_ccopy_emails(self):
        self.ui.outlook_list_email_cc.clear()
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email_pref = 'bcc'")
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(elements[0]), self.ui.outlook_list_email_cc)
            self.ui.outlook_list_email_cc.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            self.ui.outlook_list_email_cc.setFixedHeight(self.ui.outlook_list_email_cc.sizeHintForRow(0) * self.ui.outlook_list_email_cc.count() + 2 * self.ui.outlook_list_email_cc.frameWidth())

    # Запись email в скрытую копию в базу
    def outlook_save_ccopy_emails(self):
        if self.ui.outlook_input_email_cc.text() != '':
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email = ? AND outlook_email_pref = 'bcc'", [self.ui.outlook_input_email_cc.text().lower()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO outlook_email(outlook_email, outlook_email_pref) VALUES (?, 'bcc')", [self.ui.outlook_input_email_cc.text().lower()])
                    db.commit()
            self.ui.outlook_input_email_cc.setText('')
            self.outlook_init_ccopy_emails()

    # Удаление записи email в скрытую копию по клику
    def outlook_delete_ccopy_emails(self, item):
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM outlook_email WHERE outlook_email = ? AND outlook_email_pref = 'bcc'", [item.text()])
            db.commit()
        self.outlook_init_ccopy_emails()

    # Инициализация подписи
    def outlook_init_email_signature(self):

        with open(self.html_path, "r") as file:
            html = file.read()
            self.ui.outlook_input_signature.setHtml(html)

    # Вставка изображения из буфера обмена
    def outlook_paste_signature_image(self):
        clipboard = QApplication.clipboard()
        if clipboard.mimeData().hasImage():
            self.ui.outlook_input_signature.insertHtml('<br>')
            image = QImage(clipboard.mimeData().imageData())
            
            # Сохранение изображения в QByteArray в формате PNG
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.OpenModeFlag.WriteOnly)
            image.save(buffer, "PNG")
            buffer.close()
            
            # Преобразование в Base64
            b64_string = byte_array.toBase64().data().decode()
            
            # Вставка изображения как Data URL
            self.ui.outlook_input_signature.insertHtml(f'<img src="data:image/png;base64,{b64_string}"/>')

    # Сохранение подписи
    def outlook_save_email_signature(self):
        if self.ui.outlook_input_signature.toPlainText() != '':
            with open(self.html_path, "w") as file:
                file.write(self.ui.outlook_input_signature.toHtml())
            with open(self.html_path, "r") as file:
                signature = file.read()
            signature = signature.replace("margin-top:12px;", "margin-top:0px;")
            signature = signature.replace("margin-bottom:12px;", "margin-bottom:0px;")
            with open(self.html_path, "w") as file:
                file.write(signature)
            self.outlook_init_email_signature()
            self.ui.label_18.setVisible(True)
            QTimer.singleShot(3000, self.ui.label_18.hide)

    # Удаление подписи
    def outlook_delete_email_signature(self):
        with open(self.html_path, "w") as file:
            file.write("")
        self.outlook_init_email_signature()

    # Отправка приемки
    def outlook_send_acceptance(self):
        if not (self.ui.acceptance_btn_copy_1.text() == '' and (self.ui.acceptance_btn_copy_2.text() == '' and self.ui.acceptance_comboBox_2.currentText() == '')):
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email_pref = 'cc'")
                cc_emails = cursor.fetchall()
                cc = "; ".join([email[0] for email in cc_emails])
                cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email_pref = 'bcc'")
                bcc_emails = cursor.fetchall()
                bcc = "; ".join([email[0] for email in bcc_emails])
                cursor.execute("SELECT provider_email_acceptance FROM providers where provider = ?", [self.ui.acceptance_comboBox_2.currentText()])
                providers_email_acceptances = cursor.fetchone()[0]
            outlook = win32com.client.Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)
            mail.To = providers_email_acceptances
            mail.CC = cc
            mail.BCC = bcc
            mail.Subject = self.ui.acceptance_btn_copy_1.text()
            text = self.ui.acceptance_btn_copy_2.text().replace("\n", "<br>")
            with open(self.html_path, "r") as file:
                signature = file.read()
            signature = signature.replace('<img src="signature.png" />', "")
            mail.HTMLBody = '<html><body>' + text + signature + "<br>" + "<img src='" + self.png_path + "'>" + '</body></html>'
            mail.Send()
            self.acceptance.acceptance_clr()

    def outlook_send_order(self):
        if not (self.ui.orders_pushButton_2.text() == '' and (self.ui.orders_pushButton_3.text() == '' and self.ui.orders_comboBox_13.currentText() == '')):
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email_pref = 'cc'")
                cc_emails = cursor.fetchall()
                cc = "; ".join([email[0] for email in cc_emails])
                cursor.execute("SELECT outlook_email FROM outlook_email WHERE outlook_email_pref = 'bcc'")
                bcc_emails = cursor.fetchall()
                bcc = "; ".join([email[0] for email in bcc_emails])
                cursor.execute("SELECT provider_email_order FROM providers where provider = ?", [self.ui.orders_comboBox_13.currentText()])
                providers_email_acceptances = cursor.fetchone()[0]
            outlook = win32com.client.Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)
            mail.To = providers_email_acceptances
            mail.CC = cc
            mail.BCC = bcc
            mail.Subject = self.ui.orders_pushButton_2.text()
            text = self.ui.orders_pushButton_3.text().replace("\n", "<br>")
            with open(self.html_path, "r") as file:
                signature = file.read()
            signature = signature.replace('<img src="signature.png" />', "")
            mail.HTMLBody = '<html><body>' + text + signature + "<br>" + "<img src='" + self.png_path + "'>" + '</body></html>'
            mail.Send()
            self.orders.order_clear()
