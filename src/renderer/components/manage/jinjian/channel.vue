<template>
    <div class="channel">
        <head-top></head-top>
        <el-card class="box-card card1">
            <div slot="header" class="clearfix">
                <span>登陆操作设置</span>
            </div>
            <div class="text item">
                登陆延时（秒）：<el-input-number :min="1" :max="10" v-model="beanSet.loginDel" @change="beanSetSave" class="txt"></el-input-number>
            </div>
            <div class="text item">
                登陆多少个账号换一次IP？<el-input-number :min="1" :max="10" v-model="beanSet.changIp" @change="beanSetSave" class="txt"></el-input-number>
            </div>
            <div class="text item">
                <input type="checkbox" v-model="beanSet.saveUserPwd" @change="beanSetSave"/>保存账号和密码
            </div>
        </el-card>
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>通用设置</span>
            </div>
            <div class="text item">
                连续循环发送直播房间数:<el-input-number :min="1" :max="10" class="txt" v-model="beanSet.roomNums" @change="beanSetSave"></el-input-number>
            </div>
            <div class="text item">
                每个房间连续发送的次数:<el-input-number :min="1" :max="10" class="txt" v-model="beanSet.sendNum" @change="beanSetSave"></el-input-number>
            </div>
            <div class="text item">
                每个房间发送消息的间隔:<el-input-number :min="1" :max="10" class="txt" v-model="beanSet.sendSpaces" @change="beanSetSave"></el-input-number>
            </div>
            <!-- <div class="text item">
                发送内容:<el-input class="txt" v-model="beanSet.context" @change="beanSetSave"></el-input>
            </div> -->
            <div class="text item">
                固定控件点击间隔（3秒）:<el-input-number :min="1" :max="10" class="txt" v-model="beanSet.timeNor" @change="beanSetSave"></el-input-number>
            </div>
            <div class="text item">
                发送线程数:<el-input-number :min="1" :max="10" class="txt" v-model="beanSet.threadNor" @change="beanSetSave"></el-input-number>
            </div>
        </el-card>
    </div>
</template>

<script>
    import headTop from '../../common/headTop'
    var db = require('../../../db');
    export default {
        data(){
            return {
                auditStatus: 1,
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
            }
        },
        created: function () {
            this.upBeanSet();
        },
        methods: {
            beanSetSave(){
                var _this = this;
                console.log("this.beanSet.roomNums:"+_this.beanSet.roomNums)
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
        },
        components: {
            headTop
        }
    }
</script>

<style lang="less">
    .channel{
        .box-card {
            margin: 20px auto;
            width: 80%;
            .text {
                font-size: 14px;
                .txt{
                    display: inline-block;
                    margin-left: 20px;
                }
            }

            .item {
                margin-bottom: 18px;
            }

            .clearfix:before,
            .clearfix:after {
                display: table;
                content: "";
            }
            .clearfix:after {
                clear: both
            }
        }
        .card1{
            .el-card__body{
                position: relative;
                .status{
                    position: absolute;
                    top: 50px;
                    right: 20px;
                }
            }
        }
        .card3{
            .text{
                .el-textarea{
                    width: 70%;
                    margin-left: 50px;
                    .el-textarea__inner{
                        height: 200px;
                    }
                }
                .txt{
                    .idCard{
                        width: 100px;
                    }
                    .license{
                        width: 150px;
                    }
                }
            }
        }
    }
</style>