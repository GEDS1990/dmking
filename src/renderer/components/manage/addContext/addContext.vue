<template>
    <div class="add-merchant">
        <head-top></head-top>
        <el-form :model="addForm" label-width="80px" ref="addForm">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>添加内容</span>
                </div>
                <div class="text item">
                    <el-form-item label="内容" prop="conts">
                        <el-input v-model="addForm.conts" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="addMerchant">保存</el-button>
                    </el-form-item>   
                </div>
            </el-card>
        </el-form>
    </div>
</template>

<script>
    import headTop from '../../common/headTop'
    var db = require('../../../db');
    export default {
        data(){
            return {
                addForm: {
                    num: Math.random(),
                    conts: '',
                    createtime: new Date()
                }
            }
        },
        components: {
            headTop
        },
        methods: {
            addMerchant(){
                var contexts = '{"num":"'+this.addForm.num+'", "conts":"'+this.addForm.conts+'", "createtime":"'+this.addForm.createtime+'"}'
                db.rpush("contexts",contexts,null,function(err ,value){
                    if(err==null){
                        alert("添加成功！")
                        console.log(value);
                    }
                });
            },
        }
    }
</script>

<style lang="less">
    .add-merchant{
        .el-form{
            width: 85%;
            margin: 15px auto;
            .box-card{
                margin-top: 15px;
            }
        }
        .searchBtn{
            float: right;
        }
    }
</style>