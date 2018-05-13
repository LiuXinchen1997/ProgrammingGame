<template>
  <div class="manage_page fillcontain">
    <el-row :span="24">
      <el-col  class="gg">
        <el-menu :default-active="$route.path" @open="handleopen" @close="handleclose" @select="handleselect" unique-opened mode="horizontal" v-show="!collapsed" class="navmenu" background-color="#43C2EE" text-color="#fff" active-text-color="#25A0CA" theme="dark" router>
          <el-menu-item index="1" :route="{path: '/'}">
            <i class="el-icon-menu"></i>首页</el-menu-item>
          <el-submenu index="2" v-if="username !== ''">
            <template slot="title">
              <i class="usermanage"></i>用户管理</template>
            <el-menu-item index="2-1" :route="{path: '/UserManage/member'}">充值会员</el-menu-item>
            <el-menu-item index="2-2" :route="{path: '/UserManage/userInfo'}">修改个人信息</el-menu-item>
            <el-menu-item index="2-3" :route="{path: '/UserManage/modifyPsd'}">修改密码</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="challenge"></i>闯关模式</template>
            <el-menu-item v-if="username !== ''" index="3-1" @click="toSelectLevel">用户闯关</el-menu-item>
            <el-menu-item v-else index="3-1" @click="toSelectLevel">游客试玩</el-menu-item>
          </el-submenu>
          <el-submenu index="4" v-if="username !== ''">
            <template slot="title">
              <i class="free"></i>自由模式</template>
            <el-menu-item index="4-1" :route="{path: '/FreeMode/mapSquare'}">地图广场</el-menu-item>
            <el-menu-item index="4-2" :route="{path: '/FreeMode/mapCenter'}">我的地图库</el-menu-item>
            <el-menu-item index="4-3" @click="toCreateMap">创建地图</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
      <el-col class="other" :span="24">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: ''
    }
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
    toSelectLevel: function () {
      this.$router.push('/ChallengeMode/selectLevel')
    },
    toCreateMap: function () {
      this.$router.push('/FreeMode/createMap')
      location.reload()
    }
  }
}
</script>

<style>
.gg {
  background-color: black;
}
.other {
  height: 100%;
  overflow: auto;
}
</style>
