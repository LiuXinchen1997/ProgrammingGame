import Vue from 'vue'
import modifyPsdPage from '@/pages/modifyPsdPage.vue'
import request from 'XMLHttpRequest'

describe('modifyPsdPage.vue', () => {
  const Constructor = Vue.extend(modifyPsdPage)
  const vm = new Constructor().$mount()
  it('单元测试memberPage中的变量和函数', () => {
    expect(vm.active).toEqual(0)
    expect(vm.username).toEqual('')
    expect(vm.oldPsdCorrect).toEqual(false)
    expect(vm.oldPassword).toEqual('')
    expect(typeof modifyPsdPage.data).toBe('function')
    expect(typeof modifyPsdPage.methods.checkPassword).toBe('function')
    expect(typeof modifyPsdPage.methods.checkNewPassword).toBe('function')
    expect(typeof modifyPsdPage.methods.submit).toBe('function')
    expect(typeof modifyPsdPage.methods.reset).toBe('function')
  })
  it('单元测试modifyPsdPage中的登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('psd-button primary')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    modifyPsdPage._watcher.run()
  })
  it('单元测试modifyPsdPage中的账号登录按钮的点击事件', () => {
    let button = vm.$el.querySelector('psd-button warning')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    modifyPsdPage._watcher.run()
  })
  it('异步请求应该返回一个对象', done => {
    request
      .get('http://localhost:8080/findPsd')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
