INSERT INTO user (username,password,testpswd) VALUES ('sxyu','1233210',AES_ENCRYPT('1233210','key'));

CREATE TRIGGER `set_uuid` BEFORE INSERT ON `user` FOR EACH ROW BEGIN
IF new.user_id is NULL THEN
		SET new.user_id = UUID();
END IF;
END;