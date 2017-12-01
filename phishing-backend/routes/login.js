var express = require('express');
var router = express.Router();

router.post('/login', function (req, res, next) {

    var reqUsername = req.body.EmailId;
    var reqPassword = req.body.Password;

    var getUser = "SELECT * FROM admin WHERE emailid = '"+reqUsername+"' and password = '"+reqPassword+"'";
    console.log("query is :" +getUser);

    mysql.fetchData(function(err, result){
        if(err){
            throw err;
        }
        else{
            console.log('Valid Login');
            var getLogs = "SELECT * FROM logs WHERE isPhished=1";
            console.log("query is :" +getLogs);

            mysql.fetchData(function(err, result){
                if(err){
                    throw err;
                }
                else{
                    console.log('Success');

                }

            },getLogs);
        }

    },getUser);

});

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
