# 数据库表

## 0 游戏部分

### 物品

* 地图 12*12  0
* 玩家控制的小人 1
* 小人默认初始朝向：向上

### 地图元素及其编号

1. 墙 1
    * 阻挡物
1. 一次性门 2
    * 仅能通过一次，通过一次后自动关闭。
1. 按钮 3
    * 按下之后普通门可以打开
1. 普通门 4
    * 需要通过按钮控制将其打开
1. 箱子 5
    * 阻挡物，可以搬动，可以压住按钮，可以抵挡激光
1. 向上激光发射器 6
    * 向上发射激光
1. 向右激光发射器 7
    * 向右发射激光
1. 石头 8 装饰物
    * 阻挡物，不可搬动
1. 铁块 9 装饰物
    * 阻挡物，不可搬动
1. 路障 10 装饰物
    * 阻挡物，不可搬动
1. 起始点 11
1. 目的地点 12

## 1 用户管理部分

### 登录信息表

```sql
CREATE TABLE IF NOT EXISTS UserEntry(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    tel_number CHAR(11) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL
);
```

### 用户信息表

```sql
CREATE TABLE IF NOT EXISTS User(
    user_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fullname VARCHAR(20) NOT NULL,
    age INTEGER DEFAULT 10,
    gender tinyint(1) DEFAULT 1, -- 1为男，0为女
    email varchar(50),
    descr text, -- 个人描述
    level INTEGER DEFAULT 1, -- 用户闯关模式关卡
    entry_id INTEGER NOT NULL, -- 关联用户登录信息
    FOREIGN KEY(entry_id) REFERENCES UserEntry(id)
);
```

### 会员信息表

```sql
CREATE TABLE IF NOT EXISTS Membership(
    id INTEGER AUTO_INCREMENT not null PRIMARY KEY,
    user_id INTEGER NOT NULL,
    priority SMALLINT DEFAULT 0,
    starttime DATE NOT NULL,
    endtime DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);
```

## 2 闯关模式与自由模式

### 元素表

```sql
-- 元素表，用于定义地图内的基本元素
CREATE TABLE IF NOT EXISTS Element(
    element_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(100), -- 元素名
    descr text -- 元素描述信息
);
```

### 闯关模式地图表

```sql
-- 闯关模式地图表
CREATE TABLE IF NOT EXISTS ChallengeMap(
    map_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    level INTEGER NOT NULL, -- 地图对应关卡
    hint text,  -- 关卡说明信息
    descr text -- 地图描述信息
);
```

### 地图内容表

```sql
-- 地图内容表，定义构成闯关模式地图的元素内容
create table if not exists ChallengeMapContent(
    id INTEGER AUTO_INCREMENT not null PRIMARY KEY,
    position_x INTEGER NOT NULL CHECK (position_x >= 0),
    position_y INTEGER NOT NULL CHECK (position_y >= 0),
    element_id INTEGER NOT NULL,
    map_id INTEGER NOT null,
    FOREIGN KEY (element_id) REFERENCES Element(element_id),
    FOREIGN KEY (map_id) REFERENCES ChallengeMap(map_id)
);
```

### 自由模式地图表

```sql
-- 自由模式地图表
create table if not exists FreeMap(
    map_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    hint text,  -- 关卡说明信息
    descr text, -- 地图描述信息
    creator INTEGER NOT NULL,
    createdTime timestamp NOT NULL,
    isRelease tinyint(1) DEFAULT 0 -- 是否已发布
);
```

### 用户点赞表

```sql
-- 用户点赞表
CREATE TABLE IF NOT EXISTS UserLike(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    map_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (map_id) REFERENCES FreeMap(map_id)
);
```

### 用户收藏表

```sql
-- 用户收藏表
CREATE TABLE IF NOT EXISTS UserCollect(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    map_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (map_id) REFERENCES FreeMap(map_id)
);
```

### 分享链接表

