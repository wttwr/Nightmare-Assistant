from datetime import datetime

class DataManager:
    def __init__(self):
        self.nightmare_title = ""

        # two survey values
        self.survey_results = []

        # save the 5 answers entered by the user
        self.narrative_details = {
            "input_begin": "",
            "input_continue": "",
            "input_end": "",
            "input_feeling": "",
            "input_details": ""
        }

        # save the words typed by the user
        self.negative_elements_list = []

        # save the user's nightmare content before and after modification
        self.old_narrative = ""
        self.new_narrative = ""

        self.input_data = "heyhey"


    def set_nightmare_title(self, nightmare_title):
        self.nightmare_title = nightmare_title
        print("Nightmare Title:", self.nightmare_title)

    def get_nightmare_title(self):
        return self.nightmare_title

    def add_survey_result(self, survey_value):
        self.survey_results.append(survey_value)
        print("Survey Results:", self.survey_results)

    def get_survey_result(self):
        return self.survey_results

    def set_narrative_details(self, narrative_details_list):
        keys = list(self.narrative_details.keys())
        for key, detail in zip(keys, narrative_details_list):
            self.narrative_details[key] = detail.strip()
        print("Nightmare Details:", self.narrative_details)

    # combine nightmare_details and return the combined narrative
    def get_combined_narrative(self):
        combined_narrative = " ".join([
            self.narrative_details.get("input_begin", ""),
            self.narrative_details.get("input_continue", ""),
            self.narrative_details.get("input_end", ""),
            self.narrative_details.get("input_feeling", ""),
            self.narrative_details.get("input_details", "")
        ]).strip()
        print("Combined Narrative:", combined_narrative)
        self.set_old_narrative(combined_narrative)
        return combined_narrative

    def set_old_narrative(self, narrative):
        self.old_narrative = narrative
        print("Old Narrative:", self.old_narrative)

    def get_old_narrative(self):
        return self.old_narrative

    # add elements to the negative_elements list
    def add_negative_elements(self, negative_elements_str):
        elements = negative_elements_str.split(",")
        for element in elements:
            self.negative_elements_list.append(element.strip())
        print("Negative Elements:", self.negative_elements_list)

    # remove negative_elements from narrative_text and return the edited text
    def delete_negative_elements(self):
        words = self.old_narrative.split()
        edited_text = []
        for word in words:
            cleaned_word = word.lower().strip(",.?!:;/")
            if cleaned_word in self.negative_elements_list:
                edited_text.append("[       ]")
            else:
                edited_text.append(word)

        edited_text = " ".join(edited_text)
        print("Edited Text:", edited_text)
        return edited_text

    # remove brackets from new_text and return the edited text
    def delete_brackets(self):
        edited_dream = self.new_narrative.replace("[", "").replace("]", "")
        print("Edited Dream:", edited_dream)
        return edited_dream

    def set_new_narrative(self, narrative):
        self.new_narrative = narrative
        print("New Narrative:", self.new_narrative)

    def get_new_narrative(self):
        return self.new_narrative

    def compare_results(self):
        return self.survey_results[0] - self.survey_results[1]

    def deal_all_data(self):
        negative_elements_formatted = "\n".join(f"• {item}" for item in self.negative_elements_list)
        today = datetime.today().strftime("%d/%m/%Y")

        data = (
            f"NIGHTMARE TITLE: {self.nightmare_title}\n\n"
            f"OLD NIGHTMARE FEAR LEVEL: {self.survey_results[0]}\n\n"
            f"OLD NIGHTMARE: {self.old_narrative}\n\n"
            f"NEGATIVE ELEMENTS: \n{negative_elements_formatted}\n\n"
            f"NEW DREAM: {self.new_narrative}\n\n"
            f"NEW DREAM FEAR LEVEL: {self.survey_results[1]}\n\n"
            f"Date: {today}"
        )
        self.input_data = data

    # save data to a .txt file
    def save_all_data(self):
        with open("report.txt","w",encoding="utf-8") as f:
            f.write(self.input_data)