-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 18, 2020 at 10:02 AM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment3`
--

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `USER` (
  `id` int(8) NOT NULL,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nationality` varchar(100) NOT NULL,
  `significant_other` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `USER` VALUES
(9734109, 'Eduard', 'Khil', '1983-05-11', '+7 8 9912 8733', 'trolleyguy@gmail.com', 'Russian', 89734217),
(9734512, 'Mikhail', 'Mishustin', '2007-11-12', '+7 9 4782 0921', 'mikki.mishutin@hotmail.com', 'Australian', 99732114),
(19084223, 'Lucy', 'Ali','1989-05-02', '+61 4 2323 1198', 'lucy.ali1@uq.edu.au', 'Australian', 23987721),
(19084221, 'Lucy', 'Smith','1989-06-02', '+61 4 2323 1198', 'lucy.ali2@uq.edu.au', 'Australian', NULL),
(19087623, 'John', 'Monarch', '1983-12-06', '+61 4 9999 8888', 'john.monarch@uq.edu.au', 'Australian', 23987721),
(19088623, 'Ursula', 'Smith', '2000-01-01', '+61 7 8765 1234', 'u.smith@qut.edu.au', 'Bolivian', 19488623),
(19088644, 'Marcus', 'Jacobs', '1983-12-05', '+61 7 8335 1334', 'marcus.jacobs@uq.edu', 'Australian', 19439623),
(19439623, 'Nevena', 'Ivanovic', '2002-01-01', '+61 7 2222 1122', 'Nevena@gmail.com', 'Montenegrin', 19088644),
(19488623, 'Leo', 'Montgomery', '2003-01-01', '+61 7 8765 1256', 'leolovescars@gmail.com', 'Australian', 19088623),
(19609863, 'Edi', 'Rama', '1999-01-01', '+35 5 2298 0927', 'edi.rama@uq.edu.au', 'Albanian', NULL),
(22732951, 'Jamie', 'Sleeman', '1997-03-21', '+61 7 8192 2984', 'joshua@gmail.com', 'Australian', 23987721),
(23982121, 'Hye-sun', 'Ku', '1997-04-21', '+61 4 5582 1199', 'ku@uq.edu.au', 'Korean', 23987721),
(23987721, 'Min-ho', 'Lee', '2000-03-26', '+61 4 5582 1923', 'lee@uq.edu.au', 'Korean', 23982121),
(38982921, 'Jeong-hyeok', 'Ri', '1996-06-19', '+82 8 3378 7123', 'ri.jonghyok@hotmail.com', 'Korean', NULL),
(41284471, 'Bong-soon', 'Park', '1992-04-12', '+82 2 3391 2245', 'park.bongsoon@ainsoft.com', 'Australian', NULL),
(42180081, 'Se-ri', 'Yoon', '2000-04-13', '+82 2 1187 3982', 'yoon.seri@queen.com', 'Korean', NULL),
(66234500, 'Sven', 'Kirsch', '2002-04-13', '+49 3 2217 7820', 'sven.kirsch@uq.edu.au', 'German', NULL),
(66234591, 'Matthieu', 'Loiselle', '1995-04-12', '+33 9 0822 3491', 'matt.loiselle@uq.edu.au', 'French', NULL),
(66234592, 'Gabriel', 'Duperre', '2000-03-26', '+33 9 0822 3432', 'Gabe.dupe@gmail.comm', 'French', NULL),
(66234593, 'Honore', 'Avare', '2000-03-26', '+33 9 0822 3444', 'honore@hotmail', 'French', 66234594),
(66234594, 'Margit', 'Gade', '1983-12-15', '+45 3 4491 9923', 'margit.gade1@uq.edu.au', 'Australian', 66234593),
(66234595, 'Lavinia', 'Pinto', '1983-10-25', '+55 5 9920 0012', 'lavinia@hotmail.com', 'Brazilian', NULL),
(66234596, 'Yvonne', 'Holtzmann', '1999-12-12', '+49 4 8890 2311', 'holtzmann@gmail.com', 'German', NULL),
(88271481, 'Radhiya', 'Aswad', '2000-12-25', '+39 7 1182 3374', 'radhiya.aswad@uq.edu.au.com', 'Italian', 90316354),
(88272954, 'Joshua', 'Hernandez', '1985-12-26', '+1 7 8192 2984', 'joshua@gmail.com', 'American', 88276354),
(88276354, 'Beatrice', 'Hernandez', '2004-12-25', '+1 7 8892 3374', 'beatrice@gmail.com', 'American', 88272954),
(89734217, 'Nadeea', 'Volianova', '1990-12-25', '+7 8 0967 9276', 'nadeea@uq.edu.au', 'Russian', 9734109),
(90316354, 'Mahrus', 'Bitar', '1992-10-12', '+1 7 2200 3311', 'uq.edu.au@gmail.com', 'American', 88271481),
(99002931, 'Grace', 'Jeon', '1997-09-16', '+82 2 8734 3382', 'grace.jeon@uq.edu.au', 'Korean', NULL),
(99723671, 'Man-wol', 'Jang', '1983-10-12', '+82 8 2763 2383', 'jang@uq.edu.au', 'Korean', NULL),
(99732114, 'Sofia', 'Rotaru', '1988-05-12', '+38 0 1192 8337', 'sofia.rotaru@gmail.com', 'Ukraine', 9734512),
(190876632, 'Ilir', 'Meta', '1998-05-12', '+35 5 4678 0927', 'ilirmeta@hotmail.com', 'Australian', 196666632),
(196666632, 'Monika', 'Kryemadhi', '1996-05-13', '+35 5 4621 0927', 'Monika.Kryemadhi@uq.edu.au', 'Albanian', 190876632);

