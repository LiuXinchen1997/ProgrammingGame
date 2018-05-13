create database if not exists jisuanke;
use jisuanke;

CREATE TABLE IF NOT EXISTS UserEntry(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    tel_number CHAR(11) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS User(
    user_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fullname VARCHAR(20) NOT NULL,
    age INTEGER DEFAULT 10,
    gender tinyint(1) DEFAULT 1,
    email varchar(50),
    descr text,
    level INTEGER DEFAULT 1,
    entry_id INTEGER NOT NULL,
    FOREIGN KEY(entry_id) REFERENCES UserEntry(id)
);

CREATE TABLE IF NOT EXISTS Membership(
    id INTEGER AUTO_INCREMENT not null PRIMARY KEY,
    user_id INTEGER NOT NULL,
    priority SMALLINT DEFAULT 0,
    starttime DATE NOT NULL,
    endtime DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);


CREATE TABLE IF NOT EXISTS Element(
    element_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(100),
    descr text
);

CREATE TABLE IF NOT EXISTS ChallengeMap(
    map_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    level INTEGER NOT NULL,
    hint text,
    descr text
);

create table if not exists ChallengeMapContent(
    id INTEGER AUTO_INCREMENT not null PRIMARY KEY,
    position_x INTEGER NOT NULL CHECK (position_x >= 0),
    position_y INTEGER NOT NULL CHECK (position_y >= 0),
    element_id INTEGER NOT NULL,
    map_id INTEGER NOT null,
    FOREIGN KEY (element_id) REFERENCES Element(element_id),
    FOREIGN KEY (map_id) REFERENCES ChallengeMap(map_id)
);

create table if not exists FreeMap(
    map_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    hint text,
    descr text,
    creator INTEGER NOT NULL,
    createdtime DATE NOT NULL,
    isrelease tinyint(1) DEFAULT 0,
    FOREIGN KEY (creator) REFERENCES UserEntry(id)
);

create table if not exists FreeMapContent(
    id INTEGER AUTO_INCREMENT not null PRIMARY KEY,
    position_x INTEGER NOT NULL CHECK (position_x >= 0),
    position_y INTEGER NOT NULL CHECK (position_y >= 0),
    element_id INTEGER NOT NULL,
    map_id INTEGER NOT null,
    FOREIGN KEY (element_id) REFERENCES Element(element_id),
    FOREIGN KEY (map_id) REFERENCES FreeMap(map_id)
);

CREATE TABLE IF NOT EXISTS UserLike(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    map_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (map_id) REFERENCES FreeMap(map_id)
);

CREATE TABLE IF NOT EXISTS UserCollect(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    map_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (map_id) REFERENCES FreeMap(map_id)
);

CREATE TABLE IF NOT EXISTS UserShare(
    id INTEGER NOT NULL PRIMARY KEY,
    map_id INTEGER NOT NULL,
    isFree tinyint(1) DEFAULT 1,
    solution_code text NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

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

-- 挑战模式第一关
insert into ChallengeMap (map_id, level, hint, descr) values(1, 1, '您只需要控制小人，从起点达到终点就可以了哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 3, 11, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5, 8, 12, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3, 8, 8, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4, 7, 10, 1);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8, 6, 8, 1);

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

-- 挑战模式第三关
insert into ChallengeMap (map_id, level, hint, descr) values(3, 3, '您需要用箱子挡住激光，才能到达终点哦~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 3, 11, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12, 8, 7, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9, 6, 5, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11, 2, 10, 3);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6, 12, 12, 3);

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

-- 挑战模式第七关
insert into ChallengeMap (map_id, level, hint, descr) values(7, 7, '左转，左转，前方不是终点那就向左进军吧~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,4,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,5,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,6,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,7,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,8,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,9,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,10,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,8,2,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,9,5,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,10,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,8,8,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,9,2,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,10,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,7,11,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,8,2,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,10,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,6,7,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,7,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,8,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,9,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,10,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,5,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,6,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,7,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,9,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,5,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,7,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,9,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,5,2,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,9,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,3,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,4,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,5,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,9,1,7);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,8,12,7);


-- 挑战模式第八关
insert into ChallengeMap (map_id, level, hint, descr) values(8, 8, '左转，左转，一如既往，向终点进军~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,2,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,4,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,5,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,6,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,7,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,8,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,9,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,11,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,4,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,9,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,12,6,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,2,11,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,4,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,6,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,7,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,8,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,9,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,2,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,11,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,9,6,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,8,12,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,5,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,2,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,6,7,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,11,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,4,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,5,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,6,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,7,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,8,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,9,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,4,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,9,2,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,11,5,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,12,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,1,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,2,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,3,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,4,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,5,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,6,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,7,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,8,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,9,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,10,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,11,1,8);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,12,1,8);

-- 挑战模式第九关
insert into ChallengeMap (map_id, level, hint, descr) values(9, 9, '左转，左转，放下箱子打开终点前的大门~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,2,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,4,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,5,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,6,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,8,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,9,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,11,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,2,11,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,4,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,9,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,12,6,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,4,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,6,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,8,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,9,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,2,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,11,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,8,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,9,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,6,3,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,9,12,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,5,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,6,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,2,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,7,4,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,11,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,4,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,5,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,6,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,8,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,9,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,11,5,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,4,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,9,2,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,12,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,1,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,2,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,3,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,4,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,5,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,6,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,7,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,8,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,9,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,10,1,9);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,12,1,9);

-- 挑战模式第十关
insert into ChallengeMap (map_id, level, hint, descr) values(10, 10, '终章：如是，生活不止谜题，还有诗和远方~', '欢迎来到CoderRuner在线编程游戏，在这里你可以拖动代码块控制小人运动哦！赶紧来试试吧！');

insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (1,10,6,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,10,6,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (2,11,7,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (3,1,7,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,3,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,4,4,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (4,5,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,2,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,6,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,7,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (5,8,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,1,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,4,11,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (6,9,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,1,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,2,5,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,3,10,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (7,10,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,1,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,3,10,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (8,10,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,1,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,3,10,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,4,2,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,5,1,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (9,9,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,2,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,3,3,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,6,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,7,2,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (10,8,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,3,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,4,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (11,5,9,10);
insert into ChallengeMapContent (position_x, position_y, element_id, map_id) values (12,12,12,10);
