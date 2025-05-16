import sys

from PyQt6.QtWidgets import QApplication, QMessageBox, QErrorMessage

from gui import *
from collage import *
	       
from data_manager import DataManager


# initialize data manager class
data_center = DataManager()


# an error message
def error_msg(info):
	error_msg_box = QErrorMessage()
	error_msg_box.showMessage(info)
	error_msg_box.exec()

# a message box
def collage_msg(info):
	msg_box = QMessageBox()
	msg_box.setText(info)
	msg_box.exec()
	switch_ui(collage_make_window, post_survey_window)


def switch_ui(current_window, next_window):
	save_user_input(current_window)
	upload_input(next_window)
	current_window.close()
	next_window.show()


def save_user_input(current_window):
	if current_window == title_window:
		nightmare_title = title_window.get_title()
		data_center.set_nightmare_title(nightmare_title)

	if current_window  == pre_survey_window or current_window == post_survey_window:
		survey_value = current_window.get_survey_value()
		data_center.add_survey_result(survey_value)

	if current_window == describe_window:
		narrative_details = current_window.get_narrative_details()
		data_center.set_narrative_details(narrative_details)
		data_center.get_combined_narrative()

	if current_window  == identify_window:
		old_narrative = current_window.get_narrative()
		data_center.set_old_narrative(old_narrative)
		negative_elements = current_window.get_negative_elements()
		data_center.add_negative_elements(negative_elements)

	if current_window == replace_window:
		new_dream = current_window.get_narrative()
		data_center.set_new_narrative(new_dream)

	if current_window == write_window:
		new_narrative = current_window.get_narrative()
		data_center.set_new_narrative(new_narrative)


def upload_input(next_window):
	if next_window  == identify_window:
		narrative = data_center.get_old_narrative()
		next_window.set_narrative(narrative)

	if next_window == replace_window:
		edited_narrative = data_center.delete_negative_elements()
		next_window.set_narrative(edited_narrative)

	if next_window == write_window:
		edited_dream = data_center.delete_brackets()
		next_window.set_narrative(edited_dream)

# read file
def handle_read_click():
    filename = read_file_window.get_filename()
    if not filename:
        error_msg("Please enter a file.")
        return

    try:
        path = f"files/{filename}"
        with open(path, "r") as f:
            # skip the header line
            next(f)
            line = f.readline()
            if not line:
                error_msg("Invalid File: the file is empty.") # nightmare_empty.txt
                return

            parts = line.split("/")
            if len(parts) != 3:
                error_msg("Invalid File: information missing.") # nightmare_error_1.txt
                return

            title = parts[0].strip()
            fear_level_str = parts[1].strip()
            description = parts[2].strip()

            # converting fear level to an integer
            fear_level = int(fear_level_str)

            data_center.set_nightmare_title(title)
            data_center.add_survey_result(fear_level)
            data_center.set_old_narrative(description)

    except FileNotFoundError:
        error_msg(f"Couldn't find the file: {filename}")
        return
    except ValueError:
        error_msg("Invalid Data: fear level is not a number.") # nightmare_error_2.txt
        return

    switch_ui(read_file_window, identify_window)

# on click for save all data
def handle_bt_yes_click():
    data_center.deal_all_data()
    switch_ui(choices2_window, save_results_window)


def show_end_ui(current_window, next_window):
	# save all data
	data_center.save_all_data()
	current_window.close()
	next_window.show()
	next_window.start_music()


if __name__ == '__main__':
	app = QApplication(sys.argv)

	# initiate windows
	start_window = Ui1Start()
	choices_window = Ui2Choices()
	read_file_window = Ui3bReadFile() #1
	title_window = Ui3aTitle() #2
	pre_survey_window = Ui4PreSurvey()
	describe_window = Ui5Describe()
	identify_window = Ui6Identify()
	replace_window = Ui7Replace()
	write_window = Ui8Write()
	choices2_window = Ui10Choices()
	save_results_window = Ui11aSaveResults() #1
	post_survey_window = Ui9PostSurvey() #2
	end_window = Ui11bEnd()

	collage_choices_window = UiCollageChoices()
	collage_make_window = UiCollageMake()

	# buttons clicked
	start_window.bt_start.clicked.connect(lambda: switch_ui(start_window, choices_window))
	choices_window.bt_scratch.clicked.connect(lambda: switch_ui(choices_window, title_window))
	choices_window.bt_read_file.clicked.connect(lambda: switch_ui(choices_window, read_file_window))
	read_file_window.bt_read.clicked.connect(lambda: handle_read_click())
	title_window.bt_save.clicked.connect(lambda: switch_ui(title_window, pre_survey_window))
	pre_survey_window.bt_continue.clicked.connect(lambda: switch_ui(pre_survey_window, describe_window))
	describe_window.bt_continue.clicked.connect(lambda: switch_ui(describe_window, identify_window))
	identify_window.bt_done.clicked.connect(lambda: switch_ui(identify_window, replace_window))
	replace_window.bt_done.clicked.connect(lambda: switch_ui(replace_window, write_window))
	write_window.bt_finish.clicked.connect(lambda: switch_ui(write_window, collage_choices_window))
	post_survey_window.bt_continue.clicked.connect(lambda: switch_ui(post_survey_window, choices2_window))
	choices2_window.bt_yes.clicked.connect(lambda: handle_bt_yes_click())
	choices2_window.bt_no.clicked.connect(lambda: show_end_ui(choices2_window, end_window))
	save_results_window.bt_end.clicked.connect(lambda: show_end_ui(save_results_window, end_window))

	# collage buttons clicked
	collage_choices_window.bt_yes.clicked.connect(lambda: switch_ui(collage_choices_window, collage_make_window))
	collage_choices_window.bt_no.clicked.connect(lambda: switch_ui(collage_choices_window, post_survey_window))
	collage_make_window.finish_button.clicked.connect(lambda: collage_msg("Nice Job! Remember to take a screenshot of your collage 📸 Press OK to continue."))

	start_window.show()
	sys.exit(app.exec())