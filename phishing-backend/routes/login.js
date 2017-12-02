var express = require('express');
var router = express.Router();
var mysql=require("./index");

var mysql = require('mysql')
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'root',
    database : 'phishing'
});

connection.connect(function(error){
        if(!!error){
            console.log("error");
        }else{
            console.log("connected");
        }
    }
);

exports.login = function(req,res) {
    var reqUsername = req.body.username;
    var reqPassword = req.body.password;


    var getUser = "SELECT * FROM admin WHERE email = 'saisupraja@gmail.com' and password = 'admin'";
    console.log("query is :" + getUser);

    connection.query(getUser, function (err, rows, fields) {

        if (err) {
            throw err;
        }
        else {
            console.log('Valid Login');
            var getLogs = "SELECT * FROM logs WHERE isPhished=1";
            console.log("query is :" + getLogs);

            connection.query(getLogs, function (err, rows, fields) {
                if (err) {
                    throw err;
                }
                else {
                    console.log('Success');

                }

            }, getLogs);
        }

    }, getUser);


}
module.exports = router;


/*exports.login = function(req,res){
    var email= req.body.email;
    var password = req.body.password;
    connection.query('SELECT * FROM admin WHERE email = ?',[email], function (error, results, fields) {
        if (error) {
            // console.log("error ocurred",error);
            res.send({
                "code":400,
                "failed":"error ocurred"
            })
        }else{
            // console.log('The solution is: ', results);
            if(results.length >0){
                if([0].password == password){
                    res.send({
                        "code":200,
                        "success":"login sucessfull"
                    });
                }
                else{
                    res.send({
                        "code":204,
                        "success":"Email and password does not match"
                    });
                }
            }
            else{
                res.send({
                    "code":204,
                    "success":"Email does not exits"
                });
            }
        }
    });
}*/
