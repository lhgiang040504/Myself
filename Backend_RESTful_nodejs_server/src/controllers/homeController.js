const connection = require('../config/database')

const getHomepage = (req, res) => {
    // Simple query
    connection.query(
        'select * from Users u',
        function (err, results, fields) {
            console.log(">>result = ", results)
            res.send(JSON.stringify(results))
        }
    )
}

const getABC = (req, res) => {
    res.render('sample.ejs')
}

module.exports = {
    getHomepage,
    getABC
}