export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const display = new DataView(buffer);

  try {
    display.setInt8(position, value);
  } catch (error) {
    throw new Error('Position outside range');
  }

  return display;
}
