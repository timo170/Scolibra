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

-- Dumping structure for table biblioteca.abonati
CREATE TABLE IF NOT EXISTS `abonati` (
  `Cod_abonat` int(11) NOT NULL AUTO_INCREMENT,
  `Nume` varchar(10) DEFAULT NULL,
  `Prenume` varchar(20) DEFAULT NULL,
  `Clasa` varchar(50) DEFAULT NULL,
  `Data_abonarii` date DEFAULT NULL,
  `Telefon` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`Cod_abonat`),
  UNIQUE KEY `Cod_abonat` (`Cod_abonat`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.abonati: ~7 rows (approximately)
DELETE FROM `abonati`;
/*!40000 ALTER TABLE `abonati` DISABLE KEYS */;
INSERT INTO `abonati` (`Cod_abonat`, `Nume`, `Prenume`, `Clasa`, `Data_abonarii`, `Telefon`) VALUES
	(100, 'Moria', 'Vlad', '9C', '2023-04-10', '+40731321321'),
	(101, 'Conta', 'Maria', '9B', '2023-04-01', '+40732432123'),
	(102, 'Anur', 'Cora', '10B', '2023-04-05', '+40721123123'),
	(103, 'Faur', 'Vlad', '8D', '2023-05-24', '+40734345456'),
	(104, 'Comtim', 'Ale', '11A', '2023-05-24', '+40789456567'),
	(105, 'Riga', 'Onisifor', '7C', '2023-05-24', '+40738456876'),
	(106, 'Vranc', 'Moni', '9B', '2023-06-03', '+40723124567');
/*!40000 ALTER TABLE `abonati` ENABLE KEYS */;

-- Dumping structure for table biblioteca.carti
CREATE TABLE IF NOT EXISTS `carti` (
  `Cod` int(11) NOT NULL,
  `Autor` varchar(50) DEFAULT NULL,
  `Titlu` varchar(100) DEFAULT NULL,
  `Editura` varchar(50) DEFAULT NULL,
  `Anul_aparitiei` smallint(6) DEFAULT NULL,
  `Pret` decimal(20,3) unsigned DEFAULT NULL,
  `Stare` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Cod`),
  UNIQUE KEY `Cod` (`Cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.carti: ~92 rows (approximately)
DELETE FROM `carti`;
/*!40000 ALTER TABLE `carti` DISABLE KEYS */;
INSERT INTO `carti` (`Cod`, `Autor`, `Titlu`, `Editura`, `Anul_aparitiei`, `Pret`, `Stare`) VALUES
	(35608, 'Jules Verne', 'Steaua Sudului', 'Ion Creangă', 1984, 13.000, 'liberă'),
	(39577, 'Cristian Teodorescu', 'Tainele inimei', 'Cartea Românească', 2005, 22.500, 'liberă'),
	(39666, 'Marin Preda', 'Cel mai iubit dintre pământeni vol.1', 'Cartex', 2006, 32.348, 'împrumutată'),
	(39667, 'Marin Preda', 'Cel mai iubit dintre pământeni vol.2', 'Cartex', 2006, 32.348, 'împrumutată'),
	(39668, 'Marin Preda', 'Cel mai iubit dintre pământeni vol.3', 'Cartex', 2006, 32.348, 'împrumutată'),
	(39694, 'Vasile Voiculescu', 'Nuvele și povestiri', 'Cartex', 2006, 9.027, 'liberă'),
	(39724, 'Mihai Eminescu', 'Poezii', 'Cartex', 2006, 6.018, 'liberă'),
	(39743, 'Mircea Eliade', 'Maitrey', 'Cartex', 2006, 10.908, 'liberă'),
	(39764, 'Mircea Eliade', 'La Țigănci', 'Cartex', 2006, 10.908, 'liberă'),
	(39773, 'Marin Preda', 'Moromeții vol.1', 'Cartex', 2006, 23.321, 'liberă'),
	(39774, 'Marin Preda', 'Moromeții vol.2', 'Cartex', 2006, 23.321, 'liberă'),
	(39839, 'Marin Buca', 'Dicționar de antonime', 'Vox', 2005, 4.810, 'liberă'),
	(39841, 'Marin Buca', 'Dicționar de expresii românești', 'Vox', 2005, 5.500, 'liberă'),
	(39855, 'Ioan Slavici', 'Mara', 'Vox', 2006, 3.096, 'liberă'),
	(39899, 'Mihai Eminescu', 'Pagini alese', 'Vox', 2006, 3.096, 'liberă'),
	(39918, 'Alexandru Mitru', 'Din marile legende ale lumii vol.1', 'Vox', 2012, 12.042, 'liberă'),
	(40328, 'Adrian Neculau', 'Educația Adulților', 'Polirom', 2004, 17.900, 'împrumutată'),
	(40329, 'Robert J. Sternberg', 'Manual de creativitate', 'Polirom', 2005, 20.710, 'împrumutată'),
	(40330, 'Robert J. Sternberg', 'Manual de creativitate', 'Polirom', 2005, 20.710, 'împrumutată'),
	(40331, 'Andre de Peretti', 'Tehnici de comunicare', 'Polirom', 2007, 32.900, 'liberă'),
	(40332, 'Andre de Peretti', 'Tehnici de comunicare', 'Polirom', 2007, 32.900, 'liberă'),
	(40335, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40336, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40337, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40338, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40339, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40340, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40341, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40342, 'Ioan Slavici', 'Nuvele', 'Corint', 2006, 11.990, 'liberă'),
	(40345, 'Costache Negruzzi', 'Alexandru Lăpușneanu', 'Corint', 2007, 11.990, 'liberă'),
	(40346, 'Costache Negruzzi', 'Alexandru Lăpușneanu', 'Corint', 2007, 11.990, 'liberă'),
	(40347, 'Costache Negruzzi', 'Alexandru Lăpușneanu', 'Corint', 2007, 11.990, 'liberă'),
	(40348, 'Costache Negruzzi', 'Alexandru Lăpușneanu', 'Corint', 2007, 11.990, 'liberă'),
	(40355, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40356, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40357, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40358, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40359, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40360, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40361, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40362, 'Bogdan Petriceicu Hașdeu', 'Răzvan și Vidra', 'Corint', 2007, 24.500, 'liberă'),
	(40444, 'Marin Sorescu', 'Teatru', 'Minerva', 2006, 13.900, 'liberă'),
	(40474, 'Ion Creanga', 'Povești și povestiri', 'Corint', 2006, 11.000, 'liberă'),
	(40503, 'George Coșbuc', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40504, 'George Coșbuc', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40505, 'George Coșbuc', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40506, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40507, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40508, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40509, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40510, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40511, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40512, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40513, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40514, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40515, 'Vasile Alecsandri', 'Poezii', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40516, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40517, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40518, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40519, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40520, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40521, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40522, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40523, 'George Topîrceanu', 'Balade vesele și triste', 'Maxim Bit', 2006, 6.980, 'liberă'),
	(40524, 'Mark Twain', 'Aventurile lui Tom Sawyer', 'Maxim Bit', 2004, 16.000, 'liberă'),
	(40525, 'Mark Twain', 'Aventurile lui Tom Sawyer', 'Maxim Bit', 2004, 16.000, 'liberă'),
	(40526, 'Lyman Frank Baum', 'Vrăjitorul din Oz', 'Național', 2004, 14.900, 'liberă'),
	(40527, 'Lyman Frank Baum', 'Vrăjitorul din Oz', 'Național', 2004, 14.900, 'liberă'),
	(40529, 'Daniel Defoe', 'Robinson Crusoe', 'Național', 2004, 17.900, 'liberă'),
	(40530, 'Daniel Defoe', 'Robinson Crusoe', 'Național', 2004, 17.900, 'liberă'),
	(40531, 'George Bacovia', 'Plumb', 'Humanitas', 2007, 19.000, 'liberă'),
	(40532, 'George Bacovia', 'Plumb', 'Humanitas', 2007, 19.000, 'liberă'),
	(40533, 'George Bacovia', 'Plumb', 'Humanitas', 2007, 19.000, 'liberă'),
	(40534, 'Nichita Stănescu', 'Opera Poetică', 'Cartier', 2007, 21.000, 'liberă'),
	(40535, 'Mircea Cărtărescu', 'De ce iubim femeile', 'Humanitas', 2006, 15.000, 'liberă'),
	(40626, 'Alexandru Dumas', 'Invitație la vals', 'Art ', 2006, 11.920, 'liberă'),
	(40638, 'Vasile Alecsandri', 'Teatru', 'Art ', 2006, 9.520, 'liberă'),
	(40923, 'Ioan Slavici', 'Moara cu noroc.Pădureanca', 'Art ', 2006, 8.920, 'liberă'),
	(40924, 'Ion Luca Caragiale', 'Nuvele si povestiri', 'Art ', 2006, 8.920, 'liberă'),
	(40925, 'Mihail Drumes', 'Cazul Magheru', 'Art ', 2006, 11.490, 'liberă'),
	(40926, 'Mihail Drumes', 'Cazul Magheru', 'Art ', 2006, 11.490, 'liberă'),
	(40927, 'Mihail Drumes', 'Cazul Magheru', 'Art ', 2006, 11.490, 'liberă'),
	(40928, 'Mihail Drumes', 'Cazul Magheru', 'Art ', 2006, 11.490, 'liberă'),
	(40929, 'Mihail Drumes', 'Cazul Magheru', 'Art ', 2006, 11.490, 'liberă'),
	(40930, 'Adrian Costache', 'Atlasul literaturii române', 'Cartographia', 2005, 15.300, 'liberă'),
	(40931, 'Adrian Costache', 'Atlasul literaturii române', 'Cartographia', 2005, 15.300, 'liberă'),
	(40932, 'Gabriele D\'Annunzio', 'Poate că da, poate că nu', 'Art ', 2008, 16.050, 'liberă'),
	(40933, 'Gabriele D\'Annunzio', 'Poate că da, poate că nu', 'Art ', 2008, 16.050, 'liberă'),
	(40934, 'Gabriele D\'Annunzio', 'Poate că da, poate că nu', 'Art ', 2008, 16.050, 'liberă'),
	(40935, 'Gabriele D\'Annunzio', 'Poate că da, poate că nu', 'Art ', 2008, 16.050, 'liberă'),
	(41090, 'Neagu Djuvara', 'Amintiri si povesti mai deocheate', 'Humanitas', 2009, 22.000, 'liberă'),
	(41342, 'Salvador Dali', 'Jurnalul unui geniu', 'Humanitas', 2012, 32.000, 'liberă');
/*!40000 ALTER TABLE `carti` ENABLE KEYS */;

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
  `CLASA` varchar(3) DEFAULT NULL,
  `COD_CARTE` mediumint(9) DEFAULT NULL,
  `DATA_IMPRUMUT` date DEFAULT NULL,
  `DATA_RETURNARII` date DEFAULT NULL,
  `TELEFON` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`COD_IMPRUMUT`),
  UNIQUE KEY `COD_IMPRUMUT` (`COD_IMPRUMUT`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table biblioteca.imprumuturi: ~5 rows (approximately)
DELETE FROM `imprumuturi`;
/*!40000 ALTER TABLE `imprumuturi` DISABLE KEYS */;
INSERT INTO `imprumuturi` (`COD_IMPRUMUT`, `COD_ABONAT`, `NUME`, `CLASA`, `COD_CARTE`, `DATA_IMPRUMUT`, `DATA_RETURNARII`, `TELEFON`) VALUES
	(1, 104, 'Comtim', '11A', 39666, '2023-06-01', '2023-06-02', '+40738231065'),
	(2, 101, 'Conta', '9B', 39667, '2023-06-01', '2023-06-03', '+40756528688'),
	(3, 105, 'Riga', '7C', 40330, '2023-05-20', '2023-05-31', '+40738456876'),
	(4, 102, 'Anur', '10B', 40328, '2023-06-03', '2023-06-17', '+40721123123'),
	(5, 101, 'Conta', '9B', 40329, '2023-06-03', '2023-06-17', '+40732432123');
/*!40000 ALTER TABLE `imprumuturi` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
