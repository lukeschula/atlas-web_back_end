export default function createEmployeesObject(departmentName, employees) {
  const display = {};

  display[departmentName] = employees;
  return display;
}