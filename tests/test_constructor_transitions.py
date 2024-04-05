

import pytest

from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorTransitions:
    transitions_from_buns = [[TestLocators.SAUCES_TAB, TestLocators.SAUCES_LIST],
                             [TestLocators.FILLINGS_TAB, TestLocators.FILLINGS_LIST]]

    @pytest.mark.parametrize("target_tab, target_list", transitions_from_buns)
    def test_transitions_from_buns_success(self, driver, target_tab, target_list):
        driver.find_element(*target_tab).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            target_list))
        current_tab = driver.find_element(*target_tab)
        current_tab_class = current_tab.get_attribute('class')
        assert 'current' in current_tab_class
        assert driver.find_element(*target_tab).is_displayed()

    transitions_other = [[TestLocators.SAUCES_TAB, TestLocators.FILLINGS_TAB, TestLocators.FILLINGS_LIST],
                         [TestLocators.SAUCES_TAB, TestLocators.BUNS_TAB, TestLocators.BUNS_LIST],
                         [TestLocators.FILLINGS_TAB, TestLocators.SAUCES_TAB, TestLocators.SAUCES_LIST],
                         [TestLocators.FILLINGS_TAB, TestLocators.BUNS_TAB, TestLocators.BUNS_LIST]]

    @pytest.mark.parametrize("source_tab, target_tab, target_list", transitions_other)
    def test_transitions_from_fillings_and_sauces_success(self, driver, source_tab, target_tab, target_list):
        driver.find_element(*source_tab).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
                target_tab))
        driver.find_element(*target_tab).click()
        current_tab = driver.find_element(*target_tab)
        current_tab_class = current_tab.get_attribute('class')
        assert 'current' in current_tab_class
        assert driver.find_element(*target_list).is_displayed()


