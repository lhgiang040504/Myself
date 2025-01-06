const express = require('express')
const router = express.Router()

// Route 
router.get('/', (req, res) => {
    res.send('Hello World and modify')
  })
  
// Route
router.get('/abc', (req, res) => {
    res.render('sample.ejs')
})

module.exports = router