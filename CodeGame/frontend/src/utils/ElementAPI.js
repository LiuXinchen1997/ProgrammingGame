export default {
  message: function (context, msg, type) {
    context.$message({
      message: msg,
      type: type,
      showClose: true
    })
  }
}
