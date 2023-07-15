-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.9.4-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for biblioteca
CREATE DATABASE IF NOT EXISTS `biblioteca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `biblioteca`;

-- Dumping structure for table biblioteca.abonati
CREATE TABLE IF NOT EXISTS `abonati` (
  `Cod_abonat` int(11) NOT NULL AUTO_INCREMENT,
  `Nume` varchar(10) DEFAULT NULL,
  `Prenume` varchar(20) DEFAULT NULL,
  `Clasa` varchar(50) DEFAULT NULL,
  `Data_abonarii` date DEFAULT NULL,
  `Telefon` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Cod_abonat`),
  UNIQUE KEY `Cod_abonat` (`Cod_abonat`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.abonati: ~8 rows (approximately)
DELETE FROM `abonati`;
/*!40000 ALTER TABLE `abonati` DISABLE KEYS */;
INSERT INTO `abonati` (`Cod_abonat`, `Nume`, `Prenume`, `Clasa`, `Data_abonarii`, `Telefon`) VALUES
	(100, 'Moria', 'Vlad', '9C', '2023-04-10', '+40731 321 321'),
	(101, 'Conta', 'Maria', '9B', '2023-04-01', '+40738 231 065'),
	(102, 'Anur', 'Cora', '10B', '2023-04-05', '+40756 528 688'),
	(103, 'Faur', 'Vlad', '8D', '2023-05-24', '+40734 345 456'),
	(104, 'Comtim', 'Ale', '11A', '2023-05-24', '+40789 456 567'),
	(105, 'Riga', 'Onisifor', '7C', '2023-05-24', '+40738 456 876'),
	(106, 'Vranc', 'Moni', '9B', '2023-06-03', '+40723 124 567'),
	(107, 'Popescu', 'Quineea', 'profesor geografie', '2023-06-04', '+40739 231 064');
/*!40000 ALTER TABLE `abonati` ENABLE KEYS */;

-- Dumping structure for table biblioteca.carticod
CREATE TABLE IF NOT EXISTS `carticod` (
  `Cod` int(11) NOT NULL,
  `Stare` varchar(20) DEFAULT NULL,
  `Id` mediumint(9) DEFAULT NULL,
  KEY `Id` (`Id`),
  CONSTRAINT `carticod_ibfk_1` FOREIGN KEY (`Id`) REFERENCES `cartile` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.carticod: ~130 rows (approximately)
DELETE FROM `carticod`;
/*!40000 ALTER TABLE `carticod` DISABLE KEYS */;
INSERT INTO `carticod` (`Cod`, `Stare`, `Id`) VALUES
	(35608, 'împrumutată', 37),
	(39577, 'liberă', 38),
	(39666, 'liberă', 7),
	(39667, 'liberă', 8),
	(39668, 'liberă', 9),
	(39694, 'liberă', 26),
	(39724, 'liberă', 32),
	(39743, 'liberă', 18),
	(39764, 'liberă', 17),
	(39773, 'liberă', 22),
	(39774, 'liberă', 23),
	(39839, 'liberă', 11),
	(39841, 'liberă', 12),
	(39855, 'liberă', 20),
	(39899, 'liberă', 28),
	(39918, 'liberă', 13),
	(40328, 'liberă', 14),
	(40329, 'împrumutată', 19),
	(40330, 'liberă', 19),
	(40331, 'liberă', 41),
	(40332, 'liberă', 41),
	(40335, 'liberă', 24),
	(40336, 'liberă', 24),
	(40337, 'liberă', 24),
	(40338, 'liberă', 24),
	(40339, 'liberă', 24),
	(40340, 'liberă', 24),
	(40341, 'liberă', 24),
	(40342, 'liberă', 24),
	(40346, 'liberă', 1),
	(40347, 'liberă', 1),
	(40348, 'liberă', 1),
	(40355, 'liberă', 35),
	(40356, 'liberă', 35),
	(40357, 'liberă', 35),
	(40358, 'liberă', 35),
	(40359, 'liberă', 35),
	(40360, 'liberă', 35),
	(40361, 'liberă', 35),
	(40362, 'liberă', 35),
	(40444, 'liberă', 39),
	(40474, 'liberă', 34),
	(40503, 'liberă', 31),
	(40504, 'liberă', 31),
	(40505, 'liberă', 31),
	(40507, 'liberă', 33),
	(40508, 'liberă', 33),
	(40509, 'liberă', 33),
	(40510, 'liberă', 33),
	(40511, 'liberă', 33),
	(40512, 'liberă', 33),
	(40513, 'liberă', 33),
	(40514, 'liberă', 33),
	(40515, 'liberă', 33),
	(40517, 'liberă', 5),
	(40518, 'liberă', 5),
	(40519, 'liberă', 5),
	(40520, 'liberă', 5),
	(40521, 'liberă', 5),
	(40522, 'liberă', 5),
	(40523, 'liberă', 5),
	(40524, 'liberă', 4),
	(40525, 'liberă', 4),
	(40529, 'liberă', 36),
	(40530, 'liberă', 36),
	(40531, 'liberă', 29),
	(40532, 'liberă', 29),
	(40533, 'liberă', 29),
	(40534, 'liberă', 27),
	(40535, 'liberă', 10),
	(40626, 'liberă', 15),
	(40638, 'liberă', 40),
	(40923, 'împrumutată', 21),
	(40924, 'liberă', 25),
	(40925, 'împrumutată', 6),
	(40926, 'liberă', 6),
	(40927, 'liberă', 6),
	(40928, 'liberă', 6),
	(40929, 'liberă', 6),
	(40930, 'liberă', 3),
	(40931, 'liberă', 3),
	(40932, 'liberă', 30),
	(40933, 'liberă', 30),
	(40934, 'liberă', 30),
	(40935, 'liberă', 30),
	(41090, 'liberă', 2),
	(41342, 'liberă', 16),
	(40516, 'liberă', 5),
	(17214, 'liberă', 43),
	(17396, 'liberă', 44),
	(17397, 'liberă', 44),
	(17399, 'liberă', 44),
	(17400, 'liberă', 44),
	(17728, 'liberă', 45),
	(17729, 'liberă', 45),
	(17730, 'liberă', 45),
	(17731, 'liberă', 45),
	(40345, 'liberă', 1),
	(17732, 'liberă', 46),
	(17733, 'liberă', 46),
	(17735, 'liberă', 46),
	(17737, 'liberă', 46),
	(17738, 'liberă', 46),
	(17739, 'liberă', 46),
	(17740, 'liberă', 46),
	(17741, 'liberă', 46),
	(18447, 'liberă', 47),
	(18442, 'liberă', 48),
	(18451, 'liberă', 49),
	(18454, 'liberă', 50),
	(18313, 'liberă', 51),
	(18212, 'liberă', 52),
	(18213, 'liberă', 52),
	(18214, 'liberă', 52),
	(18215, 'liberă', 52),
	(18219, 'liberă', 52),
	(18220, 'liberă', 52),
	(18221, 'liberă', 52),
	(18222, 'liberă', 52),
	(40526, 'liberă', 42),
	(40527, 'liberă', 42),
	(37159, 'liberă', 63),
	(28915, 'liberă', 64),
	(23299, 'liberă', 66),
	(40255, 'liberă', 67),
	(40256, 'liberă', 68),
	(40257, 'liberă', 69),
	(37279, 'liberă', 70),
	(37261, 'liberă', 72),
	(41100, 'liberă', 73);
/*!40000 ALTER TABLE `carticod` ENABLE KEYS */;

-- Dumping structure for table biblioteca.cartile
CREATE TABLE IF NOT EXISTS `cartile` (
  `Id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `Autor` varchar(50) DEFAULT NULL,
  `Titlu` varchar(100) DEFAULT NULL,
  `Editura` varchar(50) DEFAULT NULL,
  `Anul_aparitiei` smallint(6) DEFAULT NULL,
  `Pret` decimal(20,3) unsigned DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.cartile: ~61 rows (approximately)
DELETE FROM `cartile`;
/*!40000 ALTER TABLE `cartile` DISABLE KEYS */;
INSERT INTO `cartile` (`Id`, `Autor`, `Titlu`, `Editura`, `Anul_aparitiei`, `Pret`) VALUES
	(1, 'Costache Negruzzi', 'Alexandru Lăpușneanu', 'Corint', 2007, 11.990),
	(2, 'Neagu Djuvara', 'Amintiri si povesti mai deocheate', 'Humanitas', 2009, 22.000),
	(3, 'Adrian Costache', 'Atlasul literaturii române', 'Cartographia', 2005, 15.300),
	(4, 'Mark Twain', 'Aventurile lui Tom Sawyer', 'Maxim Bit', 2004, 16.000),
	(5, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980),
	(6, 'Mihail Drumes', 'Cazul Magheru', 'Art ', 2006, 11.490),
	(7, 'Marin Preda', 'Cel mai iubit dintre pământeni vol.1', 'Cartex', 2006, 32.348),
	(8, 'Marin Preda', 'Cel mai iubit dintre pământeni vol.2', 'Cartex', 2006, 32.348),
	(9, 'Marin Preda', 'Cel mai iubit dintre pământeni vol.3', 'Cartex', 2006, 32.348),
	(10, 'Mircea Cărtărescu', 'De ce iubim femeile', 'Humanitas', 2006, 15.000),
	(11, 'Marin Buca', 'Dicționar de antonime', 'Vox', 2005, 4.810),
	(12, 'Marin Buca', 'Dicționar de expresii românești', 'Vox', 2005, 5.500),
	(13, 'Alexandru Mitru', 'Din marile legende ale lumii vol.1', 'Vox', 2012, 12.042),
	(14, 'Adrian Neculau', 'Educația Adulților', 'Polirom', 2004, 17.900),
	(15, 'Alexandru Dumas', 'Invitație la vals', 'Art ', 2006, 11.920),
	(16, 'Salvador Dali', 'Jurnalul unui geniu', 'Humanitas', 2012, 32.000),
	(17, 'Mircea Eliade', 'La Țigănci', 'Cartex', 2006, 10.908),
	(18, 'Mircea Eliade', 'Maitrey', 'Cartex', 2006, 10.908),
	(19, 'Robert J. Sternberg', 'Manual de creativitate', 'Polirom', 2005, 20.710),
	(20, 'Ioan Slavici', 'Mara', 'Vox', 2006, 3.096),
	(21, 'Ioan Slavici', 'Moara cu noroc.Pădureanca', 'Art ', 2006, 8.920),
	(22, 'Marin Preda', 'Moromeții vol.1', 'Cartex', 2006, 23.321),
	(23, 'Marin Preda', 'Moromeții vol.2', 'Cartex', 2006, 23.321),
	(24, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990),
	(25, 'Ion Luca Caragiale', 'Nuvele si povestiri', 'Art ', 2006, 8.920),
	(26, 'Vasile Voiculescu', 'Nuvele și povestiri', 'Cartex', 2006, 9.027),
	(27, 'Nichita Stănescu', 'Opera Poetică', 'Cartier', 2007, 21.000),
	(28, 'Mihai Eminescu', 'Pagini alese', 'Vox', 2006, 3.096),
	(29, 'George Bacovia', 'Plumb', 'Humanitas', 2007, 19.000),
	(30, 'Gabriele D\'Annunzio', 'Poate că da, poate că nu', 'Art ', 2008, 16.050),
	(31, 'George Coșbuc', 'Poezii', 'Maxim Bit', 2006, 6.980),
	(32, 'Mihai Eminescu', 'Poezii', 'Cartex', 2006, 6.018),
	(33, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980),
	(34, 'Ion Creanga', 'Povești și povestiri', 'Corint', 2006, 11.000),
	(35, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500),
	(36, 'Daniel Defoe', 'Robinson Crusoe', 'Național', 2004, 17.900),
	(37, 'Jules Verne', 'Steaua Sudului', 'Ion Creangă', 1984, 13.000),
	(38, 'Cristian Teodorescu', 'Tainele inimei', 'Cartea Românească', 2005, 22.500),
	(39, 'Marin Sorescu', 'Teatru', 'Minerva', 2006, 13.900),
	(40, 'Vasile Alecsandri', 'Teatru', 'Art ', 2006, 9.520),
	(41, 'Andre de Peretti', 'Tehnici de comunicare', 'Polirom', 2007, 32.900),
	(42, 'Lyman Frank Baum', 'Vrăjitorul din Oz', 'Național', 2004, 9.520),
	(43, 'Ion Luca Caragiale', 'O scrisoare pierdută', 'Ion Creangă', 1995, 3.500),
	(44, 'Sorin Cristea', 'Fundamentele pedagogiei', '', 1994, 21.420),
	(45, 'George Topîrceanu', 'Balade vesele și triste', 'Libris', 2004, 10.000),
	(46, 'Hector Malot', 'Singur pe lume', 'Libris', 2004, 10.000),
	(47, 'Gabriel Liiceanu', 'Jurnalul de la Păltiniș', 'Humanitas', 2005, 26.000),
	(48, 'Florin Măceșanu', 'Fizică:probleme și teste pentru gimnaziu', 'Corint', 2006, 17.510),
	(49, 'Gabriel Liiceanu', 'Despre limită', 'Humanitas', 2005, 19.000),
	(50, 'Gabriel Liiceanu', 'Despre minciună', 'Humanitas', 2006, 19.000),
	(51, 'Adina Baran Pescaru', 'Parteneriat în educație', 'Minerva', 2005, 8.250),
	(52, 'Florica Tibea', 'Anatomia omului, atlas școlar ', 'Corint', 2017, 12.790),
	(63, 'Sebastian Bonifaciu', 'Sportul în literatură', 'Sport-turism', 1990, 13.500),
	(64, 'Gheorghe Popa', 'Piramide', 'Sport-turism', 1975, 5.250),
	(66, 'N. Gh. Băiașu', 'Gimnastica', 'Stadion', 1972, 23.500),
	(67, 'Dumitru Stăniloae', 'Teologia dogmatică ortodoxă vol.1', 'I.B.M.B.O.R.', 2003, 40.000),
	(68, 'Dumitru Stăniloae', 'Teologia dogmatică ortodoxă vol.2', 'I.B.M.B.O.R.', 2003, 40.000),
	(69, 'Dumitru Stăniloae', 'Teologia dogmatică ortodoxă vol.3', 'I.B.M.B.O.R.', 2003, 40.000),
	(70, 'Emanuel Copăcianu', 'Iisus din Nazaret', 'Doris', 1990, 4.250),
	(72, 'Emanuel Copăcianu', 'Maria Magdalena', 'Doris', 1990, 4.250),
	(73, 'John Bowker', 'Istoria și ideile marilor religii', 'Didactică și pedagogică', 2007, 39.000);
/*!40000 ALTER TABLE `cartile` ENABLE KEYS */;

-- Dumping structure for table biblioteca.citate
CREATE TABLE IF NOT EXISTS `citate` (
  `Numar` tinyint(4) DEFAULT NULL,
  `Citate` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.citate: ~10 rows (approximately)
DELETE FROM `citate`;
/*!40000 ALTER TABLE `citate` DISABLE KEYS */;
INSERT INTO `citate` (`Numar`, `Citate`) VALUES
	(1, '"Cărţile sunt fiice ale cerului pogorâte pe pământ\r\nca să aline suferinţele neamului omenesc." \r\nBernardin de Saint-Pierre'),
	(0, '"Cartea de căpătâi nu se alege, ci te îndrăgosteşti de ea." \r\nJose Luis de Vilallonga'),
	(2, '"Chiar şi cărţile rele sunt cărţi, prin urmare ele sunt sacre." \r\nGunter Grass'),
	(3, '"Cărţile sunt amantele singuraticilor." \r\nTeodor Burnar'),
	(4, '"Cărţile sunt un refugiu, un fel de refugiu monahal,\r\nfaţă de vulgarităţile lumii reale." \r\nWalter Pater'),
	(5, '"Cei înţelepţi sunt întotdeauna deasupra cărţilor." \r\nSamuel Daniel'),
	(6, '"Nu există cărţi morale sau cărţi imorale.\r\nCărţile sunt bine scrise sau prost scrise. Asta e totul." \r\nOscar Wilde'),
	(7, '"Cărţile te vindecă de oameni, iar oamenii de cărţi." \r\nVladimir Ghika'),
	(8, '"Nimic nu este mai bun decât să aprinzi pofta şi iubirea de carte;\r\naltfel nu creşti decât măgari încărcaţi cu cărţi." \r\nMichel de Montaigne'),
	(9, '"A şti carte nu înseamnă a şti înţelepciune." \r\nNicolae Iorga');
/*!40000 ALTER TABLE `citate` ENABLE KEYS */;

-- Dumping structure for table biblioteca.imprumuturi
CREATE TABLE IF NOT EXISTS `imprumuturi` (
  `COD_IMPRUMUT` int(11) NOT NULL AUTO_INCREMENT,
  `COD_ABONAT` tinyint(4) DEFAULT NULL,
  `NUME` varchar(10) DEFAULT NULL,
  `CLASA` varchar(20) DEFAULT NULL,
  `COD_CARTE` mediumint(9) DEFAULT NULL,
  `DATA_IMPRUMUT` date DEFAULT NULL,
  `DATA_RETURNARII` date DEFAULT NULL,
  `TELEFON` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`COD_IMPRUMUT`),
  UNIQUE KEY `COD_IMPRUMUT` (`COD_IMPRUMUT`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.imprumuturi: ~4 rows (approximately)
DELETE FROM `imprumuturi`;
/*!40000 ALTER TABLE `imprumuturi` DISABLE KEYS */;
INSERT INTO `imprumuturi` (`COD_IMPRUMUT`, `COD_ABONAT`, `NUME`, `CLASA`, `COD_CARTE`, `DATA_IMPRUMUT`, `DATA_RETURNARII`, `TELEFON`) VALUES
	(18, 106, 'Vranc', '9B', 40925, '2023-06-30', '2023-07-14', '+40723 124 567'),
	(21, 107, 'Popescu', 'profesor geografie', 40329, '2023-07-10', '2023-08-07', '+40739 231 064'),
	(22, 103, 'Faur', '8D', 35608, '2023-07-10', '2023-08-07', '+40734 345 456'),
	(23, 101, 'Conta', '9B', 40923, '2023-07-10', '2023-07-24', '+40738 231 065');
/*!40000 ALTER TABLE `imprumuturi` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
