const connection = require('../config/old')

const getHomepage = (req, res) => {
    return res.render('home.ejs')
}

const getABC = (req, res) => {
    connection.query(
        `SELECT * FROM Users `,
        function (err, result) {
            console.log(result)
        }
    )
    res.render('sample.ejs')
}

const postCreateUser = (req, res) => {
    let name = req.body.name;
    let email = req.body.email;
    let city = req.body.city;
    console.log(name, email, city)

    connection.query(
        `INSERT INTO Users (email, name, city) VALUES (?, ?, ?) `,
        [email, name, city],
        function (err, result) {
            if (err) {
                console.log(err.message);
            } else {
                console.log('success');    
            }
        }
    )

}

module.exports = {
    getHomepage,
    getABC,
    postCreateUser,
}