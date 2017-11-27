var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/api/check', function(req, res, next) {
  return res.status(200).json({'status': 200, 'message' : 'success'});
})

module.exports = router;
