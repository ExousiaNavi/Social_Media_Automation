-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 01, 2024 at 05:35 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `datasource`
--

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

CREATE TABLE `dataset` (
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `date` datetime NOT NULL,
  `id` int(11) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `currency` varchar(255) NOT NULL,
  `post_id` bigint(20) NOT NULL,
  `link` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dataset`
--

INSERT INTO `dataset` (`created_at`, `date`, `id`, `brand`, `currency`, `post_id`, `link`) VALUES
('2024-10-01 03:26:45', '2024-10-01 05:26:06', 9, 'Six6s', 'BDT', 728, 'https://t.me/Six6s_Bangla/728'),
('2024-10-01 03:33:08', '2024-10-01 05:32:22', 10, 'Six6s', 'BDT', 820, 'https://t.me/Six6s_Bangla/820');

-- --------------------------------------------------------

--
-- Table structure for table `telegram_views_reactions`
--

CREATE TABLE `telegram_views_reactions` (
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id` int(11) NOT NULL,
  `dataset_id` int(11) NOT NULL,
  `views` bigint(20) DEFAULT NULL,
  `reactions` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `telegram_views_reactions`
--

INSERT INTO `telegram_views_reactions` (`created_at`, `id`, `dataset_id`, `views`, `reactions`) VALUES
('2024-10-01 03:27:20', 12, 9, 3100, 11),
('2024-10-01 03:33:59', 13, 10, 1302, 6);

-- --------------------------------------------------------

--
-- Table structure for table `twitter`
--

CREATE TABLE `twitter` (
  `id` int(11) NOT NULL,
  `date` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `views` varchar(255) NOT NULL,
  `likes` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `twitter`
--

INSERT INTO `twitter` (`id`, `date`, `url`, `views`, `likes`) VALUES
(97, '2024-08-05', 'https://x.com/BJ_BajiCharity/status/1820312314312077820', '44', '0'),
(98, '2024-08-02', 'https://x.com/BJ_BajiCharity/status/1819208549337031151', '37', '0'),
(99, '2024-08-09', 'https://x.com/BJ_BajiCharity/status/1821732818570867171', '72', '1'),
(100, '2024-08-07', 'https://x.com/BJ_BajiCharity/status/1821095785401839968', '21', '0'),
(101, '2024-08-12', 'https://x.com/BJ_BajiCharity/status/1822815489506042352', '21', '0'),
(102, 'No value', 'https://x.com/Bjsports_OFC/status/1818831287274045696', '0', '0'),
(103, 'No value', 'https://x.com/Bjsports_OFC/status/1818839131008450825', '0', '0'),
(104, 'No value', 'https://x.com/Bjsports_OFC/status/1818855076603060666', '0', '0'),
(105, 'No value', 'https://x.com/Bjsports_OFC/status/1818847446534934547', '0', '0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dataset`
--
ALTER TABLE `dataset`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `telegram_views_reactions`
--
ALTER TABLE `telegram_views_reactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `telegram_views_reactions_ibfk_1` (`dataset_id`);

--
-- Indexes for table `twitter`
--
ALTER TABLE `twitter`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dataset`
--
ALTER TABLE `dataset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `telegram_views_reactions`
--
ALTER TABLE `telegram_views_reactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `twitter`
--
ALTER TABLE `twitter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `telegram_views_reactions`
--
ALTER TABLE `telegram_views_reactions`
  ADD CONSTRAINT `telegram_views_reactions_ibfk_1` FOREIGN KEY (`dataset_id`) REFERENCES `dataset` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
