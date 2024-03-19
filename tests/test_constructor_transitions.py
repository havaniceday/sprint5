import pytest

from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructorTransitions:
    @pytest.mark.parametrize ("source_locator", [TestLocators.SAUCES_TAB, TestLocators.FILLINGS_TAB])
    def test_transitions_to_buns_success(self, driver, source_locator):
        driver.find_element(*source_locator).click()
        current_tab = driver.find_element(*source_locator)
        current_tab_class = current_tab.get_attribute('class')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUNS_TAB))
        driver.find_element(*TestLocators.BUNS_TAB).click()
        assert 'current' in current_tab_class
        assert driver.find_element(*TestLocators.BUNS_LIST).is_displayed()

    @pytest.mark.parametrize("source_locator", [TestLocators.SAUCES_TAB, TestLocators.BUNS_TAB])
    def test_transitions_to_fillings_success(self, driver, source_locator):
        current_tab = driver.find_element(*source_locator)
        current_tab_class = current_tab.get_attribute('class')
        try:
            driver.find_element(*source_locator).click()
            current_tab = driver.find_element(*source_locator)
            current_tab_class = current_tab.get_attribute('class')
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FILLINGS_TAB))
        except Exception as e:
            pass
        driver.find_element(*TestLocators.FILLINGS_TAB).click()
        assert 'current' in current_tab_class
        assert driver.find_element(*TestLocators.FILLINGS_LIST).is_displayed()

    @pytest.mark.parametrize("source_locator", [TestLocators.BUNS_TAB, TestLocators.FILLINGS_TAB])
    def test_transitions_to_sauces_success(self, driver, source_locator):
        current_tab = driver.find_element(*source_locator)
        current_tab_class = current_tab.get_attribute('class')
        try:
            driver.find_element(*source_locator).click()
            current_tab = driver.find_element(*source_locator)
            current_tab_class = current_tab.get_attribute('class')
        except Exception as e:
            pass
        driver.find_element(*TestLocators.SAUCES_TAB).click()
        assert 'current' in current_tab_class
        assert driver.find_element(*TestLocators.SAUCES_LIST).is_displayed()



