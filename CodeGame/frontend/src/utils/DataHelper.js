export default {
  objContainsElement: function (element, obj) {
    for (let key in obj) {
      if (obj[key] === element) {
        return true
      }
    }
    return false
  }
}
