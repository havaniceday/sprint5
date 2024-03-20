import random
import string


@staticmethod
def generate_random_email():
    domains = ["yandex.ru", "gmail.com"]
    username = 'GalinaKilovataia6' + str(random.randint(000, 999))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_random_password(length: int):
    password = random.choices(string.ascii_letters + string.digits, k=length)
    return str.join('', password)


def valid_user():
    return ['test1@me.com', '123456']
