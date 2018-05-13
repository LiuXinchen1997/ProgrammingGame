<template>
<div class='main-box' :style="global">
  <div class="login-box">
    <el-form :model="LoginForm" ref="LoginForm" :rules="rules" status-icon label-width="0" class="login-form" v-show="showForm">
    <el-form-item prop="userName">
    <el-input type="text" v-model="LoginForm.userName" placeholder="请输入用户名"></el-input>
    </el-form-item>
    <br/>
    <el-form-item prop="password">
    <el-input type="password" v-model="LoginForm.password" placeholder="请输入密码"></el-input>
    </el-form-item>
    <br/>
    <el-form-item>
    <el-col :span="15" :offset="12">
    <el-button type="primary" class="button_scoped" @click.native.prevent="submit" :loading="logining"><font color="#fff">登录</font></el-button>
    <el-button type="warning" class="button_scoped" @click.native.prevent="reset"><font color="#fff">重置</font></el-button>
    </el-col>
    <el-col><hr></el-col>
    </el-form-item>
    <el-col :offset="11">
      <el-button class="sub-button-username" type="primary" @click="showContent" v-show="!showForm" size="small">账号登录</el-button>
      <el-button class="sub-button-tel" type="primary" @click="showContent" v-show="showForm" size="small">手机登录</el-button>
      <el-button type="danger" @click="forgetPassword" size="small">找回密码</el-button>
    </el-col>
    </el-form>

    <el-form :model="LoginFormByTel" ref="LoginFormByTel" :rules="rules" status-icon label-width="0" class="login-form" v-show="!showForm">
      <el-form-item prop="telnumber">
        <el-input type="text" v-model="LoginFormByTel.telnumber" @blur="checkTelNum" placeholder="请输入手机号码"></el-input>
      </el-form-item>
      <br/>
      <el-form-item prop="verificationcode">
        <el-col :span="14">
          <el-input type="text"  v-model="LoginFormByTel.verificationcode" placeholder="请输入验证码"></el-input>
        </el-col>
        &nbsp;&nbsp;
        <el-button type="primary" class="verificateButton" @click.native.prevent="getVerificationcode" :disabled="sendMsgDisabled" size="small">
        <div v-if="sendMsgDisabled">{{time + '秒后获取'}}</div>
        <span v-if="!sendMsgDisabled">发送验证码</span>
        </el-button>
      </el-form-item>
      <br/>
      <el-form-item>
        <el-col :span="15" :offset="12">
        <el-button type="primary" class="button_scoped" @click.native.prevent="submitByTel" :loading="logining">登录</el-button>
        <el-button type="warning" class="button_scoped" @click.native.prevent="resetByTel">重置</el-button>
        </el-col>
        <el-col><hr></el-col>
      </el-form-item>
      <el-col :offset="12">
        <el-button class="sub-button-username" type="primary" @click="showContent" v-show="!showForm" size="small">账号登录</el-button>
        <el-button class="sub-button-tel" type="primary" @click="showContent" v-show="showForm" size="small">手机验证码登录</el-button>
        <el-button type="danger" @click="forgetPassword" size="small">找回密码</el-button>
      </el-col>
    </el-form>
</div>
</div>
</template>

<script>
import md5 from 'js-md5'
import GetURL from '../utils/GetURL'
import ElementApi from '../utils/ElementAPI'

