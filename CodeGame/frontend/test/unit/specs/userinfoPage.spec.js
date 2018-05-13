import userinfoPage from '@/pages/userinfoPage.vue'
import {destroyVM, createTest} from '../util'
import request from 'XMLHttpRequest'

describe('userinfoPage', () => {
  let vm
  afterEach(() => {
    destroyVM(vm)
  })
  it('测试获取元素内容', () => {
    vm = createTest(userinfoPage, true)
    expect(vm.$el.querySelector('el-button primary').textContent).to.equal('修改信息')
    expect(vm.$el.querySelector('el-button info').textContent).to.have.be.equal('返回')
    expect(vm.$el.querySelector('el-button primary').textContent).to.equal('确定修改')
    expect(vm.$el.querySelector('el-button warning').textContent).to.have.be.equal('重置')
  })
  it('测试获取Vue对象中的数据', () => {
    expect(vm.modifyMode).to.equal(false)
    expect(vm.active).to.equal('0')
    expect(vm.username).to.equal(null)
    expect(vm.tel_number).to.equal('')
    expect(vm.isDisable).to.equal(null)
  })
  it('单元测试userinfoPage中的修改信息按钮的点击事件', () => {
    let button = vm.$el.querySelector('el-button primary')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    userinfoPage._watcher.run()
  })
  it('单元测试userinfoPage中的返回按钮的点击事件', () => {
    let button = vm.$el.querySelector('el-button info')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    userinfoPage._watcher.run()
  })
  it('单元测试userinfoPage中的确定修改按钮的点击事件', () => {
    let button = vm.$el.querySelector('el-button primary')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    userinfoPage._watcher.run()
  })
  it('单元测试userinfoPage中的重置按钮的点击事件', () => {
    let button = vm.$el.querySelector('el-button warning')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    userinfoPage._watcher.run()
  })
  it('异步请求应该返回一个对象', done => {
    request
      .get('http://localhost:8080/UserManage/userInfo')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
