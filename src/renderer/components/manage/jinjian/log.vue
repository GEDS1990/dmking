<template>
    <div class="merchant">
        <head-top></head-top>
        <el-row>
            <el-col>
                <div>&nbsp;</div>
                <span class="czClass">操作记录:</span>
                <div>&nbsp;</div>             
                <el-button type="primary" @click="onSearchLogs" style="margin-left:100px;" >刷新</el-button>
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
                        width="80"
                        align="center">
                    </el-table-column>
                    <el-table-column
                        prop="contx"
                        label="发送内容"
                        width="380"
                        align="center">
                    </el-table-column>
                    <el-table-column
                        prop="href"
                        label="房间链接"
                        width="380"
                        align="center">
                    </el-table-column>
                    <el-table-column
                        prop="createTime"
                        label="发送时间"
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
                merchantTable: [{
                    num: '1234567',
                    contx: '小姐姐真漂亮',
                    href: '已登陆',
                    createTime: '2017-12-04-12:00'
                },{
                    num: '1234567',
                    contx: '小姐姐真漂亮',
                    href: '已登陆',
                    createTime: '2017-12-04-12:00'
                }]
            }
        },
        components: {
            headTop
        },
        mounted: function(){
            this.onSearchLogs();
        },
        methods: {
            onSearchLogs(){        
                var _this = this;
                db.LRANGE("logs", 0, 15, function(err,value){
                    var st ='[';
                    // var jsonarray ;
                    for(var i=0;i<value.length;i++){
                        value[i] = value[i].replace(new RegExp('\'',"gm"),'"');
                        value[i] = value[i].replace(new RegExp('u"',"gm"),'"');
                        var jsonstr =JSON.parse(value[i]);
                        st =st + '{"num":';
                        st =st + '"' + jsonstr.num + '"';
                        st =st + ', "contx":';
                        st =st + '"' + jsonstr.contx + '"';
                        st =st + ', "href":';
                        st =st + '"' + jsonstr.href + '"';
                        st =st + ', "createTime":';
                        st =st + '"' + jsonstr.createTime + '"';
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
                db.LRANGE("logs", startPage*15+1, endPage*15, function(err,value){
                    var st ='[';
                    // var jsonarray ;
                    for(var i=0;i<value.length;i++){
                        value[i] = value[i].replace(new RegExp('\'',"gm"),'"');
                        value[i] = value[i].replace(new RegExp('u"',"gm"),'"');
                        var jsonstr =JSON.parse(value[i]);
                        st =st + '{"num":';
                        st =st + '"' + jsonstr.num + '"';
                        st =st + ', "contx":';
                        st =st + '"' + jsonstr.contx + '"';
                        st =st + ', "href":';
                        st =st + '"' + jsonstr.href + '"';
                        st =st + ', "createTime":';
                        st =st + '"' + jsonstr.createTime + '"';
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
    .czClass {
        text-align: center;
        padding-left: 80px;
    }
</style>