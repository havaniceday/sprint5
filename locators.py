from selenium.webdriver.common.by import By
from selenium import webdriver


class TestLocators:
    MY_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")  # перейти на страницу авторизации
    MY_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # войти в акк (появляется после перехода по сслыке на формы входа)
    REGISTRATION_LINK = (By.XPATH, "//a[contains(@href, '/register')]")  # перейти на страницу регистрации
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='Пароль']")  # поле ввода пароля
    EMAIL_INPUT = (By.XPATH, "(.//label[text()='Email']/following::input)[1]")  # поле ввода email
    NAME_INPUT = (By.XPATH, "(.//label[text()='Имя']/following::input)[1]")  # поле имени
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # финальная кнопка для завершения регистрации
    PARENT_ELEMENT = (By.XPATH, "..")  # проверить, что с родителем
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # кнопка "оформить заказ" доступна только залогиненным юзерам
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # та же кнопка, но другой текст для незалогиненных юзеров
    PASSWORD_FORGOTTEN_LINK = (By.XPATH, "//a[contains(@href, '/forgot-password')]") # ссылка на восстановление забытого пароля
    REMEMBERED_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, '/login')]") # ссылка обратно на логин, если вспомнить пароль
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]") # кнопка выхода из аккаунта, доступна только залогиненным пользователям
    FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]") # переход в ленту заказов
    FEED_ITEMS_BOX = (By.XPATH, "//ul[contains(@class, 'OrderFeed')]") # показатель загрузки ленты заказов
    MAIN_LOGO = (By.XPATH, "//a[@href = '/' and ancestor::div[contains(@class, 'AppHeader_header__logo')]]")
    MAIN_CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header') and @href = '/']")
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and descendant::span[contains(text(), 'Булки')]]")
    BUNS_LIST = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients') and preceding-sibling::h2[1][contains(text(), 'Булки')]]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and descendant::span[contains(text(), 'Соусы')]]")
    SAUCES_LIST = (By.XPATH,
                 "//ul[contains(@class, 'BurgerIngredients_ingredients') and preceding-sibling::h2[1][contains(text(), 'Соусы')]]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab') and descendant::span[contains(text(), 'Начинки')]]")
    FILLINGS_LIST = (By.XPATH,
                 "//ul[contains(@class, 'BurgerIngredients_ingredients') and preceding-sibling::h2[1][contains(text(), 'Начинки')]]")




