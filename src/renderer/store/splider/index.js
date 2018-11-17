var splider = {};
var sd = require('silly-datetime');
var db = require('../../db');
var cheerio=require('cheerio');

splider.data = {
  roomid: '',
  href: '',
  title: '',
  renq: '',
  roominfos: []
};



/**
 * 图片验证码解析
 */
splider.picsParse = function(){

},
/**
 * 虎牙
 */
splider.hy = function(){
//   (async () => {
//       var browser = await puppeteer.launch();
//       var page = await browser.newPage();
//       await page.goto('https://github.com/GoogleChrome/puppeteer');
//       await page.screenshot({path: 'puppeteer.png'});
// debugger;
//       await browser.close();
//   })();
},
  /**
   * 虎牙
   */
  splider.hyselenium = function(){
  // var webdriver = require('selenium-webdriver');
  // var By = require('selenium-webdriver').By;
  // var until = require('selenium-webdriver').until;
  // const chrome = require('selenium-webdriver/chrome');
  // const firefox = require('selenium-webdriver/firefox');
  // const {Builder, By, Key, until} = require('selenium-webdriver');
  // const screen = {
  //   width: 640,
  //   height: 480
  // };
  
  // let driver = new Builder()
  //     .forBrowser('chrome')
  //     .setChromeOptions(new chrome.Options().headless().windowSize(screen))
  //     .setFirefoxOptions(new firefox.Options().headless().windowSize(screen))
  //     .build();

  // var webdriver = require('selenium-webdriver'),
  //       chrome    = require('selenium-webdriver/chrome')
  //       By        = webdriver.By,
  //       until     = webdriver.until,
  //       options   = new chrome.Options();
  //       options.addArguments('--headless');
  //   var path = require('chromedriver').path;
  //   var service = new chrome.ServiceBuilder(path).build();
  //       chrome.setDefaultService(service);
  //   var driver = new webdriver.Builder().forBrowser('chrome').withCapabilities(options.toCapabilities()).build();

  // var firefox = require('selenium-webdriver/firefox');
  // var options = new firefox.Options();
  // options.addArguments("-headless");
  // var driver = new webdriver.Builder()
  //   .forBrowser('firefox')
  //   .setFirefoxOptions(options)
  //   .build();
  // var driver = await puppeteer.launch();
  // var phantomjs = require('phantomjs-prebuilt');
  // var driver = new phantomjs.Driver();
  // By = webdriver.By,
  // until = webdriver.until;
  // const phantomjs_exe = require('phantomjs-prebuilt').path;
  // var options = webdriver.ChromeOptions();
  // options.add_argument('headless');
  // var driver = new webdriver.Builder()
  //   .forBrowser('chrome')
  //   .setChromeOptions(executable_path='chrome_executable_path',chrome_options=options)
  //   .build();
  // // capabilities.set('phantomjs.ghostdriver.path',
  // //     '/Users/xyz/ghostdriver-master/src/main.js');
  // var capabilities = webdriver.Capabilities.phantomjs();
  // capabilities.set("phantomjs.binary.path", phantomjs_exe);
  // // capabilities.set('executable_path','/Users/geds/Documents/shzhyun/mashi/danmu/eleexampple/electron-manage/src/python/core/driver/phantomsjs/mac/bin/phantomjs');
  // var driver = new webdriver.Builder().
  //     withCapabilities(capabilities).
  //     build();
  //setup custom phantomJS capability
  // const phantomjs_exe = require('phantomjs-prebuilt').path;
  // var customPhantom = webdriver.Capabilities.phantomjs(executable_path='/Users/geds/Documents/shzhyun/mashi/danmu/eleexampple/electron-manage/src/python/core/driver/phantomsjs/mac/bin/phantomjs');
  // customPhantom.set("phantomjs.binary.path", phantomjs_exe);

  //build custom phantomJS driver
  // const driver = new selenium.Builder().
  //       withCapabilities(customPhantom).
  //       build();
  var norTime = 30000;

  console.log(sd.format(new Date(), 'YYYY-MM-DD HH:mm')+":开始虎牙直播自动弹幕...");
  
  // var driver = new WebDriver( null, executor, null );
    driver.get('https://www.huya.com/l');
    
    // 登陆链接
    // driver.wait(until.elementLocated(By.xpath('//*[@id="nav-login"]')), 10000).click();
    // 注册按钮
    driver.wait(until.elementLocated(By.xpath('//*[@id="nav-regiest"]')), 90000).click().then(function(){
      // 登录tab
      driver.wait(until.elementLocated(By.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div[1]/a[1]')), 120000).click().then(function(){
        // 用户名
        driver.wait(until.elementLocated(By.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span/input')), 30000).sendKeys("15850358189").then(function(){
          // 密码框
          driver.wait(until.elementLocated(By.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span/input')), 30000).sendKeys("yang729").then(function(){
            // 登录按钮
            driver.wait(until.elementLocated(By.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/a')),30000).click().then(function(){
              // 房间链接
              // driver.wait(until.elementLocated(By.xpath('//*[@id="js-live-list"]/li[1]/a[2]')),90000).then(function(){
              driver.sleep(3000).then(function(){
                var homeWindowHandle = driver.getWindowHandle();
                // 循环房间
                var jslivelist = driver.findElements(By.xpath('//*[@id="js-live-list"]'));
                var c = 0;
                function iterator(c){
                  console.log("c:"+c);
                  if(c == jslivelist.length){
                    alert("完成"+jslivelist.length+"个房间的发送！");
                    return;
                  }
                  debugger;
                  driver.wait(until.elementLocated(By.xpath('//*[@id="js-live-list"]/li['+c+']/a[2]')),30000).click().then(function(){
                    var WindowHandles = driver.getAllWindowHandles();
                    for(wh in WindowHandles){
                      if(wh != homeWindowHandle){
                        driver.switchTo(wh);
                        driver.sleep(3000).then(function(){
                          driver.findElement(By.xpath('//*[@id="pub_msg_input"]')).sendKeys("66666").then(function(){
                            driver.findElement(By.xpath('//*[@id="msg_send_bt"]')).click().then(function(){
                              driver.switchTo(homeWindowHandle);
                              iterator(c+1);
                            });
                          });
                        });
                      }
                    }
                  });
                  // driver.findElement(By.xpath('//*[@id="js-live-list"]/li['+c+']/a[2]')).click().then(function(){
                  //   driver.sleep(3000).then(function(){
                  //     var WindowHandles = driver.getAllWindowHandles();
                  //     for(wh in WindowHandles){
                  //       if(wh != homeWindowHandle){
                  //         driver.switchTo(wh);
                  //         driver.sleep(3000).then(function(){
                  //           driver.findElement(By.xpath('//*[@id="pub_msg_input"]')).sendKeys("66666").then(function(){
                  //             driver.findElement(By.xpath('//*[@id="msg_send_bt"]')).click().then(function(){
                  //               driver.switchTo(homeWindowHandle);
                  //             });
                  //           });
                  //         });
                  //       }
                  //     }
                  //   });
                  // });
                  
                }
                iterator(0);
                // db.LRANGE("roomids", 0, -1, function(err,value){
                //   driver.findElement(By.xpath('//*[@id="js-live-list"]/li['+value+']/a[2]')).click().then(function(){
                //     driver.sleep(3000).then(function(){
                //       var WindowHandles = driver.getAllWindowHandles();
                //       for(wh in WindowHandles){
                //         if(wh != homeWindowHandle){
                //           driver.switchTo(wh);
                //           driver.findElement(By.xpath('//*[@id="pub_msg_input"]')).sendKeys("66666").then(function(){
                //             driver.findElement(By.xpath('//*[@id="msg_send_bt"]')).click();
                //           });
                //         }
                //         driver.switchTo(homeWindowHandle);
                //       }
                //     });
                //   });
                // });
              });
              // });
            });
          });
        });
        
      });
    });    
};
splider.getAllRooms = function() {
  // var webdriver = require('selenium-webdriver'),
  // By = webdriver.By,
  // until = webdriver.until;
  // var driver = new webdriver.Builder()
  //   .forBrowser('chrome')
  //   .build();
  // var capabilities = webdriver.Capabilities.phantomjs();
  // // capabilities.set('phantomjs.ghostdriver.path',
  // //     '/Users/xyz/ghostdriver-master/src/main.js');
  // capabilities.set('executable_path','/Users/geds/Documents/shzhyun/mashi/danmu/eleexampple/electron-manage/src/python/core/driver/phantomsjs/mac/bin/phantomjs');
  // var driver = new webdriver.Builder().
  //     withCapabilities(capabilities).
  //     build();

    driver.get('https://www.huya.com/l');
    driver.sleep(3000).then(function(){
      driver.getPageSource().then(function(result){
        console.log(result);
        var $=cheerio.load(result);
        //写法和jQuery一模一样
        $('.game-live-item').each(function(index, element) {
          console.log("index:"+index);
          var href = $(element).children("a")[1].attribs.href;
          var roomid = href.split("/")[3];
          var title = $(element).children("a")[1].attribs.title;
          var renq = $(element).children("span").children("span")[2].children[1].children[0].data;
          // 保存到内存对象
          var rfs = "{"+
          "\"roomid\":" + "\"" + roomid+"\""+","+
          "\"href\":" + "\"" + href+"\""+","+
          "\"title\":" + "\"" + title+"\""+","+
          "\"renq\":" + "\"" + renq+"\""+","+
          "\"createtime\":" + "\"" + new Date()+"\""
          +"}";
          // 保存到redis
          db.rpush("roominfos",rfs,null,function(erro,value){
          });
        });
        // console.log($);
      });    
    });

},
splider.getAllRooms2 = function() {
  // var webdriver = require('selenium-webdriver'),
  // By = webdriver.By,
  // until = webdriver.until;
  // var driver = new webdriver.Builder()
  //   .forBrowser('chrome')
  //   .build();

    driver.get('https://www.huya.com/l');
    var _this = this;            
    // 循环房间
    driver.sleep(3000).then(function(){
      // var jslivelist = driver.findElement(By.xpath('//*[@id="js-live-list"]'));
      driver.findElements(By.xpath('//li')).then(function(result){
        driver.sleep(3000).then(function(){
          console.log("result:"+result.length);
          // 循环房间号          
          db.del("roomids",function(erro,value){

          });
          db.del("roominfos",function(erro,value){

          });
          // for(var c = 0 ; c < result.length ; c++){
          function iterator(c){
            console.log("c:"+c);
            if(c == result.length){
              alert("完成"+result.length+"个房间信息的收录！");
              return;
            }
            var re = result[c];
            // 取房间号
            re.getAttribute("gid").then(function(roomid){
              debugger;
              _this.data.roomid = roomid;
              if(roomid != null){
                db.rpush("roomids",roomid,null,function(err,value){
  
                });
                console.log("roomid:"+roomid);
              }
            });
            re.findElements(By.tagName("a")).then(function(res){
              debugger;
              console.log(res);
              res[0].getAttribute("href").then(function(href){
                //取链接
                _this.data.href = href;
                console.log("href:"+href);
              });
              res[1].getText().then(function(title){
                //取直播内容
                _this.data.title = title;
                console.log("title:"+title);
              });
            });
            re.findElements(By.tagName("i")).then(function(res){
              debugger;
              console.log(res);
              res[3].getText().then(function(renq){
                // 粉丝数
                _this.data.renq = renq;
                console.log("renq:"+renq);
                // debugger;
              });
            });
            // debugger;
            if(_this.data.roomid != ""){
              // 保存到内存对象
              var rfs = "{"+
                "\"roomid\":" + "\"" + _this.data.roomid+"\""+","+
                "\"href\":" + "\"" + _this.data.href+"\""+","+
                "\"title\":" + "\"" + _this.data.title+"\""+","+
                "\"renq\":" + "\"" + _this.data.renq+"\""+","+
                "\"createtime\":" + "\"" + new Date()+"\""
              +"}";
              // debugger;
              // 保存到redis
              db.rpush("roominfos",rfs,null,function(erro,value){
              });
            }
            console.log("end:"+c); 
            iterator(c+1);      
          }
          iterator(0);
        });
      });
    });
    
};
/**
 * 斗鱼
 */
splider.dy = function(key, callback){

}
 
module.exports = splider;