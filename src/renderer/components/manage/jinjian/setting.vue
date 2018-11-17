<template>
    <div class="merchant">
        <head-top></head-top>
        <el-row>
            <el-col :span="24">
                <el-form :inline="true" class="form-merchant-search">
                    <!-- <el-form-item label="宽带名">
                        <el-input v-model="formInline.contact" placeholder="登录名" class="contacts"></el-input>
                    </el-form-item>    
                    <el-form-item label="账号">
                        <el-input v-model="formInline.contact" placeholder="登录名" class="contacts"></el-input>
                    </el-form-item> 
                    <el-form-item>
                        <label><input type="radio" v-model="bh" value="0" >&nbsp;拨号方式一</label>
                    </el-form-item>   
                    <el-form-item>
                        <label><input type="radio" v-model="bh" value="1">&nbsp;拨号方式二</label>
                    </el-form-item>-->
                    <el-form-item label="驱动存放目录">
                        <el-input v-model="norSet.driverPath" placeholder="驱动存放目录" class="driverPath"></el-input>
                    </el-form-item>
                    <el-form-item label="引擎存放目录">
                        <el-input v-model="norSet.enginePath" placeholder="引擎存放目录" class="enginePath"></el-input>
                    </el-form-item>  
                    <el-form-item>
                        <label><input type="radio" v-model="norSet.isShow" value="0" >&nbsp;不显示浏览器</label>
                    </el-form-item>   
                    <el-form-item>
                        <label><input type="radio" v-model="norSet.isShow" value="1">&nbsp;显示浏览器</label>
                    </el-form-item>    
                    <el-form-item>
                        <el-button type="primary" @click="onSave">保存</el-button>
                    </el-form-item>
                </el-form>
            </el-col>
            <transition name="fade">
                <div class="input-wrapper">
                    <span>浏览器追踪日志：</span>
                    <el-input class="gray-bg-input"
                            v-model="tracelog"
                            type="textarea"
                            disabled="false"
                            :rows="15">
                    </el-input>
                </div>
            </transition>
        </el-row>
    </div>
</template>

<script>
    import headTop from '../../common/headTop';
    var db = require('../../../db');
    export default {
        data(){
            return {
                total: 100,
                tracelog: '2018-10-28: 斗鱼直播抓取成功: https://www.douyu.com',
                norSet: {
                    driverPath: '/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver',
                    enginePath: '/Users/geds/Documents/shzhyun/mashi/danmu/pyspl',
                    isShow: '0',
                },
            }
        },
        components: {
            headTop
        },
        methods: {
            onSave(){
                var norSet = '{"driverPath":"'+this.norSet.driverPath+'", "enginePath":"'+this.norSet.enginePath+'", "isShow":"'+this.norSet.isShow+'"}'
                db.set("norSet",norSet,null,function(err ,value){
                    if(err==null){
                        alert("添加成功！")
                        console.log(value);
                    }
                });
            },
            getTraceLog(){
                var _this = this;
                db.get("python_stdout",function(err ,value){
                    if(err==null){
                        _this.tracelog = value;
                        console.log(value);
                    }
                });
            },
            changePage(val){
                console.log('当前页改变了' + val);
            }
        }
    }
</script>

<style lang="less">
    .merchant{
        .el-row{
            .form-merchant-search{
                margin-top: 10px;
                margin-left: 10px;
                .el-form-item__content,.contacts{
                    width: 150px;
                }
                .searchBtn{
                    padding-left: 500px;
                    .el-form-item__content{
                        width: 155px;
                    }
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
    }
</style>