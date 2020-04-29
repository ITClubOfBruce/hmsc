# hmsc
海马商城back-end code

use hmsc_db;

drop table if exists `stat_daily_site`;

create table `stat_daily_site` (
    `id` int(11) unsigned not null auto_increment,
    `date` date not null comment '日期',
    `total_pay_money` decimal(10,2) not null default '0.00' comment '当日收入总额',
    `total_member_count` int(11) not null comment '会员总数',
    `total_new_member_count` int(11) not null comment '当日新增会员数',
    `total_order_count` int(11) not null comment '当日订单数',
    `total_shared_count` int(11) not null comment '分享总数',
    `updated_time` timestamp not null default current_timestamp comment '最近更新时间',
    `created_time` timestamp not null default current_timestamp comment '插入时间',
    primary key (`id`),
    key `idx_data` (`date`)
)engine=InnoDB default charset=utf8 comment='全站日统计';




use hmsc_db;

drop table if exists `member`
create table `member` (
	`id` int(11) unsigned not null auto_increment,
	`nickname` varchar(100) not null default '' comment '会员昵称',
	`mobile` varchar(20) not null default '' comment '会员手机号码',
	`sex` tinyint(1) not null default '0' comment '1:男 2:女 0:没有填写',
	`avatar` varchar(200) not null default '' comment '会员头像',
	`salt` varchar(32) not null default '' comment '登录密码的随机密钥',
	`reg_ip` varchar(100) not null default '' comment '注册ip',
	`status` tinyint(1) not null default '1' comment '1:有效 0:无效',
	`updated_time` timestamp not null default current_timestamp comment '最后一次更新时间',
	`created_time` timestamp not null default current_timestamp comment '创建时间',
	primary key (`id`)
)ENGINE=InnoDB default charset=utf8 comment='会员表';






use hmsc_db;

drop table if exists `goods`
create table `goods` (
    `id` int(11) unsigned not null auto_increment,
    `cat_id` int(11) not null default '0' comment '分类id',
    `name` varchar(100) not null default '' comment '商品名称',
    `price` decimal(10,2) not null default '0.00' comment '商品价格',
    `main_image` varchar(100) not null default '' comment '商品主图',
    `summary` varchar(10000) not null default '' comment '商品描述',
    `stock` int(11) not null default '0' comment '库存数',
    `tags` varchar(200) not null default '' comment 'tag 标签，用“,”连接',
    `status` tinyint(1) not null default '1' comment '1:有效，0：无效',
    `month_count` int(11) not null default '0' comment '月销量',
    `total_count` int(11) not null default '0' comment '总销量',
    `view_count` int(11) not null default '0' comment '总浏览次数',
    `comment_count` int(11) not null default '0' comment '总评论数',
    `updated_time` timestamp not null default current_timestamp comment '最后一次更新时间',
	`created_time` timestamp not null default current_timestamp comment '创建时间',
	primary key (`id`)
)ENGINE=InnoDB default charset=utf8 comment='商品表';


