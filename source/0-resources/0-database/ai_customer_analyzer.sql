-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2023 at 07:25 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ai_customer_analyzer`
--

-- --------------------------------------------------------

--
-- Table structure for table `audio_data`
--

CREATE TABLE `audio_data` (
  `auto_id` int(250) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(100) NOT NULL,
  `stall_no` varchar(100) NOT NULL,
  `employee_id` varchar(250) NOT NULL,
  `employee_name` varchar(300) NOT NULL,
  `transcription` longtext NOT NULL,
  `prediction` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `audio_data`
--

INSERT INTO `audio_data` (`auto_id`, `date`, `time`, `stall_no`, `employee_id`, `employee_name`, `transcription`, `prediction`) VALUES
(7, '2023-03-21', '22:56:16', '001', 'EMP-12', 'David Mark', 'hello so this it is a wonderful product and if a music and it has longer one of usage', 'Positive'),
(8, '2023-03-21', '22:56:26', '001', 'EMP-12', 'David Mark', 'high quality product and we are highly recommend this product to buy', 'Positive'),
(9, '2023-03-21', '22:56:41', '001', 'EMP-12', 'David Mark', 'I don\'t like this I don\'t like this I don\'t I don\'t like this for I can this is one of that and it is not good', 'Negative'),
(10, '2023-02-21', '22:56:59', '001', 'EMP-12', 'David Mark', 'not not give one so what you can do you can', 'Neutral'),
(11, '2023-03-20', '22:57:15', '001', 'EMP-12', 'David Mark', 'I don\'t know whether it is possible not but it has lot of things but everything is good because it is for good', 'Positive');

-- --------------------------------------------------------

--
-- Table structure for table `setting`
--

CREATE TABLE `setting` (
  `auto_id` int(250) NOT NULL,
  `_key` varchar(1000) NOT NULL,
  `_value` varchar(3000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `setting`
--

INSERT INTO `setting` (`auto_id`, `_key`, `_value`) VALUES
(1, 'voice_lang', 'English');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `auto_id` int(250) NOT NULL,
  `username` varchar(1000) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`auto_id`, `username`, `password`) VALUES
(1, 'admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `vision_data`
--

CREATE TABLE `vision_data` (
  `auto_id` int(250) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(60) NOT NULL,
  `image_url` varchar(5000) NOT NULL,
  `mask` varchar(60) NOT NULL,
  `age` varchar(50) NOT NULL,
  `age_category` varchar(50) NOT NULL,
  `gender` varchar(60) NOT NULL,
  `emotion` varchar(100) NOT NULL,
  `race` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vision_data`
--

INSERT INTO `vision_data` (`auto_id`, `date`, `time`, `image_url`, `mask`, `age`, `age_category`, `gender`, `emotion`, `race`) VALUES
(162, '2023-03-21', '14:56:51', '[NONE]', 'Found', '28', 'Adult', 'Man', 'Angry', 'Black'),
(163, '2023-03-19', '15:57:00', '[NONE]', 'Found', '38', 'Elder', 'Woman', 'Happy', 'Asian'),
(164, '2023-02-19', '15:57:04', '[NONE]', 'Not Found', '38', 'Teenage', 'Man', 'Fear', 'Asian'),
(165, '2023-03-21', '15:57:07', '[NONE]', 'Not Found', '33', 'Kid', 'Man', 'Sad', 'White'),
(166, '2023-03-21', '15:57:10', '[NONE]', 'Not Found', '34', 'Adult', 'Man', 'Neutral', 'Asian'),
(167, '2023-03-20', '15:57:12', '[NONE]', 'Not Found', '35', 'Adult', 'Man', 'Surprise', 'Asian');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audio_data`
--
ALTER TABLE `audio_data`
  ADD PRIMARY KEY (`auto_id`);

--
-- Indexes for table `setting`
--
ALTER TABLE `setting`
  ADD PRIMARY KEY (`auto_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`auto_id`);

--
-- Indexes for table `vision_data`
--
ALTER TABLE `vision_data`
  ADD PRIMARY KEY (`auto_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audio_data`
--
ALTER TABLE `audio_data`
  MODIFY `auto_id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `setting`
--
ALTER TABLE `setting`
  MODIFY `auto_id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `auto_id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vision_data`
--
ALTER TABLE `vision_data`
  MODIFY `auto_id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=168;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
