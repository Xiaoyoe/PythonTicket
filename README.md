# 数据库结构与数据概览
## 一、数据库基本信息
- **数据库名称**：db_ticket
- **服务器类型**：MySQL
- **服务器版本**：5.7.20-log
- **字符编码**：utf8mb4
- **数据导出时间**：2025年06月05日 11:08:04


## 二、数据表结构与数据详情

### （一）轮播图表（carousel）
#### 表结构
| 字段名       | 数据类型         | 约束条件       | 描述         |
|--------------|------------------|----------------|--------------|
| id           | int(11)          | 主键，自增     | 唯一标识     |
| title        | varchar(255)     | 非空           | 轮播图标题   |
| image_url    | varchar(255)     | 非空           | 图片URL      |
| image_res_id | text             | 可为空         | 图片资源ID   |

#### 表数据
| id | title                  | image_url | image_res_id |
|----|------------------------|-----------|--------------|
| 1  | 《逆转杀局》续作       |           | banner01.jpg |
| 2  | 《消失的她》朱一龙、倪妮主演 |         | banner04.jpg |
| 3  | 开榜封神：寻榜99行     |           | banner03.jpg |
| 4  | 海贼王 航海行动!!!     |           | banner05.jpg |
| 5  | 2025年度动作大片 电影热潮 |       | banner02.jpg |


### （二）商品表（stuffs）
#### 表结构
| 字段名       | 数据类型         | 约束条件       | 描述         |
|--------------|------------------|----------------|--------------|
| id           | int(11)          | 主键，自增     | 唯一标识     |
| name         | text             | 非空           | 商品名称     |
| image_res_id | text             | 可为空         | 商品图片资源ID |
| points       | int(11)          | 可为空         | 商品积分     |

#### 表数据
| id  | name             | image_res_id | points |
|-----|------------------|--------------|--------|
| 1   | 爆米花（大）     | ic_stuff_1   | 80     |
| 2   | 爆米花（小）     | ic_stuff_2   | 50     |
| 3   | 可口可乐         | ic_stuff_3   | 20     |
| 4   | 雪碧             | ic_stuff_4   | 20     |
| 5   | 芬达             | ic_stuff_5   | 20     |
| 9   | 豆鱼雷钥匙扣..   | ic_stuff_9   | 15     |
| 10  | 豆鱼钥匙扣       | ic_stuff_10  | 12     |
| 11  | 可爱小人钥匙扣   | ic_stuff_11  | 18     |
| 12  | sample短袖       | ic_stuff_12  | 25     |
| 13  | mini甜点杯       | ic_stuff_13  | 10     |
| 14  | 一只奶糖鼠       | ic_stuff_14  | 16     |
| 15  | 旺旺黑白配焦糖   | ic_stuff_15  | 8      |
| 16  | 清新白桃糖       | ic_stuff_16  | 14     |


### （三）票务表（tickets）
#### 表结构
| 字段名       | 数据类型         | 约束条件       | 描述         |
|--------------|------------------|----------------|--------------|
| id           | int(11)          | 主键，自增     | 唯一标识     |
| type         | text             | 非空           | 票务类型（CONCERT/	MOVIE/MUSIC/COMEDY） |
| title        | text             | 非空           | 票务名称     |
| image_res_id | text             | 可为空         | 票务图片资源ID |
| score        | text             | 可为空         | 评分/热度     |
| content1     | text             | 可为空         | 详情1（如时间） |
| content2     | text             | 可为空         | 详情2（如地点） |
| price        | double           | 可为空         | 价格         |

