USE AnimalShelter;

drop trigger CustomerAgeInsert;
drop trigger EmployeeAgeInsert;
drop trigger AnimalAgeInsert;
drop trigger CustomerAgeUpdate;
drop trigger EmployeeAgeUpdate;
drop trigger AnimalAgeUpdate;

-- PES1UG20CS697
DELIMITER $$
CREATE TRIGGER CustomerAgeInsert
BEFORE INSERT ON Customer
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.Age<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Age cannot be negative';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER CustomerAgeUpdate
BEFORE UPDATE ON Customer
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.Age<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Age cannot be negative';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER EmployeeAgeInsert
BEFORE INSERT ON Employee
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.Age<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Age cannot be negative';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER EmployeeAgeUpdate
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.Age<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Age cannot be negative';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER AnimalAgeInsert
BEFORE INSERT ON Animal
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.Age<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Age cannot be negative';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER AnimalAgeUpdate
BEFORE UPDATE ON Animal
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.Age<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Age cannot be negative';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER DonationsInsert
BEFORE UPDATE ON Donations
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
If new.DAmount<0 then
SIGNAL SQLSTATE '45000'
SET message_text = 'Donations cannot be negative';
END IF;
END$$
-- PES1UG20CS697
DELIMITER $$
CREATE TRIGGER EmployeeCares
BEFORE INSERT ON Cares
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
DECLARE c int;

If (select count(*) from cares where EmployeeID = new.EmployeeID)>5 then
SIGNAL SQLSTATE '45000'
SET message_text = 'One Employee cannot care for more than 5 animals';
END IF;
END$$
drop trigger AnimalAdopted;
DELIMITER $$
CREATE TRIGGER AnimalAdopted
BEFORE INSERT ON Animal
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);
DECLARE c int;
SET c:=0;
If (SELECT count(AdoptedSSN) from animal
where AdoptedSSN = new.AdoptedSSN)>3 then
SIGNAL SQLSTATE '45000'
SET message_text = 'One Person cannot adopt more than 3 animals';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER CustomerSex
BEFORE UPDATE ON Customer
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);

If new.sex != "Male" or new.sex != "Female" or new.sex != "Others" then
SIGNAL SQLSTATE '45000'
SET message_text = 'Enter valid gender	';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER AnimalSex
BEFORE UPDATE ON Animal
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);

If new.sex != "Male" or new.sex != "Female" or new.sex != "Others" then
SIGNAL SQLSTATE '45000'
SET message_text = 'Enter valid gender	';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER EmployeeSex
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);

If new.sex != "Male" or new.sex != "Female" or new.sex != "Others" then
SIGNAL SQLSTATE '45000'
SET message_text = 'Enter valid gender	';
END IF;
END$$

DELIMITER $$
CREATE TRIGGER DeadAnimal
BEFORE UPDATE ON Animal
FOR EACH ROW
BEGIN
DECLARE message_text varchar(255);

If new.DeadOrAlive = "Dead" and new.AdoptedSSN!=NULL then
SIGNAL SQLSTATE '45000'
SET message_text = 'Cannot adopt dead animal';
END IF;
END$$

INSERT into customer(SSN, CName, Email, Age, Address, Sex) VALUES (123, "test", "test", -1, "test","test");

DELETE FROM Customer where Customer.SSN = 123;


                     