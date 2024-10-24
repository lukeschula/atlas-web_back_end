// Task 1 Combining descriptions

function calculateNumbers(type, a, b) {

    const numA = Math.round(a);
    const numB = Math.round(b);

    if (type === "SUM") {
      return numA + numB;
    } else if (type === "SUBTRACT") {
      return numA - numB;
    } else if (type === "DIVIDE") {
      if (numB === 0) {
        return('Error');
      }
      return numA / numB;
    } else {
      // throw new Error('Type must be SUM, SUBTRACT, or DIVIDE')
    }
  }

  module.exports = calculateNumbers;