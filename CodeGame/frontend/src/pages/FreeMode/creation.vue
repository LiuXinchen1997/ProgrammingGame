<template>
  <div>
    <el-row class="creation">
    <el-col :span="6" v-for="(o, index) in data.slice((currentPage - 1) * pagesize, currentPage * pagesize)" :key="o" :offset="index % 3 === 0 ? 1 : 2" class="el-col">
      <el-card :body-style="{padding: '10px'}">
        <img :src="o.image_url" class="image">
        <div style="padding: 14px;">
          <p class="fa fa-user-circle-o fa-1x">设计者&nbsp;&emsp;：{{o.username}}</p><br/>
          <p class="fa fa-calendar fa-1x">&nbsp;&nbsp;创建时间：{{o.time}}</p>
          <div class="bottom clearfix">
            <el-button type="text" class="fa fa-check-circle-o fa-1x" @click="uploadMap(o.map_id)">发布</el-button>
            <el-button type="text" class="fa fa-trash fa-1x" @click="deleteMap(o.map_id, index)">删除</el-button>
            <el-button type="text" class="fa fa-wrench fa-1x" @click="updateMap(o.map_id)">修改</el-button>
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
    const url = GetUrl('FreeMode/getAllCreatedMapByUsername')
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
    deleteMap (mapId, index) {
      const url = GetUrl('FreeMode/deleteMapById')
      this.$axios({
        method: 'get',
        url: url,
        params: {
          'map_id': mapId
        }
      }).then((res) => {
        let flag = res.data.success
        if (flag) {
          this.data.splice(index, 1)
          ElementApi.message(this, '删除成功！', 'success')
        } else {
          ElementApi.message(this, '系统错误，请重试！', 'error')
        }
      })
    },
    updateMap (mapId) {
      let pathStr = '/updateMap/' + mapId
      this.$router.push(pathStr)
      location.reload()
    },
    uploadMap (mapId) {
      let pathStr = '/freeModeUpload/' + mapId
      this.$router.push(pathStr)
      location.reload()
    }
  }
}
</script>
<style>
.fa-calendar {
  padding-bottom: 7px;
}
.fa-user-circle-o {
  padding-bottom: 7px;
}
.creation {
  min-height: 660px;
}
.el-col {
  margin-bottom: 15px;
}
.time {
    font-size: 13px;
    color: #999;
}
.bottom {
  margin-top: 5px;
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
