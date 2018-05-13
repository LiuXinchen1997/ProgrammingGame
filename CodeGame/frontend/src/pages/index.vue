<template>
  <div id="app">
   <v-app light>
    <v-content>
      <section>
        <v-parallax src="../../static/assets/city.png" height="650">
          <v-layout
            column
            align-center
            justify-center
            class="white--text"
          >
            <img src="../../static/assets/coderunner.png" alt="Vuetify.js" height="300">
            <div class="home-page1">
              <div class="sandbox sandbox-correct-pronounciation">
                <h2 class="heading-correct-pronounciation">
                  欢迎访问
                  <em>卓越创客</em>
                  <br/>
                  明星产品：在线编程游戏
                </h2>
              </div>
            </div>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12 sm4 class="my-3">
            <div class="text-xs-center">
              <h2 class="headline">CodeRunner</h2>
              <span class="subheading">
                在线编程游戏
              </span>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">color_lens</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">独特的3D游戏</div>
                    </v-card-title>
                    <v-card-text>
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">不一样的编程体验</div>
                    </v-card-title>
                    <v-card-text>
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">有趣的创建模式</div>
                    </v-card-title>
                    <v-card-text>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>

      <section>
        <v-parallax src="../../static/assets/game.png" height="580">
          <v-layout column align-center justify-center>
            <div class="headline white--text mb-3 text-xs-center"></div>
            <div class="foo">
              <p>
              <span class="letter" data-letter="1">1</span>
              <span class="letter" data-letter="0">0</span>
              <span class="letter" data-letter="个">个</span>
              <span class="letter" data-letter="挑">挑</span>
              <span class="letter" data-letter="战">战</span>
              <span class="letter" data-letter="关">关</span>
              <span class="letter" data-letter="卡">卡</span>
              </p>
              <p>
              <span class="letter" data-letter="无">无</span>
              <span class="letter" data-letter="限">限</span>
              <span class="letter" data-letter="的">的</span>
              <span class="letter" data-letter="自">自</span>
              <span class="letter" data-letter="由">由</span>
              <span class="letter" data-letter="关">关</span>
              <span class="letter" data-letter="卡">卡</span>
              </p>
              <span class="letter" data-letter="等">等</span>
              <span class="letter" data-letter="你">你</span>
              <span class="letter" data-letter="来">来</span>
              <span class="letter" data-letter="玩">玩</span>
            </div>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-container grid-list-xl>
          <v-layout row wrap justify-center class="my-5">
            <v-flex xs12 sm4>
              <v-card class="elevation-0 transparent">
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">卓越创客小组</div>
                </v-card-title>
                <v-card-text class="member">
                  <p>后台：刘昕宸 叶海松</p>
                  <p>前台：谷昊远 刘昕宸 费志伟 叶海松</p>
                  <p>游戏制作：周昊楠</p>
                  <p>关卡设计：费志伟</p>
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 sm4 offset-sm1>
              <v-card class="elevation-0 transparent">
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">联系我们</div>
                </v-card-title>
                <v-card-text>
                  如果你有好的建议或意见可以通过以下方式联系
                </v-card-text>
                <v-list class="transparent">
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-icon class="blue--text text--lighten-2">phone</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                      <v-list-tile-title>684497950</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-icon class="blue--text text--lighten-2">place</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                      <v-list-tile-title>HFUT,CN</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-icon class="blue--text text--lighten-2">email</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                      <v-list-tile-title>634428559@qq.com</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </section>
    </v-content>
  </v-app>
 </div>
</template>

<script>
import 'vuetify/dist/vuetify.min.css'
export default {

}
</script>

<style>
.headline {
  font-size: 35px;
}
.member {
  font-size: 1.5em;
}
.heading-correct-pronounciation {
  margin: auto;
  text-align: center;
  position: relative;
}
h2.heading-correct-pronounciation {
  color: white;
  font-family: 'Cardo', serif;
  font-size: 1.5em;
  font-weight: normal;
  font-style: italic;
  letter-spacing: 0.3em;
  line-height: 2.2em;
}
em {
  font-family: 'EB Garamond', serif;
  font-size: 3.5em;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  display: block;
  font-style: normal;
  padding-top: 0.3em;
  text-shadow: 0.07em 0.07em 0 rgba(0, 0, 0, 0.2);
}
div.foo {
  width: 90%;
  padding-top: 50px;
  text-align: center;
}
.letter {
  display: inline-block;
  font-weight: 900;
  font-size: 4.5em;
  margin: 0.2em;
  position: relative;
  color: grey;
  transform-style: preserve-3d;
  perspective: 400;
  z-index: 1;
}
.letter:before, .letter:after {
  position:absolute;
  content: attr(data-letter);
  transform-origin: top left;
  top: 0;
  left: 0;
}
.letter, .letter:before, .letter:after {
  transition: all 0.3s ease-in-out;
}
.letter:before {
  color: #fff;
  text-shadow:
    -1px 0px 1px rgba(255,255,255,.8),
    1px 0px 1px rgba(0,0,0,.8);
  z-index: 3;
  transform:
    rotateX(0deg)
    rotateY(-15deg)
    rotateZ(0deg);
}
.letter:after {
  color: rgba(0,0,0,.11);
  z-index: 2;
  transform:
    scale(1.08,1)
    rotateX(0deg)
    rotateY(0deg)
    rotateZ(0deg)
    skew(0deg,1deg);
}
.letter:hover:before {
  color: #fafafa;
  transform:
    rotateX(0deg)
    rotateY(-40deg)
    rotateZ(0deg);
}
.letter:hover:after {
  transform:
    scale(1.08,1)
    rotateX(0deg)
    rotateY(40deg)
    rotateZ(0deg)
    skew(0deg,22deg);
}
</style>
