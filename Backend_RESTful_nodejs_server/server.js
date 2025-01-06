const express = require('express')
require('dotenv').config()

//import express from 'express'
const app = express()
const port = process.env.PORT || 8888
const hostname = 'localhost'

// Config template engine
app.set('views', './src/views')
app.set('views engine', 'ejs')
// If error
// const path from 'path'
// app.set('views', path.join(__dirname, './src/views'))

// Config static files
const path = require('path')
app.use(express.static(path.join(__dirname, './src/public')))






// Route 
app.get('/', (req, res) => {
  res.send('Hello World and modify')
})

// Route
app.get('/abc', (req, res) => {
    res.render('sample.ejs')
})

app.listen(port, hostname, () => {
  console.log(`Example app listening on port ${port}`)
})