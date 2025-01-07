const express = require('express')
require('dotenv').config()

// Import express from 'express'
const app = express()
const port = process.env.PORT || 8888
const hostname = 'localhost'

// Config views engine
const config_viewEngine = require('./config/viewEngine')
config_viewEngine(app);

// Test database connection
const mysql = require('mysql2')
const connection = mysql.createConnection({
  host: 'localhost',
  port: 3307, //defaut 3306
  user: 'root',
  database: 'admin',
  password: 'admin',
})

// Simple query
connection.query(
  'select * from Users u',
  function (err, results, fields) {
    console.log(">>result = ", results)
    console.log(">>fields = ", fields)
  }
)

// Router test
const web = require('./routes/web')
app.use('/web', web)

app.listen(port, hostname, () => {
  console.log(`Example app listening on port ${port}`)
})