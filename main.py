import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

#导入各个页面
from ui import UiTmpWindow
from ui import Ui1Start
from ui import Ui3aTitle
from ui import Ui4PreSurvey
from ui import Ui5Describe
from ui import Ui6Identify
from ui import Ui7Replace
from ui import Ui8Write
from ui import Ui11bEnd
	       
from data_manager import DataManager
	       
#定义全局变量
user_info = {}

#初始化数据中心
data_center = DataManager()


#打印提示信息
def msg(info):
	msg_box = QMessageBox()
	msg_box.setText(info)
	msg_box.exec()


def show_title_ui(current_window, next_window):
	current_window.close()
	next_window.show()


def show_pre_survey_ui(current_window, next_window):
	nightmare_title = current_window.input.text()
	if len(nightmare_title)== 0:
		msg("Please input a short title first.")
		return

	user_info["nightmare_title"] = nightmare_title
	current_window.close()
	next_window.show()

	print(user_info)
	
	
def show_describe_ui(current_window, next_window):
	user_info["pre_survey_value"] = current_window.horizontal_slider.value()
	current_window.close()
	next_window.show()

	print(user_info)
	
	
def show_identify_ui(current_window, tmp_ui, next_window):
	if len(current_window.input_begin.text()) == 0:
		msg("Please input 'how does it begin?'")
		return
	if len(current_window.input_continue.text()) == 0:
		msg("Please input 'how does it continue?'")
		return
	if len(current_window.input_end.text()) == 0:
		msg("Please input 'how does it end?'")
		return
	if len(current_window.input_feeling.text()) == 0:
		msg("Please input 'how were you feeling?'")
		return

	user_info["input_begin"] = current_window.input_begin.text()
	user_info["input_continue"] = current_window.input_continue.text()
	user_info["input_end"] = current_window.input_end.text()
	user_info["input_feeling"] = current_window.input_feeling.text()
	user_info["input_details"] = current_window.input_details.text()

	current_window.close()
	tmp_ui.next_window = next_window
	tmp_ui.show()
	tmp_ui.go_to_next_window()

	print(user_info)
					
					
def show_replace_ui(current_window, tmp_ui, next_window):
	current_window.close()
	tmp_ui.next_window = next_window
	tmp_ui.show()
	tmp_ui.go_to_next_window()
					

def show_write_ui(current_window, next_window):
	current_window.close()
	next_window.show()
	next_window.label_title = data_center.get_nightmare()

def show_post_survey_ui(current_window, next_window):
	pass

def show_end_ui(current_window, next_window):
	#user_info["post_survey_value"] = current_window.horizontal_slider.value()

	# 保存所有数据
	data_center.save_all_data()
	current_window.close()
	next_window.show()
	next_window.start_music()

	print(user_info)
					
					
if __name__ == '__main__':
	app = QApplication(sys.argv)

	tmp_window = UiTmpWindow()
	start_window = Ui1Start()
	title_window = Ui3aTitle()
	pre_survey_window = Ui4PreSurvey()
	describe_window = Ui5Describe()
	identify_window = Ui6Identify()
	replace_window = Ui7Replace()
	write_window = Ui8Write()
	end_window = Ui11bEnd()

	start_window.bt_start.clicked.connect(lambda: show_title_ui(start_window, title_window))
	title_window.bt_save.clicked.connect(lambda: show_pre_survey_ui(title_window, pre_survey_window))
	pre_survey_window.bt_continue.clicked.connect(lambda: show_describe_ui(pre_survey_window, describe_window))
	describe_window.bt_continue.clicked.connect(lambda: show_identify_ui(describe_window, tmp_window, identify_window))
	identify_window.bt_done.clicked.connect(lambda: show_replace_ui(identify_window, tmp_window, replace_window))
	replace_window.bt_done.clicked.connect(lambda: show_write_ui(replace_window, write_window))
	write_window.bt_finish.clicked.connect(lambda: show_end_ui(write_window, end_window))

	start_window.show()
	sys.exit(app.exec())