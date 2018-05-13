export default {
  getNumberFromGender: function (genderStr) {
    if (genderStr === '男') {
      return 1
    } else {
      return 0
    }
  },
  getGenderFromNumber: function (genderNum) {
    if (genderNum === 1) {
      return '男'
    } else {
      return '女'
    }
  },
  getAgeFromBirthday: function (birthday) {
    let now = new Date()
    let nowYear = now.getFullYear()
    let nowMonth = now.getMonth()
    let nowDay = now.getDay()

    let birthYear = birthday.getFullYear()
    let birthMonth = birthday.getMonth()
    let birthDay = birthday.getDate()

    let age = nowYear - birthYear
    if (age === 0) {
      return age
    }
    if (birthMonth > nowMonth) {
      age = age - 1
    } else if (birthMonth === nowMonth) {
      if (birthDay > nowDay) {
        age = age - 1
      }
    }

    return age
  }
}
