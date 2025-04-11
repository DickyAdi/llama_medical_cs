-- MySQL dump 10.13  Distrib 9.1.0, for macos14.7 (arm64)
--
-- Host: localhost    Database: lenna_ai
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booking_table`
--

DROP TABLE IF EXISTS `booking_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_table` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `doctor_id` int NOT NULL,
  `day` varchar(50) NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `booking_table_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_table`
--

LOCK TABLES `booking_table` WRITE;
/*!40000 ALTER TABLE `booking_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `booking_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_availibility`
--

DROP TABLE IF EXISTS `doctor_availibility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_availibility` (
  `availibility_id` int NOT NULL AUTO_INCREMENT,
  `doctor_id` int DEFAULT NULL,
  `day` varchar(50) DEFAULT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  PRIMARY KEY (`availibility_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `doctor_availibility_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_availibility`
--

LOCK TABLES `doctor_availibility` WRITE;
/*!40000 ALTER TABLE `doctor_availibility` DISABLE KEYS */;
INSERT INTO `doctor_availibility` VALUES (1,1,'Monday','10:00:00','12:00:00'),(2,1,'Monday','14:00:00','16:00:00'),(3,1,'Wednesday','10:00:00','12:00:00'),(4,1,'Wednesday','14:00:00','16:00:00'),(5,1,'Friday','10:00:00','12:00:00'),(6,1,'Friday','14:00:00','16:00:00'),(7,2,'Tuesday','09:00:00','11:00:00'),(8,2,'Tuesday','13:00:00','15:00:00'),(9,2,'Thursday','09:00:00','11:00:00'),(10,2,'Thursday','13:00:00','15:00:00'),(11,3,'Monday','11:00:00','13:00:00'),(12,3,'Monday','15:00:00','17:00:00'),(13,3,'Tuesday','11:00:00','13:00:00'),(14,3,'Tuesday','15:00:00','17:00:00'),(15,3,'Thursday','11:00:00','13:00:00'),(16,3,'Thursday','15:00:00','17:00:00'),(17,4,'Monday','08:00:00','10:00:00'),(18,4,'Monday','12:00:00','14:00:00'),(19,4,'Wednesday','08:00:00','10:00:00'),(20,4,'Wednesday','12:00:00','14:00:00'),(21,5,'Tuesday','10:00:00','12:00:00'),(22,5,'Tuesday','16:00:00','18:00:00'),(23,5,'Friday','10:00:00','12:00:00'),(24,5,'Friday','16:00:00','18:00:00'),(25,6,'Monday','09:00:00','12:00:00'),(26,6,'Monday','13:00:00','17:00:00'),(27,6,'Friday','09:00:00','12:00:00'),(28,6,'Friday','13:00:00','17:00:00'),(29,7,'Tuesday','10:00:00','12:00:00'),(30,7,'Tuesday','14:00:00','16:00:00'),(31,7,'Thursday','10:00:00','12:00:00'),(32,7,'Thursday','14:00:00','16:00:00'),(33,8,'Wednesday','09:00:00','11:00:00'),(34,8,'Wednesday','13:00:00','15:00:00'),(35,8,'Friday','09:00:00','11:00:00'),(36,8,'Friday','13:00:00','15:00:00'),(37,9,'Monday','10:00:00','13:00:00'),(38,9,'Monday','14:00:00','17:00:00'),(39,9,'Thursday','10:00:00','13:00:00'),(40,9,'Thursday','14:00:00','17:00:00'),(41,10,'Tuesday','08:00:00','10:00:00'),(42,10,'Tuesday','14:00:00','16:00:00'),(43,10,'Friday','08:00:00','10:00:00'),(44,10,'Friday','14:00:00','16:00:00'),(45,11,'Wednesday','11:00:00','13:00:00'),(46,11,'Wednesday','15:00:00','17:00:00'),(47,11,'Friday','11:00:00','13:00:00'),(48,11,'Friday','15:00:00','17:00:00'),(49,12,'Monday','10:00:00','12:00:00'),(50,12,'Monday','14:00:00','16:00:00'),(51,12,'Thursday','10:00:00','12:00:00'),(52,12,'Thursday','14:00:00','16:00:00'),(53,13,'Tuesday','09:00:00','11:00:00'),(54,13,'Tuesday','13:00:00','15:00:00'),(55,13,'Friday','09:00:00','11:00:00'),(56,13,'Friday','13:00:00','15:00:00'),(57,14,'Monday','08:00:00','10:00:00'),(58,14,'Monday','12:00:00','14:00:00'),(59,14,'Wednesday','08:00:00','10:00:00'),(60,14,'Wednesday','12:00:00','14:00:00'),(61,15,'Monday','09:00:00','11:00:00'),(62,15,'Monday','13:00:00','15:00:00'),(63,15,'Wednesday','09:00:00','11:00:00'),(64,15,'Wednesday','13:00:00','15:00:00'),(65,16,'Tuesday','10:00:00','12:00:00'),(66,16,'Tuesday','14:00:00','16:00:00'),(67,16,'Friday','10:00:00','12:00:00'),(68,16,'Friday','14:00:00','16:00:00'),(69,17,'Monday','08:00:00','10:00:00'),(70,17,'Monday','14:00:00','16:00:00'),(71,17,'Friday','08:00:00','10:00:00'),(72,17,'Friday','14:00:00','16:00:00'),(73,18,'Tuesday','09:00:00','11:00:00'),(74,18,'Tuesday','13:00:00','15:00:00'),(75,18,'Thursday','09:00:00','11:00:00'),(76,18,'Thursday','13:00:00','15:00:00'),(77,19,'Monday','08:00:00','10:00:00'),(78,19,'Monday','12:00:00','14:00:00'),(79,19,'Wednesday','08:00:00','10:00:00'),(80,19,'Wednesday','12:00:00','14:00:00'),(81,20,'Tuesday','09:00:00','11:00:00'),(82,20,'Tuesday','13:00:00','15:00:00'),(83,20,'Friday','09:00:00','11:00:00'),(84,20,'Friday','13:00:00','15:00:00');
/*!40000 ALTER TABLE `doctor_availibility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `doctor_schedule`
--

DROP TABLE IF EXISTS `doctor_schedule`;
/*!50001 DROP VIEW IF EXISTS `doctor_schedule`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `doctor_schedule` AS SELECT 
 1 AS `name`,
 1 AS `specialization_name`,
 1 AS `day`,
 1 AS `start_time`,
 1 AS `end_time`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `specialization_id` int NOT NULL,
  PRIMARY KEY (`doctor_id`),
  KEY `specialization_id` (`specialization_id`),
  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`specialization_id`) REFERENCES `specialization` (`specialization_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (1,'Dr. Andi Pratama',1),(2,'Dr. Budi Santoso',2),(3,'Dr. Clara Sari',3),(4,'Dr. David Wijaya',4),(5,'Dr. Emiliana Kartika',5),(6,'Dr. Sarah Hidayati',6),(7,'Dr. Joko Sutrisno',7),(8,'Dr. Rina Kusuma',8),(9,'Dr. Miko Rahman',9),(10,'Dr. Olivia Sembiring',10),(11,'Dr. Lukas Setiawan',11),(12,'Dr. Nani Kurniawan',12),(13,'Dr. Thomas Prabowo',13),(14,'Dr. Sofia Malika',14),(15,'Dr. Hendrik Salim',15),(16,'Dr. Emma Putri',16),(17,'Dr. Daniel Nugroho',17),(18,'Dr. Grace Tan',18),(19,'Dr. Jack Gunawan',19),(20,'Dr. Lily Permata',20);
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialization`
--

DROP TABLE IF EXISTS `specialization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialization` (
  `specialization_id` int NOT NULL AUTO_INCREMENT,
  `specialization_name` varchar(100) NOT NULL,
  PRIMARY KEY (`specialization_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialization`
--

LOCK TABLES `specialization` WRITE;
/*!40000 ALTER TABLE `specialization` DISABLE KEYS */;
INSERT INTO `specialization` VALUES (1,'Cardiologist'),(2,'Neurologist'),(3,'Dermatologist'),(4,'Pediatrician'),(5,'Orthopedic'),(6,'General Practitioner'),(7,'Andrologist'),(8,'Endocrinologist'),(9,'Surgeon'),(10,'Obstetrician'),(11,'Oncologist'),(12,'Psychiatrist'),(13,'Gastroenterologist'),(14,'Pulmonologist'),(15,'Rheumatologist'),(16,'Nephrologist'),(17,'ENT Specialist'),(18,'Allergist'),(19,'Physiotherapist'),(20,'Chiropractor');
/*!40000 ALTER TABLE `specialization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'lenna_ai'
--

--
-- Final view structure for view `doctor_schedule`
--

/*!50001 DROP VIEW IF EXISTS `doctor_schedule`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `doctor_schedule` AS select `d`.`name` AS `name`,`s`.`specialization_name` AS `specialization_name`,`a`.`day` AS `day`,`a`.`start_time` AS `start_time`,`a`.`end_time` AS `end_time` from ((`doctors` `d` join `specialization` `s` on((`d`.`specialization_id` = `s`.`specialization_id`))) join `doctor_availibility` `a` on((`a`.`doctor_id` = `d`.`doctor_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-22 19:53:56
