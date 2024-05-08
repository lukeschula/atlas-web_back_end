export default function createReportObject(employeesList) {
  const newObject = {
    allEmployees: {
        ...employeesList,
    },
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };
  return newObject;
}