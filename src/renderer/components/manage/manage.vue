<template>
    <div class="manage_page fillcontain">
        <el-row style="height: 100%;">
            <el-col :span="3" style="min-height: 100%; background-color: #324057;">
                <el-menu :default-active="defaultActive" class="el-menu-dark" text-color="#bfcbd9" style="min-height: 100%;" background-color="#324057" router>
                    <el-menu-item index="adminSet" >
                        <i class="el-icon-menu"></i>
                        <span slot="title">桌面</span>
                    </el-menu-item>
                    <el-submenu index="tab1">
                        <template slot="title">
                            <i class="el-icon-star-on"></i>
                            <span>账号</span>
                        </template>
                        <el-menu-item index="channel" class="child-menu">登录设置</el-menu-item>
                        <el-menu-item index="merchant" class="child-menu">账号查询</el-menu-item>
                    </el-submenu>
                    <el-submenu index="tab2">
                        <template slot="title">
                            <i class="el-icon-document"></i>
                            <span>发弹幕</span>
                        </template>
                        <el-menu-item index="fsdanmu" class="child-menu">弹幕查询</el-menu-item>
                    </el-submenu>
                    <el-submenu index="tab3">
                        <template slot="title">
                            <i class="el-icon-printer"></i>
                            <span>日志</span>
                        </template>
                        <el-menu-item index="log" class="child-menu">日志查询</el-menu-item>
                    </el-submenu>
                    <el-submenu index="tab4">
                        <template slot="title">
                            <i class="el-icon-tickets"></i>
                            <span>内容</span>
                        </template>
                        <el-menu-item index="context" class="child-menu">内容查询</el-menu-item>
                    </el-submenu>
                    <el-submenu index="tab5">
                        <template slot="title">
                            <i class="el-icon-setting"></i>
                            <span>设置</span>
                        </template>
                        <el-menu-item index="setting" class="child-menu">系统设置</el-menu-item>
                    </el-submenu>
                </el-menu>
            </el-col>
            <el-col :span="21" style="height: 100%;overflow: auto;">
				<keep-alive>
				    <router-view></router-view>
				</keep-alive>
			</el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        computed: {
			defaultActive: function(){
                console.log(this.$route.path.replace('/', ''));
				return this.$route.path.replace('/', '');
			}
		},
    }
</script>

<style lang="less" scoped>
    @import '../../style/mixin';
    .el-menu-dark{
        overflow: hidden;
    }
</style>