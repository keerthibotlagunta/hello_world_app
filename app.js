const http = require('http');

const hostname = '0.0.0.0';   // listen on all network interfaces
const port = 8080;            // must match CDK container_port

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World Testing!!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