-- --------------------------------------------------------
--
-- Table structure for table `Attends`
--

CREATE TABLE `ATTENDS` (
  `user_id` int(8) NOT NULL,
  `title` varchar(200) NOT NULL,
  `event_location` varchar(200) NOT NULL,
  `event_date` date NOT NULL,
  `travel_method` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Attends`
--

INSERT INTO `ATTENDS` VALUES
(9734109, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(9734109, 'Melbourne Cup', 'Flemington Racecourse', '2017-11-07', 'Bus'),
(9734109, 'Melbourne Cup', 'Flemington Racecourse', '2018-11-06', 'Train'),
(9734109, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Train'),
(9734109, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(9734109, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Train'),
(9734512, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(19084223, 'Ekka', '600 Gregory Tce, Bowen Hills','2018-08-10', 'Bus'),
(19084223, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Walk'),
(19084223, 'The Nutcracker', 'Sydney Opera House', '2019-11-30', 'Bus'),
(19084223, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(19087623, 'Bathurst 1000', 'Bathurst, NSW','2019-10-10', 'Bus'),
(19087623, 'Ekka', '600 Gregory Tce, Bowen Hills','2017-08-11', 'Bus'),
(19087623, 'Ekka', '600 Gregory Tce, Bowen Hills','2018-08-10', 'Bus'),
(19087623, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Bus'),
(19087623, 'GC 600', 'Surfer\'s Paradise, QLD', '2018-10-19', 'Train'),
(19087623, 'GC 600','Surfer\'s Paradise, QLD',  '2019-10-25', 'Bus'),
(19087623, 'The Nutcracker', 'Sydney Opera House', '2019-11-30', 'Bus'),
(19087623, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(19088623, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(19088623, 'Melbourne Cup', 'Flemington Racecourse', '2019-11-05', 'Car'),
(19088623, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(19084221, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(19084221, 'Melbourne Cup', 'Flemington Racecourse', '2019-11-05', 'Car'),
(19084221, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(19088644, 'Bathurst 1000', 'Bathurst, NSW','2017-10-05', 'Bus'),
(19088644, 'Bathurst 1000', 'Bathurst, NSW','2018-10-04', 'Car'),
(19088644, 'Bathurst 1000', 'Bathurst, NSW', '2019-10-10', 'Car'),
(19088644, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(19088644, 'GC 600', 'Surfer\'s Paradise, QLD', '2016-10-21', 'Bus'),
(19088644, 'GC 600','Surfer\'s Paradise, QLD',  '2018-10-19', 'Train'),
(19088644, 'GC 600','Surfer\'s Paradise, QLD',  '2019-10-25', 'Taxi'),
(19088644, 'The Nutcracker', 'Sydney Opera House', '2019-11-30', 'Bus'),
(19088644, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Train'),
(19439623, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(19439623, 'K-Drama Appreciation Day', 'Parliament House, Canberra', '2020-04-12', 'Bus'),
(19488623, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(19609863, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Train'),
(22732951, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Bus'),
(22732951, 'The Nutcracker', 'Sydney Opera House', '2019-11-30', 'Bus'),
(23982121, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(23987721, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(41284471, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(42180081, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(66234500, 'Melbourne Cup', 'Flemington Racecourse',  '2017-11-07', 'Bus'),
(66234500, 'Melbourne Cup', 'Flemington Racecourse', '2018-11-06', 'Train'),
(66234500, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Train'),
(66234500, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(66234500, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Train'),
(66234591, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Bus'),
(66234593, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Bus'),
(66234594, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Bus'),
(66234595, 'Bathurst 1000', 'Bathurst, NSW', '2018-10-04', 'Taxi'),
(66234595, 'Bathurst 1000', 'Bathurst, NSW', '2019-10-10', 'Taxi'),
(66234595, 'Bathurst 1000', 'Bathurst, NSW', '2020-10-15', 'Bus'),
(66234595, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Taxi'),
(66234596, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(88271481, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(88271481, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(88271481, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Bus'),
(88271481, 'UQ Open Day', 'St Lucia, QLD 4072', '2020-02-12', 'Train'),
(88271481, 'UQ Open Day', 'St Lucia, QLD 4072', '2020-08-02', 'Ferry'),
(88272954, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Bus'),
(88276354, 'Bathurst 1000','Bathurst, NSW',  '2017-10-05', 'Car'),
(88276354, 'Bathurst 1000', 'Bathurst, NSW', '2018-10-04', 'Bus'),
(88276354, 'Ekka', '600 Gregory Tce, Bowen Hills', '2017-08-11', 'Ferry'),
(88276354, 'Ekka', '600 Gregory Tce, Bowen Hills', '2018-08-10', 'Bus'),
(88276354, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(88276354, 'Melbourne Cup', 'Flemington Racecourse', '2017-11-07', 'Bus'),
(88276354, 'Melbourne Cup', 'Flemington Racecourse', '2018-11-06', 'Car'),
(89734217, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(89734217, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(89734217, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Train'),
(90316354, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(90316354, 'Melbourne Cup', 'Flemington Racecourse', '2017-11-07', 'Bus'),
(90316354, 'Melbourne Cup', 'Flemington Racecourse', '2018-11-06', 'Train'),
(90316354, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Train'),
(90316354, 'UQ Open Day', 'St Lucia, QLD 4072', '2018-02-11', 'Bus'),
(99002931, 'Bathurst 1000', 'Bathurst, NSW', '2018-10-04', 'Bus'),
(99002931, 'Ekka', '600 Gregory Tce, Bowen Hills','2017-08-11', 'Walk'),
(99002931, 'GC 600', 'Surfer\'s Paradise, QLD', '2019-10-25', 'Train'),
(99002931, 'Melbourne Cup', 'Flemington Racecourse', '2019-11-05', 'Bus'),
(99002931, 'UQ Open Day', 'St Lucia, QLD 4072', '2020-02-12', 'Car'),
(99723671, 'Ekka', '600 Gregory Tce, Bowen Hills','2017-08-11', 'Bus'),
(99723671, 'Ekka', '600 Gregory Tce, Bowen Hills','2018-08-10', 'Car'),
(99723671, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Bus'),
(99723671, 'K-Drama Appreciation Day', 'Parliament House, Canberra', '2020-04-12', 'Bus'),
(99723671, 'The Nutcracker', 'Sydney Opera House', '2019-11-30', 'Bus'),
(99723671, 'UQ Open Day', 'St Lucia, QLD 4072', '2020-02-12', 'Bus'),
(99732114, 'Ekka', '600 Gregory Tce, Bowen Hills', '2019-08-09', 'Train'),
(99732114, 'Melbourne Cup', 'Flemington Racecourse', '2017-11-07', 'Bus'),
(99732114, 'Melbourne Cup', 'Flemington Racecourse', '2018-11-06', 'Train'),
(99732114, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Train'),
(99732114, 'UQ Open Day', 'St Lucia, QLD 4072', '2019-08-03', 'Train'),
(190876632, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(190876632, 'Melbourne Cup', 'Flemington Racecourse', '2017-11-07', 'Bus'),
(190876632, 'Melbourne Cup', 'Flemington Racecourse', '2018-11-06', 'Train'),
(190876632, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Bus'),
(196666632, 'Bathurst 1000', 'Bathurst, NSW',  '2018-10-04', 'Bus'),
(196666632, 'Ekka', '600 Gregory Tce, Bowen Hills','2019-08-09', 'Train'),
(196666632, 'GC 600', 'Surfer\'s Paradise, QLD', '2019-10-25', 'Bus'),
(196666632, 'Melbourne Cup', 'Flemington Racecourse', '2019-11-05', 'Bus'),
(196666632, 'UQ Open Day', 'St Lucia, QLD 4072', '2020-02-12', 'Bus'),
(196666632, 'The Happy Prince', 'Sydney Opera House', '2019-11-27', 'Train');

-- --------------------------------------------------------

--
-- Table structure for table `EVENT`
--

CREATE TABLE `EVENT` (
  `title` varchar(200) NOT NULL,
  `event_date` date NOT NULL,
  `description` text,
  `event_location` varchar(200) NOT NULL,
  `sponsor` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Event`
--

INSERT INTO `EVENT` VALUES
('Bathurst 1000', '2017-10-05', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Bathurst 1000', '2018-10-04', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Bathurst 1000', '2019-10-10', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Bathurst 1000', '2020-10-15', 'Pinnacle of motorsport in Australia held annually on  Mount Panorama Circuit', 'Bathurst, NSW', 'Supercheap Auto'),
('Ekka', '2017-08-11', 'The EKKA is Queensland\'s largest event and your greatest chance throughout the year to find out what life on the farm is really about', '600 Gregory Tce, Bowen Hills', 'Queensland Government'),
('Ekka', '2018-08-10', 'The EKKA is Queensland\'s largest event and your greatest chance throughout the year to find out what life on the farm is really about', '600 Gregory Tce, Bowen Hills', 'Queensland Government'),
('Ekka', '2019-08-09', 'The EKKA is Queensland\'s largest event and your greatest chance throughout the year to find out what life on the farm is really about', '600 Gregory Tce, Bowen Hills', 'Queensland Government'),
('GC 600', '2016-10-21', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('GC 600', '2017-10-20', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('GC 600', '2018-10-19', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('GC 600', '2019-10-25', 'Queensland’s premier Supercars event, it is the final endurance race on the Supercars calendar', 'Surfer\'s Paradise, QLD', 'Vodafone'),
('K-Drama Appreciation Day', '2020-04-12', 'For anyone with a passion for K-Dramas. We\'ll be screening Boys over Flowers, Crash Landing on You and Descendents of the Sun. Get excited! Bring popcorn and your love for K-Drams.', 'Parliament House, Canberra', 'ANU Korean Club'),
('Melbourne Cup', '2017-11-07', 'A prestigious Australian thoroughbred horse race.', 'Flemington Racecourse', 'Victoria Government'),
('Melbourne Cup', '2018-11-06', 'A prestigious Australian thoroughbred horse race.', 'Flemington Racecourse', 'Victoria Government'),
('Melbourne Cup', '2019-11-05', 'A prestigious Australian thoroughbred horse race.', 'Flemington Racecourse', 'Victoria Government'),
('The Happy Prince', '2019-11-27', 'In Oscar Wilde\'s lyrical story, a prince who has lived a carefree live behind his palace walls becomes a magnificent golden statue.', 'Sydney Opera House', 'The Australian Ballet'),
('The Nutcracker', '2019-11-30', 'There\'s nothing like a tradional Nutcracker to get you in the mood for the festive season.', 'Sydney Opera House', 'The Australian Ballet'),
('UQ Open Day', '2018-02-11', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland'),
('UQ Open Day', '2019-08-03', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland'),
('UQ Open Day', '2020-02-12', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland'),
('UQ Open Day', '2020-08-02', 'Explore options at UQ', 'St Lucia, QLD 4072', 'University of Queensland');

-- --------------------------------------------------------

--
-- Table structure for table `Friends`
--

CREATE TABLE `FRIENDS` (
  `requestor` int(8) NOT NULL,
  `requestee` int(8) NOT NULL,
  `requested_date` date NOT NULL, 
  `accepted_date` date
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Friends`
--

INSERT INTO `FRIENDS` VALUES
(9734109, 19084223, '2017-09-21', '2017-09-22'),
(9734109, 19087623, '2011-06-30', '2017-09-21'),
(9734109, 19088644, '2015-12-26', '2016-09-21'),
(9734109, 22732951, '2015-09-22', '2015-09-23'),
(9734109, 41284471, '2011-06-19', '2015-09-22'),
(9734109, 66234500, '2012-04-12', '2012-04-13'),
(9734109, 89734217, '2012-11-27', '2012-12-12'),
(9734512, 19084223, '2017-03-14', '2017-04-14'),
(9734512, 19087623, '2020-09-02', '2020-10-02'),
(9734512, 19088644, '2016-01-29', '2017-01-29'),
(9734512, 22732951, '2010-06-27', '2010-07-27'),
(9734512, 99732114, '2014-12-29', '2015-01-01'),
(19084223, 19088623, '2015-01-29', '2015-01-31'),
(19084223, 19088644, '2014-07-15', '2015-07-15'),
(19084223, 19439623, '2019-07-08', '2019-07-09'),
(19084223, 19488623, '2020-09-11', '2020-09-12'),
(19084223, 23982121, '2020-10-30', '2020-11-02'),
(19084223, 23987721, '2010-10-31', '2010-11-01'),
(19084223, 41284471, '2017-01-01', '2017-01-02'),
(19084223, 66234500, '2016-04-09', '2016-04-10'),
(19084223, 66234593, '2016-09-18', '2016-09-19'),
(19084223, 66234594, '2017-11-03', '2017-11-04'),
(19084223, 66234596, '2019-01-24', '2019-01-25'),
(19084223, 88271481, '2016-01-28', '2016-01-29'),
(19084223, 88272954, '2020-11-04', '2020-11-05'),
(19084223, 88276354, '2018-03-14', '2018-03-15'),
(19084223, 89734217, '2012-08-08', '2012-08-09'),
(19084223, 90316354, '2020-01-19', '2020-01-20'),
(19084223, 99732114, '2013-09-13', '2013-09-14'),
(19084223, 190876632, '2011-07-24', '2011-07-25'),
(19084223, 196666632, '2016-10-27', '2016-10-28'),
(196666632, 19084223, '2016-10-27', '2016-10-28'),
(19087623, 19088623, '2014-04-07', '2014-04-08'),
(19087623, 19088644, '2010-10-14', '2010-10-15'),
(19087623, 19439623, '2017-03-09', '2017-03-10'),
(19087623, 19488623, '2014-05-31', '2014-06-20'),
(19087623, 23982121, '2015-05-20', '2015-05-21'),
(19087623, 23987721, '2018-01-06', '2018-01-07'),
(19087623, 66234500, '2016-07-03', '2016-07-04'),
(19087623, 66234593, '2019-02-14', '2019-02-15'),
(19087623, 66234594, '2012-11-12', '2012-11-13'),
(19087623, 66234596, '2015-05-01', '2015-06-01'),
(19087623, 88271481, '2010-11-04', '2010-11-06'),
(19087623, 88272954, '2019-07-06', '2019-07-30'),
(19087623, 88276354, '2014-05-27', NULL),
(19087623, 89734217, '2019-03-25', '2019-03-30'),
(19087623, 90316354, '2014-03-01', '2014-04-01'),
(19087623, 99732114, '2018-08-11', '2018-09-11'),
(19087623, 190876632, '2013-02-18', NULL),
(19087623, 196666632, '2017-01-11', '2017-02-11'),
(19088623, 19088644, '2019-07-31', '2019-08-05'),
(19088623, 19488623, '2015-04-17', '2015-04-18'),
(19088623, 22732951, '2011-02-06', '2011-02-09'),
(19088644, 19439623, '2010-09-05', '2010-09-10'),
(19088644, 19488623, '2018-11-20', NULL),
(19088644, 22732951, '2014-07-13', NULL),
(19088644, 23982121, '2013-06-05', NULL),
(19088644, 23987721, '2012-01-20', NULL),
(19088644, 66234500, '2017-02-18', NULL),
(19088644, 66234593, '2010-10-12', '2010-10-13'),
(19088644, 66234594, '2010-01-08', '2010-01-10'),
(19088644, 66234596, '2018-09-23', NULL),
(19088644, 88271481, '2019-03-10', '2019-04-10'),
(19088644, 88272954, '2016-11-29', '2017-01-01'),
(19088644, 88276354, '2015-11-15', '2015-11-16'),
(19088644, 89734217, '2015-07-12', '2015-07-13'),
(19088644, 90316354, '2013-10-31', '2013-11-02'),
(19088644, 99732114, '2017-04-14', '2017-05-14'),
(19088644, 190876632, '2016-11-07', '2017-11-07'),
(19088644, 19084223, '2012-10-29', NULL),
(19088644, 19084221, '2013-10-29', NULL),
(19088644, 19087623, '2014-10-29', NULL),
(19088644, 19088644, '2015-10-29', NULL),
(19088644, 9734512, '2017-10-29', NULL),
(19088644, 41284471, '2019-10-29', NULL),
(19439623, 22732951, '2013-07-15', NULL),
(19439623, 66234500, '2010-04-30', NULL),
(19439623, 66234596, '2018-04-22', '2018-05-22'),
(19488623, 22732951, '2014-05-20', '2014-05-21'),
(19609863, 66234500, '2017-09-11', '2017-09-12'),
(19609863, 66234596, '2012-08-09', '2012-08-12'),
(22732951, 23982121, '2020-12-09', '2020-12-10'),
(22732951, 23987721, '2012-11-05', NULL),
(22732951, 66234500, '2010-11-22', '2010-11-23'),
(22732951, 66234593, '2010-10-27', '2010-10-28'),
(22732951, 66234594, '2012-05-07', '2012-05-10'),
(22732951, 66234596, '2017-08-03', NULL),
(22732951, 88271481, '2017-11-29', '2017-11-30'),
(22732951, 88272954, '2020-07-20', '2020-07-21'),
(22732951, 88276354, '2014-09-22', '2014-09-23'),
(22732951, 89734217, '2013-11-16', '2013-11-20'),
(22732951, 90316354, '2018-01-03', NULL),
(22732951, 99732114, '2019-10-10', '2019-10-12'),
(22732951, 190876632, '2011-07-08', '2011-07-10'),
(22732951, 196666632, '2010-08-06', '2010-08-07'),
(23982121, 23987721, '2015-03-15', '2015-03-20'),
(23982121, 38982921, '2019-04-05', '2019-04-10'),
(23982121, 41284471, '2018-10-16', '2018-10-20'),
(23982121, 42180081, '2015-03-24', '2015-03-25'),
(23982121, 99723671, '2020-09-15','2020-09-20'),
(23987721, 38982921, '2013-10-21', NULL),
(23987721, 41284471, '2014-01-16', NULL),
(23987721, 42180081, '2018-10-20', NULL),
(23987721, 99723671, '2019-12-19', '2019-12-25'),
(38982921, 41284471, '2014-06-22', '2014-06-23'),
(38982921, 42180081, '2011-08-11', NULL),
(38982921, 99723671, '2023-07-28', '2023-07-30'),
(41284471, 42180081, '2023-06-10', '2023-08-10'),
(41284471, 66234500, '2020-05-05', '2020-05-06'),
(41284471, 66234596, '2010-04-07', NULL),
(41284471, 99723671, '2018-10-25', '2018-10-26'),
(42180081, 99723671, '2016-01-06', '2016-01-07'),
(66234500, 66234593, '2015-01-10', '2015-01-20'),
(66234500, 66234594, '2018-01-02', '2018-01-03'),
(66234500, 66234596, '2018-04-08', NULL),
(66234500, 88271481, '2018-10-30', NULL),
(66234500, 88272954, '2014-06-30', '2014-07-30'),
(66234500, 88276354, '2015-11-30', '2015-12-30'),
(66234500, 89734217, '2016-03-02', '2016-03-10'),
(66234500, 90316354, '2019-03-15', '2019-03-20'),
(66234500, 99723671, '2019-10-18', '2019-10-20'),
(66234500, 99732114, '2014-09-09', NULL),
(66234500, 190876632, '2010-11-30', NULL),
(66234500, 196666632, '2018-01-08', NULL),
(66234593, 66234594, '2017-12-04', NULL),
(66234593, 66234596, '2012-06-04', NULL),
(66234594, 66234596, '2020-11-02', NULL),
(66234596, 88271481, '2018-05-22', NULL),
(66234596, 88272954, '2018-04-05', NULL),
(66234596, 88276354, '2014-10-13', NULL),
(66234596, 89734217, '2015-07-17', NULL),
(66234596, 90316354, '2017-06-24', NULL),
(66234596, 99723671, '2014-08-16', NULL),
(66234596, 99732114, '2019-07-27', NULL),
(66234596, 190876632, '2018-09-22', NULL),
(66234596, 196666632, '2012-12-25', NULL),
(88271481, 90316354, '2011-09-03', NULL),
(88272954, 88276354, '2014-01-14', NULL),
(190876632, 196666632, '2013-01-01', NULL);

-- --------------------------------------------------------

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Attends`
--
ALTER TABLE `ATTENDS`
  ADD PRIMARY KEY (`user_id`,`title`,`event_date`, `event_location`),
  ADD KEY `eventFK` (`title`,`event_date`, `event_location`);

--
-- Indexes for table `Event`
--
ALTER TABLE `EVENT`
  ADD PRIMARY KEY (`title`,`event_date`, `event_location`);

--
-- Indexes for table `FRIENDS`
--
ALTER TABLE `FRIENDS`
  ADD PRIMARY KEY (`requestor`,`requestee`),
  ADD KEY `requesteeFK` (`requestee`);

--
-- Indexes for table `USER`
--
ALTER TABLE `USER`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sigOtherFK` (`significant_other`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ATTENDS`
--
ALTER TABLE `ATTENDS`
  ADD CONSTRAINT `eventFK` FOREIGN KEY (`title`,`event_date`, `event_location`) REFERENCES `EVENT` (`title`, `event_date`, `event_location`),
  ADD CONSTRAINT `userFK` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`);

--
-- Constraints for table `Friends`
--
ALTER TABLE `FRIENDS`
  ADD CONSTRAINT `requesteeFK` FOREIGN KEY (`requestee`) REFERENCES `USER` (`id`),
  ADD CONSTRAINT `requestorFK` FOREIGN KEY (`requestor`) REFERENCES `USER` (`id`);

--
-- Constraints for table `User`
--
ALTER TABLE `USER`
  ADD CONSTRAINT `sigOtherFK` FOREIGN KEY (`significant_other`) REFERENCES `USER` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
