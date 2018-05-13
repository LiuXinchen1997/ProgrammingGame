<template>
  <div>
    <div class="app-head">
      <div class="app-head-inner">
        <img src="../assets/logo.png" id="logo-img">
        <div class="head-nav">
          <ul class="nav-list">
            <li @click="index" v-if="username !== ''"><i class="el-icon-view"></i>&nbsp;欢迎您，{{username}}！</li>
            <li v-if="username !== ''" class="nav-pile">|</li>
            <li v-if="username !== ''" @click="quit">退出</li>
            <li v-if="username === ''" @click="login">登录</li>
            <li class="nav-pile">|</li>
            <li v-if="username === ''" @click="register">注册</li>
            <li v-if="username === ''" class="nav-pile">|</li>
            <li v-if="username === ''" @click="tryOn">我要试玩！</li>
            <li v-if="username === ''" class="nav-pile">|</li>
            <li @click="about">关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="app-content">
      <transition :name="transitionName">
        <router-view></router-view>
      </transition>
    </div>
    <div class="app-foot">
      <p>© 2018 卓越创客 MIT</p>
    </div>
  </div>
</template>

<script>
import navmenu from '../components/navmenu'
import ElementApi from '../utils/ElementAPI'
export default {
  data () {
    return {
      username: '',
      transitionName: ''
    }
  },
  components: {
    'navmenu': navmenu
  },
  mounted () {
    this.username = sessionStorage.getItem('username')
    if (!this.username) {
      this.username = ''
    }
  },
  beforeUpdate () {
    this.username = sessionStorage.getItem('username')
    if (!this.username) {
      this.username = ''
    }
  },
  methods: {
    index: function () {
      this.$router.replace('/')
    },
    quit: function () {
      ElementApi.message(this, '退出成功！', 'success')
      sessionStorage.removeItem('username')
      this.$router.push({name: 'login'})
      location.reload()
    },
    login: function () {
      this.$router.push({name: 'login'})
      location.reload()
    },
    register: function () {
      this.$router.replace('/register')
      location.reload()
    },
    tryOn: function () {
      this.$router.push('/')
      location.reload()
    },
    about: function () {
    }
  },
  watch: {
    '$route' (to, from) {
      const toDepth = to.path.split('/').length
      const fromDepth = from.path.split('/').length
      this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
    }
  }
}
</script>

<style>
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
  display: block;
}
body {
  line-height: 1;
}
ol, ul {
  list-style: none;
}
blockquote, q {
  quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
  content: '';
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
a {
  color: inherit;
  text-decoration: none;
}
body {
  background: #f0f2f5;
  font-family: "Helvetica Neue",Helvetica,Arial,"Hiragino Sans GB","Hiragino Sans GB W3","Microsoft YaHei UI","Microsoft YaHei","WenQuanYi Micro Hei",sans-serif;
  font-size: 14px;
  color: #444;
}
.app-head {
  background: #8CD3FB;
  color: #b2b2b2;
  height: 90px;
  line-height: 90px;
  width: 100%;
}
.app-head-inner {
  width: 1200px;
  margin: 0 auto;
}
.head-logo {
  float: left;
}
.app-head-inner img {
  width: 50px;
  margin-top: 20px;
}
#logo-img {
  width: 120px;
  height: 60px;
}
.head-nav {
  float: right;
  color: #5B5F61;
  font-size: 17px;
}
.head-nav ul {
  overflow: hidden;
}
.head-nav li {
  cursor: pointer;
  float: left;
}
.nav-pile {
  padding: 0 10px;
}
.app-foot {
  text-align: center;
  height: 80px;
  width: 100%;
  line-height: 80px;
  background: #D1EAF8;
  clear: both;
}
.container {
  width: 1200px;
  margin: 0 auto;
}
.hr {
  height: 1px;
  width: 100%;
  background: #ddd;
}

.button:hover {
  background: #4fc08d;
}
.g-form-line {
  padding: 15px 0;
}
.g-form-label {
  width: 100px;
  font-size: 16px;
  display: inline-block;
}
.g-form-input {
  display: inline-block;
}
.g-form-input input {
  height: 30px;
  width: 200px;
  line-height: 30px;
  vertical-align: middle;
  padding: 0 10px;
  border: 1px solid #ccc;
}
.g-form-btn {
  padding-left: 100px;
}
.g-form-error {
  color: red;
  padding-left: 15px;
}
</style>
