<template>
  <div id="main-area">
    <el-row type="flex" class="row-bg">
    <div id="game-area">
      <div class="webgl-content">
        <div id="unity-container" class="unity-style"></div>
        <div id="cache" v-show="false"></div>
        <div id="res" v-show="false">false</div>
        <button id="trigger" @click="getMapData" v-show="false"></button>
      </div>
    </div>
    <div class="blockly-area">
      <div id="blockly-div">
      </div>
      <xml id="toolbox" ref="toolbox">
        <category name="Core">
          <category name="Control">
            <block type="controls_if"></block>
            <block type="controls_whileUntil"></block>
          </category>
          <category name="Logic">
            <block type="logic_compare"></block>
            <block type="logic_operation"></block>
            <block type="logic_boolean"></block>
            <block type="logic_negate"></block>
          </category>
          <category name="Math">
            <block type="math_number"></block>
          </category>
          <category name="text">
            <block type="text"></block>
            <block type="text_print"></block>
          </category>
        </category>
        <category name="Custom">
          <block type="WalkForward"></block>
          <block type="TurnLeft"></block>
          <block type="TurnRight"></block>
          <block type="PickUp"></block>
          <block type="PutDown"></block>
          <block type="Say"></block>
          <block type="FrontObjIs"></block>
        </category>
      </xml>
    </div>
    <div id="code-area">
      <textarea id="code-div" ref="textarea" v-model="code">
      </textarea>
        <el-button class="btn-row" @click="run" :disabled="isRun" type="primary" size="small">运行!</el-button>&nbsp;&nbsp;
        <el-button class="btn-row" @click="restart" type="warning" size="small">重新开始</el-button>&nbsp;&nbsp;
        <el-button class="btn-nextlevel" @click="finish" type="success" size="small">完成</el-button>&nbsp;&nbsp;
        <el-button size="small" type="info" @click="back">返回</el-button>
    </div>
    </el-row>
    <el-dialog title="提示" :visible.sync="dialogVisible" width="40%" :before-close="handleClose">
      <div class="link">
        <center>
          <span>恭喜您成功过关，分享下方链接给你的朋友！</span>
          <p id="linkurl">{{shareUrl}}</p>
        </center>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="finish2">完成</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import Vue from 'vue'
import Blockly from 'node-blockly/browser'
import En from 'node-blockly/lib/i18n/en'
import CodeMirror from 'codemirror'
import 'codemirror/addon/lint/lint.css'
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/rubyblue.css'
import 'codemirror/mode/lua/lua'
import 'codemirror/addon/lint/lint'
import ElementApi from '../utils/ElementAPI'
import GetUrl from '../utils/GetURL'
Blockly.setLocale(En)

Blockly.Blocks['WalkForward'] = {
  init: function () {
    this.jsonInit({
      message0: 'WalkForward %1',
      args0: [
        {
          type: 'field_dropdown',
          name: 'Num',
          options: [
            [
              '1',
              '1'
            ],
            [
              '2',
              '2'
            ],
            [
              '3',
              '3'
            ],
            [
              '4',
              '4'
            ],
            [
              '5',
              '5'
            ],
            [
              '6',
              '6'
            ],
            [
              '7',
              '7'
            ],
            [
              '8',
              '8'
            ],
            [
              '9',
              '9'
            ],
            [
              '10',
              '10'
            ],
            [
              '11',
              '11'
            ],
            [
              '12',
              '12'
            ]
          ]
        }
      ],
      previousStatement: null,
      nextStatement: null,
      colour: 160,
      tooltip: '拖动我前进哦~',
      helpUrl: 'http://www.w3schools.com/jsref/jsref_length_string.asp'
    })
  }
}
Blockly.Lua['WalkForward'] = function (block) {
  // String or array length.
  var DropdownObject = block.getFieldValue('Num')
  var code = 'me:WalkForward(' + DropdownObject + ')\n'
  return code
}

Blockly.Blocks['TurnLeft'] = {
  init: function () {
    this.jsonInit({
      type: 'TurnLeft',
      message0: 'TurnLeft',
      previousStatement: null,
      nextStatement: null,
      colour: 160,
      tooltip: '拖动我左转哦~',
      helpUrl: ''
    })
  }
}
Blockly.Lua['TurnLeft'] = function (block) {
  // String or array length.
  var code = 'me:TurnLeft()\n'
  return code
}

