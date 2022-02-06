/**
 * 6kyu | Smart Traffic Lights
 * https://www.codewars.com/kata/58587905ed1b4dad6e0000c6/javascript
 */

class SmartTrafficLight {
    constructor(st1, st2) {
        // TODO
    }
    turngreen() {
        return null;
    }
}

function test(actual, expected) {
    let checkmark = expected == actual ? '✔️' : '❌';
    console.log(`${checkmark} expected -> actual: ${new String(expected)} -> ${new String(actual)}`);
}

let t = new SmartTrafficLight([42, '27th ave'], [72, '3rd st']);
test(t.turngreen(), '3rd st');
test(t.turngreen(), '27th ave');
test(t.turngreen(), null);
