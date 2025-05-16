from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QWidget, QPushButton, QMainWindow, QTabWidget, QRadioButton, QScrollArea, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

import os

class Library(QMainWindow):
    def __init__(self, main_window, button_id):
        super().__init__()
        self.setWindowTitle("COLLAGE")
        self.main_window = main_window
        self.button_id = button_id
        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        instruction_label = QLabel("Click on the image you want to add to the collage.")
        main_layout.addWidget(instruction_label)

        # tab widget
        tab_widget = QTabWidget()
        standard_tab = QWidget()
        personalised_tab = QWidget()
        tab_widget.addTab(standard_tab, "STANDARD")
        tab_widget.addTab(personalised_tab, "PERSONALISED")

        # radio buttons
        radio_layout = QHBoxLayout()
        radio_buttons = ["All", "Green", "Red", "Yellow", "Blue", "Orange"]
        for name in radio_buttons:
            radio_button = QRadioButton(name)
            if name == "All":
                radio_button.setChecked(True)
            radio_layout.addWidget(radio_button)
        radio_layout.addStretch()

        # scrollable area
        scroll_area = QScrollArea()
        scroll_content = QWidget()
        self.grid_layout = QGridLayout()
        scroll_content.setLayout(self.grid_layout)
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)

        # standard layout
        standard_layout = QVBoxLayout()
        standard_layout.addLayout(radio_layout)
        standard_layout.addWidget(scroll_area)
        standard_tab.setLayout(standard_layout)

        # personalised layout
        personalised_layout = QVBoxLayout()
        upload_button = QPushButton("Upload")
        upload_button.setFixedWidth(80)
        upload_button.clicked.connect(self.open_folder)
        personalised_layout.addWidget(upload_button, alignment=Qt.AlignmentFlag.AlignCenter)
        personalised_tab.setLayout(personalised_layout)

        main_layout.addWidget(tab_widget)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def open_folder(self):
        image, _ = QFileDialog.getOpenFileName(
            self, 'Select Image', '',
            'Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)'
        )

        self.add_image_to_collage(image)

    def add_image_to_collage(self, image):
        button = self.main_window.findChild(QPushButton, self.button_id)
        if button:
            # resize to fit while maintaining the aspect ratio
            pixmap = QPixmap(image)
            pixmap = pixmap.scaled(
                150, 150,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            icon = QIcon(pixmap)
            button.setIcon(icon)
            button.setIconSize(pixmap.size())  # match icon size to original image size
            button.setText("")
            button.setStyleSheet("border: none;")
            self.close()


    def add_images_to_standard_library(self, directory="images"):
        """
           Loads images from the given directory and adds them as buttons in a grid layout.

           Each button shows the image and can be clicked to add it to the collage.
           """

        if not os.path.exists(directory):
                print(f"Directory '{directory}' does not exist.")
                return

        image_list = os.listdir(directory)

        # define grid parameters
        columns = 5
        row = 0
        col = 0
        button_width = 100
        button_height = 100

        for i, image_file in enumerate(image_list):
                image_path = os.path.join(directory, image_file)
                button = QPushButton()
                button.setFixedSize(button_width, button_height)
                button.setStyleSheet("border: none;")

                pixmap = QPixmap(image_path)
                icon = QIcon(pixmap)
                button.setIcon(icon)
                button.setIconSize(button.size())

                button.clicked.connect(lambda _, image=pixmap: self.add_image_to_collage(image))

                self.grid_layout.addWidget(button, row, col)
                col += 1
                if col >= columns:
                    col = 0
                    row += 1