-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Sep 18, 2022 at 11:20 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `bid` int(5) NOT NULL,
  `Pname` varchar(20) NOT NULL,
  `Disease` varchar(20) NOT NULL,
  `AddmissionDate` date NOT NULL,
  `DischargeDate` date DEFAULT NULL,
  `Doctor Name` varchar(20) NOT NULL,
  `Doctor Charge` int(10) NOT NULL,
  `Room Type` varchar(20) NOT NULL,
  `Room cost` int(10) NOT NULL,
  `Total Bill` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `did` int(5) NOT NULL,
  `dname` varchar(20) NOT NULL,
  `Speciality` varchar(20) NOT NULL,
  `Joining` date DEFAULT NULL,
  `Experince` int(5) NOT NULL,
  `Status` int(5) NOT NULL,
  `Charge` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`did`, `dname`, `Speciality`, `Joining`, `Experince`, `Status`, `Charge`) VALUES
(1, 'Dr.Jayant', 'Cardiologist', '2022-06-15', 5, 1, 2000),
(2, 'Dr.Abhishek', 'MS', '2022-06-15', 6, 1, 2500);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(10) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('Ram', 'ram123'),
('Sam', 'sam12'),
('Sham', 'sham1');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `Pid` int(5) NOT NULL,
  `Pname` varchar(20) NOT NULL,
  `AddmissionDate` date DEFAULT NULL,
  `rid` int(5) NOT NULL,
  `did` int(5) NOT NULL,
  `Diseases` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`Pid`, `Pname`, `AddmissionDate`, `rid`, `did`, `Diseases`) VALUES
(1, 'Preeti', '2022-06-06', 3, 1, 'HBP'),
(2, 'Kritika', '2022-06-12', 2, 2, 'GRP'),
(4, 'haja', '2022-08-15', 3, 1, 'asd');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `rid` int(5) NOT NULL,
  `type` varchar(20) NOT NULL,
  `cost` int(10) NOT NULL,
  `count` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`rid`, `type`, `cost`, `count`) VALUES
(1, 'General', 250, 10),
(2, 'Deluxe Non AC', 500, 20),
(3, 'Deluxe AC', 1000, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`Pid`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`rid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
