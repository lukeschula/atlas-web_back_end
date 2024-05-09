export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const newList = studentList.map((item) => {
    const newInput = newGrades.find((grade) => grade.studentId === item.id);
    const grade = newInput ? newInput.grade : 'N/A';
    return { ...item, grade };
  });

  const updatedStudentList = newList.filter((item) => item.location === city);

  return updatedStudentList;
}
