<template>
  <div class='main-box' :style="global">
    <transition name="el-zoom-in-center">
      <el-main v-show="!sendSucc" id="verifyCodeArea">
        <el-row>
          <!-- <el-col :offset="6" :span="10">
            <div class="block">
              <el-carousel class="carousel">
                <el-carousel-item v-for="item in 4" :key="item">
                  <img v-if="item === 1" src="../assets/register/1.jpg" />
                  <img v-if="item === 2" src="../assets/register/2.jpg" />
                  <img v-if="item === 3" src="../assets/register/3.png" />
                  <img v-if="item === 4" src="../assets/register/4.jpg" />
                </el-carousel-item>
              </el-carousel>
            </div>
          </el-col> -->
        </el-row>

        <el-row>
          <el-col :offset="7" :span="10" class="grid-content">
            <el-input @blur="checkTelNum" v-model="tel_number" placeholder="请输入手机号码">
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
            <el-button @click="submitVerifyCode" type="primary" size="small">确定</el-button>
          </el-col>
        </el-row>
      </el-main>
    </transition>

    <transition name="el-zoom-in-center">
    <el-main v-show="sendSucc">
      <el-form ref="registerForm" :model="form" :rules="rules" label-width="100px">
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="form.username"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="form.password"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="确认密码" prop="passwordAgain">
              <el-input type="password" v-model="form.passwordAgain"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="昵称" prop="fullname">
              <el-input v-model="form.fullname"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="出生日期" prop="birthday">
                <el-date-picker type="date" placeholder="选择日期" v-model="form.birthday" style="width: 100%;"></el-date-picker>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="性别">
              <el-radio-group v-model="form.gender">
                <el-radio label="男"></el-radio>
                <el-radio label="女"></el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="电子邮箱" prop="email">
              <el-input v-model="form.email"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="个人描述">
              <el-input type="textarea" v-model="form.descr"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="10">
            <el-form-item>
              <el-button type="primary" size="mini" @click="submit">注册</el-button>
              <el-button type="warning" size="mini" @click="reset">重置</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-main>
    </transition>
  </div>
</template>

<script>
import md5 from 'js-md5'
import GetUrl from '../utils/GetURL'
import CheckData from '../utils/CheckData'
import FormDataOperate from '../utils/FormDataOperate'
import ElementApi from '../utils/ElementAPI'

export default {
  data () {
    let validatePassAgain = (rule, value, callback) => {
      if (value !== this.form.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    let validateEmail = (rule, value, callback) => {
      let rg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/
      if (!rg.test(value)) {
        callback(new Error('请输入正确的电子邮箱地址！'))
      } else {
        callback()
      }
    }
    return {
      global: {
        backgroundImage: 'url(' + require('../assets/register_background.jpg') + ')',
        backgroundSize: '100% 100%',
        minHeight: '650px'
      },
      tel_number: '',
      realVerifyCode: '',
      verifyCode: '',
      sendMsgDisabled: false,
      time: 60,
      sendSucc: false,
      form: {
        username: '',
        password: '',
        passwordAgain: '',
        fullname: '',
        birthday: '',
        gender: '男',
        email: '',
        descr: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 6, max: 15, message: '用户名长度需要在 6 到 15 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '用户密码长度需要在 6 到 20 个字符', trigger: 'blur' }
        ],
        passwordAgain: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '用户密码长度需要在 6 到 20 个字符', trigger: 'blur' },
          { validator: validatePassAgain, trigger: 'blur' }
        ],
        fullname: [
          { required: true, message: '请输入用户昵称', trigger: 'blur' },
          { min: 6, max: 15, message: '用户昵称长度需要在 6 到 15 个字符', trigger: 'blur' }
        ],
        birthday: [
          { type: 'date', required: true, message: '请输入出生年月', trigger: 'change' }
        ],
        email: [
          { required: true, message: '请输入电子邮箱', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur' }
        ]
      }
    }
  },
  mounted () {
  },
  methods: {
    checkTelNum () {
      if (this.tel_number === '') {
        ElementApi.message(this, '手机号码不能为空！', 'error')
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
        if (flag) {
          this.$message({
            showClose: true,
            message: '该手机号码已经存在，请重试！',
            type: 'error'
          })
        }
      })
    },
    getVerifyCode () {
      if (!CheckData.checkRegisterTelNum(this, this.tel_number)) {
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
      if (CheckData.checkRegisterTelNum(this, this.tel_number)) {
        if (this.verifyCode === this.realVerifyCode) {
          this.$message({
            showClose: true,
            message: '验证成功',
            type: 'success'
          })
          this.sendSucc = true
        } else {
          this.$message({
            showClose: true,
            message: '验证失败',
            type: 'error'
          })
          this.sendSucc = false
        }
      }
    },
    submit () {
      this.$refs['registerForm'].validate(valid => {
        if (!valid) {
          this.$message({
            showClose: true,
            message: '请继续完善表单！',
            type: 'error'
          })
        } else {
          const url = GetUrl('UserManage/register')
          var params = new URLSearchParams()
          params.append('username', this.form.username)
          params.append('password', md5(this.form.password))
          params.append('gender', FormDataOperate.getNumberFromGender(this.form.gender))
          params.append('age', FormDataOperate.getAgeFromBirthday(this.form.birthday))
          params.append('email', this.form.email)
          params.append('descr', this.form.descr)
          params.append('tel_number', this.tel_number)
          params.append('fullname', this.form.fullname)
          this.$axios({
            method: 'post',
            url: url,
            data: params
          }).then((res) => {
            if (res.data.success) {
              this.$message({
                showClose: true,
                message: '恭喜您，注册成功！',
                type: 'success'
              })
              this.$destroy()
              this.$router.replace('/login')
            } else {
              this.$message({
                showClose: true,
                message: '注册失败，请重试！',
                type: 'error'
              })
              this.$destroy()
              this.$router.replace('/register')
            }
          })
        }
      })
    },
    reset () {
      this.$refs['registerForm'].resetFields()
    }
  }
}
</script>

<style scoped>
#verifyCodeArea > .el-row {
  margin-bottom: 40px;
}

.main-box {
  width: 100%;
}

.block {
  padding-bottom: 40px;
}

.carousel {
  min-height: 80%;
  width: 600px;
}

.carousel img {
  height: 100%;
  width: 100%;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}
</style>
