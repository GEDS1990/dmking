var picparse = {};
var http = require('http');
var querystring = require('querystring');

var contents = querystring.stringify({
  user_name:'byvoid',
  user_pw:'byvoid',
  yzmtype_mark:'byvoid',
  upload:'Zijing'
});

var options = {
  host:'http://v1-http-api.jsdama.com',
  path:'/api.php?mod=php&act=upload',
  method:'POST',
  headers:{
      'Content-Type':'multipart/form-data',
      'Content-Length':contents.length
  }
}

/**
 * 图片验证码解析
 */
picparse.VerificationCode = function(){
  var req = http.request(options, function(res){
    res.setEncoding('utf8');
    res.on('data',function(data){
      // {"result":true,"data":{"id":22973362,"val":6209}}
        console.log("data:",data); 
    });
  });
  req.write(contents);
  req.end;
},
 
module.exports = picparse;