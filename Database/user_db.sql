-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 25, 2026 at 07:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_id` varchar(50) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `surname` varchar(100) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `age` varchar(10) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_id`, `first_name`, `surname`, `dob`, `age`, `gender`, `address`, `mobile`) VALUES
('STU001', 'Kaweesh', 'Liyanage', '2002-05-15', '24', 'Male', 'Colombo, Sri Lanka', '0712345671'),
('STU002', 'Nimal', 'Perera', '2001-08-20', '25', 'Male', 'Kandy, Sri Lanka', '0771234562'),
('STU003', 'Kamani', 'Silva', '2003-02-10', '23', 'Female', 'Galle, Sri Lanka', '0751234563'),
('STU004', 'Ruwan', 'Kumara', '2000-11-30', '26', 'Male', 'Matara, Sri Lanka', '0781234564'),
('STU005', 'Dilini', 'Jayasinghe', '2002-01-25', '24', 'Female', 'Negombo, Sri Lanka', '0711234565'),
('STU006', 'Sunil', 'Fernando', '2001-06-12', '25', 'Male', 'Panadura, Sri Lanka', '0771234566'),
('STU007', 'Priya', 'Darshani', '2003-09-05', '23', 'Female', 'Kalutara, Sri Lanka', '0761234567'),
('STU008', 'Asanka', 'Guruge', '2002-04-18', '24', 'Male', 'Ratnapura, Sri Lanka', '0721234568'),
('STU009', 'Ishara', 'Madushanka', '2000-12-22', '26', 'Male', 'Kurunegala, Sri Lanka', '0701234569'),
('STU010', 'Sanduni', 'Hettiarachchi', '2002-07-08', '24', 'Female', 'Gampaha, Sri Lanka', '0711234570'),
('STU011', 'Kasun', 'Rajapaksha', '2001-03-14', '25', 'Male', 'Anuradhapura, Sri Lanka', '0771234571'),
('STU012', 'Tharindu', 'Bandara', '2003-10-28', '23', 'Male', 'Badulla, Sri Lanka', '0751234572'),
('STU013', 'Nuwan', 'Zoysa', '2002-11-11', '24', 'Male', 'Jaffna, Sri Lanka', '0781234573'),
('STU014', 'Hansani', 'Liyanage', '2001-05-30', '25', 'Female', 'Trincomalee, Sri Lanka', '0711234574'),
('STU015', 'Prasanna', 'Vithanage', '2000-02-15', '26', 'Male', 'Matale, Sri Lanka', '0771234575'),
('STU016', 'Malki', 'Wickramasinghe', '2003-04-20', '23', 'Female', 'Kegalle, Sri Lanka', '0761234576'),
('STU017', 'Dinesh', 'Priyantha', '2002-08-12', '24', 'Male', 'Puttalam, Sri Lanka', '0721234577'),
('STU018', 'Chathuri', 'Sanjeewani', '2001-01-05', '25', 'Female', 'Hambantota, Sri Lanka', '0701234578'),
('STU019', 'Rohan', 'Gunawardena', '2000-09-19', '26', 'Male', 'Monaragala, Sri Lanka', '0711234579'),
('STU020', 'Gayani', 'Abeykoon', '2003-12-01', '23', 'Female', 'Polonnaruwa, Sri Lanka', '0771234580'),
('STU021', 'Amal', 'Wickrama', '2002-03-25', '24', 'Male', 'Battaramulla, Sri Lanka', '0714567891'),
('STU022', 'Sajith', 'Premadasa', '2001-09-12', '25', 'Male', 'Hambantota, Sri Lanka', '0774567892'),
('STU023', 'Dilrukshi', 'Perera', '2003-11-05', '23', 'Female', 'Wattala, Sri Lanka', '0754567893'),
('STU024', 'Mahesh', 'Silva', '2000-05-18', '26', 'Male', 'Moratuwa, Sri Lanka', '0784567894'),
('STU025', 'Pavani', 'Fernando', '2002-08-30', '24', 'Female', 'Dehiwala, Sri Lanka', '0714567895'),
('STU026', 'Kusal', 'Mendis', '2001-02-14', '25', 'Male', 'Ambalangoda, Sri Lanka', '0774567896'),
('STU027', 'Nadeesha', 'Hemamali', '2003-06-22', '23', 'Female', 'Nuwara Eliya, Sri Lanka', '0764567897'),
('STU028', 'Janaka', 'Kumbuka', '2002-12-08', '24', 'Male', 'Avissawella, Sri Lanka', '0724567898'),
('STU029', 'Oshada', 'Senanayake', '2000-01-19', '26', 'Male', 'Dambulla, Sri Lanka', '0704567899'),
('STU030', 'Lakmali', 'Wijesinghe', '2002-10-10', '24', 'Female', 'Chilaw, Sri Lanka', '0714567900'),
('STU031', 'Gayan', 'Thushara', '2001-07-04', '25', 'Male', 'Balapitiya, Sri Lanka', '0774567901'),
('STU032', 'Madushan', 'Chathuranga', '2003-04-29', '23', 'Male', 'Ja-Ela, Sri Lanka', '0754567902'),
('STU033', 'Supun', 'Malshan', '2002-02-11', '24', 'Male', 'Tangalle, Sri Lanka', '0784567903'),
('STU034', 'Vindya', 'Koushalya', '2001-11-20', '25', 'Female', 'Embilipitiya, Sri Lanka', '0714567904'),
('STU035', 'Ashen', 'Bandara', '2000-06-15', '26', 'Male', 'Bibile, Sri Lanka', '0774567905'),
('STU036', 'Rashmi', 'Nisansala', '2003-08-25', '23', 'Female', 'Horana, Sri Lanka', '0764567906'),
('STU037', 'Sahan', 'Arachchi', '2002-09-12', '24', 'Male', 'Beruwala, Sri Lanka', '0724567907'),
('STU038', 'Eranga', 'Lakmal', '2001-04-05', '25', 'Male', 'Weligama, Sri Lanka', '0704567908'),
('STU039', 'Nipuni', 'Kanchana', '2000-03-19', '26', 'Female', 'Hikkaduwa, Sri Lanka', '0714567909'),
('STU040', 'Nuwanthi', 'Fernando', '2003-01-01', '23', 'Female', 'Wennappuwa, Sri Lanka', '0774567910');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `password`) VALUES
(1, 'kaweesh', 'Liyanage', 'kaweesh@gmail.com', '1234'),
(2, 'nimal', 'silva', 'silva@gmail.com', '1234'),
(3, 'sethum', 'dimanshaka', 'sethum@gmail.com', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
