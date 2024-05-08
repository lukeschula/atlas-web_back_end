import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(newValue) {
    this.amount = newValue;
  }

  get currency() {
    return this._currency;
  }

  set currency(newValue) {
    this._currency = newValue;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}