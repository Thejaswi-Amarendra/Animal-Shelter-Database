import pandas as pd
import streamlit as st
from database import viewAnimalID, viewEmployeeID, viewSSN, viewShelterlicense, deleteAnimalData, deleteCustomerData, deleteEmployeeData, deleteShelterData
from read import *

def deleteAnimal():
    readAnimal()
    listOfAnimals = [i[0] for i in viewAnimalID()]
    selectedAnimal = st.selectbox("Animal to Delete", listOfAnimals)
    st.warning("Do you want to delete data of -> {}".format(selectedAnimal))
    if st.button("Delete Animal"):
        deleteAnimalData(selectedAnimal)
        st.success("Animal has been deleted successfully")

    st.write("Table after deletion")
    readAnimal()


def deleteCustomer():
    readCustomer()
    listOfCustomers = [i[0] for i in viewSSN()]
    selectedCustomer = st.selectbox("Customer to Delete", listOfCustomers)
    st.warning("Do you want to delete data of -> {}".format(selectedCustomer))
    if st.button("Delete Customer"):
        deleteCustomerData(selectedCustomer)
        st.success("Customer has been deleted successfully")

    st.write("Table after deletion")
    readCustomer()

def deleteEmployee():
    readEmployee()
    listOfEmployees = [i[0] for i in viewEmployeeID()]
    selectedEmployee = st.selectbox("Animal to Delete", listOfEmployees)
    st.warning("Do you want to delete data of -> {}".format(selectedEmployee))
    if st.button("Delete Employee"):
        deleteAnimalData(selectedEmployee)
        st.success("Employee has been deleted successfully")

    st.write("Table after deletion")
    readEmployee()

def deleteShelter():
    readShelter()
    listOfShelters = [i[0] for i in viewEmployeeID()]
    selectedShelter = st.selectbox("Animal to Delete", listOfShelters)
    st.warning("Do you want to delete data of -> {}".format(selectedShelter))
    if st.button("Delete Shelter"):
        deleteAnimalData(selectedShelter)
        st.success("Shelter has been deleted successfully")

    st.write("Table after deletion")
    readEmployee()

def deleteGBody():
    return

def deleteRescues():
    return

def deleteDonations():
    return

def deleteCares():
    return

def deleteMonitor():
    return

