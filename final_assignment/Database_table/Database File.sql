-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: final_assignment
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `content` (
  `content_id` int NOT NULL AUTO_INCREMENT,
  `content_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`content_id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content`
--

LOCK TABLES `content` WRITE;
/*!40000 ALTER TABLE `content` DISABLE KEYS */;
INSERT INTO `content` VALUES (1,'Gaming'),(2,'Electronic'),(3,'Accessories'),(5,'Perfume'),(101,'Shoe');
/*!40000 ALTER TABLE `content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cus_Id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `delivery_address` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cus_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Anil','Thapa','Koteshwor\n','1223','koteshwor,chok\n',23,'123@gmail.com'),(2,'Anna','Gracy','lalitpur\n','1','Bhaktapur\n',20,'1'),(10,'Anuj','Maharjan','Koteshwor,Mahadevthan\n\n','123','Koteshwor Multiple Campus, Koteshwor\n',25,'anuj@gmail.com'),(40,'Shikhar','Manandar','Bhaktapur','980881111','Bhaktapur',23,'shikhar.com'),(101,'Bishal','Thapa','Bhaktapur\n','200','Bhaktapur durbar Square\n',23,'12@gmail.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_product`
--

DROP TABLE IF EXISTS `customer_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_product` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `product_code` int NOT NULL,
  `customer_Id` int NOT NULL,
  `Quantity` int DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `Status` varchar(45) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `FKCustomer_P353474` (`customer_Id`),
  KEY `FKCustomer_P817973` (`product_code`),
  CONSTRAINT `FKCustomer_P353474` FOREIGN KEY (`customer_Id`) REFERENCES `customer` (`cus_Id`),
  CONSTRAINT `FKCustomer_P817973` FOREIGN KEY (`product_code`) REFERENCES `product` (`product_code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_product`
--

LOCK TABLES `customer_product` WRITE;
/*!40000 ALTER TABLE `customer_product` DISABLE KEYS */;
INSERT INTO `customer_product` VALUES (1,5,1,1,'2020-08-17','Delivered'),(2,2,10,1,'2020-08-17','Not Shipped'),(3,1,2,1,'2020-08-20','Not Shipped'),(4,2,2,1,'2020-08-20','Not Shipped'),(5,5,2,1,'2020-08-20','Not Shipped');
/*!40000 ALTER TABLE `customer_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount`
--

DROP TABLE IF EXISTS `discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount` (
  `dis_id` int NOT NULL AUTO_INCREMENT,
  `discountoffer` int DEFAULT NULL,
  PRIMARY KEY (`dis_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount`
--

LOCK TABLES `discount` WRITE;
/*!40000 ALTER TABLE `discount` DISABLE KEYS */;
INSERT INTO `discount` VALUES (1,10),(3,20),(4,0);
/*!40000 ALTER TABLE `discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_code` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) DEFAULT NULL,
  `cost` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `discount_code` int NOT NULL,
  `content_code` int NOT NULL,
  PRIMARY KEY (`product_code`),
  KEY `FKProduct729967` (`content_code`),
  KEY `FKProduct973601` (`discount_code`),
  CONSTRAINT `FKProduct729967` FOREIGN KEY (`content_code`) REFERENCES `content` (`content_id`),
  CONSTRAINT `FKProduct973601` FOREIGN KEY (`discount_code`) REFERENCES `discount` (`dis_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Gaming Mouse',1500,'2020 leatest mouse\n',199,1,1),(2,'Joystick',1500,'compatable with PC\n\n',198,1,1),(5,'Gaming Headset',2000,'2020 leatest headset\n\n\n',19,4,1),(12,'Denever',2000,'Best Perfune leatest edition.longlasting scent\n',20,1,5),(14,'Converse Shoe',5000,'Original brand\n',5,4,101),(15,'Football shoe',9000,'Footbal shoe. Original \n',700,1,101),(16,'Axe ',200,'Men best Purfume\n',600,4,5);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-30 18:07:45