#### 表数据（部分示例）
| id  | type     | title                 | image_res_id    | score          | content1                          | content2                          | price  |
|-----|----------|-----------------------|-----------------|----------------|-----------------------------------|-----------------------------------|--------|
| 1   | CONCERT  | 林俊杰20世界巡回演唱会 | concert_lin     | 热度：189234   | 时间: 2025.07.20 周六 19:30       | 地点: 国家体育场（鸟巢）          | 880    |
| 7   | MOVIE    | 哆啦A梦               | movie_doraemon  | 评分：9.2      | 导演：山崎贵                      | 简介：讲述哆啦A梦和大雄一行人全新的奇妙冒险故事... | 39.9   |
| 13  | MUSIC    | 海音音乐节            | music_oceanmusic| 热度：9.0      | 时间: 2025.07.18 周五 18:00       | 地点: 城市滨海公园露天广场        | 299    |
| 17  | COMEDY   | 明天会好的脱口秀       | comedy_tomorrowcomedy | 热度：9.1   | 时间: 2025.07.05 周六 19:30       | 地点: 城市喜剧小剧场（XX路店）    | 89     |


### （四）用户表（user）
#### 表结构
| 字段名       | 数据类型         | 约束条件       | 描述         |
|--------------|------------------|----------------|--------------|
| id           | int(11)          | 主键，自增     | 唯一标识     |
| username     | varchar(80)      | 非空，唯一     | 用户名       |
| email        | varchar(120)     | 非空，唯一     | 邮箱         |
| password     | varchar(128)     | 可为空         | 密码         |
| phone        | varchar(20)      | 可为空         | 手机号       |
| address      | text             | 可为空         | 地址         |
| is_admin     | tinyint(1)       | 默认为0        | 是否为管理员（0=普通用户，1=管理员） |

#### 表数据
| id  | username | email              | password   | phone | address | is_admin |
|-----|----------|--------------------|------------|-------|---------|----------|
| 6   | testuser | test@example.com   | testpassword | NULL  | NULL    | 0        |
| 20  | xiaoyoe  | xiaoyoe@qq.com     | 123456     | NULL  | NULL    | 0        |


## 三、数据库说明
1. **表关联关系**：当前各表通过主键（id）独立存在，暂无外键关联，可根据业务需求添加关联字段（如用户订单表关联用户id和票务id）。
2. **数据特点**：
   - **轮播图表**：用于展示热门活动/电影的宣传图，标题直接关联票务表中的活动名称。
   - **商品表**：包含零食、周边等商品，积分可用于兑换或消费。
   - **票务表**：覆盖演唱会、电影、音乐节、脱口秀四类活动，包含时间、地点、价格等核心信息。
   - **用户表**：记录用户基本信息，`is_admin`字段用于区分用户权限。
3. **潜在扩展方向**：
   - 添加订单表（order），关联用户、票务、商品，记录购买信息。
   - 为票务表增加库存字段（stock），支持在线选座功能。
   - 在用户表中添加积分字段（user_points），关联商品表的积分兑换逻辑。

