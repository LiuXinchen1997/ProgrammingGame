import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexPage from '../pages/index'
import helloPage from '../pages/hello'
import loginPage from '../pages/loginPage'
import registerPage from '../pages/registerPage'
import findPsdPage from '../pages/findPsdPage'
import memberPage from '../pages/memberPage'
import userInfoPage from '../pages/userInfoPage'
import modifyPsdPage from '../pages/modifyPsdPage'
import navmenu from '../components/navmenu'
import notFoundPage from '../pages/errPages/404'
import rightErrorPage from '../pages/errPages/401'
import selectLevelPage from '../pages/ChallengeMode/selectLevelPage'
import blockly from '../pages/BlocklyTem'
import mapSquare from '../pages/FreeMode/mapSquare'
import mapCenter from '../pages/FreeMode/mapCenter'
import creation from '../pages/FreeMode/creation'
import collection from '../pages/FreeMode/collection'
import release from '../pages/FreeMode/release'
import shareLink from '../pages/shareLink'
import createMap from '../pages/FreeMode/createMap'
import updateMap from '../pages/FreeMode/updateMap'
import freeModeUpload from '../pages/freeModeUpload'
import freeModePlay from '../pages/freeModePlay'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [{
    path: '/hello',
    component: helloPage
  },
  {
    path: '/',
    redirect: '/UserManage/index'
  },
  {
    path: '/login',
    name: 'login',
    component: loginPage
  },
  {
    path: '/blockly/:id',
    component: blockly
  },
  {
    path: '/shareLink/:id',
    name: 'shareLink',
    component: shareLink
  },
  {
    path: '/register',
    name: 'register',
    component: registerPage
  },
  {
    path: '/findPsd',
    name: 'findPsd',
    component: findPsdPage
  },
  {
    path: '/UserManage',
    name: 'UserManage',
    component: navmenu,
    children: [
      {
        path: 'index',
        component: IndexPage
      },
      {
        path: 'member',
        component: memberPage
      },
      {
        path: 'userInfo',
        component: userInfoPage
      },
      {
        path: 'modifyPsd',
        component: modifyPsdPage
      }
    ]
  },
  {
    path: '/ChallengeMode',
    name: 'ChallengeMode',
    component: navmenu,
    children: [
      {
        path: 'selectLevel',
        component: selectLevelPage
      }
    ]
  },
  {
    path: '/FreeMode',
    name: 'FreeMode',
    component: navmenu,
    children: [
      {
        path: 'mapSquare',
        name: 'mapSquare',
        component: mapSquare
      },
      {
        path: 'mapCenter',
        name: 'mapCenter',
        component: mapCenter,
        children: [
          {
            path: '',
            redirect: 'creation'
          },
          {
            path: 'creation',
            name: 'creation',
            component: creation
          },
          {
            path: 'collection',
            name: 'collection',
            component: collection
          },
          {
            path: 'release',
            name: 'release',
            component: release
          }
        ]
      },
      {
        path: 'createMap',
        name: 'createMap',
        component: createMap
      }
    ]
  },
  {
    path: '/updateMap/:id',
    component: updateMap
  },
  {
    path: '/freeModeUpload/:id',
    component: freeModeUpload
  },
  {
    path: '/freeModePlay/:id',
    component: freeModePlay
  },
  {
    path: '/401',
    component: rightErrorPage
  },
  {
    path: '*',
    component: notFoundPage
  }
  ]
})

export default router
