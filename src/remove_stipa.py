import re


def delete_the_lucky_guys(data):
    result = re.findall(r"([А-Я][а-я]+)(-[А-Я][а-я]+)?\s([А-Я].)\3\s(P3113)", data)
    for elem in result:
        data = data.replace(f"{elem[0]} {elem[2]}{elem[2]} {elem[3]}", '')
    return data


if __name__ == '__main__':
    tests = [
        "Балакшин П.A. P3113 Балакшин В.В. P3113 Балакшин Ф.Ф. P3113 Куликов А.А. P3213Куликов А.А. P3113",
        "Петров П.П. P3113 Анищенко А.А. P9999 Примеров Е.В. P3113 Иванов И.И. P3113"
    ]

    for paragraph in tests:
        print(delete_the_lucky_guys(paragraph))
