USE animalshelter;

INSERT INTO Customer(SSN, CName, Email, Age, Address, Sex) VALUES 
(222563769, "Quintillus Nash", "quint@gmail.com", 20, "1, A-43/44, Anand Laxmi Apts, Sector 3, Mira Road, Mumbai, 401107", "Male"),
(262967894, "Rasmus Willoughby", "rasmus@gmail.com", 30, "15-b, Shaikh Mansion, Vasil Khan Street, Mumbai, 400008", "Male"),
(262967812, "Myrtle Atalia", "myrtle@gmail.com", 19, "161 Pocket A 7 Sector 17, Delhi, 110085", "Female"),
(426258063, "Moishe Aravind", "moishe@gmail.com", 72, " Plot No. D-12, Street No. 21, Blue Steel House, Midc Marol, Andheri (west), Mumbai, 400093", "Male"),
(136152038, "Alison Nechtan", "alison@gmail.com", 34, "Shop No 7, Kadri Mansion, Kadri Mansion, 150, L J Road, Mahim, Mumbai, 400016", "Female"),
(450777805, "Hrodpreht Halil", "hrodpreht@gmail.com", 23, "H No 17 Sector 18a, Delhi, 121001", "Male"),
(540067365, "Marina Evelia", "marina@gmail.com", 82, "39/9 MIG Block PWD Quarters, Nandini layout, Bengaluru, 560096", "Female"),
(540275037, "Shane Anandi", "shane@yahoo.in", 29, "2-6-106, Uppal, Hyderabad, 500039", "Male"),
(400666639, "Henricus Kärt", "henri@gmail.com", 43, "SLV Parkview apartment, Ullalu, Bengaluru, 560110", "Male"),
(433227198, "Goizargi Gerda", "goi@gmail.com", 52, "1, 403, Sukh Sagar Building, Akruli X Road, Kandivali (west), Mumbai, 400067", "Female"),
(574701575, "Amit Tase", "amit@hotmail.com", 39, "Manish Nagar Four Bunglow, J P Rd, Andheri (west), Mumbai", "Male"),
(268480827, "Mihaela Leith", "meh@email.com", 36, "63, Juhu Supreme Shopping Cnt, Gulmohar X Road 9, Jvpd Scheme, Juhu", "Female");

INSERT INTO Governmentbody(GName, Jurisdiction, Phone) VALUES 
("BBMP", "Bengaluru", 0802864652),
("BMMP", "Mysuru", 0801233444)
;

INSERT INTO Shelter(ShelterLicense, FundJurisdiction, website, Email, SName, Address, Phone) VALUES 
('5f7qsu3k16', "Bengaluru", "goodanimals.com", "goodanimals@gmail.com" ,"Good Animals", "Rajajinagar, Bengaluru", 969669696),
('okz71w4xhu', "Mysuru", "gganimals.com", "gganimals@gmail.com" ,"GG Animals", "Palace, Mysuru", 123969696),
('drs2ixklkr', "Bengaluru", "hoodanimals.com", "hoodanimals@gmail.com" ,"Hood Animals", "Kalasipalya, Bengaluru", 969469696),
('mklwwhyn1i', "Mysuru", "foodanimals.com", "foodanimals@gmail.com" ,"Foodie Animals", "BSK, Mysuru", 969692696),
('hblih6hut7', "Bengaluru", "hotanimals.com", "hotanimals@gmail.com" ,"Hot Animals", "Koramangala, Bengaluru", 965969696);

