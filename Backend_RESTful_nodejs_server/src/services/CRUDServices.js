const connection = require("../config/database")

const getAllUsers = async () => {
    try {
        [results, fields] = await connection.query(`SELECT * FROM Users`);
        return results
    } catch (err) {
        // Log or handle the error here
        console.error("An error occurred during the query:", err.message);
        console.error("Error stack trace:", err.stack);
    }
}

const getUserbyId = async (req)=> {
    [results, fields] = await connection.query(`SELECT * FROM Users WHERE id = ?`, [req.params.id]);
    return results[0]
}

module.exports = {
    getAllUsers, 
    getUserbyId
}
