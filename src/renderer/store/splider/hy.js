
var db = require('../../db');
var sd = require('silly-datetime');
var puppeteer = require('puppeteer');
var async = require('async');
const stateData = {
    sendCounts: 0,
    beanSet: {
        roomNums: 100,
        sendNum: 5,
        sendSpaces: 5,
        context: '66666',
        timeNor: 3,
        threadNor: 2,
        loginDel: 3,
        changIp: 10,
        saveUserPwd: 'true',
        threadCounts: 2
    }, 
    norSet: {
        driverPath: '',
        enginePath: '',
        isShow: '',
    },
    contexts: [],
    userinfos: [],
    cookies: [],
    iu: 4,
}
const getSet = async function() {
    console.log("---getSet---"+sd.format(new Date(), 'YYYY-MM-DD HH:mm'));
    await db.get('norSet',async function(err,value){
        console.log('norSet');
        var jsonstr = await JSON.parse(value);
        stateData.norSet.isShow = await jsonstr.isShow;
    });
    await db.LRANGE('contexts',0,-1,async function(err,value){
        console.log('contexts');
        for(var v =0; v < value.length ; v++){
            var jsonstr = await JSON.parse(value[0]);
            await stateData.contexts.push(jsonstr); 
        }
    });
    await db.LRANGE('userinfos',0,-1,async function(err,value){
        console.log('userinfos');
        var st ='[';
        for(var i=0;i<value.length;i++){
            value[i] = await value[i].replace(new RegExp('\'',"gm"),'"');
            value[i] = await value[i].replace(new RegExp('u"',"gm"),'"');
            var jsonstr = await JSON.parse(value[i]);
            st =st + '{"MOBILE":';
            st =st + '"' + jsonstr.MOBILE + '"';
            st =st + ', "PASSWD":';
            st =st + '"' + jsonstr.PASSWD + '"';
            st =st + ', "number":';
            st =st + '"00' + (i+1) + '"';
            st =st + ', "ptai":';
            st =st + '"虎牙"';
            st =st + ', "status":';
            st =st + '"未登录"';
            st =st + ', "logintime":';
            st =st + '"' + Date.now() + '"';
            st =st + '},';
        } 
        var st =st + ']';
        var jsonstr =await eval(st);
        stateData.userinfos = jsonstr;
    });
    console.log("---getSet End---"+sd.format(new Date(), 'YYYY-MM-DD HH:mm'));
}
const login = async function() {
    console.log('login');
}
const startHySend = async function() {
    getSet();
    setTimeout(send(),5000);
    console.log('startHySend end');
}
const getRooms = async function() {
    console.log('getRooms');
}
const send = async function() {
    console.log("---send---"+sd.format(new Date(), 'YYYY-MM-DD HH:mm'));
    var headlessFlag = true;
    if(stateData.norSet.isShow == 1){
        headlessFlag = false
    }
    (async () => {
        const browser = await puppeteer.launch({
            headless: false,
            // headless: headlessFlag,
            executablePath: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome',
        });
        // userinfos start
        // for(var iu = 0; iu<this.userinfos.length; iu++){ for start
            var page = await browser.newPage();
            await page.goto('https://www.huya.com/l');
            await page.setViewport({
                width:1024,
                height:768
            });
            //获取room总数
            const roomCounts = await page.$$eval('li', lis => lis.length);
            // debugger;       
            await page.waitFor(5000);                 
            //登录
            await page.click('.subscribe-text');
            // 切换   
            await page.waitFor(3000); 
            await page.click('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.qrCode.login > div.UDBSdkLgn-switch.UDBSdkLgn-webQuick > img');     
            // debugger;
            //用户名
            await page.type('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-common > div:nth-child(1) > span > input',stateData.userinfos[stateData.iu].MOBILE);
            //密码
            await page.type('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-common > div:nth-child(2) > span > input',stateData.userinfos[stateData.iu].PASSWD);
            await page.waitFor(3000); 
            //登陆按钮
            await page.click('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-mt20.clearfix > a');
            await page.waitFor(3000); 
            // debugger;
            cookies = await page.cookies('https://www.huya.com/l');
            console.log("cookies:"+cookies);
            // debugger;
            page.on('response', res => {
                if(res.hasOwnProperty('headers')){
                    for(let key in res.headers){
                        if(key === 'set-cookie'){
                            debugger;

                        // 在这里进行获取Cookie信息操作
                        }else{
                            continue;
                        }
                    }
                }
            });

            
            //进入room
            // var stateData = this;
            async function alitetor(count){
                stateData.sendCounts = count;
                // debugger;
                try{
                    for(var i =0 ; i < stateData.contexts.length ; i++){
                        console.log(stateData.contexts[i].conts+"->发送中")
                        db.lpush('logs',stateData.contexts[i].conts,null,function(err,value){

                        });
                        console.log("1"+new Date());
                        // debugger;
                        await page.click("#js-live-list > li:nth-child(1) > a.video-info.new-clickstat");
                        await page.waitFor(9000); 
                        const pageList = await browser.pages(); 
                        console.log("NUMBER TABS:", pageList.length);
                        console.log("2"+new Date());  
                        // 切换tab
                        page = pageList[2];
                        await page.bringToFront(); 
                        console.log("3"+new Date());
                        await page.type('#pub_msg_input',stateData.contexts[i].conts);
                        // await page.type('#pub_msg_input','66666');
                        await page.waitFor(3000);
                        console.log("4"+new Date());
                        await page.click('#msg_send_bt');
                        await page.waitFor(3000);
                        console.log("5"+new Date());  
                        if(i == stateData.contexts.length){
                            await page.close();
                            // 切换tab
                            page = pageList[1];
                            await page.bringToFront();  
                        } 
                    await page.waitFor(30000); 
                    }
                    count++ ;
                    alitetor(count);
                }catch(e){
                    console.log(e);
                    // browser.close();
                    // alert("自动发送接收，共发送"+count+"个房间！")
                    // return ;
                }
                if(count == roomCounts){
                    console.log("完成"+roomCounts+"个房间的发送");
                }
            };
            alitetor(1);
        // }    for end
        // userinfos end

        // debugger;
        // await page.waitFor(5000);
        // await browser.close();
    })();
    console.log('Hello World');
}
export default {
    getSet,
    login,
    send,
    getRooms,
    startHySend
  }