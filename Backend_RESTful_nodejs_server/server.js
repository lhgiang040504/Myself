// const express = require('express')
import express from 'express'
const app = express()
const port = 3000

// Route
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// Route
app.get('/abc', (req, res) => {
    res.send('<h1>Check</h1>')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})