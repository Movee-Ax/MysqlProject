create database Drugstore DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use Drugstore;
create table Shop   -- 药店
(
Shopcode varchar(20) primary key not null,  -- 药店编号
Shopname char(30) not null,     -- 药店名
Shoptype char(10) not null,     -- 类型
Shopregion char(10) not null,    -- 地区
Shopadress char(30) not null,   -- 地址
Shoparea char(40) not null,     -- 面积
Shoplat numeric(3,1) not null,  -- 纬度
Shoplng numeric(4,1) not null,  -- 经度
Doarea int,                     -- 营业面积
Housearea int,                  -- 仓库面积
Shopphone char(20) unique not null, -- 电话
Wcode char(20) not null             -- 管理该药店的药监局职工工号
);

create table Worker     -- 药监局职工
(
Wcode char(20) primary key not null,                -- 工号
Wname char(10)  not null,                           -- 姓名
Wsex enum('男','女') not null,                       -- 性别
Wage int not null,                                  -- 年龄
Wposition char(16) not null,                       -- 职位
Wphone varchar(15) unique not null -- 电话
);

create table Firm   -- 药品生产厂商
(
Firmcode varchar(20) primary key not null,          -- 生产厂商编号
Firmname char(40) not null,                        -- 生产厂商名
Firmregion char(10) not null,                       -- 生产厂商地区
Firmadress varchar(40) not null unique,             -- 生产厂商地址
Firmlat numeric(3,1) not null,                      -- 纬度
Firmlng numeric(4,1) not null,                      -- 经度
Firmphone char(20) unique not null                  -- 电话
);


create table Pharmacist  -- 药师
(
Phcode char(20) primary key not null,               -- 药师编号
Phname char(10)  not null,                          -- 姓名
Phsex enum('男','女') not null,                      -- 性别
Phage tinyint unsigned,                             -- 年龄
Phtitle char(16) not null,                           -- 职称
Shopcode varchar(20) not null,                       -- 雇佣的药店编号
Phphone char(20) unique not null,                    -- 电话
Phcor enum('是','否') not null default '否'          -- 是否继续注册
);

create table Medicine   -- 药品
(
Mname char(60) not null,                        -- 药名
Mlot varchar(20) not null,                      -- 批号
Firmcode varchar(20) not null,                  -- 生产厂商编号
Mmoney numeric(8,2) not null,                   -- 单价
Mcount int unsigned not null,                   -- 生产数量
Cdate Date,                                 -- 生产日期
Sdate Date,                                  -- 到期时间
primary key(Mname, Mlot, Firmcode)
);

create table Belong  -- 归属
(
Mname char(60) not null,                        -- 药名
Mlot varchar(20) not null,                      -- 批号
Firmcode varchar(20) not null,                  -- 生产厂商编号
Belongcode varchar(20) not null,                -- 归属者编号
Belongnum int unsigned not null,                -- 数量详情
primary key(Mname, Mlot, Firmcode, Belongcode)
);
create table Userlist   -- 用户列表
(
Username varchar(20) primary key,
Password varchar(20) not null,
root enum('TS','S','C','P')          -- TS可执行所有权限包括创建任何权限的用户，S可执行增改查，C可执行改查，P可执行查
);

