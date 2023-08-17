import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as mb
import fitz
import os
from PyQt6.QtWidgets import QApplication
import asyncio
import concurrent.futures


class converter:
    def __init__(self, ui):
        self.ui = ui
        self.clipboard = QApplication.clipboard()

########################################################
################ Работает ##############################
########################################################

    def convert_pdf2img(self):
        # Сброс прогресс бара
        self.ui.other_progressBar.setValue(0)
        # Создаем корневое окно tkinter
        root = tk.Tk()
        root.withdraw()
        # Открываем диалоговое окно выбора файлов
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")], title="Выбор файлов PDF для конвертации")
        # Проверка на выбраны файлы или нет
        if not file_paths:
            return
        # Выводим список выбранных файлов
        PDF_list = list(file_paths)
        # Альтернативны выбор пути сохранения изображений
        output_dir = filedialog.askdirectory(title="Выбор папки для сохранения изображений")
        if not output_dir:
            return
        # Перебор по файлам пдф
        output_files = []
        for input_PDF in PDF_list:
            # Открываем PDF
            PDF = fitz.open(input_PDF)
            # Перебираем страницы в одном фале пдф
            for pg in range(PDF.page_count):
                # Выберем страницу
                page = PDF[pg]
                # Делаем снимок
                zoom_x = 8
                zoom_y = 8
                mat = fitz.Matrix(zoom_x, zoom_y)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                # Именуем изображение
                output_file = f"{os.path.splitext(os.path.basename(input_PDF))[0]}_page{pg+1}.jpg"
                # Составляем список изображений
                output_files.append(output_file)
                # Альтернативное сохранение в выбранную директорию
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                temp_file = os.path.join(output_dir, output_file) # файл = (путь, файл)
                # Сохраняем изображение
                pix.save(temp_file)
                # Прогресс бар
                self.ui.other_progressBar.setValue(len(output_files) / (PDF.page_count * len(PDF_list)) * 100) 
            PDF.close()
        # Диалоговое окно
        mb.showinfo("Информация", "PDF сконвертированы")
        self.ui.other_progressBar.setValue(0)

########################################################
############## Не работает   ###########################
########################################################

    # Асинхронный конвертер
    async def get_pdf_and_output_dir(self):
        # Открываем диалоговые окна для выбора файлов PDF и папки для сохранения изображений
        root = tk.Tk()
        root.withdraw()
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")], title="Выбор файлов PDF для конвертации")
        if not file_paths:
            return None, None
        PDF_list = list(file_paths)
        output_dir = filedialog.askdirectory(title="Выбор папки для сохранения изображений")
        if not output_dir:
            return None, None
        return PDF_list, output_dir

    async def convert_pdf_to_img(self, input_PDF, output_dir):
        # Открываем PDF файл и конвертируем его в изображения
        PDF = fitz.open(input_PDF)
        output_files = []
        for pg in range(PDF.page_count):
            page = PDF[pg]
            zoom_x = 8
            zoom_y = 8
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            # Генерируем имя файла из названия PDF файла и номера страницы
            output_file = f"{os.path.splitext(os.path.basename(input_PDF))[0]}_page{pg+1}.jpg"
            output_files.append(output_file)
            # Создаем папку для сохранения изображений, если ее еще нет
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            temp_file = os.path.join(output_dir, output_file)
            pix.save(temp_file)
            # Обновляем прогресс-бар
            self.ui.other_progressBar.setValue(len(output_files) / (PDF.page_count) * 100) 
        PDF.close()
        return output_files

    async def as_convert_pdf2img(self):
        # Сбрасываем значение прогресс-бара на 0
        self.ui.other_progressBar.setValue(0)
        # Получаем список файлов PDF и папку для сохранения изображений
        PDF_list, output_dir = await self.get_pdf_and_output_dir()
        if not PDF_list or not output_dir:
            return
        tasks = []
        # Запускаем асинхронную функцию конвертации для каждого PDF файла
        for input_PDF in PDF_list:
            task = asyncio.create_task(self.convert_pdf_to_img(input_PDF, output_dir))
            tasks.append(task)
        # Дожидаемся завершения всех задач и собираем результаты
        results = await asyncio.gather(*tasks)
        # Выводим сообщение об успешном завершении конвертации
        mb.showinfo("Информация", "PDF сконвертированы")
        # Сбрасываем значение прогресс-бара на 0
        self.ui.other_progressBar.setValue(0)

