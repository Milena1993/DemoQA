from locators import LocatorsPath
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class InputFields:
    def get_page_title(self):
        driver = self.driver
        get_title = driver.title
        current_url = driver.current_url
        return get_title, current_url

    def __init__(self, driver):
        self.driver= driver
        self.input_full_name = LocatorsPath.full_name
        self.input_email = LocatorsPath.email
        self.input_current_address = LocatorsPath.current_address
        self.input_permanent_address = LocatorsPath.permanent_address
        self.click_submit = LocatorsPath.submit
        self.output_name = LocatorsPath.name
        self.output_email = LocatorsPath.submitted_email
        self.output_current_address = LocatorsPath.sumbitted_current_address
        self.output_permanent_address = LocatorsPath.submitted_permanent_address


    def input_full_name_field(self,text):
        input_name = self.driver.find_element_by_id(self.input_full_name)
        input_name.send_keys(text)
        print (input_name.text)

    def input_email_field(self, email):
        input_email = self.driver.find_element_by_id(self.input_email)
        input_email.send_keys(email)

    def input_current_address_field(self, current_address):
        input_current_address = self.driver.find_element_by_id(self.input_current_address )
        input_current_address.send_keys(current_address)

    def input_permanent_address_field(self, permanent_address):
        input_current_address = self.driver.find_element_by_id(self.input_permanent_address )
        input_current_address.send_keys(permanent_address)

    def click_submit_button(self):
        click_submit = self.driver.find_element_by_id(self.click_submit)
        click_submit.click()

    def output_text_display(self):
        output_name = self.driver.find_element_by_id(self.output_name)
        output_email = self.driver.find_element_by_id(self.output_email)
        output_current_address = self.driver.find_element_by_xpath(self.output_current_address)
        output_permanent_address = self.driver.find_element_by_xpath(self.output_permanent_address)
        return output_name.text, output_email.text,  output_current_address.text, output_permanent_address.text 
        
    