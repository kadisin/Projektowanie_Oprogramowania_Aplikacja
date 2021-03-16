-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 29 Sty 2021, 17:15
-- Wersja serwera: 10.4.17-MariaDB
-- Wersja PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `zpi_baza_danych`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `message`
--

CREATE TABLE `message` (
  `Id` int(10) NOT NULL,
  `tresc` varchar(255) NOT NULL,
  `date` datetime DEFAULT NULL,
  `IdZespol` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownik`
--

CREATE TABLE `pracownik` (
  `Id` int(10) NOT NULL,
  `imie` varchar(50) NOT NULL,
  `opiekun` tinyint(1) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pracownik`
--

INSERT INTO `pracownik` (`Id`, `imie`, `opiekun`, `nazwisko`, `login`, `password`) VALUES
(1, 'Adam', 0, 'Pracownik', 'adam', 'pracownik');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `student`
--

CREATE TABLE `student` (
  `Id` int(10) NOT NULL,
  `imie` varchar(50) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `maTemat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `student`
--

INSERT INTO `student` (`Id`, `imie`, `nazwisko`, `login`, `password`, `maTemat`) VALUES
(1, 'Tomasz', 'Logisz', 'tomek2212', 'tomek2212', 0),
(2, 'Marcin', 'Nowak', 'marcin', 'nowak', 0),
(3, 'Dominik', 'Nowakowski', 'dominik', 'nowakowski', 0),
(5, 'Maciek', 'Jaros', 'maciek', 'jaros', 0),
(6, 'Maciej', 'Kowalski', 'maciej', 'kowalski', 0),
(7, 'Andrzej', 'Bez', 'andrzej', 'bez', 0),
(8, 'Dominika', 'Andrzejewska', 'dominika', 'andrzejewska', 0),
(9, 'example_imie', 'example_nazwisko', 'example_login', 'example_password', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `temat`
--

CREATE TABLE `temat` (
  `Id` int(10) NOT NULL,
  `tytul` varchar(100) NOT NULL,
  `opis` varchar(255) NOT NULL,
  `czyZajety` int(1) NOT NULL,
  `IdPracownik` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `temat`
--

INSERT INTO `temat` (`Id`, `tytul`, `opis`, `czyZajety`, `IdPracownik`) VALUES
(1, 'Aplikacja Webowa - sklep internetowy', 'Aplikacja Webowa - opis', 0, 1),
(2, 'Strona Bankowa - Prototyp', 'Aplikacja bankowa - opis', 1, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zespol`
--

CREATE TABLE `zespol` (
  `Id` int(10) NOT NULL,
  `IdTemat` int(10) DEFAULT NULL,
  `IdStudent` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `zespol`
--

INSERT INTO `zespol` (`Id`, `IdTemat`, `IdStudent`) VALUES
(24, NULL, 1),
(25, NULL, 2),
(100, NULL, 9);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zespolstudent`
--

CREATE TABLE `zespolstudent` (
  `Id` int(10) NOT NULL,
  `IdZespol` int(10) NOT NULL,
  `IdSt` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `zespolstudent`
--

INSERT INTO `zespolstudent` (`Id`, `IdZespol`, `IdSt`) VALUES
(43, 24, 1),
(44, 24, 7),
(46, 24, 8),
(47, 25, 2),
(48, 25, 5),
(49, 100, 9),
(50, 24, 6);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_IdZespol` (`IdZespol`);

--
-- Indeksy dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- Indeksy dla tabeli `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- Indeksy dla tabeli `temat`
--
ALTER TABLE `temat`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `tytul` (`tytul`),
  ADD KEY `FK_IdPracownik` (`IdPracownik`);

--
-- Indeksy dla tabeli `zespol`
--
ALTER TABLE `zespol`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_IdTemat` (`IdTemat`),
  ADD KEY `FK_IdSt` (`IdStudent`);

--
-- Indeksy dla tabeli `zespolstudent`
--
ALTER TABLE `zespolstudent`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `FK_IdStudent` (`IdSt`),
  ADD KEY `FK_IdZp` (`IdZespol`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `message`
--
ALTER TABLE `message`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `student`
--
ALTER TABLE `student`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT dla tabeli `temat`
--
ALTER TABLE `temat`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT dla tabeli `zespol`
--
ALTER TABLE `zespol`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT dla tabeli `zespolstudent`
--
ALTER TABLE `zespolstudent`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `message`
--
ALTER TABLE `message`
  ADD CONSTRAINT `FK_IdZespol` FOREIGN KEY (`IdZespol`) REFERENCES `zespol` (`Id`);

--
-- Ograniczenia dla tabeli `temat`
--
ALTER TABLE `temat`
  ADD CONSTRAINT `FK_IdPracownik` FOREIGN KEY (`IdPracownik`) REFERENCES `pracownik` (`Id`);

--
-- Ograniczenia dla tabeli `zespol`
--
ALTER TABLE `zespol`
  ADD CONSTRAINT `FK_IdSt` FOREIGN KEY (`IdStudent`) REFERENCES `student` (`Id`),
  ADD CONSTRAINT `FK_IdTemat` FOREIGN KEY (`IdTemat`) REFERENCES `temat` (`Id`);

--
-- Ograniczenia dla tabeli `zespolstudent`
--
ALTER TABLE `zespolstudent`
  ADD CONSTRAINT `FK_IdStudent` FOREIGN KEY (`IdSt`) REFERENCES `student` (`Id`),
  ADD CONSTRAINT `FK_IdZp` FOREIGN KEY (`IdZespol`) REFERENCES `zespol` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
