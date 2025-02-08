from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QSlider, QTextEdit
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap

import pygame   #仅用来播放音乐

BUTTON_STYLE = """
QPushButton {
    border-radius: 5px;
    background-color: #00aaff;
    color: white;
}

QPushButton:hover {
    background-color: #0088cc;
}
"""

WIDTH = 600
HEIGHT = 400

WINDOW_TITLE = "NIGHTMARE ASSISTANT"

FONT = "SF Pro"
FONT_SIZE = 14


class UiTmpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("the program is processing...")
        font = QFont(FONT, 16, QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        central_widget.setLayout(layout)

    def go_to_next_window(self):
        QTimer.singleShot(3000, self.switch_to_next_window)

    def switch_to_next_window(self):
        self.hide()
        self.next_window.show()


class Ui1Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget(self)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Welcome to the Nightmare Coaching Program!\n")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont(FONT, 20, QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.bt_start = QPushButton("Start")
        self.bt_start.setFixedSize(60, 30)
        layout.addWidget(self.bt_start, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


class Ui2Choices(QMainWindow):
    pass


class Ui3aTitle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("What is your nightmare about?")
        font = QFont(FONT, FONT_SIZE, QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setPlaceholderText("please give a short title")
        self.input.setFixedSize(210, 20)
        layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.bt_save = QPushButton("Save")
        self.bt_save.setFixedSize(60, 30)
        layout.addWidget(self.bt_save, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)


class Ui3bReadFile(QMainWindow):
    pass


class Ui4PreSurvey(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("On a scale of 0-10, how scared does your nightmare make you feel?")
        font = QFont(FONT, FONT_SIZE, QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.label2 = QLabel("0 - Neutral\n10 - Highest possible")
        font2 = QFont(FONT, 11)
        self.label2.setFont(font2)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label2)

        self.dynamic_label = QLabel("\n Value: 0")
        font3 = QFont(FONT, 12)
        self.dynamic_label.setFont(font3)
        self.dynamic_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.dynamic_label)

        self.horizontal_slider = QSlider(Qt.Orientation.Horizontal)
        self.horizontal_slider.setMinimum(0)
        self.horizontal_slider.setMaximum(10)
        self.horizontal_slider.setValue(0)
        self.horizontal_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontal_slider.setTickInterval(1)
        self.horizontal_slider.setFixedSize(450, 20)
        layout.addWidget(self.horizontal_slider)

        self.horizontal_slider.valueChanged.connect(self.update_label)

        self.bt_continue = QPushButton("Continue")
        self.bt_continue.setFixedSize(85, 30)
        layout.addWidget(self.bt_continue, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)

    def update_label(self, value):
        self.dynamic_label.setText(f"\nValue: {value}")


class Ui5Describe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_title = QLabel("Could you describe your nightmare?")
        font = QFont(FONT, FONT_SIZE, QFont.Weight.Bold)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label_title)

        self.input_begin = QLineEdit()
        self.input_begin.setPlaceholderText("how does it begin?")
        layout.addWidget(self.input_begin)

        self.input_continue = QLineEdit()
        self.input_continue.setPlaceholderText("how does it continue?")
        layout.addWidget(self.input_continue)

        self.input_end = QLineEdit()
        self.input_end.setPlaceholderText("how does it end?")
        layout.addWidget(self.input_end)

        self.input_feeling = QLineEdit()
        self.input_feeling.setPlaceholderText("how were you feeling?")
        layout.addWidget(self.input_feeling)

        self.input_details = QLineEdit()
        self.input_details.setPlaceholderText("any other details?")
        layout.addWidget(self.input_details)

        layout.addSpacing(20)

        self.bt_continue = QPushButton("Continue")
        self.bt_continue.setFixedSize(85, 30)
        layout.addWidget(self.bt_continue, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)


class Ui6Identify(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_title = QLabel("Well done!")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_title = QFont(FONT, FONT_SIZE, QFont.Weight.Bold)
        self.label_title.setFont(font_title)
        layout.addWidget(self.label_title)

        self.label_description = QLabel("Sounds like your nightmare? Feel free to edit if necessary!")
        self.label_description.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_description = QFont(FONT, 12)
        self.label_description.setFont(font_description)
        layout.addWidget(self.label_description)

        self.text_nightmare = QTextEdit()
        self.text_nightmare.setText("no text yet")
        layout.addWidget(self.text_nightmare)

        self.label_negative = QLabel(
            "Now, could you identify the negative elements on it?\nCopy and paste the negative elements below."
        )
        self.label_negative.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_negative.setFont(font_description)
        layout.addWidget(self.label_negative)

        self.text_negative_elements = QTextEdit()
        layout.addWidget(self.text_negative_elements)

        self.bt_done = QPushButton("Done")
        self.bt_done.setFixedSize(60, 30)
        layout.addWidget(self.bt_done, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)


class Ui7Replace(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_title = QLabel("Magic!")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_title = QFont(FONT, FONT_SIZE, QFont.Weight.Bold)
        self.label_title.setFont(font_title)
        layout.addWidget(self.label_title)

        self.label_instruction1 = QLabel(
            "Based on the list of negative elements, I’ve removed all the unpleasant parts from your nightmare. "
            "Don’t worry if something is left out—you have the power to reshape your dream anytime you want."
        )

        self.label_instruction1.setWordWrap(True)
        self.label_instruction1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_instruction = QFont(FONT, 12)
        self.label_instruction1.setFont(font_instruction)
        layout.addWidget(self.label_instruction1)

        self.label_instruction2 = QLabel(
            "Now, let’s fill it with positive elements to create your favourite dream! "
            "Remember, in dreams, anything is possible, and you’re in control. "
            "Feel free to add or remove details as you wish."
        )
        self.label_instruction2.setWordWrap(True)
        self.label_instruction2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_instruction2.setFont(font_instruction)
        layout.addWidget(self.label_instruction2)

        self.edited_dream = QTextEdit()
        self.edited_dream.setText("no text yet")
        layout.addWidget(self.edited_dream)

        self.bt_done = QPushButton("Done")
        self.bt_done.setFixedSize(60, 30)
        layout.addWidget(self.bt_done, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)


class Ui8Write(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_title = QLabel("Great job!")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_title = QFont(FONT, 14, QFont.Weight.Bold)
        self.label_title.setFont(font_title)
        layout.addWidget(self.label_title)

        self.label_instruction = QLabel(
            "You're almost there—just one last step to complete your dream!\n"
            "Read it again and add some final touches. Make sure it has a happy ending!"
        )
        self.label_instruction.setWordWrap(True)
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_instruction = QFont(FONT, 12)
        self.label_instruction.setFont(font_instruction)
        layout.addWidget(self.label_instruction)

        self.text_edit = QTextEdit()
        self.text_edit.setText("no text yet")
        layout.addWidget(self.text_edit)

        self.bt_finish = QPushButton("Finish")
        self.bt_finish.setFixedSize(60, 30)
        layout.addWidget(self.bt_finish, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)


class Ui9PostSurvey(QMainWindow):
    pass


class Ui10Choices(QMainWindow):
    pass


class Ui11aSaveResults(QMainWindow):
    pass


class Ui11bEnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet(BUTTON_STYLE)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())

        img = QPixmap("file/end.png").scaled(self.label.width(), self.label.height())
        self.label.setPixmap(img)

    def start_music(self):
        song_name = r"file/end.mp3"
        pygame.init()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play()