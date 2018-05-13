<template>
  <div>
    <el-aside class="select">
        <el-select v-model="value" placeholder="请选择操作" @change="selectItem">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </el-aside>
    <el-row>
      <router-view></router-view>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      options: [{
        value: '/FreeMode/mapCenter/creation',
        label: '已创建'
      },
      {
        value: '/FreeMode/mapCenter/release',
        label: '已发布'
      },
      {
        value: '/FreeMode/mapCenter/collection',
        label: '已收藏'
      }],
      value: ''
    }
  },
  methods: {
    selectItem () {
      this.$router.push(this.value)
    }
  }
}
</script>
<style>
.select{
  margin-left: 30px;
  margin-bottom: 15px;
}
</style>
