/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.0.27-community-nt : Database - python_project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`python_project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `python_project`;

/*Table structure for table `vocab` */

DROP TABLE IF EXISTS `vocab`;

CREATE TABLE `vocab` (
  `sr_no` int(5) NOT NULL auto_increment,
  `word` varchar(30) NOT NULL default '',
  `meaning` varchar(200) NOT NULL,
  KEY `sr_no` (`sr_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `vocab` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
