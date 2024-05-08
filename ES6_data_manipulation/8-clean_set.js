export default function cleanSet(set, startString) {
  let returnedString = '';

  if (!startString || typeof startString !== 'string') {
    return '';
  }

  for (const element of set) {
    if (element.startsWith(startString)) {
      returnedString += `${element.slice(startString.length)}-`;
    }
  }

  returnedString = returnedString.slice(0, -1);

  return returnedString;
}
