const express = require('express')
require('dotenv').config()

// Import express from 'express'
const app = express()
const port = process.env.PORT || 8888
const hostname = 'localhost'

// Config views engine
const config_viewEngine = require('./config/viewEngine')
config_viewEngine(app);

// Config request body
app.use(express.json())
app.use(express.urlencoded({extended: true}))

// Router test
const web = require('./routes/web')
app.use('/', web)

// Router app
const monitor_app = require('./routes/app')
app.use('/app', monitor_app)

app.listen(port, hostname, () => {
  console.log(`Example app listening on port ${port}`)
})