<template>
<div>
  <el-row class="map_square">
  <el-col :span="6" v-for="(o, index) in data.slice((currentPage - 1) * pagesize, currentPage * pagesize)" :key="o" :offset="index % 3 === 0 ? 1 : 2" class="el-col">
    <el-card :body-style="{ padding: '10px' }">
      <img :src="o.image_url" class="image">
      <div class="map_info">
        <p class="fa fa-user-circle-o fa-1x">&nbsp;设计者&emsp;：{{o.username}}</p><br/>
        <p class="fa fa-map-o fa-1x">&nbsp;地图编号：{{o.map_id}}</p><br/>
        <p class="fa fa-calendar fa-1x">&nbsp;&nbsp;创建时间：{{o.time}}</p>
        <div class="bottom clearfix">
          <el-button v-if="!o.is_like" type="text" class="fa fa-thumbs-o-up fa-1x" @click="setLikeById(o.map_id, index)">点赞</el-button>
          <el-button v-else type="text" class="fa fa-thumbs-up fa-1x" @click="cancelLikeById(o.map_id, index)">取消</el-button>
          {{o.like_num}}
          <el-button v-if="!o.is_collect" type="text" class="fa fa-heart-o fa-1x" @click="setCollectById(o.map_id, index)">收藏</el-button>
          <el-button v-else type="text" class="fa fa-heart fa-1x" @click="cancelCollectById(o.map_id, index)">取消</el-button>
          {{o.collect_num}}
          <el-button type="text" class="fa fa-space-shuttle fa-1x" @click="play(o.map_id)">进入游戏</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
  </el-row>
  <el-col :offset="9" :span="10">
    <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange" :page-size="pagesize" layout="total, prev, pager, next, jumper"  :total="data.length"></el-pagination>
  </el-col>
</div>
</template>
<script>
import GetUrl from '../../utils/GetURL'
import ElementApi from '../../utils/ElementAPI'

export default{
  data () {
    return {
      username: '',
      data: [],
      currentPage: 1,
      pagesize: 6
    }
  },
  mounted () {
    this.username = sessionStorage.getItem('username')
    const url = GetUrl('FreeMode/getAllReleasedMap')
    this.$axios({
      method: 'get',
      url: url,
      params: {
        'username': this.username
      }
    }).then((res) => {
      let flag = res.data.success
      if (flag) {
        res.data.maps.forEach(function (element) {
          let num = Math.ceil(Math.random() * 20)
          let imageUrl = require('../../assets/FreeMode/' + num + '.jpg')
          this.data.push({
            'map_id': element.map_id,
            'descr': element.descr,
            'hint': element.hint,
            'username': element.username,
            'time': element.time,
            'like_num': element.like_num,
            'is_like': element.is_like,
            'collect_num': element.collect_num,
            'is_collect': element.is_collect,
            'image_url': imageUrl
          })
        }, this)
      } else {
        ElementApi.message(this, '网络错误，请重试！', 'error')
      }
    })
  },
  methods: {
    handleSizeChange: function (size) {
      this.pagesize = size
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage
    },
    setLikeById: function (mapId, index) {
      const url = GetUrl('FreeMode/setLikeById')
      this.$axios({
        method: 'get',
        url: url,
        params: {
          'username': this.username,
          'map_id': mapId
        }
      }).then((res) => {
        let flag = res.data.success
        if (flag) {
          this.data[index].like_num = this.data[index].like_num + 1
          this.data[index].is_like = true
        } else {
          ElementApi.message(this, '系统错误，请重试！', 'error')
        }
      })
    },
    cancelLikeById: function (mapId, index) {
      const url = GetUrl('FreeMode/cancelLikeById')
      this.$axios({
        method: 'get',
        url: url,
        params: {
          'username': this.username,
          'map_id': mapId
        }
      }).then((res) => {
        let flag = res.data.success
        if (flag) {
          this.data[index].like_num = this.data[index].like_num - 1
          this.data[index].is_like = false
        } else {
          ElementApi.message(this, '系统错误，请重试！', 'error')
        }
      })
    },
    setCollectById (mapId, index) {
      const url = GetUrl('FreeMode/setCollectById')
      this.$axios({
        method: 'get',
        url: url,
        params: {
          'username': this.username,
          'map_id': mapId
        }
      }).then((res) => {
        let flag = res.data.success
        if (flag) {
          this.data[index].collect_num = this.data[index].collect_num + 1
          this.data[index].is_collect = true
          ElementApi.message(this, '收藏成功！', 'success')
        } else {
          ElementApi.message(this, '系统错误，请重试！', 'error')
        }
      })
    },
    cancelCollectById (mapId, index) {
      const url = GetUrl('FreeMode/cancelCollectById')
      this.$axios({
        method: 'get',
        url: url,
        params: {
          'username': this.username,
          'map_id': mapId
        }
      }).then((res) => {
        let flag = res.data.success
        if (flag) {
          this.data[index].collect_num = this.data[index].collect_num - 1
          this.data[index].is_collect = false
          ElementApi.message(this, '取消成功！', 'success')
        } else {
          ElementApi.message(this, '系统错误，请重试！', 'error')
        }
      })
    },
    play (mapId) {
      let pathStr = '/freeModePlay/' + mapId
      this.$router.push(pathStr)
      location.reload()
    }
  }
}
</script>
<style>
.fa-calendar {
  padding-bottom: 6px;
}
.fa-map-o {
  padding-bottom: 5px;
}
.fa-user-circle-o {
  padding-bottom: 6px;
}
.map_info {
  padding-top: 10px;
}
.user-circle-o {
  color: blue;
}
.map_square {
  min-height: 670px;
}
.el-col {
  margin-bottom: 20px;
}
.time {
    font-size: 13px;
    color: #999;
}
.bottom {
  line-height: 12px;
}
.button {
  padding: 0;
  float: right;
}
.image {
  height: 150px;
  width: 100%;
  display: block;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
</style>
