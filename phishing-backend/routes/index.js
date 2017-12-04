var express = require('express');
var router = express.Router();
var request = require('request');
var app=express();
var mysql=require("./mysql");


/*
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
*/

/*app.get('/',function (req,resp) {
    connection.query("select *from admin", function (error, rows, fields) {
        if (!!error) {
            console.log("error in query");
        } else {
            console.log("success\n");
            console.log(rows);
        }

    })
});*/

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/api/check', function(req, res, next) {
  console.log(req.query.id);
  console.log(req.query.url);
  var postData = {
    url: req.query.url
  }
  var options = {
    method: 'post',
    body: postData,
    json: true,
    url: "http://54.202.123.8/check"
  }
  request.post(options, function(err,response,body){
    if(err) {
      return res.status(200).json({'status': 500, 'message' : 'some error occoured, please try again later'});
    } else {
      if(body.result) {
        return res.status(200).json({'status': 200, 'message' : 'phishing_detected'});
      } else {
        return res.status(200).json({'status': 200, 'message' : 'website safe'});
      }
    }
  });
})


router.post('/api/report', function(req, res, next) {
  console.log(req.body);
  var insert="insert into reports (url) values ('"+req.body.data+"');";
  mysql.fetchData(function(err, result) {
    if(err) {
      return res.status(200).json({'status': 500, 'message' : 'some error occoured, please try again later'});
    } else {
      return res.status(200).json({'status': 200, 'message' : 'Thanks for your feedback'});
    }
  },insert);
})

//app.listen(3001);
module.exports = router;
