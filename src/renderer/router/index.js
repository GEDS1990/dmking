import Vue from 'vue'
import Router from 'vue-router'
import Store from '../store/index'

Vue.use(Router)

const Login = r => require.ensure([], () => r(require('@/components/login/login')), 'login');
const Home = r => require.ensure([],() => r(require('@/components/home/Home')), 'home');
const News = r => require.ensure([],() => r(require('@/components/news/News')), 'news');
const Manage = r => require.ensure([],() => r(require('@/components/manage/manage')), 'manage');
const ManageHome = r => require.ensure([],() => r(require('@/components/manage/manageHome/home')), 'manageHome');
const Channel = r => require.ensure([],() => r(require('@/components/manage/jinjian/channel')), 'channel');
const Merchant = r => require.ensure([],() => r(require('@/components/manage/jinjian/merchant')), 'merchant');
const FsDanmu = r => require.ensure([],() => r(require('@/components/manage/jinjian/fsdanmu')), 'fsdanmu');
const Log = r => require.ensure([],() => r(require('@/components/manage/jinjian/log')), 'log');
const Context = r => require.ensure([],() => r(require('@/components/manage/jinjian/context')), 'context');
const Setting = r => require.ensure([],() => r(require('@/components/manage/jinjian/setting')), 'setting');
const addMerchant = r => require.ensure([],() => r(require('@/components/manage/addMerchant/addMerchant')), 'addMerchant');
const addContext = r => require.ensure([],() => r(require('@/components/manage/addContext/addContext')), 'addContext');
const Show = r => require.ensure([],() => r(require('@/components/showMsg/showMsg')), 'showMsg');

export default new Router({
  routes: [
    {
      path: '/login',
      component: Login
    },
    {
      path: '/',
      name: 'home-index',
      component: Home,
      beforeEnter: (to,from,next)=> {
        console.log(to)
        console.log(from)
        if(Store.state.isLogin == 1){
          //用户已登录
          next();
        }else{
          next({path: '/login',query: {Rurl: to.fullPath}});
        }
      },
      children: [{
        path: '/news',
        component: News
      },{
        path: '/showMsg',
        component: Show,
        meta: {title: '标题',content: ['啊啊啊','啦啦啦啦']}
      },{
        path: '/important',
        component: Show,
        meta: {title: '便签',content: ['便签1','便签2']}
      }]
    },
    {
      path: '/manage',
      name: 'manage',
      component: Manage,
      children: [{
        path: '',
        component: ManageHome,
        meta: []
      },
      {
        path: '/channel',
        component: Channel,
        meta: ['账号管理','登录设置']
      },
      {
        path: '/merchant',
        component: Merchant,
        meta: ['账号管理','账号查询']
      },
      {
        path: '/fsdanmu',
        component: FsDanmu,
        meta: ['发送弹幕','弹幕查询']
      },
      {
        path: '/log',
        component: Log,
        meta: ['日志','日志查询']
      },
      {
        path: '/context',
        component: Context,
        meta: ['内容','内容查询']
      },
      {
        path: '/setting',
        component: Setting,
        meta: ['设置','系统设置']
      },
      {
        path: '/addMerchant',
        component: addMerchant,
        meta: ['用户管理','用户管理', '新增用户']
      },
      {
        path: '/addContext',
        component: addContext,
        meta: ['内容管理','内容管理', '新增内容']
      }
    ]},
    {
      path: '*',
      redirect: '/'
    }
  ]
})