```sql
-- 分享链接表
CREATE TABLE IF NOT EXISTS UserShare(
    id INTEGER NOT NULL PRIMARY KEY,
    map_id INTEGER NOT NULL,
    isFree tinyint(1) DEFAULT 1, -- 1为自由模式，0为闯关模式
    solution_code text NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);
```

## 插入数据

### 地图元素

```sql
-- 插入地图元素
insert into Element values(1, 'wall', '阻挡物。');
insert into Element values(2, 'onceDoor', '仅能通过一次，通过一次后自动关闭。');
insert into Element values(3, 'button', '按下之后普通门可以打开。');
insert into Element values(4, 'door', '需要通过按钮控制将其打开。');
insert into Element values(5, 'box', '阻挡物，可以搬动，可以压住按钮，可以抵挡激光。');
insert into Element values(6, 'upLaser', '向上发射激光。');
insert into Element values(7, 'rightLaser', '向右发射激光。');
insert into Element values(8, 'stone', '阻挡物，不可搬动。');
insert into Element values(9, 'ironBox', '阻挡物，不可搬动。');
insert into Element values(10, 'balk', '阻挡物，不可搬动。');
insert into Element values(11, 'startPos', '起点');
insert into Element values(12, 'endPos', '终点');
```

### 挑战模式关卡

#### 第一关

```sql
-- 挑战模式第一关
insert into ChallengeMap (map_id, level, hint, descr) values(1, 1, '您只需要控制小人，从起点达到终点就可以了哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 3, 11, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 8, 12, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 8, 8, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 7, 10, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 6, 8, 1);
```
###第二关
```sql
-- 挑战模式第二关
insert into ChallengeMap (map_id, level, hint, descr) values(2, 2, '您需要绕过障碍物，才能到达终点哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 8, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 8, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 8, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 8, 10, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 8, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 8, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 8, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 7, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 6, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 5, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 4, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 3, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 2, 1, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 4, 11, 2);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 12, 12, 2);
```
###第三关
```sql
-- 挑战模式第三关
insert into ChallengeMap (map_id, level, hint, descr) values(3, 3, '您需要用箱子挡住激光，才能到达终点哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 3, 11, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12, 8, 7, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 6, 5, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 2, 10, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 12, 12, 3);
```
###第四关
```sql
-- 挑战模式第四关
insert into ChallengeMap (map_id, level, hint, descr) values(4, 4, '这是回形空间，转着走就能到达终点哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 2, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 2, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 2, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 2, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 2, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 2, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 2, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 3, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 4, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 5, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 6, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 7, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 8, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 9, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 10, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 10, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 10, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 10, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 10, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 10, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 10, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 9, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 8, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 7, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 6, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 5, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 4, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 4, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 4, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 4, 10, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 4, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 4, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 5, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 6, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 7, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 8, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 8, 1, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 8, 9, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 3, 11, 4);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 7, 12, 4);
```
###第五关
```sql
-- 挑战模式第五关
insert into ChallengeMap (map_id, level, hint, descr) values(5, 5, '您需要用箱子压住按钮，通过门才能到达终点哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 2, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 2, 10, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 2, 10, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 2, 10, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 2, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 2, 8, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 3, 8, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 4, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 5, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 6, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 6, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 6, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 6, 4, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 6, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 6, 8, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 5, 8, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 4, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 3, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 2, 9, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 3, 11, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 5, 3, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 4, 5, 5);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 10, 12, 5);
```
###第六关
```sql
-- 挑战模式第六关
insert into ChallengeMap (map_id, level, hint, descr) values(6, 6, '您需要通过迷宫，按C键切换视角，看清全貌才能到达终点哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 2, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 3, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 3, 11, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 3, 2, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 3, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 4, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 5, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 5, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 5, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 6, 2, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 6, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 7, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 7, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 7, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 7, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 8, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 8, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 8, 2, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 8, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 8, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 8, 2, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 8, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 8, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 9, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 9, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 9, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 9, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 10, 1, 6);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 12, 12, 6);
```
