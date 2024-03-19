import pytest

from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestExit:
    def test_exit_for_logged_in_user_is_successful(self, driver, valid_user):
        driver.find_element(*TestLocators.MY_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_LINK))
        email_input_element = driver.find_element(*TestLocators.EMAIL_INPUT)
        password_input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)
        email = valid_user[0]
        passwd = valid_user[1]
        email_input_element.send_keys(email)
        password_input_element.send_keys(passwd)
        driver.find_element(*TestLocators.MY_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.CHECKOUT_BUTTON))
        driver.find_element(*TestLocators.MY_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.EXIT_BUTTON))
        driver.find_element(*TestLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.MY_LOGIN_BUTTON))
        assert driver.find_element(*TestLocators.MY_LOGIN_BUTTON) is not None

