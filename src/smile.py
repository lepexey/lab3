import re

# ISU = 368403
# eyes_id = ISU % 6
# nose_id = ISU % 4
# mouth_id = ISU % 7
# print(eyes_id, nose_id, mouth_id)

# smile: 8<{(
SMILE = "8<{("


def find_smile(string):
    regular_smile = ""
    for ch in SMILE:
        if ch in ";:(){}[]+-<>=/|\\?!%$&~":
            regular_smile = regular_smile + "\\" + ch

    result = re.findall(regular_smile, string)
    return len(result)


if __name__ == '__main__':
    tests = {
        "Отсутствие 8<{(старца из кельи продолжалось минут около двадцати 8<{(пяти. Было уже за половину первого, а"
        " Дмитрия Федоровича, ради которого все собр8<{(ались, всё еще не бывало. Но о нем почти как бы и забыли, "
        "и когда старец вступил опять в келью, то застал самый оживленный общий разговор меж8<{(ду своими гостями."
        " В разговоре участвовали 8<{(прежде всего Иван Федорович и оба иеромонаха."
        : 5,

        "Ввязывался,8<{( и по-видимому очень горячо, в разговор и Миусов, но ему опять не везло; он был видимо на "
        "втором "
        " плане, и 8<{(ему даже мало отвечали, так что это новое обстоятельство лишь усилило всё накоплявшуюся его"
        " раздражительность."
        : 2,

        "Дело 8<{(в том, что он и прежд8<{(е с Иваном Федоровичем несколько пикировался в познаниях и некоторую "
        "небрежность "
        "его к 8<{(себе хладнокровно не выносил: «До сих пор, по крайней мере, стоял на высоте всего, "
        "что есть передового "
        " в Европе, а это новое поколение реш8<{(ительно нас8<{( игнорирует», — думал он8<{( про себя."
        : 6,

        "Федор Павлович, 8<{(который сам дал слово усесться на стуле и замолчать, действительно некоторое время молчал,"
        " но с насмешливою улыбочкой следил за своим соседом Петром 8<{(Александровичем и видимо радовался его "
        "раздражительности. Он давно уже собирался отплатить ему кое за что 8<{(и теперь не хотел упустить случая."
        : 3,

        "Спор 8<{(на одну минутку затих, но старец, усевшись на пр8<{(ежнее место, ог8<{(лядел всех, как бы приветливо "
        "вызывая продолжать. Алеша, изучивший8<{( почти всякое выражение его лица, вид8<{(ел ясно, что он ужасно"
        " утомлен и 8<{(себя пересиливает. В последн8<{(ее время болезни с ним случались 8<{(от истощения сил обмороки."
        "Почти такая же бледность, как пред обмороком, 8<{(распространя8<{(лась и теперь по его лицу, "
        "губы его побелели."
        : 10
    }

    for paragraph in tests:
        print(f"{find_smile(paragraph)} smiles was found")