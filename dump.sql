-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: math
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `math`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `math` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `math`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add photo',8,'add_photo'),(23,'Can change photo',8,'change_photo'),(24,'Can delete photo',8,'delete_photo'),(25,'Can add answer',9,'add_answer'),(26,'Can change answer',9,'change_answer'),(27,'Can delete answer',9,'delete_answer'),(28,'Can add problem',10,'add_problem'),(29,'Can change problem',10,'change_problem'),(30,'Can delete problem',10,'delete_problem'),(31,'Can add rating',11,'add_rating'),(32,'Can change rating',11,'change_rating'),(33,'Can delete rating',11,'delete_rating'),(34,'Can add problem unit',12,'add_problemunit'),(35,'Can change problem unit',12,'change_problemunit'),(36,'Can delete problem unit',12,'delete_problemunit'),(37,'Can add test',13,'add_test'),(38,'Can change test',13,'change_test'),(39,'Can delete test',13,'delete_test'),(40,'Can add board',14,'add_board'),(41,'Can change board',14,'change_board'),(42,'Can delete board',14,'delete_board'),(43,'Can add answer num',15,'add_answernum'),(44,'Can change answer num',15,'change_answernum'),(45,'Can delete answer num',15,'delete_answernum'),(46,'Can add comment',16,'add_comment'),(47,'Can change comment',16,'change_comment'),(48,'Can delete comment',16,'delete_comment'),(49,'Can add score',17,'add_score'),(50,'Can change score',17,'change_score'),(51,'Can delete score',17,'delete_score'),(52,'Can add recommend',18,'add_recommend'),(53,'Can change recommend',18,'change_recommend'),(54,'Can delete recommend',18,'delete_recommend'),(55,'Can add problem small unit',19,'add_problemsmallunit'),(56,'Can change problem small unit',19,'change_problemsmallunit'),(57,'Can delete problem small unit',19,'delete_problemsmallunit'),(58,'Can add problem middle unit',20,'add_problemmiddleunit'),(59,'Can change problem middle unit',20,'change_problemmiddleunit'),(60,'Can delete problem middle unit',20,'delete_problemmiddleunit'),(61,'Can add lecture',21,'add_lecture'),(62,'Can change lecture',21,'change_lecture'),(63,'Can delete lecture',21,'delete_lecture');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$HHjVAzbX5Wqq$eiey+Om5Urne3+1gAIO7RS0XWGTIB5LWj66ykjNcJG8=','2018-03-28 16:55:05.270832',1,'wonhyukcho','','','whcho888@gmail.com',1,1,'2018-03-12 01:12:18.905210');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-03-12 01:12:30.540057','1','수1',1,'[{\"added\": {}}]',12,1),(2,'2018-03-12 01:12:35.582575','2','수2',1,'[{\"added\": {}}]',12,1),(3,'2018-03-12 01:12:39.255909','3','미적1',1,'[{\"added\": {}}]',12,1),(4,'2018-03-12 01:12:44.449134','4','미적2',1,'[{\"added\": {}}]',12,1),(5,'2018-03-12 01:12:49.401656','5','확통',1,'[{\"added\": {}}]',12,1),(6,'2018-03-12 01:12:54.866344','6','기벡',1,'[{\"added\": {}}]',12,1),(7,'2018-03-15 23:40:39.506606','5','5',2,'[{\"changed\": {\"fields\": [\"name\", \"type\", \"problems\"]}}]',13,1),(8,'2018-03-17 23:43:24.450650','5','$f(n)=\\frac{1^{2}+2^{2}+3^{2}+ … +{n}^{2}}{3+5+7+…+(2n+1)}$ 일때, $\\lim\\limits_{n \\to \\infty} \\frac{f(n)}{n}$ 의 값은?\n',3,'',10,1),(9,'2018-03-17 23:43:24.453310','4','$f(n)=\\frac{1^{2}+2^{2}+3^{2}+ … +{n}^{2}}{3+5+7+…+(2n+1)}$ 일때, $\\lim\\limits_{n \\to \\infty} \\frac{f(n)}{n}$ 의 값은?\n',3,'',10,1),(10,'2018-03-17 23:43:24.457437','3','$f(n)=\\frac{1^{2}+2^{2}+3^{2}+ … +{n}^{2}}{3+5+7+…+(2n+1)}$ 일때, $\\lim\\limits_{n \\to \\infty} \\frac{f(n)}{n}$ 의 값은?\n',3,'',10,1),(11,'2018-03-17 23:43:24.458833','2','$f(n)=\\frac{1^{2}+2^{2}+3^{2}+ … +{n}^{2}}{3+5+7+…+(2n+1)}$ 일때, $\\lim\\limits_{n \\to \\infty} \\frac{f(n)}{n}$ 의 값은?\n',3,'',10,1),(12,'2018-03-17 23:43:24.461352','1','$f(n)=\\frac{1^{2}+2^{2}+3^{2}+ … +{n}^{2}}{3+5+7+…+(2n+1)}$ 일때, $\\lim\\limits_{n \\to \\infty} \\frac{f(n)}{n}$ 의 값은?\n',3,'',10,1),(13,'2018-03-18 22:39:38.996605','1','1',2,'[{\"changed\": {\"fields\": [\"user\"]}}]',11,1),(14,'2018-03-18 22:39:45.416679','2','2',2,'[{\"changed\": {\"fields\": [\"user\"]}}]',11,1),(15,'2018-03-18 22:39:50.938743','3','3',2,'[{\"changed\": {\"fields\": [\"user\"]}}]',11,1),(16,'2018-03-18 22:39:56.078136','4','4',2,'[{\"changed\": {\"fields\": [\"user\"]}}]',11,1),(17,'2018-03-18 22:40:01.602508','5','5',2,'[{\"changed\": {\"fields\": [\"user\"]}}]',11,1),(18,'2018-03-19 20:23:05.071070','5','5',2,'[{\"changed\": {\"fields\": [\"scores\"]}}]',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(9,'math_problem_app','answer'),(15,'math_problem_app','answernum'),(14,'math_problem_app','board'),(16,'math_problem_app','comment'),(21,'math_problem_app','lecture'),(8,'math_problem_app','photo'),(10,'math_problem_app','problem'),(20,'math_problem_app','problemmiddleunit'),(19,'math_problem_app','problemsmallunit'),(12,'math_problem_app','problemunit'),(11,'math_problem_app','rating'),(18,'math_problem_app','recommend'),(17,'math_problem_app','score'),(13,'math_problem_app','test'),(7,'math_problem_app','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4hv4vqn3ohk9amrgg5ekbggak81i53ub','OTViNGE2MTAwMzYzZDFjY2YxM2Y5YjUwYTlmZGEzZmMzYzZjOWMzNjp7InRlc3RTcmwiOjI3LCJ1c2VySWQiOiJhZG1pbiIsInVzZXJTcmwiOjEsIl9zZXNzaW9uX2V4cGlyeSI6NjA0ODAwfQ==','2018-04-04 16:32:24.628310'),('f4di7hzxgw32u2vjdz62w81xj0xfb4q4','NjFjMWY4Y2Q0MDQ2YzUwOTUxMDJhNWYwYzFjMmZlYzM4YjJlMDAzMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MDQ4MDAsIl9hdXRoX3VzZXJfaGFzaCI6IjE3NDg1ZTc1MTJlNDE2YzI5MjUwYTc1MjhiNDQzOTVkZGUwOWEwNmMiLCJ1c2VyU3JsIjoxLCJ1c2VySWQiOiJ3aGNobzg4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJrZXkiOjM2MTIsInRlc3RTcmwiOjUsInByb2JsZW1TcmwiOm51bGx9','2018-04-05 00:09:13.561660'),('hmc1038qq6kx1ha58bcyrd3voh16jnaw','NjJhYjdlZWEzOGNhYzEwNDlmZDc4ZDliY2RlNmFjZDE5YTE2OWM4Mzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTc0ODVlNzUxMmU0MTZjMjkyNTBhNzUyOGI0NDM5NWRkZTA5YTA2YyIsIl9hdXRoX3VzZXJfaWQiOiIxIiwidXNlclNybCI6MSwidXNlcklkIjoiYWRtaW4iLCJfc2Vzc2lvbl9leHBpcnkiOjYwNDgwMH0=','2018-04-04 16:55:05.273989'),('it0iia8s6hf2u9qb9fkp106oki9zlm0c','OGQ3NzJkMjc2NGQwODRkZGRmYThjNTVmYWEzMTY4NDgwNzQ4ZjhjNjp7Il9zZXNzaW9uX2V4cGlyeSI6NjA0ODAwLCJ1c2VySWQiOiJvc2lyaXNrZ24ifQ==','2018-03-19 23:55:38.547631'),('na25480j7nb7wlkir07mj9zh47ow3h04','OGM2YWRhZWM4ZTQ3ZTBlYWMxNGEwYmVjYWQxYWY1NGE2YzM4YjExOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwidGVzdFNybCI6NSwiX2F1dGhfdXNlcl9oYXNoIjoiMTc0ODVlNzUxMmU0MTZjMjkyNTBhNzUyOGI0NDM5NWRkZTA5YTA2YyIsInVzZXJJZCI6Im9zaXJpc2tnbiIsIl9zZXNzaW9uX2V4cGlyeSI6NjA0ODAwLCJfYXV0aF91c2VyX2lkIjoiMSJ9','2018-03-23 21:50:08.263643'),('ukid4jb71to4o0tcjzmhf9vrjgmzu8ec','NDcxY2QzNDM0MWJjZTJjYmQ5NDFlZmQ2ZmVlNzMzOTExZDA1ZDg0NTp7InVzZXJJZCI6Im9zaXJpc2tnbiIsInRlc3RTcmwiOjV9','2018-04-04 14:54:01.244247'),('uzoyf968sbuh617mdy07buoedyxzr74e','ZjMxYTA1NDNlNjA3Y2U3MzU2YzIxZjU2ZTEwY2FiYzgyZTU3NjliYzp7InRlc3RTcmwiOjUsInVzZXJJZCI6Im9zaXJpc2tnbiJ9','2018-04-01 19:59:49.116510'),('xc04ptbcky88vwtyrj8wemdgx3vcv24d','NWNjNTU2ZWQ3MzY3MjY1Y2Y4MTRmNmE4NjgzMTIwZDkzODM1MjliYTp7ImtleSI6NzU5NiwidXNlcklkIjoicmxhd2pkZ25zNDM0In0=','2018-03-29 19:39:44.095791');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_answer`
--

DROP TABLE IF EXISTS `math_problem_app_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_answer` (
  `answerSrl` int(11) NOT NULL AUTO_INCREMENT,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`answerSrl`),
  KEY `math_problem_app_ans_test_id_8678cee3_fk_math_prob` (`test_id`),
  CONSTRAINT `math_problem_app_ans_test_id_8678cee3_fk_math_prob` FOREIGN KEY (`test_id`) REFERENCES `math_problem_app_test` (`testSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_answer`
--

LOCK TABLES `math_problem_app_answer` WRITE;
/*!40000 ALTER TABLE `math_problem_app_answer` DISABLE KEYS */;
INSERT INTO `math_problem_app_answer` VALUES (1,'2018-03-15 23:41:08.965922','2018-03-15 23:41:09.003437',5),(2,'2018-03-15 23:45:17.878760','2018-03-15 23:45:17.914960',5),(3,'2018-03-16 15:31:02.435578','2018-03-16 15:31:02.462656',5),(4,'2018-03-16 21:50:00.728114','2018-03-16 21:50:00.757334',5),(5,'2018-03-17 01:45:43.740127','2018-03-17 01:45:43.767685',5),(6,'2018-03-17 23:42:58.872395','2018-03-17 23:42:58.909110',1),(7,'2018-03-17 23:43:58.443001','2018-03-17 23:43:58.479666',1),(8,'2018-03-17 23:48:11.850105','2018-03-17 23:48:11.879811',1),(9,'2018-03-17 23:50:52.270366','2018-03-17 23:50:52.298912',1),(10,'2018-03-18 00:04:11.593015','2018-03-18 00:04:11.663541',1),(11,'2018-03-18 19:58:51.383028','2018-03-18 19:58:51.410402',5),(12,'2018-03-18 19:58:56.563386','2018-03-18 19:58:56.593324',5),(13,'2018-03-19 20:21:49.587240','2018-03-19 20:21:49.610707',5),(14,'2018-03-19 20:23:10.949017','2018-03-19 20:23:10.977204',5),(15,'2018-03-21 15:22:48.838093','2018-03-21 15:22:48.864144',5),(16,'2018-03-22 00:51:55.238240','2018-03-22 00:51:55.271495',15),(17,'2018-03-22 14:30:31.748591','2018-03-22 14:30:31.779824',5),(18,'2018-03-25 02:08:55.451114','2018-03-25 02:08:55.451134',5),(19,'2018-03-29 00:06:52.822209','2018-03-29 00:06:52.854652',5),(20,'2018-03-29 00:09:22.270042','2018-03-29 00:09:22.295374',5);
/*!40000 ALTER TABLE `math_problem_app_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_answer_answers`
--

DROP TABLE IF EXISTS `math_problem_app_answer_answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_answer_answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_id` int(11) NOT NULL,
  `answernum_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_answer__answer_id_answernum_id_4f339415_uniq` (`answer_id`,`answernum_id`),
  KEY `math_problem_app_ans_answernum_id_ca4d42cc_fk_math_prob` (`answernum_id`),
  CONSTRAINT `math_problem_app_ans_answer_id_ffd3bef8_fk_math_prob` FOREIGN KEY (`answer_id`) REFERENCES `math_problem_app_answer` (`answerSrl`),
  CONSTRAINT `math_problem_app_ans_answernum_id_ca4d42cc_fk_math_prob` FOREIGN KEY (`answernum_id`) REFERENCES `math_problem_app_answernum` (`answerNumSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_answer_answers`
--

LOCK TABLES `math_problem_app_answer_answers` WRITE;
/*!40000 ALTER TABLE `math_problem_app_answer_answers` DISABLE KEYS */;
INSERT INTO `math_problem_app_answer_answers` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,3,11),(12,3,12),(13,3,13),(14,3,14),(15,3,15),(16,4,16),(17,4,17),(18,4,18),(19,4,19),(20,4,20),(21,5,21),(22,5,22),(23,5,23),(24,5,24),(25,5,25),(26,6,26),(27,6,27),(28,6,28),(29,6,29),(30,6,30),(31,7,31),(32,7,32),(33,7,33),(34,7,34),(35,7,35),(36,8,36),(37,8,37),(38,8,38),(39,8,39),(40,8,40),(41,9,41),(42,9,42),(43,9,43),(44,9,44),(45,9,45),(46,10,46),(47,10,47),(48,10,48),(49,10,49),(50,10,50),(51,10,51),(52,10,52),(53,10,53),(54,10,54),(55,10,55),(56,10,56),(57,10,57),(58,10,58),(59,10,59),(60,10,60),(61,11,61),(62,11,62),(63,11,63),(64,11,64),(65,11,65),(66,12,66),(67,12,67),(68,12,68),(69,12,69),(70,12,70),(71,13,71),(72,13,72),(73,13,73),(74,13,74),(75,13,75),(76,14,76),(77,14,77),(78,14,78),(79,14,79),(80,14,80),(81,15,81),(82,15,82),(83,15,83),(84,15,84),(85,15,85),(86,16,86),(87,16,87),(88,16,88),(89,16,89),(90,16,90),(91,17,91),(92,17,92),(93,17,93),(94,17,94),(95,17,95),(96,19,96),(97,19,97),(98,19,98),(99,19,99),(100,19,100),(101,20,101),(102,20,102),(103,20,103),(104,20,104),(105,20,105);
/*!40000 ALTER TABLE `math_problem_app_answer_answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_answernum`
--

DROP TABLE IF EXISTS `math_problem_app_answernum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_answernum` (
  `answerNumSrl` int(11) NOT NULL AUTO_INCREMENT,
  `answer` int(11) DEFAULT NULL,
  PRIMARY KEY (`answerNumSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_answernum`
--

LOCK TABLES `math_problem_app_answernum` WRITE;
/*!40000 ALTER TABLE `math_problem_app_answernum` DISABLE KEYS */;
INSERT INTO `math_problem_app_answernum` VALUES (1,4),(2,3),(3,2),(4,2),(5,1),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,2),(13,4),(14,4),(15,3),(16,3),(17,5),(18,4),(19,3),(20,3),(21,3),(22,4),(23,5),(24,4),(25,4),(26,2),(27,4),(28,3),(29,3),(30,4),(31,3),(32,3),(33,3),(34,3),(35,3),(36,3),(37,4),(38,3),(39,3),(40,3),(41,2),(42,4),(43,3),(44,2),(45,4),(46,3),(47,3),(48,3),(49,3),(50,3),(51,3),(52,3),(53,3),(54,3),(55,3),(56,4),(57,3),(58,3),(59,3),(60,3),(61,3),(62,3),(63,2),(64,2),(65,2),(66,3),(67,3),(68,2),(69,2),(70,2),(71,1),(72,3),(73,3),(74,3),(75,3),(76,1),(77,3),(78,3),(79,3),(80,3),(81,1),(82,2),(83,3),(84,4),(85,5),(86,3),(87,3),(88,4),(89,3),(90,4),(91,1),(92,2),(93,2),(94,2),(95,3),(96,1),(97,3),(98,1),(99,2),(100,3),(101,1),(102,3),(103,1),(104,3),(105,1);
/*!40000 ALTER TABLE `math_problem_app_answernum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_board`
--

DROP TABLE IF EXISTS `math_problem_app_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_board` (
  `boardSrl` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) DEFAULT NULL,
  `text` longtext,
  `viewCnt` int(11) DEFAULT NULL,
  `recommendCnt` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `writer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`boardSrl`),
  KEY `math_problem_app_boa_writer_id_517b281a_fk_math_prob` (`writer_id`),
  CONSTRAINT `math_problem_app_boa_writer_id_517b281a_fk_math_prob` FOREIGN KEY (`writer_id`) REFERENCES `math_problem_app_user` (`userSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_board`
--

LOCK TABLES `math_problem_app_board` WRITE;
/*!40000 ALTER TABLE `math_problem_app_board` DISABLE KEYS */;
INSERT INTO `math_problem_app_board` VALUES (1,'이번 수능 입시에서 000이 중요하다고 하드라구요.	','이번 수능 입시에서 000이 중요하다고 하드라구요.	',1,0,1,'2018-03-10 18:13:00.847486','2018-03-14 01:06:53.249850',1),(2,'이번 수능 입시에서 000이 중요하다고 하드라구요.	','이번 수능 입시에서 000이 중요하다고 하드라구요.	',5,0,1,'2018-03-11 03:14:01.429564','2018-03-18 14:28:34.212761',1),(3,'이번 수능 입시에서 000이 중요하다고 하드라구요.	','이번 수능 입시에서 000이 중요하다고 하드라구요.	',2,0,3,'2018-03-11 03:14:35.270958','2018-03-19 20:23:36.048697',1),(4,'이번 수능 입시에서 000이 중요하다고 하드라구요.	','이번 수능 입시에서 000이 중요하다고 하드라구요.	',3,0,2,'2018-03-11 03:14:40.480492','2018-03-28 17:26:23.260303',1),(5,'test2','test23',4,0,3,'2018-03-14 01:07:22.273235','2018-03-16 16:06:11.744351',1),(6,'123121','2312',2,0,3,'2018-03-15 22:47:53.615565','2018-03-16 21:50:57.979710',2);
/*!40000 ALTER TABLE `math_problem_app_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_board_comments`
--

DROP TABLE IF EXISTS `math_problem_app_board_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_board_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `board_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_board_c_board_id_comment_id_e6b146dd_uniq` (`board_id`,`comment_id`),
  KEY `math_problem_app_boa_comment_id_96230d53_fk_math_prob` (`comment_id`),
  CONSTRAINT `math_problem_app_boa_board_id_1dba36ef_fk_math_prob` FOREIGN KEY (`board_id`) REFERENCES `math_problem_app_board` (`boardSrl`),
  CONSTRAINT `math_problem_app_boa_comment_id_96230d53_fk_math_prob` FOREIGN KEY (`comment_id`) REFERENCES `math_problem_app_comment` (`commentSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_board_comments`
--

LOCK TABLES `math_problem_app_board_comments` WRITE;
/*!40000 ALTER TABLE `math_problem_app_board_comments` DISABLE KEYS */;
INSERT INTO `math_problem_app_board_comments` VALUES (2,1,2),(5,2,5),(8,2,8),(3,3,3),(7,6,7);
/*!40000 ALTER TABLE `math_problem_app_board_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_comment`
--

DROP TABLE IF EXISTS `math_problem_app_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_comment` (
  `commentSrl` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `writer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`commentSrl`),
  KEY `math_problem_app_com_writer_id_fea630ad_fk_math_prob` (`writer_id`),
  CONSTRAINT `math_problem_app_com_writer_id_fea630ad_fk_math_prob` FOREIGN KEY (`writer_id`) REFERENCES `math_problem_app_user` (`userSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_comment`
--

LOCK TABLES `math_problem_app_comment` WRITE;
/*!40000 ALTER TABLE `math_problem_app_comment` DISABLE KEYS */;
INSERT INTO `math_problem_app_comment` VALUES (1,'test','2018-03-14 01:06:56.529856','2018-03-14 01:06:56.532736',1),(2,'test2','2018-03-14 01:07:03.195956','2018-03-14 01:07:03.199454',1),(3,'test','2018-03-14 01:07:11.293607','2018-03-14 01:07:11.296052',1),(4,'','2018-03-14 01:07:29.139542','2018-03-16 16:06:01.250337',2),(5,'그런가여?','2018-03-15 19:41:37.488879','2018-03-15 19:41:37.491350',3),(6,'','2018-03-15 22:48:00.731686','2018-03-16 16:06:00.277564',2),(7,'','2018-03-16 21:51:01.582370','2018-03-16 21:51:06.592698',2),(8,'','2018-03-18 14:28:43.787572','2018-03-18 14:28:44.837173',2);
/*!40000 ALTER TABLE `math_problem_app_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_lecture`
--

DROP TABLE IF EXISTS `math_problem_app_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_lecture` (
  `lectureSrl` int(11) NOT NULL AUTO_INCREMENT,
  `video` varchar(300) DEFAULT NULL,
  `teacherName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lectureSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_lecture`
--

LOCK TABLES `math_problem_app_lecture` WRITE;
/*!40000 ALTER TABLE `math_problem_app_lecture` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_lecture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_photo`
--

DROP TABLE IF EXISTS `math_problem_app_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_photo` (
  `photoSrl` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(300) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`photoSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_photo`
--

LOCK TABLES `math_problem_app_photo` WRITE;
/*!40000 ALTER TABLE `math_problem_app_photo` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problem`
--

DROP TABLE IF EXISTS `math_problem_app_problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problem` (
  `problemSrl` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(2000) DEFAULT NULL,
  `answer` int(11) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `difficulty` int(11) DEFAULT NULL,
  `type1` int(11) DEFAULT NULL,
  `type2` int(11) DEFAULT NULL,
  `explanation` longtext,
  `answerType` int(11),
  `rightAnswered` int(11) NOT NULL,
  `totalAnswered` int(11) NOT NULL,
  PRIMARY KEY (`problemSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problem`
--

LOCK TABLES `math_problem_app_problem` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problem` DISABLE KEYS */;
INSERT INTO `math_problem_app_problem` VALUES (6,'$f(n)=\\frac{1^{2}+2^{2}+3^{2}+ … +{n}^{2}}{3+5+7+…+(2n+1)}$ 일때, $\\lim\\limits_{n \\to \\infty} \\frac{f(n)}{n}$ 의 값은?\n',3,'2018-03-12 01:14:27.301108','2018-03-22 00:51:55.283230',2,1,2,'',1,4,6),(7,'부등식$\\begin{cases}{x-2\\over6}\\le{{x\\over2}-{2x-4\\over3}}\\le{{x\\over3}-{1\\over6}}\\\\|x+3|+|x|\\ge1\\end{cases}$ 의 해가 $\\alpha\\le{x}\\leq{\\beta}$일 때 $\\beta-\\alpha$의 값은?\n\n$\\beta-\\alpha$의 값은?\n\n①$1​$        ②$2​$        ③$3​$        ④$4​$        ⑤$5​$',3,'2018-03-12 19:19:28.547160','2018-03-18 00:04:11.677857',2,1,1,'',1,2,5),(8,'부등식 $5x-3(2x-4)\\leq{x-4}$ 는 만족시키지 않고, 부등식 $3x-4+|x+5|\\le0$은 만족시키는 모든 정수 $x$의 값의 합은 ?\n\n①$27$	②$28$	③$33$	④$35$	⑤$36$\n',2,'2018-03-12 19:19:52.309072','2018-03-18 00:04:11.682640',2,1,1,'',1,0,5),(9,'두 함수 $f(x)=|2x-3|+|2x-5|, g(x)=x+4$에 대하여 부등식 $f(x)\\le{g(x)}$를 만족시키는 실수 $x$값의 범위는 $\\alpha\\le{x}\\le\\beta$이다. 이차항의 계수가 $1$ 이차함수 y=h(x)의 그래프가 $x$축과 만나는 점의 $x$좌표가 $15\\alpha, \\beta$이고 그래프이 꼭짓점의 좌표가 $(a,b)$일 때, $a-b$의 값을 구하시오.\n',10,'2018-03-12 19:20:14.429911','2018-03-22 00:51:55.288788',1,1,1,'',1,0,2),(10,'두 함수 $f(x)=|2x-3|+|2x-5|, g(x)=x+4$에 대하여 부등식 $f(x)\\le{g(x)}$를 만족시키는 실수 $x$값의 범위는 $\\alpha\\le{x}\\le\\beta$이다. 이차항의 계수가 $1$ 이차함수 y=h(x)의 그래프가 $x$축과 만나는 점의 $x$좌표가 $15\\alpha, \\beta$이고 그래프이 꼭짓점의 좌표가 $(a,b)$일 때, $a-b$의 값을 구하시오.',2,'2018-03-12 19:21:18.860672','2018-03-18 00:04:11.692354',2,1,1,'',1,1,5),(11,'자연수 $a$에 대하여 ${19\\over6}-{a\\over3}<3-{a\\over6}<4-{a\\over2}$가 성립한다. 부등식 $ax+2|x-4|\\leq{3x-a}$를 만족시키는 자연수 $x$의 값의 합은?\n\n①$15$		②$20$		③$25$		④$30$		⑤$35$',2,'2018-03-12 19:21:41.311929','2018-03-18 00:04:11.697292',3,1,1,'',1,0,1),(12,'부등식 $(a-b)x-|2a-b|\\leq-1$ 의 해는 존재하지 않고, 부등식 $|x-a|-3b\\leq0$의 해는 $x\\leq-{1\\over3}$ 또는 $x\\ge{2\\over3}$  일 때, 상수 $a,b$에 대하여 $a+2b$의 값은?\n\n①$1\\over6$		②$1\\over4$		③$1\\over3$		④$1\\over2$		⑤$1$',3,'2018-03-12 19:22:04.094694','2018-03-18 00:04:11.702197',2,1,2,'',1,1,1),(13,'두 실수 $a,b$에 대하여 $Max(a,b)$와 $(a,b)$를\n\n$Max(a,b)=\\begin{cases}a (a\\ge{b})\\\\b (a<b)\\end{cases}$, $min(a,b)=\\begin{cases}a (a\\leq{b})\\\\b (a>b)\\end{cases}$\n\n라고 할 때, 부등식 $Max(|x-3, 3)-min(|2x-3|, 5)\\ge2$의 해는?\n\n①$x\\le-4$	②$1\\le{x}\\le2$ 		③$1\\le{x}\\le2$ 또는 $x>10$\n\n④$x\\le-4$또는 $x\\ge10$	⑤$le/{-4}$ 또는 $1\\le{x}\\le{2}$ 또는 $x\\ge10$',3,'2018-03-12 19:22:31.460239','2018-03-22 00:51:55.294315',1,1,1,'',1,1,2),(14,'부등식 $x-4\\leq{x-6|x-2|}\\leq3$ 을 만족시키는 $x$에 대한 부등식 $|x-2|\\leq{a(x-4)}$를 만족시키도록 하는 상수 $a$의 최댓값을 $M$이라 할 때, $-10M$의 값을 구하시오.',4,'2018-03-12 19:22:54.937533','2018-03-18 00:04:11.712155',2,2,1,'',1,0,1),(15,'부등식 ~~~~~~~의 해 중 정수 $x$의 개수를 $n$, 이 정수들의 총합을 $S$라 할 때, $nS$의 값을 구하시오.\n',3,'2018-03-12 19:23:14.426525','2018-03-12 19:23:14.435880',1,2,1,'',1,0,0),(16,'독서를 좋아하는 철수는 지난 달 초까지 소설책과 시집을 합하여 $450$권 이상 $500$권 미만의 책을 갖고 있었고, 소설책과 시집의 수의 차는 $80$권 미만이었다. 이번 달 초에 철수가 가지고 있는 소설책과 시집의 수를 세어 보니 $500$권이 넘었고 지난 한 달 동안 같은 수의 소설책과 시집을 구입하여 읽었다는 사실을 알게 되었다. 이번 달 초에 확인한 소설책과 시집의 수의 비가 $4:3$일 때, 지난 한 달 동안 구입한 시집의 수의 최댓값을 $M$이라 하고, 소설책과 시집 중 더 많이 가지고 있는 책의 수의 최댓값을 $N$이라 하자. $M+N$의 값을 구하시오.',3,'2018-03-12 19:23:32.511471','2018-03-22 00:51:55.299637',1,2,1,'',1,1,1),(17,'삼각형의 세 변의 길이가 각각 $|2x+4|, |x-10|, |3x+12|$일 때, $x$의 값의 범위는?\n\n①$-1<x<1$	②$-1<x<{3\\over2}$	 ③$-{3\\over2}<x<1$\n\n④$-{3\\over2}<x<{3\\over2}$	⑤$-2<x<2$',2,'2018-03-12 19:23:55.249219','2018-03-18 00:04:11.717044',2,2,1,'',1,0,1),(18,'정수 $m$과 $x$에 대한 부등식 $|(m+1)x-m-1|>m^2+3m+2$에 대하여 세 수 $a,b,c$가 다음과 같을 때, $a-2b-3c의 값을 구하시오.\n\n****\n\n(가) 부등식의 해가 $x<-(m+1)$ 또는 $x>m+3$일 때의 정수 $m$의 최솟값은 $a$이다.\n\n(나) 부등식의 해가 존재하지 않을 때의 $m$의 값은 $b$이다.\n\n(다) 부등식의 해가 $x<m+3$ 또는 $x>-(m+1)$일 때의 정수 $m$의 최댓값은 $c$이다.\n\n****',2,'2018-03-12 19:24:16.225071','2018-03-18 00:04:11.722042',1,1,1,'',1,0,1),(19,'세 사람 $A,B,C$의 나이의 합은 $57$세이고, 두 사람 $A,B$의 나이의 차는 $4$살 미만이며 두사람 $A,C$의 나이는 $3$살 이상이다. 또한 $B$의 나이의 $2$배와 $A,C$의 나이의 합의 차는 $12$ 살 이하이다. 세 사람 $A,B,C$의 나이를 차례로 $a,b,c$라 할 때, 순서쌍 $(a,bc)$의 개수를 구하시오.\n',3,'2018-03-12 19:24:39.805656','2018-03-12 19:24:39.814978',1,1,2,'',1,0,0),(20,'두 함수 $f(x)=-x^2-x+1, g(x)=x^2-2x+a$에 대하여 $0\\leq{x_1}\\leq2$, 0$\\leq{x_2}\\le{2}$ 일 때, $f(x_1)<g(x_2)$가 항상 성립하도록 하는 정수 $a$의 최솟값은?\n\n①$1$		②$2$		③$3$		④$4$		⑤$5$	\n',2,'2018-03-12 19:24:55.225211','2018-03-22 00:51:55.305303',1,2,2,'',1,0,1),(21,'이차방정식 $2x^2-4(a-2)x-2a+7=0$의 한 근은 $0$보다 크고 $1$보다 작으며 다른 한 근은 $1$보다 크고 $2$ 보다 작을 때 실수 $a$가 존재하는 범위는 $p<a<q$이다. $60pq$의 값을 구하시오.\n',3,'2018-03-12 19:25:12.906322','2018-03-29 00:09:22.305380',3,2,2,'',1,0,5),(22,'이차방정식 $x^2+kx-k=0$의 서로 다른 두 근 중 한 근만 $0$과 $2$사이에 위치하고 $x$에 대한 이차방정식 $x^2+2kx+3k^2-2k-84=0$의 두근은 모두 $-10$과 $1$ 사이에 위치하도록 하는 정수 $k$의 값을 구하시오.\n',3,'2018-03-12 19:26:13.210471','2018-03-29 00:09:22.310087',2,2,2,'',1,4,6),(23,'함수 $y=x^2-5x+6$의 그래프는 $x$축과 서로 다른 두 점 $A,B$ 에서 만난다. 함수 $y=-2x^2+kx+k+3$의 그래프와 $x$축이 서로 다른 두 점에서 만날 때, 두 교점이 모두 선분 $AB$ 위에 있지 않도록 하는 $50$이하의 자연수 $k$의 개수는 ?\n\n①$45$	②$46$	③$47$	④$48$	⑤$49$',3,'2018-03-12 19:26:36.269967','2018-03-29 00:09:22.314866',2,2,1,'',1,3,6),(24,'연립부등식 $\\begin{cases}2[x]-3>0\\\\ [x^2]-2[x]-8\\}\\leq8\\end{cases}$의 해가 $a\\leq{x}<b$일때, 상수 $a,b$에 대하여서 $ab$의 값은? (단, $[x]$는 $x$보다 크지 않은 최대의 정수이다.)\n\n①$2$		②$4$		③$6$		④$8$		⑤$10$',3,'2018-03-12 19:26:54.841229','2018-03-29 00:09:22.320417',3,2,1,'',1,2,5),(25,'연립부등식$\\begin{cases}x^2+(a-4)x-4a>0\\\\ x^2-(a^2-1)x-a^2<0\\end{cases}$을 만족시키는 정수 $x$가 존재하지 않도록 하는 실수 $a$의 값의 범위는 $p\\leq{a}\\le{q}$이다. 실수 $p,q$에 대하여 $p+q$의 값은?\n\n①$\\sqrt3$ 		②$2$		③$\\sqrt5$		④$4$		⑤$5$\n',3,'2018-03-12 19:27:15.585093','2018-03-29 00:09:22.325489',2,1,1,'',1,6,10),(26,'정수 $P$와 $f(x)=(x-3)|x-3|+p(x-3)$에 대하여 세 수 $l, m, n$을 다음과 같이 정할 때, $n-l-m$의 값을 구하시오.\n\n****\n\n(가) 부등식 $f(x)\\le0$을 만족시키는 자연수 $x$가 7개 일때의 $p$의 값을 $l$이라 한다.\n\n(나) 부등식 $f(x+3)<0$을 만족시키는 자연수 $x$가 존재하지 않을 때의 $p$의 최솟값을 $m$이라 한다.\n\n(다) $p=-12$ 일 때, 부등식 $f(x+3)<0$의 해 중 자연수의 개수를 $n$이라 한다.\n\n****',3,'2018-03-12 19:27:35.804103','2018-03-18 00:04:11.741645',2,1,2,'',1,1,1);
/*!40000 ALTER TABLE `math_problem_app_problem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problem_middleUnit`
--

DROP TABLE IF EXISTS `math_problem_app_problem_middleUnit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problem_middleUnit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_id` int(11) NOT NULL,
  `problemmiddleunit_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_problem_problem_id_problemmiddle_9b46e4a3_uniq` (`problem_id`,`problemmiddleunit_id`),
  KEY `math_problem_app_pro_problemmiddleunit_id_e33960cb_fk_math_prob` (`problemmiddleunit_id`),
  CONSTRAINT `math_problem_app_pro_problem_id_810f419d_fk_math_prob` FOREIGN KEY (`problem_id`) REFERENCES `math_problem_app_problem` (`problemSrl`),
  CONSTRAINT `math_problem_app_pro_problemmiddleunit_id_e33960cb_fk_math_prob` FOREIGN KEY (`problemmiddleunit_id`) REFERENCES `math_problem_app_problemmiddleunit` (`problemMiddleUnitSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problem_middleUnit`
--

LOCK TABLES `math_problem_app_problem_middleUnit` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problem_middleUnit` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_problem_middleUnit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problem_photos`
--

DROP TABLE IF EXISTS `math_problem_app_problem_photos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problem_photos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_id` int(11) NOT NULL,
  `photo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_problem_problem_id_photo_id_55721242_uniq` (`problem_id`,`photo_id`),
  KEY `math_problem_app_pro_photo_id_4a41e837_fk_math_prob` (`photo_id`),
  CONSTRAINT `math_problem_app_pro_photo_id_4a41e837_fk_math_prob` FOREIGN KEY (`photo_id`) REFERENCES `math_problem_app_photo` (`photoSrl`),
  CONSTRAINT `math_problem_app_pro_problem_id_14f6cd04_fk_math_prob` FOREIGN KEY (`problem_id`) REFERENCES `math_problem_app_problem` (`problemSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problem_photos`
--

LOCK TABLES `math_problem_app_problem_photos` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problem_photos` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_problem_photos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problem_smallUnit`
--

DROP TABLE IF EXISTS `math_problem_app_problem_smallUnit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problem_smallUnit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_id` int(11) NOT NULL,
  `problemsmallunit_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_problem_problem_id_problemsmallu_9e448781_uniq` (`problem_id`,`problemsmallunit_id`),
  KEY `math_problem_app_pro_problemsmallunit_id_40f18aa9_fk_math_prob` (`problemsmallunit_id`),
  CONSTRAINT `math_problem_app_pro_problem_id_8f1b7b3e_fk_math_prob` FOREIGN KEY (`problem_id`) REFERENCES `math_problem_app_problem` (`problemSrl`),
  CONSTRAINT `math_problem_app_pro_problemsmallunit_id_40f18aa9_fk_math_prob` FOREIGN KEY (`problemsmallunit_id`) REFERENCES `math_problem_app_problemsmallunit` (`problemSmallUnitSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problem_smallUnit`
--

LOCK TABLES `math_problem_app_problem_smallUnit` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problem_smallUnit` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_problem_smallUnit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problem_unit`
--

DROP TABLE IF EXISTS `math_problem_app_problem_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problem_unit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_id` int(11) NOT NULL,
  `problemunit_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_problem_problem_id_problemunit_i_852e2fd6_uniq` (`problem_id`,`problemunit_id`),
  KEY `math_problem_app_pro_problemunit_id_4b4d5266_fk_math_prob` (`problemunit_id`),
  CONSTRAINT `math_problem_app_pro_problem_id_9fb4a054_fk_math_prob` FOREIGN KEY (`problem_id`) REFERENCES `math_problem_app_problem` (`problemSrl`),
  CONSTRAINT `math_problem_app_pro_problemunit_id_4b4d5266_fk_math_prob` FOREIGN KEY (`problemunit_id`) REFERENCES `math_problem_app_problemunit` (`problemUnitSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problem_unit`
--

LOCK TABLES `math_problem_app_problem_unit` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problem_unit` DISABLE KEYS */;
INSERT INTO `math_problem_app_problem_unit` VALUES (7,6,3),(8,6,6),(9,7,2),(10,7,3),(11,8,3),(12,9,6),(13,10,3),(14,11,2),(15,12,3),(16,13,6),(17,14,3),(18,15,5),(19,16,6),(20,17,3),(21,18,2),(22,19,4),(23,20,6),(24,21,5),(25,22,4),(26,23,3),(27,24,5),(28,25,3),(29,26,4);
/*!40000 ALTER TABLE `math_problem_app_problem_unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problemmiddleunit`
--

DROP TABLE IF EXISTS `math_problem_app_problemmiddleunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problemmiddleunit` (
  `problemMiddleUnitSrl` int(11) NOT NULL AUTO_INCREMENT,
  `middleUnit` int(11) DEFAULT NULL,
  PRIMARY KEY (`problemMiddleUnitSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problemmiddleunit`
--

LOCK TABLES `math_problem_app_problemmiddleunit` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problemmiddleunit` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_problemmiddleunit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problemsmallunit`
--

DROP TABLE IF EXISTS `math_problem_app_problemsmallunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problemsmallunit` (
  `problemSmallUnitSrl` int(11) NOT NULL AUTO_INCREMENT,
  `smallUnit` int(11) DEFAULT NULL,
  PRIMARY KEY (`problemSmallUnitSrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problemsmallunit`
--

LOCK TABLES `math_problem_app_problemsmallunit` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problemsmallunit` DISABLE KEYS */;
/*!40000 ALTER TABLE `math_problem_app_problemsmallunit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_problemunit`
--

DROP TABLE IF EXISTS `math_problem_app_problemunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_problemunit` (
  `problemUnitSrl` int(11) NOT NULL AUTO_INCREMENT,
  `unit` int(11) DEFAULT NULL,
  PRIMARY KEY (`problemUnitSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_problemunit`
--

LOCK TABLES `math_problem_app_problemunit` WRITE;
/*!40000 ALTER TABLE `math_problem_app_problemunit` DISABLE KEYS */;
INSERT INTO `math_problem_app_problemunit` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6);
/*!40000 ALTER TABLE `math_problem_app_problemunit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_rating`
--

DROP TABLE IF EXISTS `math_problem_app_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_rating` (
  `ratingSrl` int(11) NOT NULL AUTO_INCREMENT,
  `su1` int(11) DEFAULT NULL,
  `su2` int(11) DEFAULT NULL,
  `mi1` int(11) DEFAULT NULL,
  `mi2` int(11) DEFAULT NULL,
  `givec` int(11) DEFAULT NULL,
  `hwaktong` int(11) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `score` int(11) NOT NULL,
  `totalScore` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ratingSrl`),
  KEY `math_problem_app_rat_user_id_f5d0606e_fk_math_prob` (`user_id`),
  CONSTRAINT `math_problem_app_rat_user_id_f5d0606e_fk_math_prob` FOREIGN KEY (`user_id`) REFERENCES `math_problem_app_user` (`userSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_rating`
--

LOCK TABLES `math_problem_app_rating` WRITE;
/*!40000 ALTER TABLE `math_problem_app_rating` DISABLE KEYS */;
INSERT INTO `math_problem_app_rating` VALUES (1,9,9,9,9,9,9,'2018-03-17 23:42:58.944421','2018-03-18 22:39:38.995574',0,25,2),(2,9,1,4,9,1,9,'2018-03-17 23:43:58.516784','2018-03-18 22:39:45.413225',15,25,3),(3,9,9,6,9,1,9,'2018-03-17 23:48:11.913112','2018-03-18 22:39:50.937868',10,25,4),(4,9,9,8,9,9,9,'2018-03-17 23:50:52.338711','2018-03-18 22:39:56.074256',5,25,5),(5,9,6,4,1,3,9,'2018-03-18 00:04:11.744611','2018-03-18 22:40:01.601547',40,75,2),(6,9,9,1,1,9,5,'2018-03-19 20:23:11.008674','2018-03-19 20:23:11.011941',20,25,5),(7,9,9,5,9,9,9,'2018-03-21 15:22:48.896369','2018-03-21 15:22:48.901220',5,25,2),(8,9,9,1,9,6,9,'2018-03-22 00:51:55.308417','2018-03-22 00:51:55.313225',10,25,5),(9,9,9,5,9,9,9,'2018-03-22 14:30:31.817932','2018-03-22 14:30:31.821560',5,25,2),(10,9,9,5,1,9,9,'2018-03-29 00:06:52.889924','2018-03-29 00:06:52.891176',10,25,5),(11,9,9,9,1,9,5,'2018-03-29 00:09:22.328247','2018-03-29 00:09:22.330566',10,25,5);
/*!40000 ALTER TABLE `math_problem_app_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_recommend`
--

DROP TABLE IF EXISTS `math_problem_app_recommend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_recommend` (
  `recommendSrl` int(11) NOT NULL AUTO_INCREMENT,
  `aimGrade` int(11) DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`recommendSrl`),
  KEY `math_problem_app_rec_unit_id_46f7d4a4_fk_math_prob` (`unit_id`),
  CONSTRAINT `math_problem_app_rec_unit_id_46f7d4a4_fk_math_prob` FOREIGN KEY (`unit_id`) REFERENCES `math_problem_app_problemunit` (`problemUnitSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_recommend`
--

LOCK TABLES `math_problem_app_recommend` WRITE;
/*!40000 ALTER TABLE `math_problem_app_recommend` DISABLE KEYS */;
INSERT INTO `math_problem_app_recommend` VALUES (1,8,2),(2,8,5),(3,8,6),(4,8,2),(5,8,3),(6,8,6);
/*!40000 ALTER TABLE `math_problem_app_recommend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_score`
--

DROP TABLE IF EXISTS `math_problem_app_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_score` (
  `scoreSrl` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`scoreSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_score`
--

LOCK TABLES `math_problem_app_score` WRITE;
/*!40000 ALTER TABLE `math_problem_app_score` DISABLE KEYS */;
INSERT INTO `math_problem_app_score` VALUES (1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(12,5),(13,5),(14,5),(15,5),(16,5),(17,5),(18,5),(19,5),(20,5),(21,5),(22,5),(23,5),(24,5),(25,5),(26,5),(27,5),(28,5),(29,5),(30,5),(31,5),(32,5),(33,5),(34,5),(35,5),(36,5),(37,5),(38,5),(39,5),(40,5),(41,5),(42,5),(43,5),(44,5),(45,5),(46,5),(47,5),(48,5),(49,5),(50,5),(51,5),(52,5),(53,5),(54,5),(55,5),(56,5),(57,5),(58,5),(59,5),(60,5),(61,5),(62,5),(63,5),(64,5),(65,5),(66,5),(67,5),(68,5),(69,5),(70,5),(71,5),(72,5),(73,5),(74,5),(75,5),(76,5),(77,5),(78,5),(79,5),(80,5),(81,5),(82,5),(83,5),(84,5),(85,5),(86,5),(87,5),(88,5),(89,5),(90,5),(91,5),(92,5),(93,5),(94,5),(95,5),(96,5),(97,5),(98,5),(99,5),(100,5),(101,5),(102,5),(103,5),(104,5),(105,5),(106,5),(107,5),(108,5),(109,5),(110,5),(111,5),(112,5),(113,5),(114,5),(115,5),(116,5),(117,5),(118,5),(119,5),(120,5),(121,5),(122,5),(123,5),(124,5),(125,5),(126,5),(127,5),(128,5),(129,5),(130,5),(131,5),(132,5),(133,5),(134,5),(135,5),(136,5),(137,5),(138,5),(139,5),(140,5),(141,5),(142,5),(143,5),(144,5),(145,5),(146,5),(147,5),(148,5),(149,5),(150,5),(151,5),(152,5),(153,5),(154,5),(155,5),(156,5),(157,5),(158,5),(159,5),(160,5);
/*!40000 ALTER TABLE `math_problem_app_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_test`
--

DROP TABLE IF EXISTS `math_problem_app_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_test` (
  `testSrl` int(11) NOT NULL AUTO_INCREMENT,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`testSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_test`
--

LOCK TABLES `math_problem_app_test` WRITE;
/*!40000 ALTER TABLE `math_problem_app_test` DISABLE KEYS */;
INSERT INTO `math_problem_app_test` VALUES (1,'2018-03-12 01:14:55.822772','2018-03-18 00:01:59.166862','test',1),(2,'2018-03-12 01:19:49.937788','2018-03-12 01:19:49.955278','',1),(3,'2018-03-12 19:30:02.713294','2018-03-12 19:30:02.735675','',1),(4,'2018-03-12 19:31:11.259813','2018-03-16 15:33:28.153180','123123',1),(5,'2018-03-15 19:42:30.081335','2018-03-19 20:23:05.063339','진단고사',2),(6,'2018-03-17 23:53:03.774474','2018-03-18 00:01:31.631450','test11',1),(7,'2018-03-17 23:53:28.025389','2018-03-18 00:01:37.979867','test12',1),(8,'2018-03-17 23:54:54.959016','2018-03-17 23:54:54.966480','test2',1),(9,'2018-03-17 23:55:03.458911','2018-03-17 23:55:03.462229','test3',1),(10,'2018-03-22 00:50:00.119624','2018-03-22 00:50:00.167530',NULL,3),(11,'2018-03-22 00:50:04.727770','2018-03-22 00:50:04.772959',NULL,3),(12,'2018-03-22 00:50:06.126776','2018-03-22 00:50:06.175402',NULL,3),(13,'2018-03-22 00:50:06.565154','2018-03-22 00:50:06.607376',NULL,3),(14,'2018-03-22 00:50:29.060400','2018-03-22 00:50:29.102918',NULL,3),(15,'2018-03-22 00:51:41.062163','2018-03-22 00:51:41.104955',NULL,3),(16,'2018-03-25 02:04:54.298309','2018-03-25 02:04:54.353062',NULL,3),(17,'2018-03-25 02:05:03.856439','2018-03-25 02:05:03.899665',NULL,3),(18,'2018-03-25 02:05:06.826680','2018-03-25 02:05:06.872709',NULL,3),(19,'2018-03-25 02:05:24.321704','2018-03-25 02:05:24.362597',NULL,3),(20,'2018-03-25 02:05:27.572885','2018-03-25 02:05:27.618403',NULL,3),(21,'2018-03-25 02:06:02.034493','2018-03-25 02:06:02.078220',NULL,3),(22,'2018-03-25 02:06:10.343789','2018-03-25 02:06:10.387374',NULL,3),(23,'2018-03-25 02:06:20.376483','2018-03-25 02:06:20.422431',NULL,3),(24,'2018-03-25 09:58:56.662591','2018-03-25 09:58:56.705246',NULL,3),(25,'2018-03-25 10:01:14.767845','2018-03-25 10:01:14.810650',NULL,3),(26,'2018-03-25 15:11:50.279351','2018-03-25 15:11:50.319730',NULL,3),(27,'2018-03-28 16:11:33.071223','2018-03-28 16:11:33.115180',NULL,3);
/*!40000 ALTER TABLE `math_problem_app_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_test_problems`
--

DROP TABLE IF EXISTS `math_problem_app_test_problems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_test_problems` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL,
  `problem_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_test_problems_test_id_problem_id_d9f2fd96_uniq` (`test_id`,`problem_id`),
  KEY `math_problem_app_tes_problem_id_78c94f8f_fk_math_prob` (`problem_id`),
  CONSTRAINT `math_problem_app_tes_problem_id_78c94f8f_fk_math_prob` FOREIGN KEY (`problem_id`) REFERENCES `math_problem_app_problem` (`problemSrl`),
  CONSTRAINT `math_problem_app_tes_test_id_0cd451c5_fk_math_prob` FOREIGN KEY (`test_id`) REFERENCES `math_problem_app_test` (`testSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_test_problems`
--

LOCK TABLES `math_problem_app_test_problems` WRITE;
/*!40000 ALTER TABLE `math_problem_app_test_problems` DISABLE KEYS */;
INSERT INTO `math_problem_app_test_problems` VALUES (74,1,6),(75,1,7),(76,1,8),(77,1,9),(78,1,10),(79,1,11),(87,1,12),(80,1,13),(81,1,14),(82,1,17),(83,1,18),(84,1,22),(85,1,23),(86,1,25),(88,1,26),(6,3,7),(7,3,8),(8,3,10),(9,3,25),(18,4,10),(17,4,11),(14,5,21),(15,5,22),(16,5,23),(12,5,24),(13,5,25),(56,6,7),(57,6,8),(58,6,10),(59,6,25),(60,7,21),(89,10,6),(90,10,9),(91,10,13),(92,10,16),(93,10,20),(94,11,6),(95,11,9),(96,11,13),(97,11,16),(98,11,20),(99,12,6),(100,12,9),(101,12,13),(102,12,16),(103,12,20),(104,13,6),(105,13,9),(106,13,13),(107,13,16),(108,13,20),(109,14,6),(110,14,9),(111,14,13),(112,14,16),(113,14,20),(114,15,6),(115,15,9),(116,15,13),(117,15,16),(118,15,20),(119,16,6),(120,16,9),(121,16,13),(122,16,16),(123,16,20),(124,17,6),(125,17,9),(126,17,13),(127,17,16),(128,17,20),(129,18,6),(130,18,9),(131,18,13),(132,18,16),(133,18,20),(134,19,6),(135,19,9),(136,19,13),(137,19,16),(138,19,20),(139,20,6),(140,20,9),(141,20,13),(142,20,16),(143,20,20),(144,21,6),(145,21,9),(146,21,13),(147,21,16),(148,21,20),(149,22,6),(150,22,9),(151,22,13),(152,22,16),(153,22,20),(154,23,6),(155,23,9),(156,23,13),(157,23,16),(158,23,20),(159,24,6),(160,24,9),(161,24,13),(162,24,16),(163,24,20),(164,25,6),(165,25,9),(166,25,13),(167,25,16),(168,25,20),(169,26,6),(170,26,9),(171,26,13),(172,26,16),(173,26,20),(174,27,6),(175,27,9),(176,27,13),(177,27,16),(178,27,20);
/*!40000 ALTER TABLE `math_problem_app_test_problems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_test_scores`
--

DROP TABLE IF EXISTS `math_problem_app_test_scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_test_scores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL,
  `score_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_test_scores_test_id_score_id_4220e8e7_uniq` (`test_id`,`score_id`),
  KEY `math_problem_app_tes_score_id_8d4d03ca_fk_math_prob` (`score_id`),
  CONSTRAINT `math_problem_app_tes_score_id_8d4d03ca_fk_math_prob` FOREIGN KEY (`score_id`) REFERENCES `math_problem_app_score` (`scoreSrl`),
  CONSTRAINT `math_problem_app_tes_test_id_4f413265_fk_math_prob` FOREIGN KEY (`test_id`) REFERENCES `math_problem_app_test` (`testSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_test_scores`
--

LOCK TABLES `math_problem_app_test_scores` WRITE;
/*!40000 ALTER TABLE `math_problem_app_test_scores` DISABLE KEYS */;
INSERT INTO `math_problem_app_test_scores` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63),(64,1,64),(65,1,65),(66,1,66),(67,1,67),(68,1,68),(69,1,69),(70,1,70),(71,5,1),(72,5,2),(73,5,3),(74,5,4),(75,5,5),(14,6,14),(15,6,15),(16,6,16),(17,6,17),(38,6,38),(39,6,39),(40,6,40),(41,6,41),(27,7,27),(42,7,42),(76,10,71),(77,10,72),(78,10,73),(79,10,74),(80,10,75),(81,11,76),(82,11,77),(83,11,78),(84,11,79),(85,11,80),(86,12,81),(87,12,82),(88,12,83),(89,12,84),(90,12,85),(91,13,86),(92,13,87),(93,13,88),(94,13,89),(95,13,90),(96,14,91),(97,14,92),(98,14,93),(99,14,94),(100,14,95),(101,15,96),(102,15,97),(103,15,98),(104,15,99),(105,15,100),(106,16,101),(107,16,102),(108,16,103),(109,16,104),(110,16,105),(111,17,106),(112,17,107),(113,17,108),(114,17,109),(115,17,110),(116,18,111),(117,18,112),(118,18,113),(119,18,114),(120,18,115),(121,19,116),(122,19,117),(123,19,118),(124,19,119),(125,19,120),(126,20,121),(127,20,122),(128,20,123),(129,20,124),(130,20,125),(131,21,126),(132,21,127),(133,21,128),(134,21,129),(135,21,130),(136,22,131),(137,22,132),(138,22,133),(139,22,134),(140,22,135),(141,23,136),(142,23,137),(143,23,138),(144,23,139),(145,23,140),(146,24,141),(147,24,142),(148,24,143),(149,24,144),(150,24,145),(151,25,146),(152,25,147),(153,25,148),(154,25,149),(155,25,150),(156,26,151),(157,26,152),(158,26,153),(159,26,154),(160,26,155),(161,27,156),(162,27,157),(163,27,158),(164,27,159),(165,27,160);
/*!40000 ALTER TABLE `math_problem_app_test_scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_user`
--

DROP TABLE IF EXISTS `math_problem_app_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_user` (
  `userSrl` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `grade` int(11) DEFAULT NULL,
  `id` varchar(200) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `school` varchar(200) DEFAULT NULL,
  `sex` varchar(20) DEFAULT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  PRIMARY KEY (`userSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_user`
--

LOCK TABLES `math_problem_app_user` WRITE;
/*!40000 ALTER TABLE `math_problem_app_user` DISABLE KEYS */;
INSERT INTO `math_problem_app_user` VALUES (1,'mathadmin@math.co.kr','pbkdf2_sha256$100000$dzToDYw6xIyp$XzFPQ17r1YAQlSmXJeT21GlhIeXyMQZt2XmSAtnPP1c=',3,'admin',NULL,NULL,NULL,NULL,'2018-03-10 18:12:43.484263','2018-03-18 00:04:11.750021'),(2,'osiriskgn93@gmail.com','pbkdf2_sha256$100000$wyP4C9bwqWcS$h+GcNZZmYOrevJ3Zj9vb54OCIWcdGSqomIo4vsZGWQs=',3,'osiriskgn','임종현','01029343187','한국과학영재학교','man','2018-03-11 16:03:04.428019','2018-03-16 21:50:00.762210'),(3,'rlawjdgns4345@gmail.com','pbkdf2_sha256$100000$FkrCkN3a9m43$ElQkPw3y3yGWtPO0NaBuFoS+EIUP4em11rJSSNeqR28=',3,'rlawjdgns434','김정훈','01045394345','신반포중학교','man','2018-03-15 19:39:43.995497','2018-03-15 19:42:37.069429'),(4,'yh04060@gmail.com','pbkdf2_sha256$100000$5o8V86zpia6u$s7JzQUoP6FFEMTH+PjSyNIXRyyQgiMVGN67rquJMGAA=',3,'yh04060','최민규','01044413721','대구일과학고','man','2018-03-16 15:51:26.590954','2018-03-16 15:51:26.683194'),(5,'whcho88@nate.com','pbkdf2_sha256$100000$dd8km8Fu7Rbj$zDTe51NEbpm+gKfAImxfr1IzjTbcCvkU1zY/79q/1UQ=',3,'whcho88','조원혁','01074999948','신성고등학교','man','2018-03-18 14:28:52.202504','2018-03-29 00:09:22.354293');
/*!40000 ALTER TABLE `math_problem_app_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_user_answers`
--

DROP TABLE IF EXISTS `math_problem_app_user_answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_user_answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `answer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_user_answers_user_id_answer_id_d9f34ec7_uniq` (`user_id`,`answer_id`),
  KEY `math_problem_app_use_answer_id_f93ea62d_fk_math_prob` (`answer_id`),
  CONSTRAINT `math_problem_app_use_answer_id_f93ea62d_fk_math_prob` FOREIGN KEY (`answer_id`) REFERENCES `math_problem_app_answer` (`answerSrl`),
  CONSTRAINT `math_problem_app_use_user_id_bce34d60_fk_math_prob` FOREIGN KEY (`user_id`) REFERENCES `math_problem_app_user` (`userSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_user_answers`
--

LOCK TABLES `math_problem_app_user_answers` WRITE;
/*!40000 ALTER TABLE `math_problem_app_user_answers` DISABLE KEYS */;
INSERT INTO `math_problem_app_user_answers` VALUES (1,1,1),(2,1,2),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(3,2,3),(4,2,4),(11,2,11),(12,2,12),(15,2,15),(17,2,17),(13,5,13),(14,5,14),(16,5,16),(18,5,19),(19,5,20);
/*!40000 ALTER TABLE `math_problem_app_user_answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `math_problem_app_user_recommend`
--

DROP TABLE IF EXISTS `math_problem_app_user_recommend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `math_problem_app_user_recommend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `recommend_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `math_problem_app_user_re_user_id_recommend_id_04b813d0_uniq` (`user_id`,`recommend_id`),
  KEY `math_problem_app_use_recommend_id_f9c477cf_fk_math_prob` (`recommend_id`),
  CONSTRAINT `math_problem_app_use_recommend_id_f9c477cf_fk_math_prob` FOREIGN KEY (`recommend_id`) REFERENCES `math_problem_app_recommend` (`recommendSrl`),
  CONSTRAINT `math_problem_app_use_user_id_58072eb9_fk_math_prob` FOREIGN KEY (`user_id`) REFERENCES `math_problem_app_user` (`userSrl`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_problem_app_user_recommend`
--

LOCK TABLES `math_problem_app_user_recommend` WRITE;
/*!40000 ALTER TABLE `math_problem_app_user_recommend` DISABLE KEYS */;
INSERT INTO `math_problem_app_user_recommend` VALUES (4,5,4),(5,5,5),(6,5,6);
/*!40000 ALTER TABLE `math_problem_app_user_recommend` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-28 15:13:13
