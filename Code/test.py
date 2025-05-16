import unittest
import os
from data_manager import DataManager


class TestExample(unittest.TestCase):
    """Example unit test class."""

    def setUp(self):
        """Hook method for setting up the test fixture before exercising it."""
        self.data_manager = DataManager()

    def tearDown(self):
        """Hook method for deconstructing the test fixture after testing it."""
        del self.data_manager

    # operations with logic inside the function can be tested (data_manager)
    def test_set_and_get_nightmare_title(self):
        test_name = "Nightmare"
        self.data_manager.set_nightmare_title(test_name)
        result = self.data_manager.get_nightmare_title()
        self.assertEqual(result, test_name, "set_nightmare is wrong")

    def test_add_and_get_survey_results(self):
        self.data_manager.add_survey_result(7)
        self.data_manager.add_survey_result(5)
        self.assertEqual(self.data_manager.get_survey_result(), [7, 5])

    def test_compare_results(self):
        self.data_manager.add_survey_result(7)
        self.data_manager.add_survey_result(5)
        self.assertEqual(self.data_manager.compare_results(), 2)

    def test_get_combined_narrative(self):
        self.data_manager.narrative_details['input_begin'] = "1"
        self.data_manager.narrative_details['input_continue'] = "2"
        self.data_manager.narrative_details['input_end'] = "3"
        self.data_manager.narrative_details['input_feeling'] = "4"
        self.data_manager.narrative_details['input_details'] = "5"
        result = self.data_manager.get_combined_narrative()
        self.assertEqual(result, "1 2 3 4 5", "get_combined_narrative is wrong")

    def test_delete_negative_elements(self):
        self.data_manager.set_old_narrative("This is a bad and terrible nightmare.")
        self.data_manager.add_negative_elements("bad, terrible")
        edited_text = self.data_manager.delete_negative_elements()
        self.assertNotIn("bad", edited_text)
        self.assertNotIn("terrible", edited_text)
        self.assertEqual(edited_text, "This is a [       ] and [       ] nightmare.", "delete_negative_elements is wrong")

    def test_delete_brackets(self):
        self.data_manager.set_new_narrative("This is a [wonderful] and [happy] dream!")
        edited_text = self.data_manager.delete_brackets()
        self.assertEqual(edited_text, "This is a wonderful and happy dream!")

    def test_music_file_exists(self):
        self.assertFalse(os.path.exists("nonexistent_music.mp3"))

    def test_save_all_data_creates_file(self):
        self.data_manager.input_data = "Sample report data"
        report_filename = "report.txt"
        self.data_manager.save_all_data()
        self.assertTrue(os.path.exists(report_filename))
        os.remove(report_filename)

    def test_deal_and_save_all_data_integrity(self):
        filepath = "test_output.txt"
        content = "Some random session data"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        with open(filepath, "r", encoding="utf-8") as f:
            result = f.read()
        self.assertEqual(result, content)
        os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
