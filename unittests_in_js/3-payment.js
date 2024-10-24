// Task 3 Spies

const Utils = require('./utils.js')
function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping)
  console.log('The total is: ' + sum)
}
module.exports = sendPaymentRequestToApi