<template>
  <div class="main" id="main">
    <el-popover
      ref="normal"
      placement="top-start"
      title="普通会员(10元/月)"
      width="200"
      trigger="hover"
      content="普通会员，享有所有关卡免费玩特权。">
    </el-popover>
    <el-popover
      ref="excellent"
      placement="top-start"
      title="白金会员(30元/月)"
      width="200"
      trigger="hover"
      content="白金会员，享有所有关卡免费玩、多人游戏等特权。">
    </el-popover>
    <el-popover
      ref="super"
      placement="top-start"
      title="超级会员(45元/月)"
      width="200"
      trigger="hover"
      content="超级会员，享有所有关卡免费玩、多人游戏、游戏道具随便用等特权。">
    </el-popover>
    <el-col :offset="9" :span="13">
      <div class="dropping-texts">
        <div>挑战更多的关卡！</div>
        <div>畅玩自由模式！</div>
        <div>创建你自己的游戏！</div>
        <div>成为会员,加入我们！</div>
      </div>
    </el-col>
    <el-row v-if="memberInfo.isMember">
      <el-col :offset="10" :span="8">
        <h1><span class="fa fa-user-circle fa-1x"></span>&nbsp;尊贵的会员，您好！</h1>
        <h2><span class="fa fa-address-book fa-1x"></span>&nbsp;会员类型：{{memberInfo.memberName}}</h2>
        <h2><span class="fa fa-hand-o-up fa-1x"></span>&nbsp;开通时间：{{memberInfo.starttime}}</h2>
        <h2><span class="fa fa-hand-o-down fa-1x"></span>&nbsp;截止时间：{{memberInfo.endtime}}</h2>
      </el-col>
    </el-row>
    <el-form ref="form" class="form" :model="form" label-width="150px" @submit.prevent="onSubmit">
      <el-row>
        <el-col class="member-form" :offset="13" :span="12">
          <el-form-item label="用户名">
            <el-input v-model="form.username" prop="username" :disabled="true"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col class="member-form" :offset="13">
          <el-form-item label="会员类型">
            <el-radio-group v-model="form.membertype" @change="changeHandler">
              <el-radio v-popover:normal label="普通会员"></el-radio>
              <el-radio v-popover:excellent label="白金会员"></el-radio>
              <el-radio v-popover:super label="超级会员"></el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col class="member-form" :offset="13">
          <el-form-item label="购买时长">
            <el-radio-group v-model="form.time" @change="changeHandler">
              <el-radio label="1个月"></el-radio>
              <el-radio label="3个月"></el-radio>
              <el-radio label="6个月"></el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col class="member-form" :offset="13">
          <el-form-item label="支付方式" justify="center;">
            <el-radio-group v-model="form.resource">
              <el-radio label="支付宝"></el-radio>
              <el-radio label="微信"></el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col class="member-form" :offset="18">
          <p><img src="../assets/member/cash.png" height="5%" width="5%">总金额&nbsp;&nbsp;&nbsp;{{money}}&nbsp;&nbsp;元</p>
        </el-col>
      </el-row>
      <br> <br>
      <el-row>
        <el-col class="member-form" :offset="14">
          <el-form-item>
            <el-button type="primary" @click="submit" size="mini">购 买</el-button>
            <el-button type="warning" @click="back" size="mini">返 回</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog title="支付页面" :visible.sync="dialogFormVisible">
      <center>
        <p>扫描下方二维码进行支付</p>
        <img src="../assets/zfb.jpg" height="40%" width="40%" />
      </center>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="sub" size="mini">确 定</el-button>
        <el-button @click="cancel" size="mini">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import GetUrl from '../utils/GetURL'
import ElementApi from '../utils/ElementAPI'