Blockly.Blocks['TurnRight'] = {
  init: function () {
    this.jsonInit({
      type: 'TurnRight',
      message0: 'TurnRight',
      previousStatement: null,
      nextStatement: null,
      colour: 160,
      tooltip: '拖动我右转哦~',
      helpUrl: ''
    })
  }
}
Blockly.Lua['TurnRight'] = function (block) {
  // String or array length.
  var code = 'me:TurnRight()\n'
  return code
}

Blockly.Blocks['PickUp'] = {
  init: function () {
    this.jsonInit({
      type: 'PickUp',
      message0: 'PickUp',
      previousStatement: null,
      nextStatement: null,
      colour: 160,
      tooltip: '拖动我捡起箱子哦~',
      helpUrl: ''
    })
  }
}
Blockly.Lua['PickUp'] = function (block) {
  // String or array length.
  var code = 'me:PickUp()\n'
  return code
}

Blockly.Blocks['PutDown'] = {
  init: function () {
    this.jsonInit({
      type: 'PutDown',
      message0: 'PutDown',
      previousStatement: null,
      nextStatement: null,
      colour: 160,
      tooltip: '拖动我放下箱子哦~',
      helpUrl: ''
    })
  }
}
Blockly.Lua['PutDown'] = function (block) {
  // String or array length.
  var code = 'me:PutDown()\n'
  return code
}

Blockly.Blocks['Say'] = {
  init: function () {
    this.jsonInit({
      message0: 'say %1',
      args0: [
        {
          type: 'field_dropdown',
          name: 'Object',
          options: [
            [
              '墙',
              'wall'
            ],
            [
              '石头',
              'stone'
            ],
            [
              '箱子',
              'box'
            ],
            [
              '一次性门',
              'onceDoor'
            ],
            [
              '按钮',
              'button'
            ],
            [
              '普通门',
              'door'
            ],
            [
              '激光发射器',
              'layser'
            ],
            [
              '花坛',
              'ironBox'
            ]
          ]
        }
      ],
      previousStatement: null,
      nextStatement: null,
      colour: 160,
      tooltip: '选择查看前面的物体哦~',
      helpUrl: ''
    })
  }
}
Blockly.Lua['Say'] = function (block) {
  // String or array length.
  var DropdownObject = block.getFieldValue('Object')
  var code = 'me:Say("There is a ' + DropdownObject + '")\n'
  return code
}

Blockly.Blocks['FrontObjIs'] = {
  init: function () {
    this.jsonInit({
      message0: 'FrontObjIs %1',
      args0: [
        {
          type: 'field_dropdown',
          name: 'Object',
          options: [
            [
              '墙',
              'wall'
            ],
            [
              '石头',
              'stone'
            ],
            [
              '箱子',
              'box'
            ],
            [
              '一次性门',
              'onceDoor'
            ],
            [
              '按钮',
              'button'
            ],
            [
              '普通门',
              'door'
            ],
            [
              '下激光发射器',
              'upLaser'
            ],
            [
              '右激光发射器',
              'rightLaser'
            ],
            [
              '花坛',
              'ironBox'
            ]
          ]
        }
      ],
      output: 'Boolean',
      colour: 160,
      tooltip: '配合循环使用更好哦~',
      helpUrl: ''
    })
  }
}
Blockly.Lua['FrontObjIs'] = function (block) {
  // String or array length.
  var DropdownObject = block.getFieldValue('Object')
  var code = 'me:FrontObjIs(' + DropdownObject + ')'
  return [code, Blockly.Lua.ORDER_NONE]
}

