# 7 kyu | What a "Classy" Song
# https://www.codewars.com/kata/6089c7992df556001253ba7d/python

class Song:
    pass


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
print('actual: ' + mount_moose.title + ' expected: ' + 'Mount Moose')
print('actual: ' + mount_moose.artist + ' expected: ' + 'The Snazzy Moose')
print('actual: ' + str(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn'])) + ' expected: ' + str(5))
print('actual: ' + str(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA'])) + ' expected: ' + str(2))
print('actual: ' + str(mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus'])) + ' expected: ' + str(2))
print('actual: ' + str(mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE'])) + ' expected: ' + str(1))
print('actual: ' + str(mount_moose.how_many(['Jack', 'jacK'])) + ' expected: ' + str(1))
