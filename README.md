This project covers a part of functionality to test https://stellarburgers.nomoreparties.site/ using pytest and selenium. Project structure description:

locators.py  - all the locators used in tests are there 

helper.py - functions to generate random email and random password

conftest.py - fixture to launch and close a driver + fixture where sample user login data is stored
tests folder 

tests folder:

Регистрация test_registration.py

Успешную регистрацию.     
test_registration_new_user_is_successfull

Ошибку для некорректного пароля.
test_registration_password_less_than_six_throws_error


Вход test_login.py

вход по кнопке «Войти в аккаунт» на главной, test_login_from_enter_account_with_valid_credentials_success

вход через кнопку «Личный кабинет», test_login_from_enter_account_with_valid_credentials_success

вход через кнопку в форме регистрации,
test_login_from_registration_with_valid_credentials_success

вход через кнопку в форме восстановления пароля.
test_login_forgotten_password_remembered_success


Переход в личный кабинет test_my_account_redirect.py

Проверь переход по клику на «Личный кабинет».
test_my_account_from_main_logged_in_user_is_redirected
test_my_account_from_feed_logged_in_user_is_redirected

Переход из личного кабинета в конструктор test_main_redirect.py

Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
test_logged_in_user_redirect_from_account_to_main_success


Выход из аккаунта test_exit.py
Проверь выход по кнопке «Выйти» в личном кабинете.
test_exit_for_logged_in_user_is_successful

Раздел «Конструктор» test_constructor_transitions.py

Проверь, что работают переходы к разделам:
«Булки», test_transitions_from_buns_success
«Соусы», test_transitions_from_fillings_and_sauces_success
«Начинки». 