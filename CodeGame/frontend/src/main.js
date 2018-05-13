// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from './components/layout'
import router from './router'
import constval from './utils/ConstVal'
import DataHelper from './utils/DataHelper'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import { codemirror } from 'vue-codemirror'
import { Blockly } from 'node-blockly/browser'
import 'font-awesome/css/font-awesome.css'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
Vue.prototype.$axios = axios

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.use(Vuetify)

Vue.component('codemirror', codemirror)
Vue.component('blockly', Blockly)

router.beforeEach((to, from, next) => {
  if (to.path.indexOf('shareLink') !== -1) {
    next()
    return
  }
  if (DataHelper.objContainsElement(to.path, constval.REMOVE_SESSION_URL)) {
    sessionStorage.removeItem('username')
  }
  let username = sessionStorage.getItem('username')
  if (!username && !DataHelper.objContainsElement(to.path, constval.NO_NEED_LOGIN_URL)) {
    alert('您还未登录，请先登录！')
    next({path: constval.NO_NEED_LOGIN_URL.LOGIN})
  } else {
    next()
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { Layout },
  template: '<Layout/>'
})
