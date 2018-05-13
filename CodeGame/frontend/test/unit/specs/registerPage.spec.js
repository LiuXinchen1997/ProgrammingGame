import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import {destroyVM} from '../util'
import request from 'XMLHttpRequest'

import registerPage from '@/pages/registerPage'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
Vue.prototype.$axios = axios

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(ElementUI)

describe('registerPage.vue', () => {
  let vm
  afterEach(() => {
    destroyVM(vm)
  })
  it('should render correct contents', () => {
    const Constructor = Vue.extend(registerPage)
    const vm = new Constructor().$mount()
    expect(vm.form.gender)
      .to.equal('男')
  })
  it('should render correct contents', () => {
    const Constructor = Vue.extend(registerPage)
    const vm = new Constructor().$mount()
    expect(vm.form.username)
      .to.equal('')
  })
  it('should render correct contents', () => {
    const Constructor = Vue.extend(registerPage)
    const vm = new Constructor().$mount()
    expect(vm.form.password)
      .to.equal('')
  })
  it('should render correct contents', () => {
    const Constructor = Vue.extend(registerPage)
    const vm = new Constructor().$mount()
    expect(vm.form.fullname)
      .to.equal('')
  })
  it('should render correct contents', () => {
    const Constructor = Vue.extend(registerPage)
    const vm = new Constructor().$mount()
    expect(vm.form.email)
      .to.equal('')
  })
  it('单元测试registerPage中的登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('button_scoped')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    registerPage._watcher.run()
  })
  it('单元测试registerPage中的账号登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('sub-button-username')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    registerPage._watcher.run()
  })
  it('单元测试registerPage中的手机验证码登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('sub-button-tel')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    registerPage._watcher.run()
  })
  it('异步请求应该返回一个对象', done => {
    request
      .get('http://localhost:8080/register')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
