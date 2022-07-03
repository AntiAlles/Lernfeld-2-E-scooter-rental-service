-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server Version:               10.4.24-MariaDB - mariadb.org binary distribution
-- Server Betriebssystem:        Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Exportiere Datenbank Struktur für scoteqdatabase
CREATE DATABASE IF NOT EXISTS `scoteqdatabase` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `scoteqdatabase`;

-- Exportiere Struktur von Tabelle scoteqdatabase.maintable
CREATE TABLE IF NOT EXISTS `maintable` (
  `PERSONID` int(11) NOT NULL AUTO_INCREMENT,
  `RouteID` int(11) DEFAULT NULL,
  `distance` decimal(20,6) DEFAULT NULL,
  `price` decimal(20,6) DEFAULT NULL,
  `day` date DEFAULT NULL,
  `start_at` time DEFAULT NULL,
  PRIMARY KEY (`PERSONID`),
  KEY `Schlüssel 2` (`RouteID`),
  CONSTRAINT `FK1 RouteID` FOREIGN KEY (`RouteID`) REFERENCES `userinterface` (`RouteID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Daten Export vom Benutzer nicht ausgewählt

-- Exportiere Struktur von Tabelle scoteqdatabase.userinterface
CREATE TABLE IF NOT EXISTS `userinterface` (
  `RouteID` int(11) NOT NULL AUTO_INCREMENT,
  `PersonenID` int(11) DEFAULT NULL,
  `distance` decimal(20,6) DEFAULT NULL,
  `price` decimal(20,6) DEFAULT NULL,
  PRIMARY KEY (`RouteID`),
  KEY `Schlüssel 2` (`PersonenID`),
  CONSTRAINT `PersonenID` FOREIGN KEY (`PersonenID`) REFERENCES `maintable` (`PERSONID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Daten Export vom Benutzer nicht ausgewählt

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
