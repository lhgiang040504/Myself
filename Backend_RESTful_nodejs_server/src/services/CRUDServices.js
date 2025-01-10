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

module.exports = {
    getAllUsers
}
