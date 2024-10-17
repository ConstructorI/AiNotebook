import sys

from gradio_client import Client
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QTextCursor, QPixmap, QPainter, QIcon, QBrush, QPen, QTextCharFormat, QFont

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.ui_main.textEdit.setCurrentFont("Arial")
        self.ui_main.textEdit.setFontPointSize(12)
        self.current_color = Qt.white
        self.update_button_color()
        self.ui_main.textEdit.setContentsMargins(50, 50, 50, 50)
        self.ui_main.comboBox_size.setCurrentIndex(3)
        self.cursor = QTextCursor()
        self.ui_main.label_2.setHidden(True)
        self.current_file = None
        self.act()

    def act(self):
        self.ui_main.comboBox_size.activated.connect(lambda: self.choose_fontsize())
        self.ui_main.comboBox_font.activated.connect(lambda: self.choose_font())
        self.ui_main.pushButton_textcolor.clicked.connect(lambda: self.text_color())

        self.ui_main.pushButton_bold.clicked.connect(lambda: self.choose_font_bold())
        self.ui_main.pushButton_italic.clicked.connect(lambda: self.choose_font_italic())
        self.ui_main.pushButton_underline.clicked.connect(lambda: self.choose_font_underline())

        self.ui_main.pushButton_alignleft.clicked.connect(lambda: self.choose_alignleft())
        self.ui_main.pushButton_aligncenter.clicked.connect(lambda: self.choose_aligncenter())
        self.ui_main.pushButton_alignright.clicked.connect(lambda: self.choose_alignright())
        self.ui_main.pushButton_alignjust.clicked.connect(lambda: self.choose_alignjust())

        self.ui_main.pushButton_AI.clicked.connect(lambda: self.transfer_to_AI())

        self.ui_main.pushButton_new.clicked.connect(lambda: self.new_text_edit_content())
        self.ui_main.pushButton_save.clicked.connect(lambda: self.save_text_edit_content())
        self.ui_main.pushButton_open.clicked.connect(lambda: self.load_text_edit_content())

        self.ui_main.pushButton_clear.clicked.connect(lambda: self.clear())
        self.ui_main.pushButton_gen.clicked.connect(lambda: self.gen())

    def choose_font(self):
        default_format = QTextCharFormat()
        default_format.setFont(QFont(self.ui_main.comboBox_font.currentText(),
                                     int(self.ui_main.comboBox_size.currentText())))
        default_format.setForeground(self.current_color)
        self.ui_main.textEdit.setCurrentCharFormat(default_format)

    def choose_fontsize(self):
        default_format = QTextCharFormat()
        default_format.setFont(QFont(self.ui_main.comboBox_font.currentText(),
                                     int(self.ui_main.comboBox_size.currentText())))
        default_format.setForeground(self.current_color)
        self.ui_main.textEdit.setCurrentCharFormat(default_format)

    def text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.current_color = color
            default_format = QTextCharFormat()
            default_format.setFont(QFont(self.ui_main.comboBox_font.currentText(),
                                         int(self.ui_main.comboBox_size.currentText())))
            default_format.setForeground(self.current_color)
            self.ui_main.textEdit.setCurrentCharFormat(default_format)
            self.update_button_color()

    def update_button_color(self):
        img = self.create_gradient_pixmap(15, 15)
        icon = QIcon(img)
        self.ui_main.pushButton_textcolor.setIcon(icon)
        self.ui_main.pushButton_textcolor.setIconSize(img.size())

    def create_gradient_pixmap(self, width, height):
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        fill = QBrush(self.current_color)
        painter.fillRect(0, 0, width, height, fill)

        border_pen = QPen(Qt.black, 1)
        painter.setPen(border_pen)
        painter.drawRect(0, 0, width - 1, height - 1)

        painter.end()
        return pixmap

    def choose_font_bold(self):
        if self.ui_main.textEdit.fontWeight() == 400:
            self.ui_main.textEdit.setFontWeight(600)
        else:
            self.ui_main.textEdit.setFontWeight(400)

    def choose_font_italic(self):
        if self.ui_main.textEdit.fontItalic():
            self.ui_main.textEdit.setFontItalic(False)
        else:
            self.ui_main.textEdit.setFontItalic(True)

    def choose_font_underline(self):
        if self.ui_main.textEdit.fontUnderline():
            self.ui_main.textEdit.setFontUnderline(False)
        else:
            self.ui_main.textEdit.setFontUnderline(True)

    def choose_alignleft(self):
        self.ui_main.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def choose_aligncenter(self):
        self.ui_main.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def choose_alignright(self):
        self.ui_main.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def choose_alignjust(self):
        self.ui_main.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def transfer_to_AI(self):
        self.cursor = self.ui_main.textEdit.textCursor()
        self.ui_main.textEdit_AI.setHtml(self.cursor.selectedText())

    def new_text_edit_content(self):
        html_content = self.ui_main.textEdit.toHtml()
        if self.current_file is not None:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(html_content)
            except FileNotFoundError:
                pass
        new_file = QFileDialog.getSaveFileUrl(self, "Создать", "", "html (*.html);;Все файлы (*)")
        self.current_file = new_file[0].toLocalFile()
        self.ui_main.statusBar.showMessage(self.current_file)
        self.ui_main.textEdit.clear()

    def save_text_edit_content(self):
        html_content = self.ui_main.textEdit.toHtml()
        if self.current_file is not None:
            if self.current_file != "":
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(html_content)
        else:
            save_file = QFileDialog.getSaveFileUrl(self, "Сохранить", "", "html (*.html);;Все файлы (*)")
            self.current_file = save_file[0].toLocalFile()
            if save_file[0].toLocalFile() != "":
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(html_content)

    def load_text_edit_content(self):
        open_file = QFileDialog.getOpenFileUrl(self, "Открыть", "", "html (*.html);;Все файлы (*)")
        self.current_file = open_file[0].toLocalFile()
        if open_file[0].toLocalFile() != "":
            with open(open_file[0].toLocalFile(), 'r', encoding='utf-8') as file:
                html_content = file.read()
            self.ui_main.textEdit.setHtml(html_content)
        self.ui_main.statusBar.showMessage(self.current_file)

    def gen(self):
        self.ui_main.pushButton_clear.setHidden(True)
        self.ui_main.pushButton_gen.setHidden(True)
        self.ui_main.label_2.setHidden(False)
        self.wait = WaitingDialog()
        self.wait.query = "Вот текст: " + self.ui_main.textEdit_AI.toPlainText() + \
                          "\nВот что с ним делать: " + self.ui_main.plainTextEdit.toPlainText() + \
                          "\nОТВЕЧАЙ, ИСПОЛЬЗУЯ РАЗМЕТКУ HTML, но НЕ выделяй при помощи ```html ```"
        self.wait.mes.connect(self.gen_end)
        self.wait.start()

    def gen_end(self, message):
        self.ui_main.textEdit_AI.clear()
        self.ui_main.textEdit_AI.setHtml(message)
        self.ui_main.pushButton_clear.setHidden(False)
        self.ui_main.pushButton_gen.setHidden(False)
        self.ui_main.label_2.setHidden(True)

    def clear(self):
        self.ui_main.textEdit_AI.clear()
        self.ui_main.plainTextEdit.clear()


class WaitingDialog(QThread):
    mes = Signal(str)
    query = ""

    def run(self):
        client = Client("Qwen/Qwen2-72b-Instruct")
        result = client.predict(
            query=self.query,
            history=[],
            system="You are a helpful assistant.",
            api_name="/model_chat"
        )
        second_element = result[1]
        nested_list = second_element[0]
        result = nested_list[1].strip('"')
        print(result)
        self.mes.emit(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
