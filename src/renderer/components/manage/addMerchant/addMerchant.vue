<template>
    <div class="add-merchant">
        <head-top></head-top>
        <el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>联系人信息</span>
                </div>
                <div class="text item">
                    <el-form-item label="用户名" prop="username">
                        <el-input v-model="addForm.username" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="passwd">
                        <el-input v-model="addForm.passwd" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="平台" prop="ptai">
                        <el-input v-model="addForm.ptai" auto-complete="off"></el-input>
                    </el-form-item>
                </div>
            </el-card>
        </el-form>
    </div>
</template>

<script>
    import headTop from '../../common/headTop';
    var db = require('../../../db');
    export default {
        data(){
            return {
                addForm: {
                    addName: '',
                    addPhone: '',
                    addEmail: '',
                    shortMerchantName: '',
                    merchantType: '',
                    manageType: {
                        business: '',
                        business2: '',
                        business3: '',
                    },
                    servicePhone: ''
                }
            }
        },
        components: {
            headTop
        },
        methods: {
            addMerchant(){
                console.log('创建用户');
                console.log(this.addForm.manageType);
                console.log(this.addForm.merchantType);
                db.set("demo","demo")
            }
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
    }
</style>