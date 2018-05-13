# 前后端接口文档

## 1 用户管理模块

### 1.1 用户登录

1. URL:`UserManage/login`

1. 方式：post

1. 请求参数:
    ```json
    {
        username: username,
        password: password
    }
    ```
1. 返回参数：
    ```json
    {
        success: true/false
    }
    ```

### 1.2 请求短信验证码

1. URL: `UserManage/login_tel`

1. 方式：get

1. 请求参数:
    ```json
    {
        tel_number: tel_number
    }
    ```
1. 返回参数：
    ```json
    {
        success: flag,
        status_code: status_code, // 状态码，0表示成功
        verifyCode: verifyCode
    }
    ```

### 1.3 用户注册

1. URL:`UserManage/register`

1. 方式：post

1. 请求参数：
    ```json
   {
       username: username,
       password: password,
       fullname: fullname,
       telnumber: telnumber,
       gender: gender,
       verificationcode: verificationcode
   }
    ```

1. 返回参数：
    ```json
    {
        success: true/false
    }
    ```

### 1.4 找回密码

1. URL:`UserManage/retrieve`

1. 方式：post

1. 请求参数：
    ```json
   {
        telnumber: telnumber,
        verificationcode: verificationcode
   }
    ```

1. 返回参数：
    ```json
    {
        success: true/false
    }
    ```

### 1.5 购买会员

1. URL:`UserManage/pay`

1. 方式：post

1. 请求参数：
    ```json
   {
        username:username
   }
    ```

1. 返回参数：
    ```json
    {
        success: ture/false
    }

1. URL:`UserManage/member`

1. 方式：get

1. 请求参数：
    ```json
   {
        username: username
   }
    ```

1. 返回参数：
    ```json
    {
        success: true/false,
        deadline: deadline,
        startingtime:startingtime
    }
    ```

### 1.6 修改个人信息

1. URL:`UserManage/modifyinformation`

1. 方式：post

1. 请求参数：
    ```json
    {
        username: username,
        fullname: fullname,
        gender: gender
    }
    ```
1. 返回参数
    {
        success: true/false
    }

### 1.7 用户修改密码

1. URL:`UserManage/confirm`

1. 方式：post

1. 请求参数：
    ```json
    {
        username: username,
        password: password
    }
    ```

1. 返回参数：
    ```json
    {
        success: ture/false
    }
    ```

1. URL:`UserManage/modifypassword`

1. 方式：post

1. 请求参数：
    {
        username:username,
        password:password
    }

1. 返回参数：
    ```json
    {
        success: ture/false
    }
    ```

## 2 闯关模式

### 2.1 游客试玩

1. URL:`ChallengeMode/tourist/selectlevel`

1. 方式:get

1. 请求参数：
    ```json
    {
        mapid: mapid
    }
    ```

1. 返回参数：
    ```json
    {
        map:[{
            mapid:,
            positionx: positionx,
            positiony: positiony
        }, {
            mapid:,
            positionx: positionx,
            positiony: positiony
        }...],
        hint:hint,
        hint:hint,
        descr:descr
    }
    ```

### 2.2 用户闯关

1. URL:`ChallengeMode/user/selectlevel`

1. 方式:get

1. 请求参数：
    ```json
    {
        mapid: mapid
    }
    ```

1. 返回参数：
    ```json
    {   map:[{
            mapid:,
            positionx: positionx,
            positiony: positiony
        }, {
            mapid:,
            positionx: positionx,
            positiony: positiony
        }...],
        hint:hint
        descr:descr,
        hint:hint
    }
    ```
1. URL:`ChallengeMode/user/finished`

1. 方式:post

1. 请求参数：
    ```json
    {
        username: username,
        mapid: mapid
    }
    ```

1. 返回参数：
    ```json
    {
        success: true/false;
    }
    ```

## 3 自由模式

### 2.3.1 用户自由模式挑战

1. URL: `FreeMode/user/selectlevel`

1. 方式: post

1. 请求参数:
    ```json
    {
        mapid: mapid
    }
    ```
1. 返回参数:
    ```json
    {
        map:[{
            mapid:,
            positionx: positionx,
            positiony: positiony
        }, {
            mapid:,
            positionx: positionx,
            positiony: positiony
        }...],
        hint:hint
    }
    ```
1. URL: `FreeMode/user/finished`

1. 方式：post

1. 请求参数：
    ```json
    {
        username: username,
        mapid: mapid
    }
    ```

1. 返回参数：
    ```json
    {
        success: true/false;
    }
    ```

### 2.3.2 用户创建地图

1. URL：`FreeMode/user/create`

1. 方式：post

1. 请求参数：
    ```json
    {
        map:[{
            mapid:,
            positionx: positionx,
            positiony: positiony
        }, {
            mapid:,
            positionx: positionx,
            positiony: positiony
        }...],
        hint:hint
        descr:descr
    }
    ```

1. 返回参数:
    ```json
    {
        success: true/false;
    }
    ```

### 2.3.3 用户发布地图

1. URL：`FreeMode/user/publishmap`

1. 方式：post

1. 请求参数：
    ```json
    {
        mapid:mapid
    }
    ```

1. 返回参数：
    ```json
    {
        success：true/false
        地图链接：地图链接
    }
    ```

### 2.3.4 用户删除地图

1. URL：`FreeMode/user/deletemap`

1. 方式：get

1. 请求参数：
    ```json
    {
        mapid:mapid
    }

1. 返回参数：
    ```json
    {
        success：true/false
        地图链接：地图链接
    }
    ```

### 2.3.5 用户修改地图

1. URL：`FreeMode/user/modifymap`

1. 方式：get

1. 请求参数：
    ```json
    {
        map:[{
            mapid:,
            positionx: positionx,
            positiony: positiony
        }, {
            mapid:,
            positionx: positionx,
            positiony: positiony
        }...],
        hint:hint
        descr:descr
    }
    ```

1. 返回参数：
    ```json
    {
        map:[{
            mapid:,
            positionx: positionx,
            positiony: positiony
        }, {
            mapid:,
            positionx: positionx,
            positiony: positiony
        }...],,
        hint:hint
        descr:descr
    }
    ```
