import re


def find_fullname(string):
    result = re.findall(r"[А-Я][а-я]+(?:-[А-Я][а-я]+)?\s[А-Я]\.[А-Я]\.", string)
    all_names = []
    for name in result:
        all_names.append(name.split(' ')[0])
    all_names.sort()
    for name in all_names:
        print(name)
    print()


if __name__ == '__main__':
    tests = [
        "Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, "
        "которые будут ему помогать:"" Анищенко А.А., Машина Е.А. и Голованова-Иванова Д.В.",
        "Ая И.Ф.",
        "Куликов А.А. выполнил Лр 3.",
        "Салихов П.Й.Громова Щ.Х.",
        "Тетерин Т.В. и человек по имени Мухин Ф.К.",
        "     Белозеров Ф.Д."
    ]

    for paragraph in tests:
        find_fullname(paragraph)
