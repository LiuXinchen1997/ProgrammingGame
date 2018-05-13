<template>
<div class="modify-psd">
  <el-col class="step" :offset="7" :span="14">
    <el-steps  :space="350" :active="active" finish-status="success">
      <el-step title="验证原密码"></el-step>
      <el-step title="输入新密码"></el-step>
      <el-step title="确认"></el-step>
    </el-steps>
  </el-col>
  <el-row >
    <el-col class="old-password" :offset="8" :span="8">
      <el-input type="password" v-model="oldPassword" @blur="checkPassword" placeholder="请输入原密码" :disabled="oldPsdCorrect">
        <template slot="prepend">原密码</template>
      </el-input>
    </el-col>
  </el-row>
  <transition name="el-fade-in-linear">
    <el-main v-show="oldPsdCorrect">
      <el-form ref="passwordForm" :model="form" :rules="rules" label-width="100px">
        <el-row>
          <el-col class="new-password" :offset="7" :span="9">
            <el-form-item label="新的密码" prop="newPassword">
              <el-input type="password" v-model="form.newPassword"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="9">
            <el-form-item label="确认密码" prop="passwordAgain">
              <el-input type="password" v-model="form.passwordAgain" @blur="checkNewPassword"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col class="psd-button" :offset="9" :span="8">
            <el-form-item>
              <el-button type="primary" size="mini" @click="submit">确 定</el-button>
              <el-button type="warning" size="mini" @click="reset">重 置</el-button>
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

export default {
  data () {
    let validatePassAgain = (rule, value, callback) => {
      if (value !== this.form.newPassword) {
        callback(new Error('两次输入密码不一致!'))
        this.active = '1'
      } else {
        this.active = '2'
        callback()
      }
      console.log(this.active)
    }
    return {
      active: '0',
      username: '',
      oldPsdCorrect: false,
      oldPassword: '',
      form: {
        newPassword: '',
        passwordAgain: ''
      },
      rules: {
        newPassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '用户名长度需要在 6 到 20 个字符', trigger: 'blur' }
        ],
        passwordAgain: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '用户名长度需要在 6 到 20 个字符', trigger: 'blur' },
          { validator: validatePassAgain, trigger: 'blur' }
        ]
      }
    }
  },
  mounted () {
    this.username = sessionStorage.getItem('username')
  },
  methods: {
    checkPassword () {
      const url = GetUrl('UserManage/checkPassword')
      let params = new URLSearchParams()
      params.append('username', this.username)
      params.append('oldPassword', md5(this.oldPassword))
      this.$axios({
        method: 'post',
        url: url,
        data: params
      }).then((res) => {
        if (res.data.success) {
          this.$message({
            showClose: true,
            message: '原密码正确！',
            type: 'success'
          })
        } else {
          this.$message({
            showClose: true,
            message: '原密码错误，请重试！',
            type: 'error'
          })
          return
        }
        this.oldPsdCorrect = true
        this.active = 1
      })
    },
    checkNewPassword () {
      if (this.newPassword === this.passwordAgain) {
        this.active = 2
      }
    },
    submit () {
      this.$refs['passwordForm'].validate(valid => {
        if (!valid) {
          this.$message({
            showClose: true,
            message: '请继续完善表单！',
            type: 'error'
          })
        } else {
          this.active = 3
          const url = GetUrl('UserManage/UpdatePsw')
          var params = new URLSearchParams()
          params.append('userName', this.username)
          params.append('password', md5(this.form.newPassword))
          this.$axios({
            method: 'post',
            url: url,
            data: params
          }).then((res) => {
            if (res.data.success) {
              this.$message({
                showClose: true,
                message: '恭喜您，修改成功，请重新登录！',
                type: 'success'
              })
              alert('恭喜您，修改成功，请重新登录！')
              this.$router.push('/login')
              location.reload()
            } else {
              this.$message({
                showClose: true,
                message: '修改失败，请重试！',
                type: 'error'
              })
            }
          })
        }
      })
    },
    reset () {
      this.$refs['passwordForm'].resetFields()
    }
  }
}
</script>

<style>
#verify-code-area > .el-row {
  margin-bottom: 80px;
}
.modify-psd {
  background-image: url(../assets/usermanage_background.png);
  background-size: cover;
  min-height: 700px;
}
.step {
  margin-top: 75px;
}
.old-password {
  margin-top: 55px;
  margin-bottom: 35px;
}
.new-password {
  margin-bottom: 35px;
}
.psd-button {
  margin-top: 30px;
}
</style>
