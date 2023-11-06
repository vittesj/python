'''В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.'''

from datetime import datetime
from sys import argv

def date_validate(date_text: str) -> bool:
    try:
        datetime.strptime(date_text, '%d.%m.%Y').date()
        print(True)
        leap_info(date_text)
        return True
    except:
        print(False)
        return False


def leap_info(date_text: str) -> bool:
    year = int(date_text.split(".")[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(True)
        return True
    else:
        print(False)
        return False


if __name__ == '__main__':
    date_validate(argv[1])

'''в argv подаются 2 значения, первое имя запускаемого файла, второе это сама дата'''