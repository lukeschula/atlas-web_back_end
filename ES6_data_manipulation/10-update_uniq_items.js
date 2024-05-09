export default function updateUniqueItems(newMap) {
  if (!(newMap instanceof Map)) {
    throw new TypeError('Cannot process');
  }
  for (const [ item, quantity ] of newMap) {
    if (quantity === 1) {
      newMap.set(item, 100);
    }
  }
}
