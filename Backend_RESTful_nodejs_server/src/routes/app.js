const express = require('express')
const router = express.Router()
const {oldConnection, poolConnection} = require('../controllers/monitor')

router.get('/old', oldConnection)

router.get('/pool', poolConnection)

module.exports = router