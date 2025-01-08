const express = require('express')
const router = express.Router()
const {getHomepage, getABC, getCreateUser, postCreateUser} = require('../controllers/homeController')

// Route 
// router.Method('/route', handler)
router.get('/', getHomepage)
  
// Route
router.get('/abc', getABC)

router.get('/create', getCreateUser)
router.post('/create-user', postCreateUser)

module.exports = router