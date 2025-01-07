require('dotenv').config()
const mysql = require('mysql2')

// const connection = mysql.createConnection({
//   host: process.env.DB_HOST,
//   port: Number(process.env.DB_PORT), //defaut 3306
//   user: process.env.DB_USER,
//   database: process.env.DB_NAME,
//   password: process.env.DB_PASSWORD,
// })

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  port: Number(process.env.DB_PORT), // Default is 3306
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  connectionLimit: 10, // Optional: Adjust based on your requirements
  waitForConnections: true,
  queueLimit: 0
});

module.exports = pool