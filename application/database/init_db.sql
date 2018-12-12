CREATE TABLE `griffon_vulture_db`.`user_login` (
  `person_id` INT NOT NULL,
  `rating_id` INT NOT NULL,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`person_id`));

CREATE TABLE `griffon_vulture_db`.`user_contact` (
  `user_contact_id` INT NOT NULL,
  `person_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  `first_name` VARCHAR(50) NULL,
  `last_name` VARCHAR(50) NULL,
  `mobile_phone` VARCHAR(45) NULL,
  `email_address` VARCHAR(45) NULL,
  PRIMARY KEY (`user_contact_id`));

CREATE TABLE `griffon_vulture_db`.`user_venue_admin` (
  `venue_admin_id` INT NOT NULL,
  `person_id` INT NOT NULL,
  `venue_id` INT NOT NULL,
  `authorisation_token` VARCHAR(50),
  PRIMARY KEY (`venue_admin_id`));

CREATE TABLE `griffon_vulture_db`.`venue` (
  `venue_id` INT NOT NULL,
  `venue_contact_id` INT NOT NULL,
  `venue_name` VARCHAR(50) NULL,
  `venue_type` VARCHAR(50) NULL,
  `description` VARCHAR(45) NULL,
  `licences` VARCHAR(50) NULL,
  `other_info` VARCHAR(100) NULL,
  PRIMARY KEY (`venue_id`));

CREATE TABLE `griffon_vulture_db`.`venue_contact` (
  `venue_contact_id` INT NOT NULL,
  `venue_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  `phone_1` VARCHAR(45) NULL,
  `phone_2` VARCHAR(45) NULL,
  `email_address` VARCHAR(45) NULL,
  `website` VARCHAR(99) NULL,
  PRIMARY KEY (`venue_contact_id`));

CREATE TABLE `griffon_vulture_db`.`address` (
  `address_id` INT NOT NULL,
  `line_1` VARCHAR(50) NULL,
  `line_2` VARCHAR(50) NULL,
  `line_3` VARCHAR(50) NULL,
  `line_4` VARCHAR(45) NULL,
  `postcode` VARCHAR(45) NULL,
  PRIMARY KEY (`address_id`));

CREATE TABLE `griffon_vulture_db`.`rating` (
  `rating_id` INT NOT NULL,
  `rating_total` VARCHAR(50) NULL,
  PRIMARY KEY (`rating_id`));

CREATE TABLE `griffon_vulture_db`.`review` (
  `review_id` INT NOT NULL,
  `rating_id` INT NOT NULL,
  `reviewer_id` INT NOT NULL,
  `score` INT NULL,
  `comment` VARCHAR(50) NULL,
  PRIMARY KEY (`review_id`));