// Reading a file synchronously with Node JS

const fs = require('fs');


function countStudents(path) {
  let fileLine;
  try {
    fileLine = fs.readFileSync(path, 'utf8');
    // stores the file content as a long string
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  console.log(`Number of students: ${fileLine.split('\n').length - 2}`);
  // calculate student num: splite fileLine with '\n', get file line num, then minus 1 head line and 1 end empty line
  const CScount = fileLine.split('\n').filter((line) => line.includes('CS')).length;
  const SWEcount = fileLine.split('\n').filter((line) => line.includes('SWE')).length;
  // how many students on field CS or SWE
  let CSlist = fileLine.split('\n').filter((line) => line.includes('CS')).map((line) => line.split(',')[0]);
  let SWElist = fileLine.split('\n').filter((line) => line.includes('SWE')).map((line) => line.split(',')[0]);
  // filter only gets CS or SWE students, and get their firstname (first item in the array [0])
  CSlist = CSlist.join(', ');
  SWElist = SWElist.join(', ');
  // Joins the extracted names into comma-separated lists using join
  console.log(`Number of students in CS: ${CScount}. List: ${CSlist}`);
  console.log(`Number of students in SWE: ${SWEcount}. List: ${SWElist}`);
}

module.exports = countStudents;
