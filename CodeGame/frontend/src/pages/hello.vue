<template>
  <h1>This is a hello page.</h1>
</template>

<script>
import axios from 'axios'
import GetUrl from '../api/GetURL'

/*
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.baseURL = 'http://localhost:8000';
Vue.prototype.$ajax = axios;
*/

export default {
  data () {
    return {
      username: '',
      age: '',
      gender: ''
    }
  },
  mounted () {
  },
  methods: {
    hello: function () {
      axios.get(GetUrl('UserManage/getDemo'))
        .then((res) => {
          this.username = res.data.username
          this.gender = res.data.password
          this.age = res.data.tel_number
        })
        .catch((error) => {
          console.log(error)
        })
    },
    greet: function () {
      this.$axios({
        method: 'post',
        url: 'UserManage/postDemo',
        data: {
          usera: '111'
        }
      }).then((res) => {
        alert('aaaa')
      }).catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
</style>
