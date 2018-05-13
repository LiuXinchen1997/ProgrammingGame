<template>
  <div id="main-area">
    <div id="game-area">
      <div class="webgl-content">
        <div id="unity-container" class="unity-style"></div>
        <div id="cache" v-show="false"></div>
        <div id="res" v-show="false"></div>
        <button id="trigger" @click="startCreate" v-show="false"></button>
        <button id="saveBtn" @click="saveCreate" v-show="false"></button>
      </div>
    </div>
  </div>
</template>
<script>
import Vue from 'vue'
import GetUrl from '../../utils/GetURL'
import ElementApi from '../../utils/ElementAPI'

export default {
  data () {
    return {
      username: ''
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
    this.username = sessionStorage.getItem('username')
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
  },
  methods: {
    startCreate: function () {
      this.gameInstance.SendMessage('floot', 'CreateMap', '{"editor": "yes"}')
    },
    saveCreate: function () {
      let data = document.getElementById('res').innerText
      const url = GetUrl('FreeMode/saveCreateMap')
      let params = new URLSearchParams()
      params.append('username', this.username)
      params.append('data', data)
      this.$axios({
        method: 'post',
        url: url,
        data: params
      }).then((res) => {
        if (res.data.success) {
          ElementApi.message(this, '恭喜您，创建成功！', 'success')
          this.$router.push('/FreeMode/mapCenter/')
        } else {
          ElementApi.message(this, '创建失败，请重试！', 'error')
        }
      })
    }
  }
}
</script>

<style scoped>
.btn-nextlevel {
  margin-top: 15px;
}

#game-area {
  width: 100%;
  height: 600px;
  background-color: black;
}

.unity-style {
  width: 100%;
  height: 600px;
}

.link {
  font-size: 15px;
}
</style>