/*
 Navicat Premium Dump SQL

 Source Server         : mydb
 Source Server Type    : MySQL
 Source Server Version : 50720 (5.7.20-log)
 Source Host           : localhost:3306
 Source Schema         : db_ticket

 Target Server Type    : MySQL
 Target Server Version : 50720 (5.7.20-log)
 File Encoding         : 65001

 Date: 05/06/2025 11:08:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for carousel
-- ----------------------------
DROP TABLE IF EXISTS `carousel`;
CREATE TABLE `carousel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image_res_id` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of carousel
-- ----------------------------
INSERT INTO `carousel` VALUES (1, '《逆转杀局》续作', '', 'banner01.jpg');
INSERT INTO `carousel` VALUES (2, '《消失的她》朱一龙、倪妮主演', '', 'banner04.jpg');
INSERT INTO `carousel` VALUES (3, '开榜封神：寻榜99行', '', 'banner03.jpg');
INSERT INTO `carousel` VALUES (4, '海贼王 航海行动!!!', '', 'banner05.jpg');
INSERT INTO `carousel` VALUES (5, '2025年度动作大片 电影热潮', '', 'banner02.jpg');

-- ----------------------------
-- Table structure for stuffs
-- ----------------------------
DROP TABLE IF EXISTS `stuffs`;
CREATE TABLE `stuffs`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image_res_id` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `points` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stuffs
-- ----------------------------
INSERT INTO `stuffs` VALUES (1, '爆米花（大）', 'ic_stuff_1', 80);
INSERT INTO `stuffs` VALUES (2, '爆米花（小）', 'ic_stuff_2', 50);
INSERT INTO `stuffs` VALUES (3, '可口可乐', 'ic_stuff_3', 20);
INSERT INTO `stuffs` VALUES (4, '雪碧', 'ic_stuff_4', 20);
INSERT INTO `stuffs` VALUES (5, '芬达', 'ic_stuff_5', 20);
INSERT INTO `stuffs` VALUES (9, '豆鱼雷钥匙扣..', 'ic_stuff_9', 15);
INSERT INTO `stuffs` VALUES (10, '豆鱼钥匙扣', 'ic_stuff_10', 12);
INSERT INTO `stuffs` VALUES (11, '可爱小人钥匙扣', 'ic_stuff_11', 18);
INSERT INTO `stuffs` VALUES (12, 'sample短袖', 'ic_stuff_12', 25);
INSERT INTO `stuffs` VALUES (13, 'mini甜点杯', 'ic_stuff_13', 10);
INSERT INTO `stuffs` VALUES (14, '一只奶糖鼠', 'ic_stuff_14', 16);
INSERT INTO `stuffs` VALUES (15, '旺旺黑白配焦糖', 'ic_stuff_15', 8);
INSERT INTO `stuffs` VALUES (16, '清新白桃糖', 'ic_stuff_16', 14);

-- ----------------------------
-- Table structure for tickets
-- ----------------------------
DROP TABLE IF EXISTS `tickets`;
CREATE TABLE `tickets`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image_res_id` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `score` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `content1` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `content2` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `price` double NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tickets
-- ----------------------------
INSERT INTO `tickets` VALUES (1, 'CONCERT', '林俊杰20世界巡回演唱会', 'concert_lin', '热度：189234', '时间: 2025.07.20 周六 19:30', '地点: 国家体育场（鸟巢）', 880);
INSERT INTO `tickets` VALUES (2, 'CONCERT', '更好2024跨年演唱会', 'concert_geng', '热度：167890', '时间: 2025.12.31 周二 20:00', '地点: 梅赛德斯 - 奔驰文化中心', 699);
INSERT INTO `tickets` VALUES (3, 'CONCERT', '李克勤演唱会', 'concert_li', '热度：145678', '时间: 2025.08.15 周五 19:30', '地点: 广州体育馆', 580);
INSERT INTO `tickets` VALUES (4, 'CONCERT', '薛之谦天外来物巡回演唱会', 'concert_xue', '热度：178901', '时间: 2025.09.22 周一 19:00', '地点: 上海体育场', 799);
INSERT INTO `tickets` VALUES (5, 'CONCERT', '张韶涵演唱会', 'concert_zhang', '热度：156789', '时间: 2025.10.18 周六 19:30', '地点: 成都凤凰山体育中心', 620);
INSERT INTO `tickets` VALUES (6, 'CONCERT', '缘来有你全明星演唱会', 'concert_yuan', '热度：134567', '时间: 2025.11.11 周二 19:30', '地点: 杭州奥体中心体育馆', 650);
INSERT INTO `tickets` VALUES (7, 'MOVIE', '哆啦A梦', 'movie_doraemon', '评分：9.2', '导演：山崎贵', '简介：讲述哆啦A梦和大雄一行人全新的奇妙冒险故事，穿梭于奇妙世界，遭遇各种神奇生物与挑战，一起守护珍贵的友谊与梦想！', 39.9);
INSERT INTO `tickets` VALUES (8, 'MOVIE', '你的名字', 'movie_yourname', '评分：9.0', '导演：新海诚', '简介：在奇妙的时空交错中，男女主角寻找彼此、探寻真相，邂逅浪漫与感动，书写一段跨越时空的青春故事，画面唯美，情感真挚。', 35.5);
INSERT INTO `tickets` VALUES (9, 'MOVIE', '你想活出什么样的人生', 'movie_whatlife', '评分：8.8', '导演：宫崎骏', '简介：少年在成长旅程中，面对困惑与选择，在奇幻经历里感悟人生意义，跟随主角一起思考“想活出什么样的人生”，充满哲理与温情。', 42);
INSERT INTO `tickets` VALUES (10, 'MOVIE', '神偷奶爸4', 'movie_despicableme4', '评分：8.7', '导演：皮艾尔·柯芬', '简介：格鲁一家再启欢乐冒险，新反派登场制造混乱，小黄人们继续搞怪，还有精彩的特工行动与亲情故事，笑点与燃点并存。', 38);
INSERT INTO `tickets` VALUES (11, 'MOVIE', '理查大冒险', 'movie_richadadventure', '评分：8.5', '导演：托比·格恩科尔', '简介：小鸟理查离开舒适区，踏上充满未知的冒险之旅，在过程中结识伙伴、突破自我，经历刺激挑战，收获成长与勇气。', 33);
INSERT INTO `tickets` VALUES (12, 'MOVIE', '熊出没', 'movie_booniebears', '评分：8.9', '导演：林汇达', '简介：熊大、熊二和光头强又有新故事，在奇妙场景中遭遇新危机，凭借勇气与智慧化解难题，延续系列的欢乐与温馨，适合全家观看。', 36);
INSERT INTO `tickets` VALUES (13, 'MUSIC', '海音音乐节', 'music_oceanmusic', '热度：9.0', '时间: 2025.07.18 周五 18:00', '地点: 城市滨海公园露天广场', 299);
INSERT INTO `tickets` VALUES (14, 'MUSIC', '夏日潮玩', 'music_summerfun', '热度：8.8', '时间: 2025.08.02 周六 17:30', '地点: 市中心文化创意园区广场', 269);
INSERT INTO `tickets` VALUES (15, 'MUSIC', '音乐狂欢节', 'music_musiccarnival', '热度：9.2', '时间: 2025.09.13 周五 19:00', '地点: 大型体育中心室外场地', 329);
INSERT INTO `tickets` VALUES (16, 'MUSIC', '2023音你而乐音乐节', 'music_musicforyou2023', '热度：8.7', '时间: 2025.10.25 周六 16:30', '地点: 郊外生态音乐谷场地', 289);
INSERT INTO `tickets` VALUES (17, 'COMEDY', '明天会好的脱口秀', 'comedy_tomorrowcomedy', '热度：9.1', '时间: 2025.07.05 周六 19:30', '地点: 城市喜剧小剧场（XX路店）', 89);
INSERT INTO `tickets` VALUES (18, 'COMEDY', '健康脱口秀', 'comedy_healthcomedy', '热度：8.8', '时间: 2025.07.12 周六 20:00', '地点: 创意园区喜剧展演空间', 79);
INSERT INTO `tickets` VALUES (19, 'COMEDY', '脱口秀大会5', 'comedy_talkshow5', '热度：9.3', '时间: 2025.07.19 周六 19:00', '地点: 大型演艺场馆喜剧专区', 129);
INSERT INTO `tickets` VALUES (20, 'COMEDY', '脱口秀反跨年', 'comedy_tiny', '热度：9.0', '时间: 2025.12.31 周二 21:00', '地点: 市中心体育馆（跨年专场）', 159);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `is_admin` tinyint(1) NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (6, 'testuser', 'test@example.com', 'testpassword', NULL, NULL, 0);
INSERT INTO `user` VALUES (20, 'xiaoyoe', 'xiaoyoe@qq.com', '123456', NULL, NULL, 0);

SET FOREIGN_KEY_CHECKS = 1;

