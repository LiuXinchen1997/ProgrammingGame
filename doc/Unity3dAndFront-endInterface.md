# unity3d与前端接口文档

## 玩家行为接口(前端到unity)

*注：传递给unity的代码格式为lua语言*

### 预制的对象为me，在提交前在lua脚本字符串前添加

```Lua
    local Actor = CS.ActorBehavior
    local me = Actor()
```

### 还应包含的预制对象代码为

```Lua
    local Pawn = CS.PawnObj
    local floor = Pawn('floor')

    local wall = Pawn('wall')
    local onceDoor = Pawn('onceDoor')
    local button = Pawn('button')
    local door = Pawn('door')
    local box = Pawn('box')
    local upLaser = Pawn('upLaser')
    local rightLaser = Pawn('rightLaser')
    local stone = Pawn('stone')
    local ironBox = Pawn('ironBox')
    local balk = Pawn('balk')
    local startPos = Pawn('startPos')
    local endPos = Pawn('endPos')
```

### **前端传递给unity的普通行为函数如下：**

1. 向前行走 `me:WalkForward(n)`
    - 此函数可以接收整型参数n，表示前进的步数
1. 拾起箱子（举到头顶上） `me:PickUp()`
1. 放下箱子 `me:PutDown()`
1. 左转 `me:TurnLeft()`
1. 右转 `me:TurnRight()`

### **前端传递给unity的判断行为函数如下（待添加）**

1. 前面的物体是否是Pawn类的特定对象（wall,door...） `me:FrontObjIs(object：Pawn)`，返回值为`Bool`
    - 此函数参数为可选离散类型，为以上设计的地图元素
1. 玩家输出语句，可供玩家测试 `me:say('hello world')`
    - 此函数参数为字符串，以供玩家调试程序使用

### **例子**

```Lua
    --[ 自动添加 --]
    local Actor = CS.ActorBehavior
    local me = Actor()
    local Pawn = CS.PawnObj
    local wall = Pawn('wall')
    local onceDoor = Pawn('onceDoor')
    local button = Pawn('button')
    local door = Pawn('door')
    local box = Pawn('box')
    local floor = Pawn('floor')
    local laser = Pawn('laser')
    local startPos = Pawn('startPos')
    local endPos = Pawn('endPos')
    local stone = Pawn('stone')
    local ironBox = Pawn('ironBox')
    local balk = Pawn('balk')

    --[ Blockly生成的代码 --]
    --[ 前进一格 --]
    me:WalkForward()
    a = 100;
    --[ 检查条件 --]
    if(me.FrontObjIs(wall))
    then
        me:say("有墙" )
    else
        me:say("可以继续前进" )
    end
    me:say("a 的值为 :"+a)
```

## 用例传输接口约定

### 1 挑战模式（包括游客试玩和用户挑战模式这两个用例）

> 过程概述：
> 1. Unity加载完成之后，前端向Unity发送地图信息，Unity加载地图并完成。
> 1. 用户拖拽代码块完成后，生成Lua代码，前端将Lua代码传递给Unity。
> 1. Unity执行之后将结果传递给前端。

1. 前端向Unity传递地图信息

    ```Json
    {
        "username": "string",
        "map_id": "int",
        "state": "User/System",
        "map_data":
        [
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            ...
        ],
    }
    ```

1. 前端向Unity传递Lua代码

    ```Json
    {
        "code": "string"
    }
    ```

1. Unity向前端传递运行结果
    ```json
    {
        "success": true/false
    }
    ```

### 2 自由模式 创建地图

> 过程简述：
> 1. 用户拖拽完成地图之后，Unity将得到的地图信息传给前端。

1. Unity向前端传递地图信息：

    ```json
    {
        "map_data":
        [
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            ...
        ]
    }
    ```

### 3 自由模式 修改地图

> 过程简述：

1. 前端向Unity传递地图信息：

    ```json
    {
        "map_id": "int",
        "map_data":
        [
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            ...
        ]
    }
    ```

1. Unity向前端传递修改后的地图信息：

    ```json
    {
        "map_id": "int",
        "map_data":
        [
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            {"pos":"xx-yy","obj":"int"},
            ...
        ]
    }
    ```
