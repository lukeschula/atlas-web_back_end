export default function getStudentIdsSum(students) {
  const totalSum = students.reduce((total, student) => total + student.id, 0);
  return totalSum;
}
