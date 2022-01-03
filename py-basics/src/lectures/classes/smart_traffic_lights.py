# 6kyu | Smart Traffic Lights
# https://www.codewars.com/kata/58587905ed1b4dad6e0000c6/python

class SmartTrafficLight:
    def __init__(self, st1, st2):
        pass

    def turngreen(self):
        return


def test(actual, expected):
    checkmark = '✔️' if expected == actual else '❌'
    print(f"{checkmark} expected -> actual: {str(expected)} -> {str(actual)}")


t = SmartTrafficLight([42, '27th ave'], [72, '3rd st'])
test(t.turngreen(), '3rd st')
test(t.turngreen(), '27th ave')
test(t.turngreen(), None)
