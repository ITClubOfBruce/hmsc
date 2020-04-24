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


