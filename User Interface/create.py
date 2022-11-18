import streamlit as st
from database import addAnimalData, addCustomerData, addEmployeeData, addShelterData, addGData, addDonations, addCares, addMonitor, addRescues, viewSSN, viewShelterlicense, viewEmployeeID, viewJurisdiction
import pandas as pd

def createAnimal():
    customerlist = [i[0] for i in viewSSN()]
    shelterlist = [i[0] for i in viewShelterlicense()]
    employeelist = [i[0] for i in viewEmployeeID()]

    col1, col2 = st.columns(2)
    with col1:
        AnimalID = st.text_input("Animal ID:")
        AnimalName = st.text_input("Animal name:")
        AnimalSpecies = st.text_input("Species:")
        Shelterlicense = st.selectbox("Shelter license", shelterlist)
        neuter = st.selectbox("Employee ID of neuterer", employeelist)
    with col2:
        Sex = st.selectbox("Sex: ", ["Male", "Female", "Others"])
        Age = st.text_input("Age: ")
        Breed = st.text_input("Breed: ")
        DeadorAlive = st.text_input("Dead or Alive:")
        euthanize = st.selectbox("Employee ID of Euthanizer", employeelist)
    CustomerID = st.selectbox("ID of person who adopted", customerlist)
    PlaceOfOrigin = st.text_input("Place of Origin: ")
    if st.button("Add Animal to database"):
        addAnimalData(AnimalID, AnimalName, Sex, PlaceOfOrigin,DeadorAlive, Age, neuter, euthanize, Shelterlicense, CustomerID, AnimalSpecies, Breed)
        st.success("Successfully added Animal: {}".format(AnimalName))

def createCustomer():
    col1, col2 = st.columns(2)
    with col1:
        CustomerID = st.text_input("Customer ID:")
        CustomerName = st.text_input("Animal name:")
        Email = st.text_input("Email: ")
    with col2:
        Sex = st.selectbox("Sex: ", ["Male", "Female", "Others"])
        Age = st.text_input("Age: ")
        Address = st.text_input("Address: ")

    if st.button("Add Customer to database"):
        addCustomerData(CustomerID, CustomerName, Email, Age, Address, Sex)
        st.success("Successfully added Customer: {}".format(CustomerName))

def createEmployee():
    shelterlist = [i[0] for i in viewShelterlicense()]
    col1, col2 = st.columns(2)
    with col1:
        EmployeeID = st.text_input("Employee ID:")
        EmployeeName = st.text_input("Employee name:")
        Email = st.text_input("Email: ")
    with col2:
        Sex = st.selectbox("Sex: ", ["Male", "Female", "Others"])
        Age = st.text_input("Age: ")
        Address = st.text_input("Address: ")
    Shelterlicense = st.selectbox("Shelter license", shelterlist)

    if st.button("Add Customer to database"):
        addEmployeeData(EmployeeID, Shelterlicense, EmployeeName, Email, Age, Address, Sex)
        st.success("Successfully added Employee: {}".format(EmployeeName))

def createShelter():
    jurisdictionlist = [i[0] for i in viewJurisdiction()]

    col1, col2 = st.columns(2)
    with col1:
        Sname = st.text_input("ShelterName: ")
        FundJurisdiction = st.selectbox("Jursidiction of funding government body:", jurisdictionlist)
        Email = st.text_input("Email: ")
    with col2:
        Website = st.text_input("Website: ")
        Phone = st.text_input("Phone: ")
        Address = st.text_input("Address: ")
    Shelterlicense = st.text_input("Shelter license: ")

    if st.button("Add Customer to database"):
        addShelterData(Shelterlicense, FundJurisdiction, Website, Email, Sname, Address, Phone)
        st.success("Successfully added Shelter: {}".format(Sname))

def createGBody():
    col1, col2 = st.columns(2)
    with col1:
        Jurisdiction = st.text_input("Jurisdiction: ")
    with col2:
        GName = st.text_input("Government body name: ")
    Address = st.text_input("Address: ")

    if st.button("Add Customer to database"):
        addGData(GName, Jurisdiction, Address)
        st.success("Successfully added Shelter: {}".format(GName))

def createDonations():
    shelterlist = [i[0] for i in viewShelterlicense()]
    customerlist = [i[0] for i in viewSSN()]

    col1, col2 = st.columns(2)
    with col1:
        SSN = st.selectbox("SSN of person who donated", customerlist)
    with col2:
        Shelterlicense = st.selectbox("Shelter license", shelterlist)
    DAmount = st.text_input("Donation Amount: ")
    if st.button("Add Customer to database"):
        addDonations(SSN, DAmount, Shelterlicense)
        st.success("Successfully added Donation by: {}".format(SSN))

def createRescues():
    col1, col2 = st.columns(2)
    with col1:
        SSN = st.text_input("SSN of Rescuer: ")
    with col2:
        AnimalID = st.text_input("Animal Rescued: ")
    
    if st.button("Add Customer to database"):
        addRescues(SSN, AnimalID)
        st.success("Successfully added Rescue by: {}".format(SSN))

def createMonitor():
    col1, col2 = st.columns(2)
    with col1:
        Jurisdiction = st.text_input("Jurisdiction of monitoring Govt body: ")
    with col2:
        ShelterID = st.text_input("Shelter being monitored: ")
    
    if st.button("Add Customer to database"):
        addMonitor(Jurisdiction, ShelterID)
        st.success("Successfully added Shelter monitored by: {}".format(Jurisdiction))

def createCares():
    col1, col2 = st.columns(2)
    with col1:
        EmployeeID = st.text_input("EmployeeID: ")
    with col2:
        AnimalID = st.text_input("Animal: ")
    
    if st.button("Add Customer to database"):
        addCares(EmployeeID, AnimalID)
        st.success("Successfully added Animal cared by: {}".format(EmployeeID))