import GetUrl from './GetURL'
import ElementApi from './ElementAPI'

export default {
  telNumExists: async function (context, telNumber) {
    const url = GetUrl('UserManage/checkTelNum')
    context.$axios({
      method: 'get',
      url: url,
      params: {
        'tel_number': telNumber
      }
    }).then((res) => {
      let flag = res.data.exists
      if (flag) {
        return true
      }
      return false
    }).catch((err) => {
      console.log(err)
      return false
    })
  },
  telNumIsNull: function (telNum) {
    if (telNum === '') {
      return true
    }
    return false
  },
  telNumIsValidate: function (telNum) {
    let telRg = /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/
    if (telRg.test(telNum)) {
      return true
    }
    return false
  },
  checkFindPsdTelNum: function (context, telNum) {
    if (this.telNumIsNull(telNum)) {
      ElementApi.message(context, '手机号码不能为空！', 'error')
      return false
    }
    if (!this.telNumIsValidate(telNum)) {
      ElementApi.message(context, '请输入正确的手机号码！', 'error')
      return false
    }
    if (!this.telNumExists(context, telNum)) {
      ElementApi.message(context, '手机号码不存在，请重试！', 'error')
      return false
    } else {
      return true
    }
  },
  checkRegisterTelNum: function (context, telNum) {
    if (context.tel_number === '') {
      context.$message({
        showClose: true,
        message: '手机号码不能为空！',
        type: 'error'
      })
      return false
    }
    let telRg = /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/
    if (!telRg.test(context.tel_number)) {
      context.$message({
        showClose: true,
        message: '请输入正确的手机号码！',
        type: 'error'
      })
      return false
    }
    const url = GetUrl('UserManage/checkTelNum')
    context.$axios({
      method: 'get',
      url: url,
      params: {
        'tel_number': context.tel_number
      }
    }).then((res) => {
      let flag = res.data.exists
      if (flag) {
        context.$message({
          showClose: true,
          message: '该手机号码已经存在，请重试！',
          type: 'error'
        })
        return false
      }
      return true
    }).catch((err) => {
      console.log(err)
      return false
    })
    return true
  }
}
