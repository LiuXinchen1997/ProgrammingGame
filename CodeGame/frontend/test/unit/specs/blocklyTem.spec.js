import Vue from 'vue'
import BlocklyPage from '@/pages/BlocklyTem.vue'
import request from 'XMLHttpRequest'

describe('memberPage.vue', () => {
  const Constructor = Vue.extend(BlocklyPage)
  const vm = new Constructor().$mount()
  it('单元测试memberPage中的变量和函数', () => {
    expect(vm.previousStatement).toEqual(null)
    expect(vm.nextStatement).toEqual(null)
    expect(vm.colour).toEqual(160)
    expect(vm.tooltip).toEqual('拖动我前进哦~')
    expect(typeof BlocklyPage.data).toBe('function')
    expect(typeof BlocklyPage.methods.click).toBe('function')
    expect(typeof BlocklyPage.methods.myUpdateFunction).toBe('function')
    expect(typeof BlocklyPage.methods.run).toBe('function')
    expect(typeof BlocklyPage.methods.next1).toBe('function')
    expect(typeof BlocklyPage.methods.next2).toBe('function')
    expect(typeof BlocklyPage.methods.restart).toBe('function')
    expect(typeof BlocklyPage.methods.getMapData).toBe('function')
    expect(typeof BlocklyPage.methods.back).toBe('function')
  })
  it('单元测试BlocklyPage中的运行按钮的点击事件', () => {
    let button = vm.$el.querySelector('btn-row')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    BlocklyPage._watcher.run()
  })
  it('单元测试BlocklyPage中的重新开始按钮的点击事件', () => {
    let button = vm.$el.querySelector('btn-row warning')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    BlocklyPage._watcher.run()
  })
  it('单元测试BlocklyPage中的进入下一关按钮的点击事件', () => {
    let button = vm.$el.querySelector('btn-nextlevel')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    BlocklyPage._watcher.run()
  })
  it('单元测试BlocklyPage中的返回按钮的点击事件', () => {
    let button = vm.$el.querySelector('info')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    BlocklyPage._watcher.run()
  })
  it('异步请求链接分享页面应该返回一个对象', done => {
    request
      .get('http://localhost:8080/shareLink')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
  it('异步请求挑战模式页面应该返回一个对象', done => {
    request
      .get('http://localhost:8080/ChallengeMode/getChallengeMapContent')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
  it('异步请求添加链接分享页面应该返回一个对象', done => {
    request
      .get('http://localhost:8080/ChallengeMode/addShareLink')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
