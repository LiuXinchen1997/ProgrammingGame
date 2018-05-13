import Vue from 'vue'
import release from '@/pages/FreeMode/release.vue'
import request from 'XMLHttpRequest'

describe('release.vue', () => {
  const Constructor = Vue.extend(release)
  const vm = new Constructor().$mount()
  it('单元测试release中的变量和函数', () => {
    expect(vm.username).toEqual('')
    expect(vm.data).toEqual(null)
    expect(vm.currentPage).toEqua(6)
    expect(typeof release.data).toBe('function')
    expect(typeof release.methods.handleSizeChange).toBe('function')
    expect(typeof release.methods.handleCurrentChange).toBe('function')
    expect(typeof release.methods.deleteMap).toBe('function')
    expect(typeof release.methods.play).toBe('function')
  })
  it('单元测试release中的删除按钮的点击事件', () => {
    let button = vm.$el.querySelector('fa fa-trash fa-1x')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    release._watcher.run()
  })
  it('单元测试release中的进入游戏按钮的点击事件', () => {
    let button = vm.$el.querySelector('fa fa-space-shuttle fa-1x')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    release._watcher.run()
  })
  it('异步请求删除地图应该返回一个对象', done => {
    request
      .get('http://localhost:8080/FreeMode/deleteMapById')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
