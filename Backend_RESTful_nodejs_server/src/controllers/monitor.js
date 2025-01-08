const oldConnection = (req, res) => {
    try {
        let totalExec = 0;
        for (let i = 0; i < 1000; i++) {
            let pre_query = new Date().getTime();
            let con = null
            con = require('../config/old')

            con.query(
                'SELECT * FROM Users',
                function (err, results, fields) {
                    // get a timestamp after running the query
                    const post_query = new Date().getTime();
                    const duration = (post_query - pre_query) / 1000; //unit: second
                    totalExec += duration;

                    // console.log(">>>", " i = ", i, " duration = ", duration)

                    if (i == 999) {
                        const ave = totalExec / 1000;
                        return res.send("Average = " + ave)
                    }
                }
            );

            //con.destroy();
        }
    } catch (error) {
        console.log(">>> check error old: ", error)
    }
}

const poolConnection = (req, res) => {
    try {
        let totalExec = 0;

        let con = require('../config/database')

        for (let i = 0; i < 1000; i++) {
            let pre_query = new Date().getTime();
            con.query(
                'SELECT * FROM Users',
                function (err, results, fields) {
                    // get a timestamp after running the query
                    const post_query = new Date().getTime();
                    const duration = (post_query - pre_query) / 1000; //unit: second
                    totalExec += duration;

                    // console.log(">>>", " i = ", i, " duration = ", duration)

                    if (i == 999) {
                        const ave = totalExec / 1000;
                        return res.send("Average = " + ave)
                    }
                }
            );
        }
    } catch (error) {
        console.log(">>> check error pool: ", error)
    }
}

module.exports = {
    oldConnection,
    poolConnection
}