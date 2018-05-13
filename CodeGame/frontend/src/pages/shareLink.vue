<template>
  <body>
    <div class="header">
      <h1>你的好友已经完成了该关卡,快来试试吧!</h1>
    </div>
    <div class="w3-main">
      <div class="agile-info">
        <h2 v-if="share_obj.isFree === 1">自由模式</h2>
        <h2 v-else>闯关模式</h2>
        <h3>地图编号：{{share_obj.map_id}}</h3>
        <p>分享用户名：{{share_obj.username}}</p>
        <div class="social">
          <ul>
            <li><a href="#" class="link facebook"><span class="fa fa-thumbs-o-up fa-1"></span></a></li>
            <li><a href="#" class="link twitter" target="_parent"><span class="fa fa-twitter fa-1x"></span></a></li>
            <li><a href="#" class="link google-plus" target="_parent"><span class="fa fa-google-plus-square fa-1x"></span></a></li>
            <div class="clear"></div>
          </ul>
        </div>
        <el-button @click="back" icon='arrow-left' class="pan-back-btn" type="primary">立即试玩！</el-button>
      </div>
    </div>
  </body>
</template>

<script>
import errGif from '../assets/shareLink.gif'
import GetUrl from '../utils/GetURL'
import CodeMirror from 'codemirror'
import 'codemirror/addon/lint/lint.css'
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/rubyblue.css'
import 'codemirror/mode/lua/lua'
import 'codemirror/addon/lint/lint'

export default {
  data () {
    return {
      errGif: errGif + '?' + new Date(),
      id: 0,
      workspace: null,
      luaEditor: false,
      share_obj: {
        map_id: 0,
        level: 0,
        isFree: 0,
        code: '',
        username: ''
      }
    }
  },
  mounted () {
    this.id = parseInt(this.$route.params.id)
    this.$axios({
      method: 'get',
      url: GetUrl('ChallengeMode/getShareLinkById'),
      params: {
        'id': this.id
      }
    }).then((res) => {
      this.share_obj.map_id = res.data.share_obj.map_id
      this.share_obj.isFree = res.data.share_obj.isfree
      this.share_obj.code = res.data.share_obj.solution_code
      this.share_obj.username = res.data.username
      this.share_obj.level = res.data.level
      this.luaEditor.setValue(this.share_obj.code)
    })
    this.luaEditor = CodeMirror.fromTextArea(this.$refs.textarea, {
      lineNumbers: true,
      mode: 'lua',
      theme: 'rubyblue',
      lint: true,
      smartIndent: true
    })
  },
  methods: {
    back () {
      let playUrl = '/'
      if (this.share_obj.isFree === 0) {
        playUrl += 'blockly/'
        playUrl += this.share_obj.level
      } else {
        playUrl += 'freeModePlay/'
        playUrl += this.share_obj.map_id
      }
      this.$router.push({
        path: playUrl
      })
      location.reload()
    }
  }
}
</script>

