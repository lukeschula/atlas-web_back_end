// Create a more complex HTTP server using Node's HTTP module

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  const filepath = './database.csv';
  try {
    if (req.url === '/students') {
      const studentList = await countStudents(filepath);
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(`This is the list of our students.\n${studentList}`);
    } else if (req.url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello Holberton School!');
    } else {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('Not Found');
    }
  } catch (err) {
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end('Server Error');
  }
});

app.listen(1245, () => {
  console.log('...');
});

module.exports = app;