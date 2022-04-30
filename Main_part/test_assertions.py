from numpy import exp
from selenium import webdriver
from base_page import Base
from functions import InputFields
from test_data import TestData
from time import sleep
import pytest


@pytest.mark.usefixtures('set_up')
class TestPositive(Base, TestData):

#Assert that https://demoqa.com/ page is opened
    def test_title(self):
        actual_result = InputFields.get_page_title(self)
        expected_result = ("ToolsQA", "https://demoqa.com/text-box")
        assert actual_result == expected_result
        print(actual_result)
     
# Assert a new item is added with correct information
#in DemoQA page output field there is typo of Permanent address , instead of Permanent it's written Permananet 
    def test_input_fields(self):
        driver = self.driver
        test_input = InputFields(driver)
        test_input.input_full_name_field(self.text)
        test_input.input_email_field(self.email)
        test_input.input_current_address_field(self.current_address)
        test_input.input_permanent_address_field(self.permanent_address)
        test_input.click_submit_button()
        actual_result = test_input.output_text_display()
        print(actual_result)
        expected_result = ('Name:' + self.text, 'Email:'+ self.email, 'Current Address :' + self.current_address, 'Permananet Address :' + self.permanent_address)
        assert actual_result == expected_result
        