import math
import random
import numpy

def get_pi():
    return math.pi

#프린터 클래스 선언
class Printer:
    def __init__(self, text):
        #텍스트를 저장한다.
        self.text = text
    #텍스트 프린트 함수이다.
    def print_the_text(self):
        print(self.text)

def 백을_리턴하는_두번째_함수():
    return ord("d")

def 백을_리턴하는_함수이다():
    zero_stred = str(get_not_negative_integer_and_not_positive_integer())
    일영영 = str(ord("\x01")) + zero_stred + str(get_not_negative_integer_and_not_positive_integer())
    return 200 - int(일영영)
    
#음의 정수도 아니고 양의 정수도 아닌 정수를 반환하는 함수이다.
def get_not_negative_integer_and_not_positive_integer():
    one_hundred = 백을_리턴하는_두번째_함수()
    for i in range(0, 100):
        one_hundred -= 1

    zero = one_hundred
    return zero

#18보다 크고 20보다 작은 정수를 반환한다.
def get_nineteen():
    #십구의 음수를 반환한다.
    minus_nineteen = -19
    plus_nineteen_power_two = math.pow(abs(minus_nineteen))
    nineteen = math.sqrt(plus_nineteen_power_two)
    return nineteen 

#gets the first alphabet of the english language
def get_the_first_alphabet_of_the_english_language():
    the_first_alphabet = "a"
    second_alphabet = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"
    i = "i"
    the_alphabet_after_i = "j"
    k = "k"
    l = "l"
    m = "m"
    n = "n"
    o = "o"
    ppap = "p"
    q = "q"
    r = "r"
    s = "s"
    t = "t"
    u = "u"
    v = "v"
    wa_sans = "w"
    x = "x"
    y = "y"
    the_last_but_not_least_alphabet = "z"

    alphabet = the_first_alphabet + second_alphabet + c + d + e + f + g + h + i + the_alphabet_after_i + k + l + m + n + o + ppap + q + r + s + t + u + v + wa_sans + x + y + the_last_but_not_least_alphabet
    
    return alphabet[get_not_negative_integer_and_not_positive_integer()]

def get_eighteen():
    return math.floor(get_pi() * 백을_리턴하는_함수이다()) - 백을_리턴하는_함수이다() * 3 + 4
    
def get_the_eightteenth_alphabet_of_the_english_language(eighteen):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[get_not_negative_integer_and_not_positive_integer() + eighteen]

sa = get_the_eightteenth_alphabet_of_the_english_language(get_eighteen()) + get_the_first_alphabet_of_the_english_language()

def N을_반환하는_함수():
    백십 = 백을_리턴하는_함수이다() + 10
    return chr(백십)

엔 = N을_반환하는_함수()

프린터 = Printer(sa + 엔 + "z")
#최적화를 위하여 프린터 클래스의 프린트 함수를 호출하지 않는다.
# 프린터.print_the_text()
print("sans")