<style scoped>
  html,
  body,
  div,
  span,
  applet,
  object,
  iframe,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  p,
  blockquote,
  pre,
  a,
  abbr,
  acronym,
  address,
  big,
  cite,
  code,
  del,
  dfn,
  em,
  img,
  ins,
  kbd,
  q,
  s,
  samp,
  small,
  strike,
  strong,
  sub,
  sup,
  tt,
  var,
  b,
  u,
  i,
  dl,
  dt,
  dd,
  ol,
  nav ul,
  nav li,
  fieldset,
  form,
  label,
  legend,
  table,
  caption,
  tbody,
  tfoot,
  thead,
  tr,
  th,
  td,
  article,
  aside,
  canvas,
  details,
  embed,
  figure,
  figcaption,
  footer,
  header,
  hgroup,
  menu,
  nav,
  output,
  ruby,
  section,
  summary,
  time,
  mark,
  audio,
  video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
  }

  article,
  aside,
  details,
  figcaption,
  figure,
  footer,
  header,
  hgroup,
  menu,
  nav,
  section {
    display: block;
  }

  ol,
  ul {
    list-style: none;
    margin: 0px 0px 0px 0px;
    padding: 0px;
  }

  blockquote,
  q {
    quotes: none;
  }

  blockquote:before,
  blockquote:after,
  q:before,
  q:after {
    content: '';
    content: none;
  }

  table {
    border-collapse: collapse;
    border-spacing: 0;
  }

  a {
    text-decoration: none;
  }

  .txt-rt {
    text-align: right;
  }

  .txt-lt {
    text-align: left;
  }

  .txt-center {
    text-align: center;
  }

  .float-rt {
    float: right;
  }

  .float-lt {
    float: left;
  }

  .clear {
    clear: both;
  }

  .pos-relative {
    position: relative;
  }

  .pos-absolute {
    position: absolute;
  }

  .vertical-base {
    vertical-align: baseline;
  }

  .vertical-top {
    vertical-align: top;
  }

  nav.vertical ul li {
    display: block;
  }

  nav.horizontal ul li {
    display: inline-block;
  }

  img {
    max-width: 100%;
  }

  body p,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-family: 'Open Sans', sans-serif;
  }

  body {
    background: #e64c65;
    text-align: center;
    height: 680px;
    padding-bottom: 20px;
  }

  .header h1 {
    font-size: 51px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: white;
    font-weight: 100;
    margin: 0.0em 0em;
    padding-top: 2.0em;
  }

  .w3-main {
    background: #f76a81;
    width: 53%;
    margin: 2em auto 0px auto;
    -webkit-box-shadow: -2px 11px 32px -13px rgba(0, 0, 0, 0.45);
    -moz-box-shadow: -2px 11px 32px -13px rgba(0, 0, 0, 0.45);
    box-shadow: -2px 11px 32px -13px rgba(0, 0, 0, 0.45);
    padding-bottom: 0px;
  }

  .agile-info {
    padding: 100px 0px 50px 0px;
  }

  .agile-info h2 {
    font-size: 5em;
    color: black;
    line-height: 1;
    font-weight: 100;
    letter-spacing: 15px;
  }

  .agile-info h3 {
    font-size: 38px;
    text-transform: uppercase;
    color: white;
    line-height: 1.5;
    font-weight: 100;
    letter-spacing: 2px;
    margin-top: 12px;
  }

  .agile-info p {
    font-size: 18px;
    color: rgba(0, 0, 0, 0.71);
    text-transform: capitalize;
    letter-spacing: 6px;
    margin-bottom: 46px;
  }

  .agile-info a {
    font-size: 15px;
    text-transform: uppercase;
    color: white;
    border: 1px solid #3b5998;
    padding: 10px 40px;
    border-radius: 20px;
    letter-spacing: 1px;
    display: inline-block;
    margin-top: 8px;
    background: #3b5998;
    font-family: 'Open Sans', sans-serif;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -o-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -ms-transition: 0.5s all;
  }

  .agile-info a:hover {
    background: #1f3c7b;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -o-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -ms-transition: 0.5s all;
  }

  .social {
    text-align: center;
    transform: translateY(-50%);
  }

  .social li {
    display: inline;
    margin-right: 7px;
  }

  .social .link {
    display: inline-block;
    vertical-align: middle;
    position: relative;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: 2px dashed white;
    background-clip: content-box;
    padding: 4px;
    transition: .5s;
    color: #D7D0BE;
    margin-left: 10px;
    margin-right: 8px;
    text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2), 0 1px 0 rgba(255, 255, 255, 0.2);
    font-size: 16px;
  }

  .social .link span {
    display: block;
    position: absolute;
    text-align: center;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .social .link:hover {
    color: white;
    transform: translateX(0px) rotate(360deg);
  }

  .social .link.google-plus {
    background-color: tomato;
    color: white;
  }

  .social .link.twitter {
    background-color: #00ACEE;
    color: white;
  }

  .social .link.facebook {
    background-color: #3B5998;
    color: white;
  }

  .footer-w3l p {
    margin: 2.8em 0em;
    color: #fff;
    font-size: 15px;
    font-weight: 100;
    letter-spacing: 2px;
  }

  .footer-w3l a {
    color: #fff;
  }

  .footer-w3l a:hover {
    color: rgb(36, 228, 219);
    text-decoration: underline;
  }

  @media(max-width:1440px) {
    .w3-main {
      width: 55%;
    }
  }

  @media(max-width:1366px) {
    .w3-main {
      width: 58%;
    }
  }

  @media(max-width:1280px) {
    .w3-main {
      width: 64%;
    }
  }

  @media(max-width:1024px) {
    .w3-main {
      width: 76%;
    }
  }

  @media(max-width:991px) {
    .w3-main {
      width: 76%;
    }
  }

  @media(max-width:800px) {
    .w3-main {
      width: 90%;
    }
    .agile-info {
      padding: 46px 0px 0px 0px;
    }
  }

  @media(max-width:768px) {
    .w3-main {
      width: 91%;
      margin: 4em auto 0px 0px;
    }
    .agile-info {
      padding: 87px 0px 0px 0px;
    }
  }

  @media(max-width:736px) {
    .w3-main {
      width: 94%;
      margin: 2em auto 0 0;
    }
    .agile-info {
      padding: 40px 0px 0px 0px;
    }
    .header h1 {
      margin: 0.5em 0em;
    }
  }

  @media(max-width:667px) {
    .agile-info h2 {
      font-size: 11em;
    }
    .agile-info {
      padding: 35px 0px 0px 0px;
    }
    .header h1 {
      margin: 0.4em 0em;
    }
  }

  @media(max-width:640px) {
    .header h1 {
      font-size: 48px;
    }
  }

  @media(max-width:600px) {
    .header h1 {
      letter-spacing: 8px;
      font-size: 44px;
    }
    .w3-main {
      margin: 2em auto 0 0;
    }
    .agile-info h2 {
      font-size: 10em;
    }
    .footer-w3l p {
      margin: 2em 0.8em;
      line-height: 26px;
    }
  }

  @media(max-width:480px) {
    .header h1 {
      letter-spacing: 6px;
      font-size: 40px;
    }
    .agile-info h2 {
      font-size: 9em;
    }
    .agile-info h3 {
      font-size: 28px;
    }
    .agile-info p {
      font-size: 17px;
    }
    .agile-info a {
      margin-top: 0px;
    }
    .footer-w3l p {
      margin: 1.9em 0.8em;
      line-height: 27px;
    }
  }

  @media(max-width:414px) {
    .header h1 {
      letter-spacing: 5px;
      font-size: 35px;
      margin-top: 28px;
    }
    .w3-main {
      margin: 2em auto 0 0;
    }
    .agile-info h2 {
      font-size: 8em;
    }
    .agile-info {
      padding: 58px 0px 0px 0px;
    }
    .footer-w3l p {
      margin: 1.4em 0.7em;
      line-height: 27px;
    }
  }

  @media(max-width:384px) {
    .header h1 {
      letter-spacing: 3px;
      font-size: 35px;
      margin-top: 12px;
    }
    .w3-main {
      margin: 2em auto 0px 0px;
    }
    .agile-info h2 {
      font-size: 7em;
      letter-spacing: 13px;
    }
    .agile-info {
      padding: 47px 0px 0px 0px;
    }
    .footer-w3l p {
      margin: 1.4em 0.3em;
      line-height: 23px;
    }
  }

  @media(max-width:375px) {
    .header h1 {
      font-size: 36px;
      margin-top: 16px;
    }
  }

  @media(max-width:320px) {
    .header h1 {
      font-size: 30px;
      margin-top: 16px;
      letter-spacing: 2px;
    }
    .agile-info h2 {
      font-size: 6em;
      letter-spacing: 12px;
    }
    .agile-info {
      padding: 20px 0px 0px 0px;
    }
    .agile-info h3 {
      font-size: 26px;
    }
    .agile-info p {
      font-size: 16px;
      letter-spacing: 3px;
    }
  }
</style>
