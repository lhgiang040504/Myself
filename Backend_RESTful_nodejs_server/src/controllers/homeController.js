const connection = require('../config/database')

const getHomepage = (req, res) => {
    return res.render('home.ejs')
}

const getABC = (req, res) => {
    res.render('sample.ejs')
}

const postCreateUser = (req, res) => {
    console.log(req.body)
    //console.log(res)
    res.send("Create successfully")
}


module.exports = {
    getHomepage,
    getABC,
    postCreateUser,
}