<template>
  <div class="find">
    <transition name="el-zoom-in-top">
      <div class="form" v-show="!sendSucc" id="verifyCodeArea">
        <el-row>
          <el-col :offset="7" :span="10" class="grid-content">
            <el-input @blur="checkTelNum" v-model="tel_number" placeholder="请输入手机号码" :disabled="sendMsgDisabled">
              <template slot="prepend">手机号码</template>
            </el-input>
          </el-col>
        </el-row>
        <el-row :gutter="5">
          <el-col :offset="7" :span="8">
            <el-input v-model="verifyCode" placeholder="请输入验证码">
            </el-input>
          </el-col>
          <el-col :span="1">
            <el-button type="success" size="medium" @click.native.prevent="getVerifyCode" :disabled="sendMsgDisabled">
              <div v-if="sendMsgDisabled">{{time + '秒后获取'}}</div>
              <span v-if="!sendMsgDisabled">发送验证码</span>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="1" :offset="16">
            <el-button @click="submitVerifyCode" type="primary" size="mini">确定</el-button>
          </el-col>
        </el-row>
      </div>
    </transition>

    <transition name="el-zoom-in-top">
      <div v-show="sendSucc" class="new_password">
        <el-form :model="passwordForm" ref="passwordForm" :rules="rules" status-icon label-width="0" class="password-form">
          <el-form-item prop="password">
            <el-input type="password" v-model="passwordForm.password" placeholder="请输入新密码"></el-input>
          </el-form-item>
          <el-form-item prop="passwordAgain">
            <el-input type="password" v-model="passwordForm.passwordAgain" @blur="checkout_psd" placeholder="请确认新密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="danger" class="button" size="small" round @click.native.prevent="submitModify">确 定</el-button>
            <el-button type="primary" class="button" size="small" round @click.native.prevent="reset">重 置</el-button>
            <hr>
            <p><span ></span></p>
          </el-form-item>
        </el-form>
      </div>
    </transition>
  </div>
</template>

<script>
import GetUrl from '../utils/GetURL'
import CheckData from '../utils/CheckData'
import ElementApi from '../utils/ElementAPI'
import md5 from 'js-md5'

export default {
  data () {
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.passwordForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      tel_number: '',
      true_tel_number: '',
      realVerifyCode: '',
      verifyCode: '',
      sendMsgDisabled: false,
      time: 60,
      sendSucc: false,
      passwordForm: {
        password: '',
        passwordAgain: ''
      },
      rules: {
        password: [
          { required: true, message: '请输入新密码', trigger: 'blur' },
          { min: 6, max: 20, message: '用户密码长度需要在 6 到 20 个字符', trigger: 'blur' }
        ],
        passwordAgain: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '用户密码长度需要在 6 到 20 个字符', trigger: 'blur' },
          { validator: validatePass, required: true, trigger: 'blur' }
        ]
      }
    }
  },
  mounted () {
  },
  methods: {
    checkout_psd () {
      if (this.passwordForm.password === this.password.passwordAgain) {
      }
    },
    checkTelNum () {
      if (this.tel_number === '') {
        this.$message({
          showClose: true,
          message: '手机号码不能为空！',
          type: 'error'
        })
        return
      }
      let telRg = /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/
      if (!telRg.test(this.tel_number)) {
        this.$message({
          showClose: true,
          message: '请输入正确的手机号码！',
          type: 'error'
        })
        return
      }
      const url = GetUrl('UserManage/checkTelNum')
      this.$axios({
        method: 'get',
        url: url,
        params: {
          'tel_number': this.tel_number
        }
      }).then((res) => {
        let flag = res.data.exists
        if (!flag) {
          ElementApi.message(this, '该手机号码不存在，请重试！', 'error')
        } else {
          this.true_tel_number = this.tel_number
        }
      })
    },
    getVerifyCode () {
      if (!CheckData.checkFindPsdTelNum(this, this.tel_number)) {
        return
      }
      let clock = this
      if (!clock.sendMsgDisabled) {
        clock.sendMsgDisabled = true
        this.$axios({
          method: 'get',
          url: GetUrl('UserManage/sendMessage'),
          params: {
            'tel_number': this.tel_number
          }
        }).then((res) => {
          if (res.data.status_code === 22) {
            this.$message({
              showClose: true,
              message: '请求过于频繁，请休息一会！',
              type: 'error'
            })
            return
          } else if (!res.data.success) {
            this.$message({
              showClose: true,
              message: '系统错误，请重试！',
              type: 'error'
            })
            return
          }
          this.realVerifyCode = res.data.verifyCode
        }).catch((error) => {
          console.log(error)
        })
        let interval = window.setInterval(function () {
          if ((clock.time--) <= 0) {
            clock.time = 60
            clock.sendMsgDisabled = false
            window.clearInterval(interval)
          }
        }, 1000)
      }
    },
    submitVerifyCode () {
      if (CheckData.checkFindPsdTelNum(this, this.tel_number)) {
        if (this.verifyCode === this.realVerifyCode) {
          ElementApi.message(this, '验证成功', 'success')
          this.sendSucc = true
        } else {
          ElementApi.message(this, '验证失败', 'error')
          this.sendSucc = false
        }
      }
    },
    submitModify () {
      this.$refs['passwordForm'].validate(valid => {
        if (valid) {
          let telNumber = this.tel_number
          let password = this.passwordForm.password
          let params = new URLSearchParams()
          params.append('telNumber', telNumber)
          params.append('password', md5(password))
          this.$axios({
            method: 'post',
            url: GetUrl('UserManage/UpdatePsdByTelNum'),
            data: params
          })
            .then(response => {
              if (response.data.success) {
                alert('重置密码成功！')
                this.$router.push('/login')
                location.reload()
                ElementApi.message(this, '重置密码成功', 'success')
              } else {
                ElementApi.message(this, '重置密码失败，请重试！', 'error')
              }
            })
        } else {
          ElementApi.message(this, '请完善表单！', 'error')
        }
      })
    },
    reset () {
      this.$refs.passwordForm.resetFields()
    }
  }
}
</script>

<style>
#verifyCodeArea > .el-row {
  padding-bottom: 20px;
}
.password-form {
  margin: 20px auto;
  width: 310px;
  padding: 30px 30px 0 30px;
  border-radius: 25px;
}
.button {
  width: 22%;
  margin-left: 155px;
}
.to {
  color: #67c23a;
  cursor: pointer;
}
.find {
  background-image: url(../assets/备用.png);
  background-size: cover;
  min-height: 700px;
}
.new_password {
  padding-top: 100px;
}
.form {
  padding-top: 150px;
}
</style>
