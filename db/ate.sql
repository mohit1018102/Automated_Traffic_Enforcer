-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 21, 2020 at 06:54 AM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ate`
--

-- --------------------------------------------------------

--
-- Table structure for table `currentvoilator`
--

DROP TABLE IF EXISTS `currentvoilator`;
CREATE TABLE IF NOT EXISTS `currentvoilator` (
  `p_number` varchar(7) NOT NULL,
  PRIMARY KEY (`p_number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `processedvoilator`
--

DROP TABLE IF EXISTS `processedvoilator`;
CREATE TABLE IF NOT EXISTS `processedvoilator` (
  `p_number` varchar(7) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `processedvoilator`
--

INSERT INTO `processedvoilator` (`p_number`) VALUES
('apy8600'),
('auy1857'),
('awh1935'),
('aws7935'),
('awt7935'),
('ayd8871'),
('erf4296'),
('mos9927'),
('ter4236');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_details`
--

DROP TABLE IF EXISTS `vehicle_details`;
CREATE TABLE IF NOT EXISTS `vehicle_details` (
  `plateNumber` varchar(7) NOT NULL,
  `FirstName` varchar(10) NOT NULL,
  `secondName` varchar(10) NOT NULL,
  `email` varchar(40) NOT NULL,
  PRIMARY KEY (`plateNumber`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle_details`
--

INSERT INTO `vehicle_details` (`plateNumber`, `FirstName`, `secondName`, `email`) VALUES
('ter4236', 'Mohit', 'Negi', 'mohit@gmail.com'),
('awt7935', 'Kushagr', 'Bansal', 'kushbansal@gmail.com'),
('ayd8871', 'Naman', 'Bharwaj', 'nambhardwaj@gmail.com'),
('auy1857', 'Deepak', 'Sharma', 'deepak@gmail.com'),
('aws7935', 'Geeta', 'vishwas', 'geeta123@gmail.com'),
('mos9927', 'Amir', 'Khan', 'amir@gmail.com'),
('apy8600', 'Abhishek', 'Rana', 'abhi@gmail.com'),
('awh1935', 'Mukesh', 'Rawat', 'mukesh@gmail.com'),
('aws1935', 'Gaurav', 'Sharma', 'gauravsharma101@gmail.com'),
('erf4296', 'Mansi', 'Singh', 'singhmansi@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
