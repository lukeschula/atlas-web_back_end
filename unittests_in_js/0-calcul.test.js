//Task 0 test

const assert = require('assert')
const calculateNumber = require('./0-calcul')

describe('test_group', () => {
  it('returns the sum of its rounded arguments', () => {
    assert.ok(calculateNumber(1, 3) === 4);
    assert.ok(calculateNumber(1, 3.7) === 5);
    assert.ok(calculateNumber(1, 3.4) === 4);
    assert.ok(calculateNumber(1.2, 3) === 4);
    assert.ok(calculateNumber(1.6, 3) === 5);
    assert.ok(calculateNumber(1.5, 3.7) === 6);
  });
});