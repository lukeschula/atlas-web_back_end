export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(newValue) {
    if (typeof newValue === 'string') {
      this._code = newValue;
    }
  }

  get name() {
    return this._name;
  }

  set name(newValue) {
    if (typeof newValue === 'string') {
      this._name = newValue;
    }
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
