//Task 6 test

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', (done) => {
  it('async test with done', () => getPaymentTokenFromAPI(true)
    .then((success) => {
      expect(success).to.eql({ data: 'Successful response from the API' });
    }));
});