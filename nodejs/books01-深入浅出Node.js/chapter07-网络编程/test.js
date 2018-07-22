const net = require('net');
var server = net.createServer();
server.on('connection', function(c) {
    console.log('client connected');
  c.on('end', () => {
    console.log('client disconnected');
  });
  c.write('good\r\n');
  c.pipe(c);
});
server.listen(8124);
// server.listen('/tmp/echo.sock');

