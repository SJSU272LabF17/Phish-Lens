var express = require('express');
var router = express.Router();
var mysql=require("./mysql");
var ejs = require("ejs");


function login(req,res)
{
    ejs.renderFile('./views/index.ejs',function(err,result){
        // if it is success
        if(!err)
        {
            res.end(result);
        }
        //ERROR
        else
        {
            res.end("ERROR OCCURED ");
            console.log(err);
        }
    });
}

function postlogin(req,res){
    var username= req.body.username;
    var password= req.body.password;

    var getuser="select * from admin where email ='"+username+"' AND password='"+password+"'";
    mysql.fetchData(function (err,result) {
        if(err)
        {
            res.end("ERROR OCCURED ");
            console.log(err);
        }
        else {
            console.log("---------------get user query succesful -----");
            if (result.length == 1) {
                console.log("---------------user found -----");

                var getlogs = "select * from logs where isPhished =1";
                var logs = [];
                mysql.fetchData(function (err, result) {
                    if (result.length > 0) {

                        console.log("---------------posts found -----");
                        for (var i = 0; i < result.length; i++) {
                            var log = {
                                clientId: result[i].clientId,
                                website: result[i].website,
                                isPhished: result[i].isPhished,
                                isReportedPhish: result[i].isReportedPhish,
                                date: result[i].date

                            }
                            console.log("---------------logs found -----");
                            logs.push(log);
                        }

                    }
                    console.log("---------------posts query dones -----");
                    ejs.renderFile('./views/login.ejs', {logs: logs}, function (err, result) {
                        // if it is success
                        if (!err) {
                            res.end(result);
                        }
                        //ERROR
                        else {
                            res.end("ERROR OCCURED ");
                            console.log(err);
                        }
                    });
                }, getlogs)
            }
            else {
                res.end("No user Found!!")
            }
        }

    },getuser);
}




exports.login=login;
exports.postlogin = postlogin;
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