INSERT INTO Employee(EmployeeID, WorkShelterLicense, EName, Email, Age, Address, Sex) VALUES 
(319224919, '5f7qsu3k16', "Jyoti Manju", "jyoti@gmail.com", 50, "29/3, Diagonalrd,4thblkjayangrblr-11, Jayanagar, Bangalore, Karnataka, 560011", "Female"),
(502064996, '5f7qsu3k16', "Kalidas Ankit", "kalidas@gmail.com", 43, "3/36, M K S Arcade, Bellary Road, Ganga Nagar, Bangalore, Karnataka, 560032", "Male"),
(532296596, '5f7qsu3k16', "Devaraj Gautam", "devaraj@gmail.com", 22, "26/1, 26/1seshadrirdblr-9, Seshadri Road, Bangalore, Karnataka, 560009", "Male"),
(486167771, '5f7qsu3k16', "Manjula Kuldeep", "manjula@gmail.com", 45, "79, Gundopanth Street, Bangalore, Karnataka, 560002", "Female"),
(363841702, 'okz71w4xhu', "Nisha Gopal", "misha@gmail.com", 34, "12 abc apt, Mysuru Karnataka", "Female"),
(526973901, 'okz71w4xhu', "Diya Hema", "diya@gmail.com", 23, "16, asf apartment, Mysuru, Karnataka", "Female"),
(425502081, 'okz71w4xhu', "Pramod Arati", "pramod@gmail.com", 23, "16, asf apartment, Mysuru, Karnataka", "Male"),
(577470531, 'okz71w4xhu', "Jyoti Harpreet", "jyoti@gmail.com", 35, "76, poi lane, Mysuru, Karnataka", "Male"),
(002667505, 'drs2ixklkr', "Vasundhara Shubham", "vasundhara@gmail.com", 39, "abc, 13th cross, Bengaluru, Karnataka", "Female"),
(574354562, 'drs2ixklkr', "Vinay Inderjit", "vinay@gmail.com", 25, "def, 15th road, Bengaluru, Karnataka", "Male"),
(450265227, 'drs2ixklkr', "Kishor Jaswinder", "kishor@gmail.com", 19, "26/1, 26/1seshadrirdblr-9, Seshadri Road, Bangalore, Karnataka, 560009", "Male"),
(479129288, 'drs2ixklkr', "Ramakant Aurobindo", "ramakant@gmail.com", 49, "qwert apt, Bangalore, Karnataka", "Male"),
(441603835, 'mklwwhyn1i', "Anisha Baldev", "anisha@gmail.com", 61, "79, Gundopanth Street, Bangalore, Karnataka, 560002", "Female"),
(319064001, 'mklwwhyn1i', "Ashok Kailash", "ashok@gmail.com", 50, "3/36, M K S Arcade, Bellary Road, Ganga Nagar, Bangalore, Karnataka, 560032", "Male"),
(238675531, 'mklwwhyn1i', "Murali Harish", "murali@gmail.com", 34, "1/15, abc arcade, bangalore, Karnataka", "Male"),
(545986776, 'mklwwhyn1i', "Deo Priya", "deo@gmail.com", 29, "XYZ Apartment, Bangalore, Karnataka", "Male"),
(575206302, 'hblih6hut7', "Saral Vasu", "saral@gmail.com", 39, "SLV Apartment, Bangalore, Karnataka", "Male"),
(527869735, 'hblih6hut7', "Prabhu Apurva", "prabhu@gmail.com", 40, "ZWF Villa, Bangalore, Karnataka", "Male"),
(526976364, 'hblih6hut7', "Dev Purushottam", "dev@gmail.com", 20, "POI apt, Bangalore, Karnataka", "Male"),
(160401256, 'hblih6hut7', "Rajkumari Narinder", "rajkumari@gmail.com", 38, "No yes apartment, Karnataka", "Female");

INSERT INTO animal(AnimalID, AName, Sex, PlaceOfOrigin, DeadOrAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed) VALUES 
(1989, "Shunti", "Male", "Bengaluru", "Alive", 3, 160401256, NULL, 'hblih6hut7', NULL, "Cat", "Street"), 
(3689, "Jamun", "Female", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',222563769, "Cat", "Street"),
(6467, "Shanti", "Female", "Mysuru", "Dead", 17, NULL, 526973901, 'okz71w4xhu', NULL, "Cat", "Street"),
(3122, "Bun", "Male", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',222563769, "Cat", "Street"), 
(3112, "Burger", "Male", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',NULL, "Cat", "Street"), 
(3100, "Lettuce", "Female", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',NULL, "Cat", "Street"), 
(3022, "Jam", "Male", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',574701575, "Cat", "Street"), 
(3233, "Ketchup", "Female", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',NULL, "Cat", "Street");

INSERT INTO animal(AnimalID, AName, Sex, PlaceOfOrigin, DeadOrAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed) 
VALUES
(3000, "Leaf", "Male", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',222563769, "Cat", "Street"),
(3788, "Butterlee", "Male", "Bengaluru", "Alive", 2, 441603835, NULL, 'mklwwhyn1i',222563769, "Cat", "Street");

INSERT INTO CustomerPhone(Phone, SSN) 
VALUES
(992929929, 222563769), 
(992929912, 222563769),
(999929911, 262967894),
(929929910, 262967812), 
(929929909, 426258063),
(929929901, 136152038),
(929929902, 450777805), 
(929929003, 540067365),
(929929004, 540275037),
(929929005, 400666639), 
(929929006, 574701575),
(929929007, 400666639)
;

INSERT INTO Donations(SSN, DAmount, Shelterlicense) VALUES
(222563769, 100000, '5f7qsu3k16'), 
(574701575, 20000, 'hblih6hut7'),
(433227198, 69000, 'okz71w4xhu'),
(540275037, 12000, 'drs2ixklkr'),
(400666639, 10000000, 'mklwwhyn1i'),
(450777805, 123123, 'drs2ixklkr');

INSERT INTO Cares(EmployeeID, AnimalID) VALUES
(238675531, 1989),
(238675531, 3689),
(238675531, 6467),
(238675531, 3122),
(238675531, 3112), 
(238675531, 3022);




Select * from cares;

Delete from cares where EmployeeID>0;


DELETE from donations where SSN>0;

DELETE FROM Animal where animalID>0;
