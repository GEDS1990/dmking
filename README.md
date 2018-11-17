# vue-electron-manage

> 一个使用vue-electron构建的管理应用
* 模仿win8来创建的管理界面
* 使用vue-router的导航守卫进行跳转权限判断
* 使用vuex进行登录状态的管理
* 使用element-ui来进行页面的构建
* 使用echarts进行图表的制作
* 使用less进行样式设置

#### Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:9080
npm run dev

# build electron application for production
npm run build
npm run-script buildwin

or 

electron-packager . elem --out ../electron  (x)
此时electron-packager就会自动判别当前的操作系统打包对应的文件，例如windows系统下就会打包成.exe格式。

如果你想一次性把所有的操作系统都打包一遍，可以在上面打包语句后面加上-all。


``` 
------------------------------------------------------------------------------------------------------------------

技术栈：
    python2.7   selenium 3.14.1    chromedriver v2.43        chrome 70.0

    npm install phantomjs-prebuilt
需求：
    主流直播网站自动弹幕
    自动注册
    自动登录
    弹幕内容可配置
    弹幕间隔可配置

记录：
    六房间：
        登录ok
           注册
    虎牙：登录ok，注册
    斗鱼：
        登录需要对接打码平台cookies;
        目前使用cookies登录；
            dyGetCookies.py运行获取cookies，将u'换成'，保存到dy-cookies.txt
            运行dyUtil.py进行爬取
        注册
    熊猫：
    龙珠：

------------------------------------------------------------------------------------------------------------------
