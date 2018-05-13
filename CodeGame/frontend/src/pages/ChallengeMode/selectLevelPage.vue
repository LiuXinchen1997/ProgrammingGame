<template>
  <div :style ="global" class="main-box">
    <el-row class="schedule_space">
      <el-col :offset="6" :span="2">
        <p>当前闯关进度：</p>
      </el-col>
      <el-col :span="8">
        <el-progress :text-inside="true" :stroke-width="23" :percentage="maxLevelPer" color="rgb(163,106,227)"></el-progress>
      </el-col>
    </el-row>
    <el-row class="space">
      <el-col :offset="10" :span="7">
        <h1 class="title"><i class="el-icon-edit"></i>请选择关卡</h1>
      </el-col>
    </el-row>
    <el-row class="card_space">
      <el-col>
        <el-carousel :interval="4000" type="card" height="353px" @change="changeItem">
          <el-carousel-item v-for="item in 10" :key="item">
            <el-container>
              <el-aside class="el-aside" height="100%" width="30%">
                <el-row class="sub-space">
                  <el-col :offset="8" :span="8">
                    <h2 class="sub-title">第{{item}}关</h2>
                  </el-col>
                </el-row>
                <el-row class="sub-space">
                  <el-col>
                    <h2 class="title_tip"><hr><i class="el-icon-message"></i>&nbsp;关卡提示&nbsp;</h2>
                  </el-col>
                </el-row>
                <el-row class="sub-space">
                  <el-col>
                    <p class="sub-tip">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{curHint}}</p><hr>
                  </el-col>
                </el-row>
                <el-row class="sub-space">
                  <el-col>
                    <h2 class="title_info"><i class="el-icon-document">&nbsp;关卡描述</i></h2>
                  </el-col>
                </el-row>
                <el-row class="sub-space">
                  <el-col>
                    <p class="sub-info">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{curDescr}}</p><hr>
                  </el-col>
                </el-row>
                <el-row class="sub-space">
                  <el-col :offset="7" :span="2">
                    <el-button @click="play(item)" type="primary" size="mini">进入游戏</el-button>
                  </el-col>
                </el-row>
              </el-aside>
              <el-main class="el-main" height="380px">
                <img v-if="item === 1" :src='image1'/>
                <img v-if="item === 2" :src='image2'/>
                <img v-if="item === 3" :src='image3'/>
                <img v-if="item === 4" :src='image4'/>
                <img v-if="item === 5" :src='image5'/>
                <img v-if="item === 6" :src='image6'/>
                <img v-if="item === 7" :src='image7'/>
                <img v-if="item === 8" :src='image8'/>
                <img v-if="item === 9" :src='image9'/>
                <img v-if="item === 10" :src='image10'/>
              </el-main>
            </el-container>
          </el-carousel-item>
        </el-carousel>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import GetUrl from '../../utils/GetURL'
import ElementApi from '../../utils/ElementAPI'

export default {
  data () {
    return {
      levelCount: 10,
      global: {
        backgroundImage: 'url(' + require('../../assets/userinfo_background.png') + ')',
        backgroundRepeat: 'no-repeat',
        backgroundSize: '100% 630px'
      },
      username: '',
      maxLevel: 1,
      maxLevelPer: 10,
      hints: [],
      descrs: [],
      curHint: '',
      curDescr: '',
      image1: require('../../assets/ChallengeMode/1.jpg'),
      image2: require('../../assets/ChallengeMode/2.jpg'),
      image3: require('../../assets/ChallengeMode/3.jpg'),
      image4: require('../../assets/ChallengeMode/4.jpg'),
      image5: require('../../assets/ChallengeMode/5.jpg'),
      image6: require('../../assets/ChallengeMode/6.jpg'),
      image7: require('../../assets/ChallengeMode/7.jpg'),
      image8: require('../../assets/ChallengeMode/8.jpg'),
      image9: require('../../assets/ChallengeMode/9.jpg'),
      image10: require('../../assets/ChallengeMode/10.jpg')
    }
  },
  mounted () {
    this.username = sessionStorage.getItem('username')
    this.maxLevel = 5
    if (!this.username) {
      this.username = ''
    }

    let url = GetUrl('ChallengeMode/getAllLevels')
    this.$axios({
      method: 'get',
      url: url
    }).then((res) => {
      if (res.data.success) {
        this.levelCount = res.data.hints.length
        this.hints = res.data.hints
        this.descrs = res.data.descrs
        this.curHint = this.hints[0]
        this.curDescr = this.descrs[0]
      }
    })

    if (this.username === '') {
      return
    }
    url = GetUrl('ChallengeMode/getLevelByUsername')
    this.$axios({
      method: 'get',
      url: url,
      params: {
        'username': this.username
      }
    }).then((res) => {
      if (res.data.success) {
        this.maxLevel = res.data.level
        this.maxLevelPer = Math.ceil((this.maxLevel + 0.0) * 100 / this.levelCount)
      } else {
        ElementApi.message(this, '您没有联网，请重试！', 'error')
      }
    })
  },
  methods: {
    play: function (item) {
      if (this.username === '' && item > 5) {
        ElementApi.message(this, '登录账号，才可以享受更多精彩关卡呦~', 'error')
        return
      }
      if (item > this.maxLevel) {
        ElementApi.message(this, '您还未解锁当前关卡~', 'error')
        return
      }
      let str = '/blockly/' + item
      this.$router.push(str)
    },
    changeItem: function (from) {
      let cur = from + 1
      this.curHint = this.hints[cur - 1]
      this.curDescr = this.descrs[cur - 1]
    }
  }
}
</script>

<style scoped>
.title {
  font-weight: 700;
  color: #257F6D;
  font-size: 25px;
  padding-top: 15px;
  padding-bottom: 15px;
}
.schedule_space {
  padding-top: 55px;
}
.card_space {
  margin-left: 3%;
  width: 95%;
}
.space {
  padding-top: 20px;
}
.main-box {
  height: 630px;
  width: 100%;
}
.sub-space {
  padding-left: 8px;
  padding-top: 10px;
}
.sub-info {
  min-height: 60px;
}
.sub-tip {
  min-height: 60px;
}
.sub-title {
  margin-top: 12px;
  font-size: 18px;
  font-family: "Hiragino Sans GB";
}
.text {
  font-size: 14px;
  font-family: "PingFang SC";
}
.el-main img {
  height: 300px;
  width: 100%;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
.el-carousel__item:nth-child(2n) {
  background: linear-gradient(#C8F8EF, #4EA6A1);
}
.el-carousel__item:nth-child(2n+1) {
  background: linear-gradient(#99DAAB, #BCF8FA);
}
</style>
