import Vue from 'vue'
import loginPage from '@/pages/loginPage.vue'
import request from 'XMLHttpRequest'

describe('login.vue', () => {
  const Constructor = Vue.extend(loginPage)
  const vm = new Constructor().$mount()
  it('单元测试loginPage中的变量和函数', () => {
    expect(vm.dialogVisible).toEqual(false)
    expect(vm.logining).toEqual(false)
    expect(vm.time).toEqual(60)
    expect(vm.sendMsgDisabled).toEqual(false)
    expect(typeof loginPage.data).toBe('function')
    expect(typeof loginPage.methods.submit).toBe('function')
    expect(typeof loginPage.methods.checkTelNum).toBe('function')
    expect(typeof loginPage.methods.getVerificationcode).toBe('function')
    expect(typeof loginPage.methods.submitByTel).toBe('function')
    expect(typeof loginPage.methods.reset).toBe('function')
    expect(typeof loginPage.methods.resetByTel).toBe('function')
    expect(typeof loginPage.methods.forgetPassword).toBe('function')
  })
  it('单元测试loginPage中的登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('button_scoped')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    loginPage._watcher.run()
  })
  it('单元测试loginPage中的账号登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('sub-button-username')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    loginPage._watcher.run()
  })
  it('单元测试loginPage中的手机验证码登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('sub-button-tel')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    loginPage._watcher.run()
  })
  it('异步请求应该返回一个对象', done => {
    request
      .get('http://localhost:8080/logins')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
