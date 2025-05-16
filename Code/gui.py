from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStatusBar, QProgressBar, QLineEdit, QSlider, QTextEdit
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

BUTTON_STYLE = """
QPushButton {
    border-radius: 5px;
    background-color: #00aaff;
    color: white;
    font-size: 10pt;
    text-transform: uppercase;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #0088cc;
}
"""

FONT = "SF Pro"
FONT_SIZE = 14

'''Each window corresponds to a UI class.'''

class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NIGHTMARE ASSISTANT")
        self.resize(600, 400)
        self.setStyleSheet(BUTTON_STYLE)


class Ui1Start(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        self.bt_start = None
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        self.label = QLabel("WELCOME TO THE NIGHTMARE\nCOACHING PROGRAM! 😴")
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


class Ui2Choices(BaseWindow):
    def __init__(self):
        super().__init__()
        self.bt_scratch = None
        self.bt_read_file = None
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bt_scratch = QPushButton("From scratch")
        self.bt_scratch.setFixedSize(120, 30)
        self.bt_read_file = QPushButton("Read from a file")
        self.bt_read_file.setFixedSize(120, 30)

        layout.addWidget(self.bt_scratch, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)
        layout.addWidget(self.bt_read_file, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


class Ui3aTitle(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        self.input = None
        self.bt_save = None
        self.setup_ui()

    def setup_ui(self):
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

        # status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().setStatusTip('10/100%')

        self.progress = QProgressBar()
        self.progress.setValue(10)
        self.status.addPermanentWidget(self.progress)

        central_widget.setLayout(layout)

    def get_title(self):
        return self.input.text()


class Ui3bReadFile(Ui3aTitle):
    def __init__(self):
        super().__init__()
        self.bt_read = None
        self.modify_ui()

    def modify_ui(self):
        self.label.setText("Please enter the file name:")
        self.input.setPlaceholderText("")
        self.input.setFixedSize(180, 20)

        self.bt_read = self.bt_save
        self.bt_read.setText("Read")

    def get_filename(self):
        return self.input.text()


class Ui4PreSurvey(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        self.label2 = None
        self.dynamic_label = None
        self.horizontal_slider = None
        self.bt_continue = None
        self.value = None
        self.setup_ui()

    def setup_ui(self):
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

        self.dynamic_label = QLabel(f"\nValue: 0")
        font3 = QFont(FONT, 12)
        self.dynamic_label.setFont(font3)
        self.dynamic_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.dynamic_label)

        self.horizontal_slider = QSlider(Qt.Orientation.Horizontal)
        self.horizontal_slider.setMinimum(0)
        self.horizontal_slider.setMaximum(10)
        self.horizontal_slider.setFixedSize(450, 20)
        layout.addWidget(self.horizontal_slider)

        self.horizontal_slider.valueChanged.connect(self.update_label)

        self.bt_continue = QPushButton("Continue")
        self.bt_continue.setFixedSize(85, 30)
        layout.addWidget(self.bt_continue, alignment=Qt.AlignmentFlag.AlignCenter)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().setStatusTip('20/100%')

        self.progress = QProgressBar()
        self.progress.setValue(20)
        self.status.addPermanentWidget(self.progress)

        central_widget.setLayout(layout)

    def update_label(self, value):
        self.dynamic_label.setText(f"\nValue: {value}")
        self.value = value

    def get_survey_value(self):
        return self.value


class Ui5Describe(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label_title = None
        self.input_begin = None
        self.input_continue = None
        self.input_end = None
        self.input_details = None
        self.input_feeling = None
        self.bt_continue = None
        self.setup_ui()

    def setup_ui(self):
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

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().setStatusTip('1/4 Describe')

        self.progress = QProgressBar()
        self.progress.setValue(30)
        self.status.addPermanentWidget(self.progress)

        central_widget.setLayout(layout)

    def get_narrative_details(self):
        narrative_details = [
            self.input_begin.text(),
            self.input_continue.text(),
            self.input_end.text(),
            self.input_feeling.text(),
            self.input_details.text()
        ]
        return narrative_details


class Ui6Identify(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label_title = None
        self.label_description = None
        self.text_nightmare = None
        self.label_instruction = None
        self.text_negative_elements = None
        self.bt_done = None
        self.narrative = "hey"
        self.setup_ui()

    def setup_ui(self):
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
        self.text_nightmare.setText(self.narrative)
        layout.addWidget(self.text_nightmare)

        self.label_instruction = QLabel(
            "Now, could you identify the negative elements on it?\nCopy and paste the negative elements below.")
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_instruction.setFont(font_description)
        layout.addWidget(self.label_instruction)

        self.text_negative_elements = QTextEdit()
        self.text_negative_elements.setPlaceholderText("Put a comma in between the words! The program is NOT case-sensitive.")
        layout.addWidget(self.text_negative_elements)

        self.bt_done = QPushButton("Done")
        self.bt_done.setFixedSize(60, 30)
        layout.addWidget(self.bt_done, alignment=Qt.AlignmentFlag.AlignCenter)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().setStatusTip('2/4 Identify')

        self.progress = QProgressBar()
        self.progress.setValue(40)
        self.status.addPermanentWidget(self.progress)

        central_widget.setLayout(layout)

    # Refresh the content while setting the text
    def set_narrative(self, narrative):
        self.narrative = narrative
        self.text_nightmare.setText(self.narrative)

    def get_narrative(self):
        return self.text_nightmare.toPlainText()

    def get_negative_elements(self):
        return self.text_negative_elements.toPlainText()


class Ui7Replace(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label_title = None
        self.label_instruction1 = None
        self.label_instruction2 = None
        self.edited_dream = None
        self.bt_done = None
        self.narrative = "hey2"
        self.setup_ui()

    def setup_ui(self):
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
        self.edited_dream.setText(self.narrative)
        layout.addWidget(self.edited_dream)

        self.bt_done = QPushButton("Done")
        self.bt_done.setFixedSize(60, 30)
        layout.addWidget(self.bt_done, alignment=Qt.AlignmentFlag.AlignCenter)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().setStatusTip('3/4 Describe')

        self.progress = QProgressBar()
        self.progress.setValue(50)
        self.status.addPermanentWidget(self.progress)

        central_widget.setLayout(layout)

    def set_narrative(self, narrative):
        self.narrative = narrative
        self.edited_dream.setText(self.narrative)

    def get_narrative(self):
        return self.edited_dream.toPlainText()


class Ui8Write(Ui7Replace):
    def __init__(self):
        super().__init__()
        self.bt_finish = None
        self.modify_ui()

    def modify_ui(self):
        self.label_title.setText("Great job!")
        self.label_instruction1.setText(
            "You're almost there—just one last step to complete your dream!\n"
            "Read it again and add some final touches. Make sure it has a happy ending!"
        )

        self.label_instruction2.hide()

        self.edited_dream.setText(self.narrative)

        self.bt_finish = self.bt_done
        self.bt_finish.setText("Finish")

        self.statusBar().setStatusTip('4/4 Write')
        self.progress.setValue(60)


class Ui9PostSurvey(Ui4PreSurvey):
    def __init__(self):
        super().__init__()
        self.modify_ui()

    def modify_ui(self):
        self.label.setText("On a scale of 0-10, how scared does your new dream make you feel?")
        self.statusBar().setStatusTip('70/100%')
        self.progress.setValue(70)


class Ui10Choices(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label_title = None
        self.label_description = None
        self.label_instruction = None
        self.bt_yes = None
        self.bt_no = None
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_title = QLabel("Thanks!")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_title = QFont(FONT, FONT_SIZE, QFont.Weight.Bold)
        self.label_title.setFont(font_title)
        layout.addWidget(self.label_title)

        self.label_description = QLabel("That’s the end of the session. Hope this helps you feel more comfortable confronting your nightmare.")
        self.label_description.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_description = QFont(FONT, 12)
        self.label_description.setFont(font_description)
        layout.addWidget(self.label_description)

        self.label_instruction = QLabel("Would you like to save your results in a .txt file?\n")
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font_instruction = QFont(FONT, 12, QFont.Weight.Medium)
        self.label_instruction.setFont(font_instruction)
        layout.addWidget(self.label_instruction)

        self.bt_yes = QPushButton("Save results")
        self.bt_no = QPushButton("No, thanks.")
        self.bt_yes.setFixedSize(100, 30)
        self.bt_no.setFixedSize(100, 30)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.bt_yes)
        layout2.addWidget(self.bt_no)
        layout.addLayout(layout2)

        central_widget.setLayout(layout)


class Ui11aSaveResults(Ui1Start):
    def __init__(self):
        super().__init__()
        self.bt_end = None
        self.modify_ui()

    def modify_ui(self):
        self.label.setText("The operation was completed successfully!")
        font = QFont(FONT, 16, QFont.Weight.Medium)
        self.label.setFont(font)

        self.bt_end = self.bt_start
        self.bt_end.setText("End")
        self.bt_end.setFixedSize(45, 30)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.statusBar().setStatusTip('90/100%')

        self.progress = QProgressBar()
        self.progress.setValue(90)
        self.status.addPermanentWidget(self.progress)


class Ui11bEnd(BaseWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setup_ui()

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())

        img = QPixmap("files/end.png").scaled(self.label.width(), self.label.height())
        self.label.setPixmap(img)

    def start_music(self):
        song_name = "files/end.mp3"
        self.player.setSource(QUrl.fromLocalFile(song_name))
        self.audio_output.setVolume(0.7)
        self.player.play()
