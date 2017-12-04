var mysql = require('mysql');

//Put your mysql configuration settings - user, password, database and port

function getConnection(){
    var connection = mysql.createConnection({

        host     : 'localhost',
        user     : 'root',
        password : 'root',
        database : 'phishing',
        port	 : 3306

    });


    return connection;
}
var connection=getConnection();
connection.connect(function(error){
        if(!!error){
            console.log("error");
        }else{
            console.log("connected");
        }
    }
);
function fetchData(callback,sqlQuery){

    console.log("\nSQL Query::"+sqlQuery);
    var connection=getConnection();
    try
    {
        connection.query(sqlQuery, function(err, rows, fields) {
            if(err){

                console.log("ERROR: " + err.message);
            }
            else
            {	// return err or result

                callback(err, rows);

            }
        });
    }
    catch (ex)
    {
        console.log('IN CATCH');
        callback(ex,1);
        console.log(ex);

    }
    console.log("\nConnection closed..");
    connection.end();
}

exports.fetchData=fetchData;

