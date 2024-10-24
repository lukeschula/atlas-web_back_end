// Task 1 - Tests for Task 1

const assert = require('assert');
const calculateNumbers = require('./1-calcul');

// Function to be tested
describe('calculateNumbers', function() {
  // Type = SUM
  describe('When type is SUM...', function() {
    it('should round both numbers and add them.', function() {
      assert.strictEqual(calculateNumbers('SUM', 2.2, 3.3), 5);
    });
  });

  // Type = SUBTRACT
  describe('When type is SUBTRACT...', function() {
    it('should round both numbers and subtract them.', function() {
      assert.strictEqual(calculateNumbers('SUBTRACT', 5.2, 3.3), 2);
    });
  });

  // Type = DIVIDE
  describe('When type is DIVIDE...', function() {
    it('should round both numbers and divide them.', function() {
      assert.strictEqual(calculateNumbers('DIVIDE', 10.3, 2.3), 5);
    });

    it('should return Error.', function() {
      assert.strictEqual(calculateNumbers('DIVIDE', 2.2, 0), 'Error');
    });
  });
});