########################################################
############## Не работает   ###########################
########################################################

# Асинхронны конвертер с многопоточностью
    async def get_pdf_files(self):
        root = tk.Tk()
        root.withdraw()
        file_paths = await asyncio.to_thread(lambda: filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")], title="Выбор файлов PDF для конвертации"))
        return list(file_paths)

    async def as_m_convert_pdf2img(self, input_PDF, output_dir):
        PDF = fitz.open(input_PDF)
        output_files = []
        for pg in range(PDF.page_count):
            page = PDF[pg]
            zoom_x = 8
            zoom_y = 8
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            output_file = f"{os.path.splitext(os.path.basename(input_PDF))[0]}_page{pg+1}.jpg"
            output_files.append(output_file)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            temp_file = os.path.join(output_dir, output_file)
            pix.save(temp_file)
        PDF.close()
        return output_files

    async def as_thr_convert_pdf2img(self):
        self.ui.other_progressBar.setValue(0)
        PDF_list = await self.get_pdf_files()
        output_dir = await asyncio.to_thread(lambda: filedialog.askdirectory(title="Выбор папки для сохранения изображений"))
        if not output_dir:
            return
        tasks = []
        with concurrent.futures.ThreadPoolExecutor() as pool:
            loop = asyncio.get_running_loop()
            for input_PDF in PDF_list:
                task = loop.run_in_executor(pool, self.convert_pdf2img, input_PDF, output_dir)
                tasks.append(task)
        output_files_list = await asyncio.gather(*tasks)
        output_files = [f for files in output_files_list for f in files]
        mb.showinfo("Информация", "PDF сконвертированы")
        self.ui.other_progressBar.setValue(0)

########################################################

    # Подбор ширины и высоты пачек для приемки
    def selection(self):
        # Константы
        base_height = 0.01
        base_width = 0.01
        lenght = float(self.ui.other_input_lenght_1.text().replace(',', '.'))
        value = float(self.ui.other_input_value_1.text().replace(',', '.'))
        height_limiter = 2.37
        width_limiter = 2.37

        # Математика
        if lenght != 0 and value != 0:
            height_and_width = []
            while base_height <= height_limiter and base_width <= width_limiter:
                while base_width <= width_limiter:
                    if round(round(base_height, 2) * round(base_width, 2) * round(lenght, 2), 2) == round(value, 2):
                        # self.ui.other_list_1.addItem(f'Ширина: {round(base_height, 2)} Высота: {round(base_width, 2)}')
                        height_and_width.append(f'Ширина: {round(base_height, 2)}, Высота: {round(base_width, 2)}')
                        base_width = round(base_width, 2) + 0.01
                    else:
                        base_width = round(base_width, 2) + 0.01
                base_height = round(base_height, 2) + 0.01
                base_width = 0.01
        
        # Вывод в лист
        if height_and_width != []:
            for i in range(len(height_and_width) // 2 + 1):
                self.ui.other_list_1.addItem(height_and_width[i])

    # Вывод в окошки для копирования по клику
    def item_for_copy(self, item):
        self.ui.other_copy_1.setText(item.text().split(', ')[0][7:])
        self.ui.other_copy_2.setText(item.text().split(', ')[1][7:])

    # Копирование в буфер обмена
    def btn_copy_1(self):
        self.clipboard.setText(self.ui.other_copy_1.text())
    def btn_copy_2(self):
        self.clipboard.setText(self.ui.other_copy_2.text())

    # Переключатель длины
    def lenght_selection_1(self):
        if self.ui.other_radioButton_lenght_1.isChecked():
            self.ui.other_input_lenght_1.setValue(3)
    def lenght_selection_2(self):
        if self.ui.other_radioButton_lenght_2.isChecked():
            self.ui.other_input_lenght_1.setValue(6)