# .1 עבודה עם- tupple
from operator import index

from dict_comp import value

# a. צור tuple המכיל את המספר .99 רמז: (99,)
num: tuple[int] = (99,)
print("a", num)
# b. צור tuple המכיל את המספר ,77 ,88 .99 רמז: 99 88, 77, = [int[tuple :tup
tup: tuple[int, int, int] = (99,88,77)
print("b", tup)

# c. כתוב פונקציה המקבלת tuple, ומחזירה את אורכו. רמז: len
def len_tup(x: tuple) -> int:
    """
    :param x: tuple
    :return: length tuple
    """
    return len(x)
t = (6,5,4,3,4)
print("c", len_tup(t))

# d. כתוב פונקציה המקבלת שני tuples, ומחזירה אותם מחוברים. רמז: השתמש ב +
def add_two_tup(tup1: tuple, tup2: tuple) -> tuple:
    return tup1 + tup2

tup1 = (4,7)
tup2 = (5,3)
print("d", add_two_tup(tup1, tup2))


# e. כתוב פונקציה המקבלת שני tuples, ומחזירה tuple המכיל רק את האיברים
# המשותפים. לדוגמא עבור (6 5, 4, 3,) ,(4 3, 2, 1,) יחזור: ) ,4 3(
def same_num_two_tup(tup1: tuple, tup2: tuple) -> tuple:
    t = tuple(i for i in tup1 if i in tup2)
    return t

tup1 = (6, 5, 4, 3)
tup2 = (4, 3, 2, 1)
print("e", same_num_two_tup(tup1, tup2))

# f. כתוב פונקציה המקבלת שני tuples, ומחזירה tuple המכיל רק את האיברים השונים.
# לדוגמא עבור (6 5, 4, 3,) ,(4 3, 2, 1,) יחזור: ),6 ,5 ,2 1(. רמז השתמש בפונקציה
# מהסעיף הקודם

def diff_num_two_tup(tup1: tuple, tup2: tuple) -> tuple:
    t = tuple(i for i in tup1+tup2 if (i in tup1) != (i in tup2))
    return t
    #2
    t = tuple(i for i in tup1 + tup2 if i not in same_num_two_tup(tup1,tup2))
    return t
tup1 = (6, 5, 4, 3)
tup2 = (4, 3, 2, 1)
print("f", diff_num_two_tup(tup1, tup2))

# g. כתוב פונקציה המקבלת tuple ואינדקס , ומחזירה את האיבר באותו האינדקס. אם
# האינדקס מחוץ לטווח החזר None

def index_tup(tup: tuple,index)-> [int, None]:
    try:
        value = tup[index]
        return value
    except IndexError:
        return None
print("g", index_tup((4,6,8,5,3,2,7,1), 3))
print("g", index_tup((4,6,8,5,3,2,7,1), 9))

# h. כתוב פונקציה המקבלת tuple, ומחזירה את ה- tuple בסדר הפוך
def revers_tup(tup: tuple)-> tuple:
    return tup[::-1]
print("h", revers_tup((1,2,3,4)))

# i. כתוב פונקציה המקבלת tuple ומספר , ומחזירה את ה- tuple משוכפל בגודל שנשלח.
# לדוגמא אם נשלח ),1 2( והמספר 3 התשובה תהיה ),1 ,2 ,1 ,2 ,1 2(. רמז: *
def duplication_tup(tup: tuple, dup: int)-> tuple:
    return tup * dup
print("i", duplication_tup((4,5,6), 2))

# j. כתוב פונקציה המקבלת tuple ומספר, ומחזירה tuple ללא המספר
def del_num_in_tup(tup: tuple, num: int)-> tuple:
    return tuple(i for i in tup if i != num)
print("j", del_num_in_tup((5,7,5,3,2),5))

# k. כתוב פונקציה המקבלת tuple, ומחזירה tuple ללא כפילויות. רמז: רוץ בלולאה והוסף
# לרשימה את כל איברי ה- tuple. בכל פעם שנתקלת באיבר שכבר קיים ברשימה אז אל
# תוסיף אותו. בסוף הפוך את ה list ל - tuple
def not_duplication_tup(tup: tuple)-> tuple:
    list_num: list = []
    for i in tup:
        if i not in list_num:
            list_num.append(i)
    return tuple(list_num)
print("k", not_duplication_tup((3,4,5,3,2,5,6)))

# l.** בונוס: כתוב פונקציה המקבלת tuple ומספר, ומחזירה את האינדקסים של המספר
# ב tuple, לדוגמא-
# אם התקבל המספר 5 , וה- tuple הבא ),40 ,30 ,10 ,5 ,2 ,3 ,5 ,5 ,8 10(
# יחזור ),6 ,3 2(. כי המספר 5 מופיע באינדקס ,2 3 ו- 6

def index_num_tup(tup: tuple, num: int)-> tuple:
    list_index_num: list = []
    for i, value in enumerate(tup):
        if value == num:
            list_index_num.append(i)
    return tuple(list_index_num)

print("l", index_num_tup((40, 30, 10, 5, 2, 3, 5, 5, 8, 10), 5))

# m. קלוט מהמשתמש רשימה של שמות עד אשר ייקלט "done"
# כעת קלוט מהמשתמש רשימה של ציונים עד אשר ייקלט מינוס 999
# כעת צור tuple המכיל כל שם ואת הציון שלו בזוגות
# לדוגמא אם נקלטו השמות Charlie Bob Alice
# ונקלטו הציונים ,100 ,85 ,92 78
# (("Alice", 85), ("Bob", 92), ("Charlie", 78)) :יחזור
# חובה להשתמש ב - zip

list_name: list[str]= []
list_score: list[int]= []
out= "done" or -999

while True:
    name= input("your name: ")
    if name.lower() == out.lower():
        break
    list_name.append(name)
print(list_name)

while True:
    score= int(input("enter score: "))
    if score == -999:
        break
    list_score.append(score)
print(list_score)

combines_tuple: tuple = tuple(zip(list_name,list_score))
print("m", combines_tuple)

# .2 מה ההבדל בין tuple ל- list ? מתי תעדיף להשתמש בכל אחד מהם?
# list זה מבנה נתונים שמאפשר לאחסן בתוכו אובייקטים ולשנות אותם ואת תוכנו לפי הצורך
# tuple כמו הרשימה רק שאי אפשר לשנות את האובייקטים ותוכן הטאפל

# .3 ה- tuple הוא רשימה שלא ניתן לשנות אותה.
# הסבר מדוע הקוד הבא לא גורם לשגיאה:

data_tuple = (
{"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0] ["age"] = 31
data_tuple[0] .clear()

# בטאפל הזה יש מספר איברים, כאמור אי אפשר לשנות את כמות וסוג האיברים בטאפל אך ניתן לשנות איברים המורכבים כמו מילונים ורשימות שבתוכו
# כמות וסוג האיברים בטאפל עדיין נשמרים לכן זה לא יוצר שגיאה