export default {
  data () {
    return {
      form: {
        time: 0,
        username: '',
        resource: '',
        membertype: 0
      },
      money: 0,
      imgchoose: '',
      dialogFormVisible: false,
      isPaid: false,
      memberInfo: {
        isMember: false,
        memberName: '',
        starttime: '',
        endtime: ''
      }
    }
  },
  mounted: function () {
    this.form.username = sessionStorage.getItem('username')
    const url = GetUrl('UserManage/getMemberByUsername')
    this.$axios({
      method: 'get',
      url: url,
      params: {
        'username': this.form.username
      }
    }).then((res) => {
      if (res.data.success) {
        if (res.data.isMember) {
          this.memberInfo.isMember = true
          this.memberInfo.starttime = res.data.starttime
          this.memberInfo.endtime = res.data.endtime
          switch (res.data.priority) {
            case 1:
              this.memberInfo.memberName = '普通会员'
              break
            case 2:
              this.memberInfo.memberName = '白金会员'
              break
            case 3:
              this.memberInfo.memberName = '超级会员'
              break
          }
        }
      } else {
        ElementApi.message(this, '系统错误，请重试！', 'error')
      }
    })
  },
  methods: {
    getmonth () {
      if (this.form.time === '1个月') {
        return 1
      } else if (this.form.time === '3个月') {
        return 3
      } else if (this.form.time === '6个月') {
        return 6
      } else {
        return 0
      }
    },
    getmembertype () {
      if (this.form.membertype === '普通会员') {
        return 1
      } else if (this.form.membertype === '白金会员') {
        return 2
      } else if (this.form.membertype === '超级会员') {
        return 3
      } else {
        return 0
      }
    },
    getMoneyFromType () {
      switch (this.getmembertype()) {
        case 0:
          return 0
        case 1:
          return 10
        case 2:
          return 30
        case 3:
          return 45
      }
    },
    sub () {
      this.dialogFormVisible = false
      this.isPaid = true
      if (!this.isPaid) {
        return
      }
      this.$refs.form.validate(valid => {
        if (valid) {
          let username = this.form.username
          let month = this.getmonth()
          let type = this.getmembertype()
          let params = new URLSearchParams()
          params.append('username', username)
          params.append('month', month)
          params.append('type', type)
          this.$axios({
            method: 'post',
            url: GetUrl('UserManage/member'),
            data: params
          }).then((response) => {
            if (response.data.success) {
              this.$message({
                type: 'success',
                message: '充值成功',
                showClose: true
              })
              this.$destroy()
              this.$router.replace('/')
            } else {
              this.$message({
                type: 'error',
                message: '充值失败，请重试！',
                showClose: true
              })
            }
          })
        }
      })
    },
    cancel () {
      this.dialogFormVisible = false
      this.$message({
        type: 'warning',
        message: '支付已取消',
        showClose: true
      })
      this.isPaid = false
    },
    changeHandler () {
      this.money = this.getmonth() * this.getMoneyFromType()
    },
    submit () {
      if (this.getmonth() === 0) {
        this.$message({
          type: 'error',
          message: '请选择会员时长！',
          showClose: true
        })
        return
      }
      if (this.getmembertype() === 0) {
        this.$message({
          type: 'error',
          message: '请选择会员类型！',
          showClose: true
        })
        return
      }
      if (this.form.resource === '') {
        this.$message({
          type: 'error',
          message: '请选择支付方式！',
          showClose: true
        })
        return
      }
      this.dialogFormVisible = true
    },
    back () {
      this.$message({
        message: '已返回',
        showClose: true
      })
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 25px;
}

h2 {
  margin-top: 20px;
  font-size:20px;
}

.main {
  height: 100%;
  width: 100%;
  animation:bg 13s linear infinite;
  background-image: url(../assets/member_background.png);
  background-size: cover;
  min-height: 700px;
}
.member-form {
  margin-bottom: 20px;
}
.form {
  padding-top: 50px;
  width: 55%;
}
/*动态文字*/
.dropping-texts {
  margin-top: 40px;
  margin-bottom: 20px;
  display:inline-block;
  color:#7FCCF8;
  text-shadow: 0 0 1px currentColor,-1px -1px 1px #000,0 -1px 1px #000,1px -1px 1px #000,1px 0 1px #000,1px 1px 1px #000,0 1px 1px #000;
  -webkit-filter:url(#diff1);
  filter:url(#diff1);
  font-size: 50px;
  display: inline-block;
  font-family:"黑体";
  height: 80px;
}

.dropping-texts > div {
  font-size: 0px;
  opacity: 0;
  margin-left: -30px;
  position:absolute;
  font-weight: 300;
}

.dropping-texts > div:nth-child(1) {
  animation: roll 13s linear infinite 0s;
}
.dropping-texts > div:nth-child(2) {
  animation: roll 13s linear infinite 3s;
}
.dropping-texts > div:nth-child(3) {
  animation: roll 13s linear infinite 6s;
}
.dropping-texts > div:nth-child(4) {
  animation: roll 13s linear infinite 9s;
}

@keyframes roll {
  0% {
    font-size: 0px;
    opacity: 0;
    margin-left: -30px;
    margin-top: 0px;
    transform: rotate(-25deg);
  }
  3% {
    opacity: 1;
    transform: rotate(0deg);
  }
  5% {
    font-size:inherit;
    opacity: 1;
    margin-left: 0px;
    margin-top: 0px;
  }
  20% {
    font-size:inherit;
    opacity: 1;
    margin-left: 0px;
    margin-top: 0px;
    transform: rotate(0deg);
  }
  27% {
    font-size: 0px;
    opacity: 0.5;
    margin-left: 20px;
    margin-top: 100px;
  }
  100% {
    font-size: 0px;
    opacity: 0;
    margin-left: -30px;
    margin-top: 0px;
    transform: rotate(15deg);
  }

}
/* @keyframes bg {
  0% {background: #F6E2FE;}
  3% {background: #F6E2FE;}
  22% {background: #D9D5FD;}
  26% {background: #CDEDFF;}
  40% {background: #CDEDFF;}
  45% {background: #DCFFEF;}
  50% {background: #F2FDDF;}
  55% {background: #FFFAD5;}
  69% {background: #FFF0C4;}
  70% {background: #FEE4C3;}
  83% {background: #FFDCDC;}
  90% {background: #FFDCDC;}
  95% {background: #FFDCF5;}
  95% {background: #FFE3FF;}
} */
</style>
