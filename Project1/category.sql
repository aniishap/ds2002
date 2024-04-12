-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 12, 2024 at 01:48 AM
-- Server version: 8.0.36-0ubuntu0.22.04.1
-- PHP Version: 8.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sakila`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` tinyint UNSIGNED NOT NULL,
  `name` varchar(25) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `name`, `last_update`) VALUES
(1, 'Action', '2006-02-15 04:46:27'),
(2, 'Animation', '2006-02-15 04:46:27'),
(3, 'Children', '2006-02-15 04:46:27'),
(4, 'Classics', '2006-02-15 04:46:27'),
(5, 'Comedy', '2006-02-15 04:46:27'),
(6, 'Documentary', '2006-02-15 04:46:27'),
(7, 'Drama', '2006-02-15 04:46:27'),
(8, 'Family', '2006-02-15 04:46:27'),
(9, 'Foreign', '2006-02-15 04:46:27'),
(10, 'Games', '2006-02-15 04:46:27'),
(11, 'Horror', '2006-02-15 04:46:27'),
(12, 'Music', '2006-02-15 04:46:27'),
(13, 'New', '2006-02-15 04:46:27'),
(14, 'Sci-Fi', '2006-02-15 04:46:27'),
(15, 'Sports', '2006-02-15 04:46:27'),
(16, 'Travel', '2006-02-15 04:46:27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `category_id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
