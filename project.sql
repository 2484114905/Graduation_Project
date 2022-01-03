/*
 Navicat Premium Data Transfer

 Source Server         : demo1
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : project

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 04/06/2021 10:02:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for login_info
-- ----------------------------
DROP TABLE IF EXISTS `login_info`;
CREATE TABLE `login_info`  (
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `device_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `login_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for raw_image
-- ----------------------------
DROP TABLE IF EXISTS `raw_image`;
CREATE TABLE `raw_image`  (
  `image_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `content` longblob NULL,
  `judge_result` tinyint(1) NULL DEFAULT NULL,
  `image_shape` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `create_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`image_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for result_image
-- ----------------------------
DROP TABLE IF EXISTS `result_image`;
CREATE TABLE `result_image`  (
  `image_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `parent_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `raw_content` longblob NOT NULL,
  `segment_content` longblob NOT NULL,
  `judge_result` int(1) NOT NULL,
  `raw_image_shape` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `segment_image_shape` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`image_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `user_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varbinary(255) NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Function structure for add_user
-- ----------------------------
DROP FUNCTION IF EXISTS `add_user`;
delimiter ;;
CREATE FUNCTION `add_user`(name VARCHAR(20), insert_password VARCHAR(20))
 RETURNS int(11)
BEGIN
	#Routine body goes here...
	INSERT INTO `user`(username, password) VALUES(name, insert_password);

	RETURN 0;
END
;;
delimiter ;

-- ----------------------------
-- Function structure for update_user
-- ----------------------------
DROP FUNCTION IF EXISTS `update_user`;
delimiter ;;
CREATE FUNCTION `update_user`(name VARCHAR(20), new_password VARCHAR(20))
 RETURNS int(11)
BEGIN
	#Routine body goes here...
	UPDATE `user`
	set PASSWORD = new_password
	WHERE username = name;

	RETURN 0;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table raw_image
-- ----------------------------
DROP TRIGGER IF EXISTS `set_iameg_id`;
delimiter ;;
CREATE TRIGGER `set_iameg_id` BEFORE INSERT ON `raw_image` FOR EACH ROW IF new.image_id is NULL THEN
		SET new.image_id = UUID();
END IF
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table result_image
-- ----------------------------
DROP TRIGGER IF EXISTS `set_result_image_id2`;
delimiter ;;
CREATE TRIGGER `set_result_image_id2` BEFORE INSERT ON `result_image` FOR EACH ROW IF new.image_id is NULL THEN
		SET new.image_id = UUID();
END IF
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user
-- ----------------------------
DROP TRIGGER IF EXISTS `encrypt`;
delimiter ;;
CREATE TRIGGER `encrypt` BEFORE INSERT ON `user` FOR EACH ROW set new.`password` = AES_ENCRYPT(new.`password`, 'key')
;
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user
-- ----------------------------
DROP TRIGGER IF EXISTS `set_uuid`;
delimiter ;;
CREATE TRIGGER `set_uuid` BEFORE INSERT ON `user` FOR EACH ROW BEGIN
IF new.user_id is NULL THEN
		SET new.user_id = UUID();
END IF; 
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user
-- ----------------------------
DROP TRIGGER IF EXISTS `encrypt2`;
delimiter ;;
CREATE TRIGGER `encrypt2` BEFORE UPDATE ON `user` FOR EACH ROW set new.`password` = AES_ENCRYPT(new.`password`, 'key')
;
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
