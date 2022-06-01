import os
import pathlib
import configparser
import sys
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64
from typing import Union

FOLDER_NAME = "InstaBot"
CONFIG_FILE = "config.ini"

USERNAME = "username"
PASSWORD = "password"


def init(reset: bool = False) -> Union[str, tuple]:
    # check python version - run only with python3
    if sys.version_info.major != 3:
        print("You must use Python3 to run this program")
        sys.exit(-1)

    user = os.getlogin()
    windisk = pathlib.Path.home().drive

    path = windisk + "\\" + "Users\\" + user + "\\" + FOLDER_NAME + "\\"
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists(path + CONFIG_FILE) and reset:
        os.remove(path + CONFIG_FILE)

    username = ""
    password = ""

    if not os.path.exists(path + CONFIG_FILE):
        print("As long as it is better to protect your Instagram credentials, we're going to use a password!")

        password_ok = False
        password_match = False
        credential_pw = ""

        while not password_ok or not password_match:
            
            credential_pw = input("insert a secret password: ")
            password_ok = password_check(credential_pw)
            if not password_ok:
                continue

            credential_pw_confirm = input("insert the password again: ")
            if credential_pw_confirm == credential_pw:
                password_match = True

            print('\n')

        key = get_fernet_key(credential_pw)
        fernet = Fernet(key)

        username = input("insert your instagram username: ")
        password = input("insert your instagram password: ")

        config = configparser.ConfigParser()
        config['DEFAULT'][USERNAME] = fernet.encrypt(username.encode()).decode()
        config['DEFAULT'][PASSWORD] = fernet.encrypt(password.encode()).decode()

        with open(path + CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
    else:
        config = configparser.ConfigParser()
        config.read(path + CONFIG_FILE)

        encrypted_username = config['DEFAULT'][USERNAME]
        encrypted_password = config['DEFAULT'][PASSWORD]

        secret_password = input("insert your secret password: ")

        key = get_fernet_key(secret_password)
        fernet = Fernet(key)

        try:
            username = fernet.decrypt(encrypted_username.encode()).decode()
            password = fernet.decrypt(encrypted_password.encode()).decode()
        except (cryptography.fernet.InvalidToken, TypeError):
            print("secret password may be wrong")
            sys.exit(-1)
    return path, (username, password)


def password_check(passwd, min_chars: int = 8, max_chars: int = 20) -> bool:
    special_symbols = ['$', '@', '#', '%', '!', '?']
    val = True

    if len(passwd) < min_chars:
        print('length should be at least {}'.format(min_chars))
        val = False

    if len(passwd) > max_chars:
        print('length should be not be greater than {}'.format(max_chars))
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in special_symbols for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False

    return val


def get_fernet_key(password: str):
    salt = password.encode()

    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2 ** 14,
        r=8,
        p=1,
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)


def encrypt_cookies(password: str, filename: str):
    key = get_fernet_key(password)
    fernet = Fernet(key)

    data = None
    with open(filename, "rb") as f1:
        data = f1.read()

    os.remove(filename)
    encrypted_data = fernet.encrypt(data)

    with open(filename, "wb") as f2:
        f2.write(encrypted_data)


def decrypt_cookies(password: str, filename: str):
    key = get_fernet_key(password)
    fernet = Fernet(key)

    data = None
    with open(filename, "rb") as f1:
        data = f1.read()

    os.remove(filename)
    encrypted_data = fernet.decrypt(data)

    with open(filename, "wb") as f2:
        f2.write(encrypted_data)
