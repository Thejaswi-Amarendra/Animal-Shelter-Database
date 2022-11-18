import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "animalshelter"
)

c = mydb.cursor()

# Adding new values into database

def addAnimalData(AnimalID, AName, Sex, PlaceofOrigin, DeadorAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed):
    Age = int(Age)
    AnimalID = int(AnimalID)
    NeuterEmployeeID = int(NeuterEmployeeID)
    EuthanizeEmployeeID = int(EuthanizeEmployeeID)

    c.execute('INSERT INTO Animal(AnimalID, AName, Sex, PlaceofOrigin, DeadorAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (AnimalID, AName, Sex, PlaceofOrigin, DeadorAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed))
    mydb.commit()

def addCustomerData(SSN, CName, Email, Age, Address, Sex):
    Age = int(Age)
    SSN = int(SSN)
    c.execute('INSERT INTO Customer(SSN, CName, Email, Age, Address, Sex) VALUES (%s, %s, %s, %s, %s, %s)', (SSN, CName, Email, Age, Address, Sex))
    mydb.commit()

def addEmployeeData(EmployeeID, WorkShelterlicense, EName, Email, Age, Address, Sex):
    Age = int(Age)
    EmployeeID = int(EmployeeID)
    c.execute('INSERT INTO Employee(EmployeeID,WorkShelterlicense, EName, Email, Age, Address, Sex) VALUES (%s, %s, %s, %s, %s, %s, %s)', (EmployeeID,WorkShelterlicense, EName, Email, Age, Address, Sex))
    mydb.commit()

def addShelterData(Shelterlicense, FundJurisdiction, website, email, Sname, Address, Phone):
    Phone = int(Phone)
    c.execute('INSERT INTO Shelter(Shelterlicense, FundJurisdiction, website, email, Sname, Address, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)', (Shelterlicense, FundJurisdiction, website, email, Sname, Address, Phone))

def addGData(GName, Jurisdiction, Address):
    Phone = int(Phone)
    c.execute('INSERT INTO GovernmentBody(GName, Jurisdiction, Address) VALUES (%s, %s, %s)', (GName, Jurisdiction, Address))

def addDonations(SSN, DAmount, Shelterlicense):
    SSN = int(SSN)
    DAmount = int(DAmount)
    c.execute('INSERT INTO donations(SSN, DAmount, Shelterlicense) VALUES (%s, %s, %s)', (SSN, DAmount, Shelterlicense))

def addRescues(SSN, AnimalID):
    SSN = int(SSN)
    AnimalID = int(AnimalID)
    c.execute('INSERT INTO rescues(SSN, AnimalID) VALUES (%s, %s)', (SSN, AnimalID))

def addCares(EmployeeID, AnimalID):
    EmployeeID = int(EmployeeID)
    AnimalID = int(AnimalID)
    c.execute('INSERT INTO cares(EmployeeID, AnimalID) VALUES (%s, %s)', (EmployeeID, AnimalID))

def addMonitor(Jurisdiction, Shelterlicense):
    c.execute('INSERT INTO monitors(Jurisdiction, Shelterlicense) VALUES (%s, %s)', (Jurisdiction, Shelterlicense))

#Reading values from database

def viewAnimalData():
    c.execute('SELECT * FROM Animal')
    data = c.fetchall()
    return data

def viewCustomerData():
    c.execute('SELECT * FROM Customer')
    data = c.fetchall()
    return data

def viewEmployeeData():
    c.execute('SELECT * FROM Employee')
    data = c.fetchall()
    return data

def viewShelterData():
    c.execute('SELECT * FROM Shelter')
    data = c.fetchall()
    return data

def viewGData():
    c.execute('SELECT * FROM GovernmentBody')
    data = c.fetchall()
    return data

def viewDonations():
    c.execute('SELECT * FROM donations')
    data = c.fetchall()
    return data

def viewRescues():
    c.execute('SELECT * FROM rescues')
    data = c.fetchall()
    return data

def viewCares():
    c.execute('SELECT * FROM cares')
    data = c.fetchall()
    return data

def viewMonitor():
    c.execute('SELECT * FROM Monitors')
    data = c.fetchall()
    return data

#Updating values in database

def updateAnimalData(AnimalID, AName, Sex, PlaceofOrigin, DeadorAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed, oldAnimalID):
    Age = int(Age)
    AnimalID = int(AnimalID)
    NeuterEmployeeID = int(NeuterEmployeeID)
    EuthanizeEmployeeID = int(EuthanizeEmployeeID)

    c.execute('UPDATE ANIMAL SET AnimalID = %s, AName = %s, Sex = %s, PlaceofOrigin = %s, DeadorAlive = %s, Age = %s, NeuterEmployeeID = %s, EuthanizeEmployeeID = %s, LiveShelterlicense = %s, AdoptedSSN = %s, Species = %s, Breed = %s WHERE AnimalID = %s', 
    (AnimalID, AName, Sex, PlaceofOrigin, DeadorAlive, Age, NeuterEmployeeID, EuthanizeEmployeeID, LivesShelterlicense, AdoptedSSN, Species, Breed, oldAnimalID))
    mydb.commit()
    data = c.fetchall()
    return data

def updateCustomerData(SSN, CName, Email, Age, Address, Sex, oldSSN):
    Age = int(Age)
    SSN = int(SSN)
    c.execute('UPDATE Customer SET SSN = %s, CName = %s, Email = %s, Age = %s, Address = %s, Sex = %s WHERE SSN = %s', 
    (SSN, CName, Email, Age, Address, Sex, oldSSN))
    mydb.commit()
    data = c.fetchall()
    return data

def updateEmployeeData(EmployeeID, WorkShelterlicense, EName, Email, Age, Address, Sex, oldEmployeeID):
    Age = int(Age)
    EmployeeID = int(EmployeeID)
    c.execute('UPDATE Employee SET EmployeeID = %s, WorkShelterlicense = %s, EName = %s, Email = %s, Age = %s, Address = %s, Sex = %s WHERE EmployeeID = %s', 
    (EmployeeID, WorkShelterlicense, EName, Email, Age, Address, Sex, oldEmployeeID))
    mydb.commit()
    data = c.fetchall()
    return data

def updateShelterData(Shelterlicense, FundJurisdiction, website, email, Sname, Address, Phone, oldShelterlicense):
    Phone = int(Phone)
    c.execute('UPDATE Shelter SET Shelterlicense = %s, FundJurisdiction = %s, website = %s, email = %s, Sname = %s, Address = %s, Phone = %s WHERE Shelterlicense = %s', 
    (Shelterlicense, FundJurisdiction, website, email, Sname, Address, Phone, oldShelterlicense))
    mydb.commit()
    data = c.fetchall()
    return data

def updateGData(GName, Jurisdiction, Address, oldJurisdiction):
    c.execute('UPDATE GovernmentBody SET GName = %s, jurisdiction = %s, Address = %s WHERE jurisdiction = %s', 
    (GName, Jurisdiction, Address, oldJurisdiction))
    mydb.commit()
    data = c.fetchall()
    return data

def viewAnimalID():
    c.execute('SELECT AnimalID FROM Animal')
    data = c.fetchall()
    return data

def viewSSN():
    c.execute('SELECT SSN FROM Customer')
    data = c.fetchall()
    return data

def viewEmployeeID():
    c.execute('SELECT EmployeeID FROM Employee')
    data = c.fetchall()
    return data

def viewShelterlicense():
    c.execute('SELECT Shelterlicense FROM Shelter')
    data = c.fetchall()
    return data

def viewJurisdiction():
    c.execute('SELECT jurisdiction FROM GovernmentBody')
    data = c.fetchall()
    return data

def getAnimal(AnimalID):
    c.execute('SELECT * FROM ANIMAL WHERE AnimalID="{}"'.format(AnimalID))
    data = c.fetchall()
    return data

def getCustomer(SSN):
    c.execute('SELECT * FROM CUSTOMER WHERE SSN="{}"'.format(SSN))
    data = c.fetchall()
    return data

def getEmployee(EmployeeID):
    c.execute('SELECT * FROM EMPLOYEE WHERE EmployeeID="{}"'.format(EmployeeID))
    data = c.fetchall()
    return data

def getShelter(Shelterlicense):
    c.execute('SELECT * FROM SHELTER WHERE Shelterlicense="{}"'.format(Shelterlicense))
    data = c.fetchall()
    return data


#DELETE DATA

def deleteAnimalData(AnimalID):
    c.execute('DELETE FROM Animal WHERE AnimalID="{}"'.format(AnimalID))
    mydb.commit()

def deleteCustomerData(SSN):
    c.execute('DELETE FROM Customer WHERE SSN="{}"'.format(SSN))
    mydb.commit()

def deleteEmployeeData(EmployeeID):
    c.execute('DELETE FROM Animal WHERE EmployeeID="{}"'.format(EmployeeID))
    mydb.commit()

def deleteShelterData(Shelterlicense):
    c.execute('DELETE FROM Shelter WHERE Shelterlicense="{}"'.format(Shelterlicense))
    mydb.commit()

# def edit_train_data(new_train_no, new_train_name, new_train_type, new_source, new_destination,new_availability, train_no, train_name, train_type, source, destination, availability):
#     c.execute("UPDATE TRAIN SET train_no=%s, train_name=%s, train_type=%s, source=%s, destination=%s, availability = %s WHERE train_no=%s and train_name=%s and train_type=%s and source=%s and destination=%s and availability=%s", 
#               (new_train_no, new_train_name, new_train_type, new_source, new_destination, new_availability, train_no, train_name, train_type, source, destination, availability))
    
#     mydb.commit()
#     data = c.fetchall()
#     return data



