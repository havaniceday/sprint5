from locators import TestLocators
from helper import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_password_less_than_six_throws_error(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_LINK))

        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))

        input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)
        register_button = driver.find_element(*TestLocators.REGISTER_BUTTON)
        parent_div = input_element.find_element(*TestLocators.PARENT_ELEMENT)

        for i in range(1, 6):
            input_element.send_keys(generate_random_password(i))
            register_button.click()
            parent_div_class = parent_div.get_attribute('class')
            assert 'input_status_error' in parent_div_class
            input_element.send_keys(u'\ue009' + u'\ue003')

    def test_registration_new_user_is_successfull(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_LINK))

        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))
        password_input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)

        register_button = driver.find_element(*TestLocators.REGISTER_BUTTON)
        name_input_element = driver.find_element(*TestLocators.NAME_INPUT)
        email_input_element = driver.find_element(*TestLocators.EMAIL_INPUT)

        name_input_element.send_keys('Galina')
        email = generate_random_email()
        email_input_element.send_keys(email)
        passwd = generate_random_password(7)
        password_input_element.send_keys(passwd)

        register_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.MY_LOGIN_BUTTON))

        email_input_element = driver.find_element(*TestLocators.EMAIL_INPUT)

        password_input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)
        email_input_element.send_keys(email)
        password_input_element.send_keys(passwd)

        driver.find_element(*TestLocators.MY_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.MY_LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.MY_LOGIN_BUTTON) is not None
