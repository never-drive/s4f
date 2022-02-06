/**
 * 7 kyu | What a "Classy" Song
 * https://www.codewars.com/kata/6089c7992df556001253ba7d/javascript
 */

class Song {
    constructor(title, artist) {
        // TODO
    }
    howMany(people) {
        return [];
    }
}

function test(actual, expected) {
    let checkmark = expected == actual ? '✔️' : '❌';
    console.log(`${checkmark} expected -> actual: ${new String(expected)} -> ${new String(actual)}`);
}

let mountMoose = new Song('Mount Moose', 'The Snazzy Moose');
test('Mount Moose', mountMoose.title);
test('The Snazzy Moose', mountMoose.artist);
test(5, mountMoose.howMany(['John', 'Fred', 'Bob', 'Carl', 'RyAn']));
test(2, mountMoose.howMany(['JoHn', 'Luke', 'AmAndA']));
test(2, mountMoose.howMany(['Amanda', 'CalEb', 'CarL', 'Furgus']));
test(1, mountMoose.howMany(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']));
test(1, mountMoose.howMany(['Jack', 'jacK']));
