const express = require('express');
const { Server } = require('ws');
const pty = require('node-pty');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the public directory
app.use(express.static('/var/www/public'));

const server = app.listen(port, () => {
  console.log(`Web terminal server running on port ${port}`);
});

const wss = new Server({ server });

wss.on('connection', (ws) => {
  const ptyProcess = pty.spawn('tmux', ['attach'], {
    name: 'xterm-color',
    cols: 80,
    rows: 30,
    cwd: process.env.PWD,
    env: process.env
  });

  ws.on('message', message => {
    try {
      const msg = JSON.parse(message);
      if (msg.action === 'resize') {
        ptyProcess.resize(msg.cols, msg.rows);
      } else if (msg.action === 'input') {
        // Make sure you only write to the ptyProcess here and not elsewhere
        ptyProcess.write(msg.data);
      }
    } catch (e) {
      // Handle non-JSON input data
      ptyProcess.write(message);
    }
  });
	
  ptyProcess.onData(data => {
    ws.send(data);
  });

  ws.on('close', () => {
    ptyProcess.kill();
  });
});
