export default function hasValuesFromArray(set, array) {
  const elementsPresent = array.every((element) => set.has(element));
  return elementsPresent;
}
