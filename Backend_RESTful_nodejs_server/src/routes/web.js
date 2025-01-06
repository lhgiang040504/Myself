const express = require('express')
const router = express.Router()
const {getHomepage, getABC} = require('../controllers/homeController')

// Route 
// router.Method('/route', handler)
router.get('/', getHomepage)
  
// Route
router.get('/abc', getABC)

module.exports = router