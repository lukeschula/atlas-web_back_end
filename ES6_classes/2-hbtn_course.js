export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }

    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  get name() {
    return this._name;
  }

  set name(newValue) {
    if (typeof newValue === 'string') {
      this._name = newValue;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(newValue) {
    if (typeof newValue === 'number') {
      this._length = newValue;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newValue) {
    if (typeof newValue === 'object') {
      this._student = newValue;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}