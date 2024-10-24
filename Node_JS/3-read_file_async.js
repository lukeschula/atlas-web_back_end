// Reading a file asynchronously with Node JS

const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    const lines = data.trim().split('\n');
    lines.shift();
    const total = lines.length;
    let result = `Number of students: ${total}\n`;
    // console.log(`Number of students: ${total}`);
    const fields = {};
    lines.forEach((line) => {
      // eslint-disable-next-line no-unused-vars
      const [firstname, lastname, age, field] = line.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });
    for (const [field, students] of Object.entries(fields)) {
      result += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
    }
    result = result.trim();
    // console.log(result);
    return result;
  } catch (err) {
    console.error('Cannot load the database');
    throw err;
  }
}

module.exports = countStudents;
