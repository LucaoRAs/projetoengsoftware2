
CREATE DATABASE banco_agenda_exames

USE banco_agenda_exames

CREATE TABLE IF NOT EXISTS `exames` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome_paciente` varchar(255) DEFAULT NULL,
  `nome` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=LATIN1_SWEDISH_CI;

SELECT * FROM exames

