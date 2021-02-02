require('dotenv/types').config()
const {NodeSSH} = require('node-ssh')
const ssh = new NodeSSH()

async function start() {
  await ssh.connect({
    host: process.env.REMOTE_HOST,
    username: process.env.REMOTE_USER,
    password: process.env.REMOTE_PWD
  })
  await ssh.putDirectory("site/", process.env.REMOTE_PATH)
  await ssh.dispose()
  console.log('done')
}

start()