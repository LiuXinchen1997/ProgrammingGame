import Vue from 'vue'
import memberPage from '@/pages/memberPage.vue'
import request from 'XMLHttpRequest'

describe('memberPage.vue', () => {
  const Constructor = Vue.extend(memberPage)
  const vm = new Constructor().$mount()
  it('单元测试memberPage中的变量和函数', () => {
    expect(vm.money).toEqual(0)
    expect(vm.imgchoose).toEqual('')
    expect(vm.dialogFormVisible).toEqual(false)
    expect(vm.isPaid).toEqual(false)
    expect(typeof memberPage.data).toBe('function')
    expect(typeof memberPage.methods.getmonth).toBe('function')
    expect(typeof memberPage.methods.getmembertype).toBe('function')
    expect(typeof memberPage.methods.getMoneyFromType).toBe('function')
    expect(typeof memberPage.methods.sub).toBe('function')
    expect(typeof memberPage.methods.cancel).toBe('function')
    expect(typeof memberPage.methods.changeHandler).toBe('function')
    expect(typeof memberPage.methods.submit).toBe('function')
  })
  it('单元测试memberPage中的登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('button_scoped')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    memberPage._watcher.run()
  })
  it('单元测试memberPage中的账号登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('sub-button-username')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    memberPage._watcher.run()
  })
  it('单元测试memberPage中的手机验证码登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('sub-button-tel')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    memberPage._watcher.run()
  })
  it('异步请求应该返回一个对象', done => {
    request
      .get('http://localhost:8080/UserManage/member')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
