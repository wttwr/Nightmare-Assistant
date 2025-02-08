class DataManager:
    def __init__(self):
        # 第一个页面的名字
        self.nightmare = ""

        # 两个survey值
        self.survey_results = []

        # 保存5个用户回答的问题
        self.narrative_details = {
            "input_begin": "",
            "input_continue": "",
            "input_end": "",
            "input_feeling": "",
            "input_details": ""
        }

        # 保存用户输入的单词
        self.negative_elements = []

        # 保存用户修改前后的噩梦内容
        self.old_narrative = ""
        self.new_narrative = ""


    # 设置单词
    def set_negative_elements(self):
        self.negative_elements.append("")

    # 在 narrative_details 删除 negative_element
    def delete_negative_elements(self):
        return ""

    def update_narrative(self):
        self.new_narrative = ""

    # 设置函数
    def set_narrative_details(self):
        self.narrative_details["input_feeling"] = self.narrative_details["input_details"]

    # 拼接5个问题
    def get_combined_narrative(self):
        return ""

    def add_survey_result(self, survey_value):
        self.survey_results.append(survey_value)

    def get_survey_result(self):
        return self.survey_results

    def compare_results(self):
        # 后续根据返回的数据变换音乐(可能）
        return self.survey_results[-1] - self.survey_results[0]

    def set_nightmare(self, nightmare):
        self.nightmare = nightmare

    def get_nightmare(self):
        return self.nightmare

    # 保存数据到txt文件中
    def save_all_data(self):
        with open("result.txt","w") as f:
            f.write("")