export default {
  name: 'hello',
  data () {
    return {
      share: 'http://localhost:8080/shareLink',
      dialogVisible: false,
      username: '',
      level: 1,
      map_id: 1,
      isRun: false,
      workspace: null,
      luaEditor: false,
      code: '',
      shareUrl: ''
    }
  },
  beforeMount () {
    if (!this.eventBus) {
      this.eventBus = new Vue({
        data: {
          ready: false,
          load: false
        }
      })
    }
    this.eventBus.ready = true
    this.eventBus.load = true
  },
  mounted () {
    ElementApi.message(this, '您可以拖拽代码块控制小人运动，通过本关卡呦~', 'info')
    this.username = sessionStorage.getItem('username')
    if (!this.username) {
      this.username = ''
    }
    this.map_id = parseInt(this.$route.params.id)
    this.$axios({
      method: 'get',
      url: GetUrl('FreeMode/getFreeMapContent'),
      params: {
        'map_id': this.map_id
      }
    }).then((res) => {
      let data = {
        'username': this.username,
        'map_id': this.map_id + '',
        'state': 'User',
        'map_data': res.data.map_data
      }
      let dataStr = JSON.stringify(data)
      document.getElementById('cache').innerText = dataStr
    })

    this.workspace = Blockly.inject('blockly-div', {
      toolbox: document.getElementById('toolbox'),
      transhcan: true
    })
    this.workspace.addChangeListener(this.myUpdateFunction)
    function init () {
      this.gameInstance = UnityLoader.instantiate('unity-container', '../../static/Build/Desktop.json', {onProgress: UnityProgress})
    }
    if (this.eventBus.ready) {
      init.bind(this)()
    } else {
      this.eventBus.$on('onload', () => {
        init.bind(this)()
      })
    }
    this.luaEditor = CodeMirror.fromTextArea(this.$refs.textarea, {
      lineNumbers: true,
      mode: 'lua',
      theme: 'rubyblue',
      lint: true,
      smartIndent: true
    })
  },
  methods: {
    click: function () {
      this.code = Blockly.Lua.workspaceToCode(this.workspace)
      console.log(this.code)
      this.luaEditor.setValue(this.code)
    },
    myUpdateFunction: function (event) {
      this.code = Blockly.Lua.workspaceToCode(this.workspace)
      this.luaEditor.setValue(this.code)
    },
    run: function () {
      if (this.code === '') {
        ElementApi.message(this, '请拖拽需要执行的代码~', 'warning')
        return
      }
      this.isRun = true
      this.gameInstance.SendMessage('ThirdPersonController', 'Run', this.code)
    },
    finish: function () {
      if (document.getElementById('res').innerText === 'false') {
        ElementApi.message(this, '您尚未通过本关卡，无法发布，请重试~', 'error')
        return
      }
      const url = GetUrl('ChallengeMode/addShareLink')
      let params = new URLSearchParams()
      params.append('username', this.username)
      params.append('code', this.code)
      params.append('isFree', 1)
      params.append('map_id', this.map_id)
      this.$axios({
        method: 'post',
        url: url,
        data: params
      }).then((res) => {
        if (res.data.success) {
          this.shareUrl = '127.0.0.1:8080/shareLink/' + res.data.share_obj.id
          this.dialogVisible = true
        } else {
          ElementApi.message(this, '系统错误，请重试！', 'error')
        }
      })
    },
    finish2: function () {
      this.$router.push('/FreeMode/mapSquare/')
      ElementApi.message(this, '恭喜您成功完成本关卡！', 'success')
    },
    restart: function () {
      let str = document.getElementById('cache').innerText
      this.gameInstance.SendMessage('floot', 'CreateMap', str)
      this.isRun = false
    },
    getMapData: function () {
      let str = document.getElementById('cache').innerText
      this.gameInstance.SendMessage('floot', 'CreateMap', str)
    },
    back: function () {
      this.$router.push('/ChallengeMode/selectLevel')
      location.reload()
    }
  }
}
</script>

<style scoped>
.btn-nextlevel {
  margin-top: 15px;
}

.btn-row {
  margin-top: 10px;
  margin-left: 10px;
}

#game-area {
  width: 800px;
  height: 550px;
  background-color: black;
}

.unity-style {
  width: 800px;
  height: 550px;
}

#blockly-div {
  width: 360px;
  height: 550px;
}

#code-area {
  width: 200px;
  height: 550px;
}

#code-div {
  height: 500px;
}

.link {
  font-size: 15px;
}
</style>