export default {
  data () {
    return {
      global: {
        backgroundImage: 'url(' + require('../assets/login_background.jpg') + ')',
        backgroundSize: '100% 100%',
        minHeight: '400px'
      },
      varifyMessageCode: '',
      showForm: true,
      LoginForm: {
        userName: '',
        password: ''
      },
      LoginFormByTel: {
        telnumber: '',
        verificationcode: ''
      },
      rules: {
        userName: [{
          required: true,
          max: 14,
          min: 3,
          message: '请输入用户名,长度为3-14位',
          trigger: 'blur'
        }],
        password: [{
          required: true,
          max: 14,
          min: 3,
          message: '请输入密码,长度为3-14位',
          trigger: 'blur'
        }],
        telnumber: [{
          required: true,
          pattern: /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/,
          message: '请输入格式正确的11位手机号码',
          trigger: 'blur'
        }]
      },
      dialogVisible: false,
      logining: false,
      time: 60,
      sendMsgDisabled: false
    }
  },
  methods: {
    showContent () {
      let a = this.showForm
      this.showForm = !a
    },
    submit () {
      this.$refs.LoginForm.validate(valid => {
        if (valid) {
          let name = this.LoginForm.userName
          let password = this.LoginForm.password
          let params = new URLSearchParams()
          params.append('userName', name)
          params.append('password', md5(password))
          this.$axios({
            method: 'post',
            url: GetURL('UserManage/Login'),
            data: params
          }).then((response) => {
            if (response.data.status === 1) {
              ElementApi.message(this, '登录成功！', 'success')
              sessionStorage.setItem('username', this.LoginForm.userName)
              this.$destroy()
              this.$router.replace('/')
            } else {
              this.$message({
                type: 'error',
                message: '用户名或密码错误',
                showClose: true
              })
            }
          }).catch((error) => {
            console.log(error)
          })
        } else {
          console.log('Validation ERROR')
        }
      })
    },
    checkTelNum () {
      this.$refs.LoginFormByTel.validate(valid => {
        if (valid) {
          const url = GetURL('UserManage/checkTelNum')
          this.$axios({
            method: 'get',
            url: url,
            params: {
              'tel_number': this.LoginFormByTel.telnumber
            }
          }).then((res) => {
            let flag = res.data.exists
            if (!flag) {
              this.$message({
                showClose: true,
                message: '该手机号码不存在，请重试！',
                type: 'error'
              })
            }
          })
        }
      })
    },
    getVerificationcode () {
      this.$refs.LoginFormByTel.validate(valid => {
        if (valid) {
          let clock = this
          if (!clock.sendMsgDisabled) {
            clock.sendMsgDisabled = true
            let telNumber = this.LoginFormByTel.telnumber
            this.$axios({
              method: 'get',
              url: GetURL('UserManage/sendMessage'),
              params: {
                'tel_number': telNumber
              }
            }).then((response) => {
              this.varifyMessageCode = response.data.verifyCode
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
        } else {
          console.log('Validation ERROR')
        }
      })
    },
    submitByTel () {
      this.$refs.LoginFormByTel.validate(valid => {
        if (valid) {
          if (this.LoginFormByTel.verificationcode.length !== 6) {
            this.$message({
              showClose: true,
              message: '请输入6位验证码！',
              type: 'error'
            })
            return
          }
          if (this.varifyMessageCode === this.LoginFormByTel.verificationcode) {
            ElementApi.message(this, '登录成功！', 'success')
            let params = new URLSearchParams()
            params.append('telnumber', this.LoginFormByTel.telnumber)
            this.$axios({
              method: 'post',
              url: GetURL('UserManage/getUsernameByTel'),
              data: params
            }).then((res) => {
              if (res.data.success) {
                sessionStorage.setItem('username', res.data.username)
                this.$destroy()
                this.$router.replace('/')
              } else {
                ElementApi.message(this, '系统错误，请重试！', 'error')
              }
            })
          } else {
            this.$message({
              showClose: true,
              message: '验证码错误',
              type: 'error'
            })
          }
        }
      })
    },
    reset () {
      this.$refs.LoginForm.resetFields()
    },
    resetByTel () {
      this.$refs.LoginFormByTel.resetFields()
    },
    forgetPassword () {
      this.$router.replace('/findPsd')
      location.reload()
    }
  }
}
</script>

<style scoped>
.main-box {
  height: 650px;
  padding: 20px 0px 0px 0px;
}
.login-box {
  width: 30%;
  height: 65%;
  border: 2px solid #FFFFFF;
  margin-top: 45px;
  margin-left: 60%;
  padding: 40px 40px 20px 40px;
  border-radius: 10px;
  background:rgba(64, 160, 255, 0.397);
}
.header-button {
  margin: 0px auto 30px auto;
  text-align: center;
}
.login-form {
  margin-top:20px;
  width: 100%;
  min-height: 250px;
}
</style>
