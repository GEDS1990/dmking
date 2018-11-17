<template>
    <div class="login_page fillcontain">
	  	<transition name="form-fade" mode="in-out">
	  		<section class="form_contianer" v-show="showLogin">
		  		<div class="manage_tip">
		  			<p>神灯营销系统登录</p>
		  		</div>
		    	<el-form :model="loginForm" :rules="rules" ref="loginForm">
					<el-form-item prop="username">
						<el-input v-model="loginForm.username" placeholder="用户名"></el-input>
					</el-form-item>
					<el-form-item prop="password">
						<el-input type="password" v-model="loginForm.password" placeholder="密码"></el-input>
					</el-form-item>
					<el-form-item>
				    	<el-button type="primary" @click="submitForm('loginForm')" class="submit_btn">登陆</el-button>
				  	</el-form-item>
				</el-form>
	  		</section>
	  	</transition>
  	</div>
</template>

<script>
	// import { base_url } from '@/api/api'
	import { mapActions,mapState } from 'vuex'
	var db = require("../../db");
    export default {
        name: 'Login',
        data(){
            return{
				loginForm: {
					username: 'admin',
					password: 'admin',
				},
                rules: {
					username: [
			            { required: true, message: '请输入用户名', trigger: 'blur' },
			        ],
					password: [
						{ required: true, message: '请输入密码', trigger: 'blur' }
					],
				},
				showLogin: false,
				passwd: "",
            }
        },
        mounted(){
			this.showLogin = true;						
			var _this = this;
			db.get("loginValid",function(err,value){
				_this.passwd = value;   
			});
        },
		computed: {
			...mapState(['isLogin']),
			returnIsLogin: function(){
				return this.isLogin;
			},
			returnloginValid: function(){				
				var _this = this;
				db.get("loginValid",function(err,value){
					_this.passwd = value;   
				});
			},
		},
		methods: {
			//你可以在组件中使用 this.$store.commit('xxx') 提交 mutation，
			//或者使用 mapMutations 辅助函数将组件中的 methods 映射为 store.commit 调用（需要在根节点注入 store）。
			...mapActions(['loginAction']),
			submitForm(formName){
				this.$refs[formName].validate((valid) => {
					if(valid){
						var _this = this;
						db.get("loginValid",function(err,value){
							_this.passwd = value;   
							if(_this.loginForm.username == 'admin' && _this.loginForm.password == _this.passwd){
							// if(_this.loginForm.username == 'admin' && _this.loginForm.password == 'admin'){
								console.log('验证通过');
								_this.loginAction();
								_this.$router.push('/');
							}else if(_this.passwd == "") {
								console.log('链接redis中...');
								_this.$message({
									type: 'info',
									message: '稍等，链接服务中'
								});
							}else{
								console.log('账号密码出错');
								_this.$message({
									type: 'error',
									message: '账号密码出错'
								});
							}
						});
						
						// console.log('请求地址: ' + base_url);
					}else{
						console.log('验证失败');
						return false;
					}
				})
			}
		}
    }
</script>

<style lang="less" scoped>
    @import '../../style/mixin';
	.login_page{
		background-color: #324057;
	}
	.manage_tip{
		position: absolute;
		width: 100%;
		top: -100px;
		left: 0;
		p{
			font-size: 34px;
			color: #fff;
		}
	}
	.form_contianer{
		.wh(320px, 210px);
		.ctp(320px, 210px);
		padding: 25px;
		border-radius: 5px;
		text-align: center;
		background-color: #fff;
		.submit_btn{
			width: 100%;
			font-size: 16px;
		}
	}
	.tip{
		font-size: 12px;
		color: red;
	}
	.form-fade-enter-active, .form-fade-leave-active {
	  	transition: all 1s;
	}
	.form-fade-enter, .form-fade-leave-active {
	  	transform: translate3d(0, -50px, 0);
	  	opacity: 0;
	}
</style>