<template>
    <div class="merchant">
        <head-top></head-top>
        <el-row>
            <el-col :span="24">
                <el-form :inline="true" class="form-merchant-search">
                    <el-form-item label="房间内发送多少条消息">                        
                        <input type="number" class="numberClass" v-model="beanSet.sendNum" @change="beanSetSave"/>
                        <span>条</span>
                    </el-form-item>
                    <!-- <el-form-item label="发送延时多少秒">                        
                        <input type="number" class="numberClass" value="1"/>   
                        至                    
                        <input type="number" class="numberClass" value="5"/>
                        <span>秒</span>
                    </el-form-item> -->
                    <el-form-item label="启动线程数：">                        
                        <input type="number" class="numberClass" v-model="beanSet.threadCounts" @change="beanSetSave"/>
                        <span>条</span>
                    </el-form-item>
                    <el-form-item label="自动发送消息数：">                        
                        <input type="number" class="numberClass" style="color:red" v-model="sendCounts" disabled="true"/>
                        <span>个</span>
                    </el-form-item>
                    <el-form-item>
                        <!-- <el-button :disabled='startClicked' type="primary" @click="sendDanmu_Python">开始</el-button> -->
                        <el-button :disabled='startClicked' type="primary" @click="sendDanmu">开始</el-button>
                    </el-form-item>  
                    <el-form-item>
                        <el-button :disabled='pauseClicked' type="primary" @click="sendPause">暂停</el-button>
                    </el-form-item>                   
                    <el-form-item>
                        <el-button :disabled='continueClicked' type="primary" @click="onSearch">继续</el-button>
                    </el-form-item>                   
                    <el-form-item>
                        <el-button :disabled='stopClicked' type="primary" @click="onSearch">停止</el-button>
                    </el-form-item>                 
                    <el-form-item>
                        <el-button type="primary" @click="onSearchRoomInfos(0)">刷新</el-button>
                    </el-form-item>
                </el-form>
            </el-col>
            <!-- 列表 -->
            <el-card class="box-card show-merchant">
                <el-table
                    :data="merchantTable"
                    stripe
                    style="width: 100%">
                    <el-table-column
                        prop="roomid"
                        label="房间ID"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        prop="renq"
                        label="人气"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        prop="title"
                        label="标题"
                        width="230">
                    </el-table-column>
                    <el-table-column
                        prop="href"
                        label="链接"
                        width="260">
                    </el-table-column>
                </el-table>
                <el-pagination
                    background
                    @current-change="changePage"
                    layout="prev, pager, next"
                    :page-size="10"
                    :total="total">
                </el-pagination>
            </el-card>
        </el-row>
    </div>
</template>

