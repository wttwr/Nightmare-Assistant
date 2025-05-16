from gui import Ui10Choices
from PyQt6.QtWidgets import QColorDialog, QHBoxLayout, QVBoxLayout, QGridLayout, QDockWidget, QLabel, QLineEdit, \
    QWidget, QFrame, QPushButton, QListWidget, QMainWindow
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import Qt

from library import Library


class UiCollageChoices(Ui10Choices):
    def __init__(self):
        super().__init__()
        self.modify_ui()

    def modify_ui(self):
        self.label_title.setText("Such a wonderful dream!")
        self.label_description.hide()
        self.label_instruction.setText("Would you like to bring your newly created dream to life by turning it into a collage?\n")
        self.bt_yes.setText("Let’s do it!")


'''
class UiCollageStart(UiCollageChoices):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COLLAGE")
        self.modify_ui()

    def modify_ui(self):
        self.label_title.setText("Hey, welcome!")
        self.label_description.hide()
        self.label_instruction.setText(
            "Good luck.\n"
        )
        self.bt_yes.setText("continue")
        self.bt_yes.setFixedSize(90, 30)
        self.bt_no.hide()
'''

class UiCollageMake(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COLLAGE")
        self.selected_color = None
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        form_layout = QVBoxLayout()

        # title and keywords
        title_label = QLabel("Title:")
        self.title_input = QLineEdit()
        keywords_label = QLabel("Keywords:")
        self.keywords_input = QLineEdit()

        form_layout.addWidget(title_label)
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(keywords_label)
        form_layout.addWidget(self.keywords_input)

        # grid
        grid_frame = QFrame()
        grid_layout = QGridLayout(grid_frame)

        for row in range(3):
            for col in range(3):
                add_button = QPushButton("Add")
                add_button.setFixedSize(150, 150)
                add_button.setObjectName(f"button_{row}_{col}")
                add_button.clicked.connect(self.add_button_clicked)
                grid_layout.addWidget(add_button, row, col)
        form_layout.addWidget(grid_frame)

        # author and data
        author_label = QLabel("Author:")
        self.author_input = QLineEdit()
        date_label = QLabel("Date:")
        self.date_input = QLineEdit()

        form_layout.addWidget(author_label)
        form_layout.addWidget(self.author_input)
        form_layout.addWidget(date_label)
        form_layout.addWidget(self.date_input)

        # background color button
        self.color_button = QPushButton("Change background color")
        self.color_button.clicked.connect(self.show_color_dialog)
        form_layout.addWidget(self.color_button)

        # finnish button
        self.finish_button = QPushButton("Finish")
        self.finish_button.setFixedWidth(80)
        form_layout.addWidget(self.finish_button)

        # instructions, a dock widget
        self.dock_widget = QDockWidget()
        self.dock_widget.setWindowTitle('Instructions')
        self.list_widget = QListWidget()
        instructions = [
            "1. Add a title",
            "2. Choose 3-4 keywords",
            "3. Upload images from the library",
            "4. Write your name",
            "5. Write the date",
            "6. Choose a background color",
            "7. Click 'Finish' once you're done!"
        ]
        self.list_widget.addItems(instructions)
        self.dock_widget.setWidget(self.list_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock_widget)

        main_layout.addLayout(form_layout)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_button_clicked(self):
        button_id = self.get_button_id()
        self.library_window = Library(self, button_id)
        self.library_window.add_images_to_standard_library()
        self.library_window.show()

    def get_button_id(self):
        button = self.sender()
        if button:
            button_id = button.objectName()
            print(f"Clicked button ID: {button_id}")
            return button_id

    def show_color_dialog(self):
        self.color = QColorDialog(self)
        self.color.currentColorChanged.connect(self.change_background_color)
        self.color.show()

    def change_background_color(self, color):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, color)
        self.setPalette(palette)

