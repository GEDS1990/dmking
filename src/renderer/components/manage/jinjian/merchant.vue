<template>
    <div class="merchant">
        <head-top></head-top>
        <el-row>
            <el-col :span="24">
                <el-form :inline="true" class="form-merchant-search">
                    <el-form-item label="直播平台">
                        <el-select v-model="formInline.region" placeholder="直播平台">
                        <el-option label="全部" value="all"></el-option>
                        <el-option label="虎牙直播" value="done"></el-option>
                        <el-option label="斗鱼直播" value="wait"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="手机号">
                        <el-input v-model="formInline.contact" placeholder="手机号" class="contacts"></el-input>
                    </el-form-item>      
                    <!-- <div class="block" style="display: inline-block;">
                        <span class="demonstration">创建时间：</span>
                        <el-date-picker
                            v-model="timeValue"
                            type="daterange"
                            range-separator="至"
                            start-placeholder="开始日期"
                            end-placeholder="结束日期"
                            value-format="yyyy-MM-dd">
                        </el-date-picker>
                    </div> -->
                    <!-- <el-form-item>
                        <el-button type="primary" @click="addApprove">批量导入</el-button>
                    </el-form-item> -->
                    <el-form-item>
                        <el-button type="primary" @click="autoPro">批量生成</el-button>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSearch">查询</el-button>
                    </el-form-item>
                    <el-form-item>
                        <router-link to="addMerchant">
                            <el-button type="primary" @click="addApprove">新增</el-button>
                        </router-link>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="exportexcel">导出</el-button>                        
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="importexcel">导入</el-button>
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
                        prop="number"
                        label="编号"
                        width="80">
                    </el-table-column>
                    <el-table-column
                        prop="MOBILE"
                        label="手机号"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        prop="PASSWD"
                        label="密码"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        prop="ptai"
                        label="平台"
                        width="100">
                    </el-table-column>
                    <el-table-column
                        prop="status"
                        label="登录状态">
                    </el-table-column>
                    <el-table-column
                        prop="logintime"
                        label="登录时间">
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
    import headTop from '../../common/headTop'
    import { debug } from 'util';
    var db = require('../../../db');
    var exec = require('child_process').exec;
    import NProgress from 'nprogress';
    import 'nprogress/nprogress.css';

    export default {
        data(){
            return {
                total: 100,
                timeValue: '',
                formInline: {
                    contact: '',
                    region: '',
                    merchant: ''
                },
                merchantTable: []
            }
        },
        components: {
            headTop
        },
        mounted: function () {
            this.onSearch();
        },
        created:function(){
        },
        methods: {
            exportexcel(){
                NProgress.start(); 
                // next();
                exec('python '+__dirname+'/../../../../python/core/exportExcel.py ',function(error,stdout,stderr){
                    if(stdout.length >1){
                        console.log('excel:',stdout);
                        NProgress.end(); 
                        alert("文件导出目录："+stdout)
                    } else {
                        NProgress.end(); 
                        console.log('系统繁忙，请稍后重试');
                    }
                });
            },
            importexcel(){

            },
            onSearch(){
                var _this = this;
                //0 为起始位置，-1为最后的位置
                db.LRANGE('userinfos', 0, 15, function(err,value){
                    var st ='[';
                    for(var i=0;i<value.length;i++){
                        value[i] = value[i].replace(new RegExp('\'',"gm"),'"');
                        value[i] = value[i].replace(new RegExp('u"',"gm"),'"');
                        var jsonstr =JSON.parse(value[i]);
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
                    var jsonstr =eval(st);
                    _this.merchantTable = jsonstr;
                });
            },
            addApprove(){
                console.log('新增');
            },
            changePage(val){
                console.log('当前页改变了' + val);
                var startPage = val - 1;
                var endPage = val;
                var _this = this;
                db.LRANGE('userinfos', startPage*15+1, endPage*15, function(err,value){
                    var st ='[';
                    // var jsonarray ;
                    for(var i=0;i<value.length;i++){
                        value[i] = value[i].replace(new RegExp('\'',"gm"),'"');
                        value[i] = value[i].replace(new RegExp('u"',"gm"),'"');
                        var jsonstr =JSON.parse(value[i]);
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
                    var jsonstr =eval(st);
                    _this.merchantTable = jsonstr;
                });
            },
            autoPro(){
                NProgress.start(); 
                // next();
                var exec = require('child_process').exec;
                console.log('批量生成账号');
                exec('python /Users/geds/Documents/shzhyun/mashi/danmu/eleexampple/electron-manage/python/core/hyFpwd.py hy 3',function(error,stdout,stderr){
                    if(stdout == 'success'){
                        alert("完成！");
                    } 
                    if(error) {
                        console.info('stderr : '+stderr);
                    }
                });
                NProgress.end();
            },
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
                    .el-form-item__content{
                        width: 155px;
                    }
                    float: left;
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