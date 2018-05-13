import Vue from 'vue'
import mapSquare from '@/pages/FreeMode/mapSquare.vue'
import request from 'XMLHttpRequest'

describe('mapSquare.vue', () => {
  const Constructor = Vue.extend(mapSquare)
  const vm = new Constructor().$mount()
  it('单元测试mapSquare中的变量和函数', () => {
    expect(vm.username).toEqual('')
    expect(vm.data).toEqual(null)
    expect(vm.currentPage).toEqua(6)
    expect(typeof mapSquare.data).toBe('function')
    expect(typeof mapSquare.methods.handleSizeChange).toBe('function')
    expect(typeof mapSquare.methods.handleCurrentChange).toBe('function')
    expect(typeof mapSquare.methods.setLikeById).toBe('function')
    expect(typeof mapSquare.methods.cancelLikeById).toBe('function')
    expect(typeof mapSquare.methods.setCollectById).toBe('function')
    expect(typeof mapSquare.methods.cancelCollectById).toBe('function')
    expect(typeof mapSquare.methods.play).toBe('function')
  })
  it('单元测试mapSquare中的点赞按钮的点击事件', () => {
    let button = vm.$el.querySelector('fa fa-thumbs-o-up fa-1x')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    mapSquare._watcher.run()
  })
  it('单元测试mapSquare中的进入取消按钮的点击事件', () => {
    let button = vm.$el.querySelector('fa fa-space-shuttle fa-1x')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    mapSquare._watcher.run()
  })
  it('单元测试mapSquare中的进入收藏按钮的点击事件', () => {
    let button = vm.$el.querySelector('fa fa-heart-o fa-1x')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    mapSquare._watcher.run()
  })
  it('单元测试mapSquare中的进入游戏按钮的点击事件', () => {
    let button = vm.$el.querySelector('fa fa-space-shuttle fa-1x')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    mapSquare._watcher.run()
  })
  it('异步请求得到所有地图应该返回一个对象', done => {
    request
      .get('http://localhost:8080/FreeMode/getAllReleasedMap')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
