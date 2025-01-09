const connection = require('../config/database')

const getHomepage = (req, res) => {
    return res.render('home.ejs')
}

const getABC = async (req, res) => {
    // connection.query(
    //     `SELECT * FROM Users `,
    //     function (err, result) {
    //         console.log(result)
    //     }
    // )
    
    try {
        const [results, fields] = await connection.query(`SELECT * FROM Users`);
        console.log(results, fields)
    } catch (err) {
        // Log or handle the error here
        console.error("An error occurred during the query:", err.message);
        console.error("Error stack trace:", err.stack);
    }
        
    res.render('sample.ejs')
}

const getCreateUser = (req, res) => {
    return res.render('create.ejs')
}

const postCreateUser = async (req, res) => {
    let name = req.body.name;
    let email = req.body.email;
    let city = req.body.city;
    console.log(name, email, city)

    // const [results, fields] = await connection.query(
    //     `INSERT INTO Users (email, name, city) VALUES (?, ?, ?) `,
    //     [email, name, city],
    //     function (err, result) {
    //         if (err) {
    //             console.log(err.message);
    //         } else {
    //             console.log('success'); 
    //             res.send("success")   
    //         }
    //     }
    // )

    try {
        const [results, fields] = await connection.query(
            `INSERT INTO Users (email, name, city) VALUES (?, ?, ?) `,
            [email, name, city])
        console.log(results, fields)
        console.log('success')
        res.send("success")   
    } catch (err) {
        // Log or handle the error here
        console.error("An error occurred during the query:", err.message);
        console.error("Error stack trace:", err.stack);
    }
}

module.exports = {
    getHomepage,
    getABC,
    getCreateUser,
    postCreateUser,
}