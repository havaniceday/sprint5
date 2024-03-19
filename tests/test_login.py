from helper import *
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    def test_login_from_my_account_with_valid_credentials_success(self, driver, valid_user):
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
        assert driver.find_element(*TestLocators.CHECKOUT_BUTTON) is not None

    def test_login_from_enter_account_with_valid_credentials_success(self, driver, valid_user):
        driver.find_element(*TestLocators.ENTER_ACCOUNT_BUTTON).click()
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
        assert driver.find_element(*TestLocators.CHECKOUT_BUTTON) is not None

    def test_login_from_registration_with_valid_credentials_success(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_LINK))

        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_INPUT))
        password_input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)


        name_input_element = driver.find_element(*TestLocators.NAME_INPUT)
        email_input_element = driver.find_element(*TestLocators.EMAIL_INPUT)

        name_input_element.send_keys('Galina')
        email = generate_random_email()
        email_input_element.send_keys(email)
        passwd = generate_random_password(7)
        password_input_element.send_keys(passwd)

        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.MY_LOGIN_BUTTON))

        email_input_element = driver.find_element(*TestLocators.EMAIL_INPUT)
        password_input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)
        email_input_element.send_keys(email)
        password_input_element.send_keys(passwd)

        driver.find_element(*TestLocators.MY_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
         TestLocators.CHECKOUT_BUTTON))
        assert driver.find_element(*TestLocators.CHECKOUT_BUTTON) is not None

    def test_login_forgotten_password_remembered_success (self, driver, valid_user):
        driver.find_element(*TestLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_LINK))
        driver.find_element(*TestLocators.PASSWORD_FORGOTTEN_LINK).click()
        driver.find_element(*TestLocators.REMEMBERED_PASSWORD_LINK).click()
        email_input_element = driver.find_element(*TestLocators.EMAIL_INPUT)
        password_input_element = driver.find_element(*TestLocators.PASSWORD_INPUT)
        email = valid_user[0]
        passwd = valid_user[1]
        email_input_element.send_keys(email)
        password_input_element.send_keys(passwd)
        driver.find_element(*TestLocators.MY_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.CHECKOUT_BUTTON))
        assert driver.find_element(*TestLocators.CHECKOUT_BUTTON) is not None



