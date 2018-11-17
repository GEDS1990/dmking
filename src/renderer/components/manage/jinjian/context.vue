<template>
    <div class="merchant">
        <head-top></head-top>
        <el-row>
            <el-col :span="24">
                <el-form :inline="true" class="form-merchant-search">
                    <el-form-item label="发送内容">
                        <el-input v-model="formInline.contact" placeholder="登录名" class="contacts"></el-input>
                    </el-form-item>    
                    <div class="block" style="display: inline-block;">
                        <span class="demonstration">创建时间：</span>
                        <el-date-picker
                            v-model="timeValue"
                            type="daterange"
                            range-separator="至"
                            start-placeholder="开始日期"
                            end-placeholder="结束日期"
                            value-format="yyyy-MM-dd">
                        </el-date-picker>
                    </div>                
                    <el-form-item>
                        <!-- <el-button type="primary" @click="addApprove">批量导入</el-button> -->
                        <el-button type="primary" @click="addApprove">清空内容</el-button>
                    </el-form-item>             
                    <el-form-item>
                        <el-button type="primary" @click="onSearch">查询</el-button>
                    </el-form-item>             
                    <el-form-item>
                        <router-link to="addContext">
                            <el-button type="primary" @click="addApprove">新增内容</el-button>
                        </router-link>
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
                        prop="num"
                        label="编号"
                        width="180">
                    </el-table-column>
                    <el-table-column
                        prop="conts"
                        label="发送内容"
                        width="380"
                        align="center">
                    </el-table-column>
                    <el-table-column
                        prop="createtime"
                        label="创建时间"
                        width="180">
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
    var db = require('../../../db');
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
        created: function() {
            this.onSearch();
        },
        methods: {
            onSearch(){
                var _this = this;
                db.LRANGE("contexts", 0, 15, function(err,value){
                    var st ='[';
                    // var jsonarray ;
                    for(var i=0;i<value.length;i++){
                        var jsonstr =JSON.parse(value[i]);
                        st =st + '{"num":';
                        st =st + '"' + jsonstr.num + '"';
                        st =st + ', "conts":';
                        st =st + '"' + jsonstr.conts + '"';
                        st =st + ', "createtime":';
                        st =st + '"' + jsonstr.createtime + '"';
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
                db.LRANGE("contexts", startPage*15+1, endPage*15, function(err,value){
                    var st ='[';
                    // var jsonarray ;
                    for(var i=0;i<value.length;i++){
                        var jsonstr =JSON.parse(value[i]);
                        st =st + '{"num":';
                        st =st + '"' + jsonstr.num + '"';
                        st =st + ', "conts":';
                        st =st + '"' + jsonstr.conts + '"';
                        st =st + ', "createtime":';
                        st =st + '"' + jsonstr.createtime + '"';
                        st =st + '},';
                    } 
                    var st =st + ']';
                    var jsonstr =eval(st);
                    _this.merchantTable = jsonstr;   
                });
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
    .pldrClass {
        padding-left: 100px;
        padding-right:100px;
    }
</style>