<template>
  <div class="info">
    <el-main>
      <el-col class="step" :offset="7" :span="14">
        <el-steps  :space="350" :active="active" finish-status="success">
          <el-step title="点击修改信息按钮"></el-step>
          <el-step title="修改个人信息"></el-step>
          <el-step title="确认"></el-step>
        </el-steps>
      </el-col>
      <el-form ref="userInfoForm" :model="form" :rules="rules" label-width="90px">
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="username" disabled></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="手机号码" prop="tel_number">
              <el-input v-model="tel_number" disabled></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="昵称" prop="fullname">
              <el-input v-model="form.fullname" @blur="checkout" :disabled="this.isDisable"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="年龄" prop="age">
              <el-input v-model="form.age" @blur="checkout" :disabled="this.isDisable"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="性别">
              <el-radio-group v-model="form.gender" :disabled="this.isDisable" @change="change_gender">
                <el-radio label="男"></el-radio>
                <el-radio label="女"></el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="电子邮箱" prop="email">
              <el-input v-model="form.email" @blur="checkout" :disabled="this.isDisable"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item label="个人描述">
              <el-input type="textarea" v-model="form.descr" @blur="checkout" :disabled="this.isDisable"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :offset="7" :span="8">
            <el-form-item v-if="!modifyMode">
              <el-button type="primary" size="mini" @click="checkModify">修改信息</el-button>
              <el-button type="info" size="mini" @click="back">返回</el-button>
            </el-form-item>
            <el-form-item v-else>
              <el-button type="primary" size="mini" @click="submitModify">确认修改</el-button>
              <el-button type="warning" size="mini" @click="reset">重置</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-main>
  </div>
</template>

<script>
import GetUrl from '../utils/GetURL'
import FormDataOperate from '../utils/FormDataOperate'

export default {
  data () {
    let validateEmail = (rule, value, callback) => {
      let rg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/
      if (!rg.test(value)) {
        callback(new Error('请输入正确的电子邮箱地址！'))
      } else {
        callback()
      }
    }
    let validateAge = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('请输入年龄'))
      }
      let rg = /^[0-9]*$/
      if (!rg.test(value + '')) {
        return callback(new Error('请输入数字值'))
      }
      if (value < 0 || value > 120) {
        return callback(new Error('年龄必须在0-120之间'))
      } else {
        return callback()
      }
    }
    return {
      active: '0',
      modifyMode: false,
      isDisable: true,
      username: '',
      tel_number: '',
      form: {
        fullname: '',
        age: 0,
        gender: '男',
        email: '',
        descr: ''
      },
      rules: {
        fullname: [
          { required: true, message: '请输入用户昵称', trigger: 'blur' },
          { min: 6, max: 15, message: '用户昵称长度需要在 6 到 15 个字符', trigger: 'blur' }
        ],
        age: [
          { validator: validateAge, trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入电子邮箱', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur' }
        ]
      }
    }
  },
  mounted () {
    this.username = sessionStorage.getItem('username')
    this.$axios({
      method: 'get',
      url: GetUrl('UserManage/getByUsername'),
      params: { 'username': this.username }
    }).then((res) => {
      if (!res.data.success) {
        this.$message({
          message: '网络未连接，请重试！',
          type: 'error',
          showClose: true
        })
      } else {
        this.tel_number = res.data.user_entry.tel_number
        this.form.fullname = res.data.user.fullname
        this.form.age = res.data.user.age
        this.form.gender = FormDataOperate.getGenderFromNumber(res.data.user.gender)
        this.form.email = res.data.user.email
        this.form.descr = res.data.user.descr
      }
    })
  },
  methods: {
    change_gender () {
      this.active = 2
    },
    checkout () {
      this.active = 2
    },
    checkModify () {
      this.active = 1
      this.modifyMode = true
      this.isDisable = false
    },
    back () {
      this.$message({
        message: '已返回主页！',
        showClose: true
      })
      this.$router.push('/')
    },
    submitModify () {
      this.$refs['userInfoForm'].validate(valid => {
        if (valid) {
          const url = GetUrl('UserManage/modifyInfo')
          let params = new URLSearchParams()
          params.append('username', this.username)
          params.append('gender', FormDataOperate.getNumberFromGender(this.form.gender))
          params.append('age', this.form.age)
          params.append('email', this.form.email)
          params.append('descr', this.form.descr)
          params.append('fullname', this.form.fullname)
          this.$axios({
            method: 'post',
            url: url,
            data: params
          }).then((res) => {
            if (res.data.success) {
              this.isDisable = true
              this.modifyMode = false
              this.$message({
                type: 'success',
                message: '修改成功！',
                showClose: true
              })
            } else {
              this.$message({
                type: 'error',
                message: '修改失败，请重试！',
                showClose: true
              })
            }
          })
        } else {
          this.$message({
            type: 'error',
            message: '请完善表单！',
            showClose: true
          })
        }
      })
    },
    reset () {
      this.$axios({
        method: 'get',
        url: GetUrl('UserManage/getByUsername'),
        params: { 'username': this.username }
      }).then((res) => {
        this.form.fullname = res.data.user.fullname
        this.form.age = res.data.user.age
        this.form.gender = FormDataOperate.getGenderFromNumber(res.data.user.gender)
        this.form.email = res.data.user.email
        this.form.descr = res.data.user.descr
      })
    }
  }
}
</script>

<style>
#verify-code-area > .el-row {
  margin-bottom: 20px;
}

.step {
  margin-top: 30px;
  margin-bottom: 30px;
}

.info {
  background-image: url(../assets/userinfo_background.png);
  background-size: cover;
  min-height: 620px;
}
</style>
