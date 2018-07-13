CREATE TABLE `db_book` (
   `id` int(4) NOT NULL AUTO_INCREMENT,
   `title` varchar(11) NOT NULL DEFAULT '',
   `titlepic` varchar(255) NOT NULL DEFAULT '',
   `writer` varchar(255) NOT NULL COMMENT '作者',
   `translater` VARCHAR(20) not null default '',
    `publisher` VARCHAR(20) not null default '',
   `pub_at` VARCHAR(20) not null default '',
   `price` DECIMAL(6,2) NOT null default '0.00',
	 `pl_nums` MEDIUMINT(10) NOT NULL default 0,
   `vote_nums` MEDIUMINT(10) not null default 0,
   `titleurl` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;