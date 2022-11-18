CREATE DATABASE AnimalShelter;

USE AnimalShelter;

drop table animal, cares, customer, customerphone, donations, employee, employeephone, governmentbody, monitors, rescues, shelter;

CREATE TABLE Customer (SSN int NOT NULL,
					   CName varchar(255),
                       Email varchar(255),
                       Age int,
                       Address varchar(255),
                       Sex varchar(255),
                       PRIMARY KEY(SSN));

CREATE TABLE Governmentbody (GName varchar(255),
							Jurisdiction varchar(255) NOT NULL,
                            Phone int,
                            PRIMARY KEY(Jurisdiction));
                        
CREATE TABLE Shelter (Shelterlicense varchar(255) NOT NULL,
					FundJurisdiction varchar(255),
						website varchar(255),
                        email varchar(255),
                        SName varchar(255),
                        Address varchar(255),
                        Phone int,
                        FOREIGN KEY (FundJurisdiction) REFERENCES Governmentbody(Jurisdiction),
                        PRIMARY KEY(Shelterlicense));
     
CREATE TABLE Employee (EmployeeID int NOT NULL,
						WorkShelterlicense varchar(255),
					   EName varchar(255),
                       Email varchar(255),
                       Age int,
                       Address varchar(255),
                       Sex varchar(255),
                       FOREIGN KEY (WorkShelterlicense) REFERENCES Shelter(Shelterlicense),
                       PRIMARY KEY(EmployeeID));     
     
CREATE TABLE Animal (AnimalID int NOT NULL, 
                     AName varchar(255),
                     Sex varchar(255),
                     PlaceOfOrigin varchar(255),
                     DeadOrAlive varchar(255),
                     Age int,
                     NeuterEmployeeID int,
                     EuthanizeEmployeeID int,
                     LivesShelterlicense varchar(255),
                     AdoptedSSN int,
                     Species varchar(255),
                     Breed varchar(255),
                     FOREIGN KEY (EuthanizeEmployeeID) REFERENCES Employee(EmployeeID),
                     FOREIGN KEY (NeuterEmployeeID) REFERENCES Employee(EmployeeID),
                     FOREIGN KEY (LivesShelterlicense) REFERENCES Shelter(Shelterlicense),
                     FOREIGN KEY (AdoptedSSN) REFERENCES Customer(SSN),
                     PRIMARY KEY (AnimalID));
	
CREATE TABLE EmployeePhone (Phone int,
						EmployeeID int NOT NULL,
                        FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
                        PRIMARY KEY(Phone)); 
                        
CREATE TABLE CustomerPhone (Phone int,
						SSN int NOT NULL,
                        FOREIGN KEY (SSN) REFERENCES Customer(SSN),
                        PRIMARY KEY(Phone)); 
                        
CREATE TABLE Donations(SSN int NOT NULL,
				DAmount int NOT NULL,
				Shelterlicense varchar(255) NOT NULL,
                FOREIGN KEY (SSN) REFERENCES Customer(SSN),
                FOREIGN KEY (Shelterlicense) REFERENCES Shelter(Shelterlicense),
                PRIMARY KEY(SSN, Shelterlicense));
                
CREATE TABLE Rescues(SSN int NOT NULL,
				AnimalID int NOT NULL,
                FOREIGN KEY (SSN) REFERENCES Customer(SSN),
                FOREIGN KEY (AnimalID) REFERENCES Animal(AnimalID),
                PRIMARY KEY(SSN, AnimalID));
                
CREATE TABLE Monitors(Jurisdiction varchar(255) NOT NULL,
				Shelterlicense varchar(255) NOT NULL,
                FOREIGN KEY (Jurisdiction) REFERENCES Governmentbody(Jurisdiction),
                FOREIGN KEY (Shelterlicense) REFERENCES Shelter(Shelterlicense),
                PRIMARY KEY(Jurisdiction, Shelterlicense));
                
CREATE TABLE Cares(EmployeeID int NOT NULL,
				AnimalID int NOT NULL,
                FOREIGN KEY (AnimalID) REFERENCES Animal(AnimalID),
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
                PRIMARY KEY(EmployeeID, AnimalID));


                        
