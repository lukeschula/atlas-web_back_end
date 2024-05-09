export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const divide = mathFunction();
    queue.push(divide);
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
