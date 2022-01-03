# 7 kyu | What a "Classy" Song
# https://www.codewars.com/kata/6089c7992df556001253ba7d/python

class Song:
    pass


def test(expected, actual):
    checkmark = '✔️' if expected == actual else '❌'
    print(f"{checkmark} expected -> actual: {str(expected)} -> {str(actual)}")


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
test('Mount Moose', mount_moose.title)
test('The Snazzy Moose', mount_moose.artist)
test(5, mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']))
test(2, mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))
test(2, mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']))
test(1, mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']))
test(1, mount_moose.how_many(['Jack', 'jacK']))