<script>
    import headTop from '../../common/headTop';
    var db = require('../../../db');
    var splider = require('../../../store/splider');
    var spliderHy = require('../../../store/splider/hy');
    import NProgress from 'nprogress';
    import 'nprogress/nprogress.css';
    import { defaultCoreCipherList } from 'constants';
    var puppeteer = require('puppeteer');
    var async = require('async');

    export default {
        data(){
            return {
                sendCounts: 0,
                total: 100,
                timeValue: '',
                startClicked: false,
                pauseClicked: false,
                continueClicked: false,
                stopClicked: false,
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
                merchantTable: [],
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
        },
        components: {
            headTop
        },
        mounted: function () {
                this.onSearchRoomInfos(1);
        },
        created: function () {
            this.upBeanSet();
        },
        methods: {
            beanSetSave(){
                var _this = this;
                var params = JSON.stringify(_this.beanSet);
                db.set("beanSet",params,null,function(err,value){
                    if(value == "OK"){
                        alert("保存设置成功！");
                    }else {
                        alert("保存设置失败！");
                    }
                });                
            },
            upBeanSet(){
                var _this = this;
                db.get("beanSet",function(err,value){
                    _this.beanSet = JSON.parse(value);      
                    console.log("更新设置成功");
                });
            },
            onSearchRoomInfos(flag){
                if(flag == 0){
                    // 爬取更新
                    splider.getAllRooms();
                }

                var _this = this;
                db.LRANGE("roominfos", 0, 15, function(err,value){
                    var st ='[';
                    for(var i=0;i<value.length;i++){
                        var jsonstr =JSON.parse(value[i]);
                        st =st + '{"renq":';
                        st =st + '"' + jsonstr.renq + '"';
                        st =st + ', "href":';
                        st =st + '"' + jsonstr.href + '"';
                        st =st + ', "roomid":';
                        st =st + '"' + jsonstr.roomid + '"';
                        st =st + ', "title":';
                        st =st + '"' + jsonstr.title + '"';
                        st =st + '},';
                    } 
                    var st =st + ']';
                    var jsonstr =eval(st);
                    _this.merchantTable = jsonstr;   
                    // console.log("更新设置成功");
                });
            },
            onSearch(){
                console.log('查询');
                console.log('起始时间：' + this.timeValue[0]);
                console.log('终止时间：' + this.timeValue[1]);
            },
            sendPause() {
                this.startClicked = false;
                this.pauseClicked = true;
                console.log("python_stdout:"+db.get("python_stdout"));
                console.log("python_stderr:"+db.get("python_stderr"));
            },
            sendDanmu() {
                spliderHy.default.startHySend();
            },
            async sendDanmuBak() {
                // 调用nodejs方法
                var _this = this;
                await db.get('norSet',async function(err,value){
                    debugger;
                    var jsonstr = await JSON.parse(value);
                    _this.norSet.isShow = await jsonstr.isShow;
                });
                await db.LRANGE('contexts',0,-1,async function(err,value){
                    debugger;
                    for(var v =0; v < value.length ; v++){
                        var jsonstr = await JSON.parse(value[0]);
                        await _this.contexts.push(jsonstr); 
                    }
                });
                await db.LRANGE('userinfos',0,-1,async function(err,value){
                    debugger;
                    var st ='[';
                    // var jsonarray ;
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
                    _this.userinfos = jsonstr;
                    // debugger;
                });
                var headlessFlag = true;
                if(_this.norSet.isShow == 1){
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
                        debugger;
                        //用户名
                        await page.type('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-common > div:nth-child(1) > span > input',this.userinfos[this.iu].MOBILE);
                        //密码
                        await page.type('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-common > div:nth-child(2) > span > input',this.userinfos[this.iu].PASSWD);
                        await page.waitFor(3000); 
                        //登陆按钮
                        await page.click('body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-mt20.clearfix > a');
                        await page.waitFor(3000); 
                        debugger;
                        cookies = await page.cookies('https://www.huya.com/l');
                        console.log("cookies:"+cookies);
                        debugger;
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
                        var _this = this;
                        async function alitetor(count){
                            _this.sendCounts = count;
                            // debugger;
                            try{
                                for(var i =0 ; i < _this.contexts.length ; i++){
                                    console.log(_this.contexts[i].conts+"->发送中")
                                    db.lpush('logs',_this.contexts[i].conts,null,function(err,value){

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
                                    await page.type('#pub_msg_input',_this.contexts[i].conts);
                                    // await page.type('#pub_msg_input','66666');
                                    await page.waitFor(3000);
                                    console.log("4"+new Date());
                                    await page.click('#msg_send_bt');
                                    await page.waitFor(3000);
                                    console.log("5"+new Date());  
                                    if(i == _this.contexts.length){
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
            },
            sendDanmu_Python() {

                NProgress.start(); 
                // next();
                // 设置查询
                var _this = this;
                db.get("beanSet",function(err,value){
                    _this.beanSet = JSON.parse(value);  
                });
                // 调用python方法
                this.startClicked = true;
                this.pauseClicked = false;
                var exec = require('child_process').exec;
                // 连续循环发送直播房间数
                var roomNums = this.beanSet.roomNums;
                // 每个房间连续发送的次数
                var sendNum = this.beanSet.sendNum;
                // 每个房间发送消息的间隔
                var sendSpaces = this.beanSet.sendSpaces;
                // 发送内容
                var context = this.beanSet.context;
                // 固定控件点击间隔（3秒）
                var timeNor = this.beanSet.timeNor;
                // 发送线程数
                var threadNor = this.beanSet.threadNor;
                alert('p '+__dirname+'/../../../../python/core/hyUtil.py ');
                exec('python '+__dirname+'/../../../../python/core/hyUtil.py '+ roomNums+' '+sendNum+' '+sendSpaces+' '+context+' '+timeNor+' '+threadNor+' ',function(error,stdout,stderr){
                    if(stdout.length >1){
                        alert('you offer args:',stdout);
                        db.set('python_stdout',stdout,);
                    } else {
                        alert('you don\'t offer args');
                        db.set('pythonlog','you don\'t offer args');
                    }
                    if(error) {
                        alert('stderr : '+stderr);
                        db.set('python_stderr',stderr);
                    }
                    if(stdout == 'success'){
                        alert('完成发送！')
                    }
                });
                // this.btnClicked = 'false';
                NProgress.end();
            },
            addApprove(){
                console.log('新增');
            },
            changePage(val){
                console.log('当前页改变了' + val);
                var startPage = val - 1;
                var endPage = val;
                var _this = this;
                db.LRANGE("roominfos", startPage*15+1, endPage*15, function(err,value){
                    var st ='[';
                    for(var i=0;i<value.length;i++){
                        var jsonstr =JSON.parse(value[i]);
                        st =st + '{"renq":';
                        st =st + '"' + jsonstr.renq + '"';
                        st =st + ', "href":';
                        st =st + '"' + jsonstr.href + '"';
                        st =st + ', "roomid":';
                        st =st + '"' + jsonstr.roomid + '"';
                        st =st + ', "title":';
                        st =st + '"' + jsonstr.title + '"';
                        st =st + '},';
                    } 
                    var st =st + ']';
                    var jsonstr =eval(st);
                    _this.merchantTable = jsonstr;
                });
            },
            // async getAllRooms() {
            //     var webdriver = require('selenium-webdriver'),
            //     By = webdriver.By,
            //     until = webdriver.until;
            //     var driver = new webdriver.Builder()
            //         .forBrowser('chrome')
            //         .build();

            //     driver.get('https://www.huya.com/l');
            //     var _this = this;            
            //     // 循环房间
            //     driver.sleep(3000).then(function(){
            //     // var jslivelist = driver.findElement(By.xpath('//*[@id="js-live-list"]'));
            //     driver.findElements(By.xpath('//li')).then(function(result){
            //         driver.sleep(3000).then(function(){
            //         console.log("result:"+result.length);
            //         // 循环房间号
            //         for(var c = 0 ; c < result.length ; c++){
            //             // debugger;
            //             // 取房间号
            //             result[c].getAttribute("gid").then(function(roomid){
            //             _this.data.roomid = roomid;
            //             db.rpush("roomids",roomid);
            //             console.log("roomid:"+roomid);
            //             });
            //             // await setTimeout(function () {
            //                 console.log("0:"+new Date());
            //                 result[c].findElements(By.tagName("a")).then(function(res){
            //                     console.log(res);
            //                     // await setTimeout(function () {
            //                         console.log("1:"+new Date());
            //                         res[0].getAttribute("href").then(function(href){
            //                             //取链接
            //                             _this.data.href = href;
            //                             console.log("href:"+href);
            //                         });
            //                     // }, 1000);
            //                     // await setTimeout(function () {
            //                         console.log("2:"+new Date());
            //                         res[1].getText().then(function(title){
            //                             //取直播内容
            //                             _this.data.title = title;
            //                             console.log("title:"+title);
            //                         });
            //                     // }, 1000);                            
            //                 });
            //             // }, 1000);
            //             // await setTimeout(function () {
            //             //     console.log("3:"+new Date());
            //             //     result[c].findElements(By.tagName("i")).then(function(res){
            //             //     console.log(res);
            //             //     res[3].getText().then(function(renq){
            //             //         // 粉丝数
            //             //         _this.data.renq = renq;
            //             //         console.log("renq:"+renq);
            //             //     });
            //             //     });  
            //             // }, 1000);
            //             // await setTimeout(function () {
            //             //     console.log("4:"+new Date());
            //             //     // 保存到内存对象
            //             //     var rfs = {
            //             //         roomid: _this.data.roomid,
            //             //         href: _this.data.href,
            //             //         title: _this.data.title,
            //             //         renq: _this.data.renq,
            //             //         createtime: new Date()
            //             //     };
            //             //     // debugger;
            //             //     _this.data.roominfos.push(rfs);
            //             // }, 1000);
                        
            //         }
            //         // await setTimeout(function () {
            //         //     console.log("5:"+new Date());
            //         //     // 保存到redis
            //         //     db.rpush(this.data.roominfos);
            //         // }, 1000);
            //         });
            //     });
            //     });
                
            // }
        }
    }
</script>

<style lang="less">
    .merchant{
        .el-row{
            .form-merchant-search{
                margin-top: 10px;
                margin-left: 10px;
                padding-left: 50px;
                padding-right: 140px;
                .el-form-item__content,.contacts{
                    width: 150px;
                }
                .searchBtn{
                    .el-form-item__content{
                        width: 155px;
                    }
                    position:relative;
                    left:50%;
                }
            }
            .show-merchant{
                width: 85%;
                margin: 10px auto;
                .el-pagination{
                    width: 405px;
                    margin: 15px auto 0;
                }
            }
        }
        .numberClass{
            border: 2em;
            /* border-color: blue; */
            background: #f1eff0;
            min-height: 2em;
            max-width: 4em;
            text-align: center;
            font-size: 13px;
            border-radius: 6px;
            // font-family: Georgia, "Times New Roman", Times, serif;
        }
    }
</style>