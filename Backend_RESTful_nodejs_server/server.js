const express = require('express')
//import express from 'express'
const app = express()
const port = 3000

// Config template engine
app.set('views', './src/views')
app.set('views engine', 'ejs')
// If error
// const path from 'path'
// app.set('views', path.join(__dirname, './src/views'))

// Route 
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// Route
app.get('/abc', (req, res) => {
    res.render('sample.ejs')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})