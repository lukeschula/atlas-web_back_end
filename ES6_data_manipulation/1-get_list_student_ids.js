export default function getListStudentIds(studentList) {
  if (!Array.isArray(studentList)) {
    const newlist = [];
    return newlist;
  }

  const newArray = studentList.map((item) => item.id);

  return newArray;
}
