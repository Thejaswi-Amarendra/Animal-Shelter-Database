import streamlit as st
from create import *
from delete import *
from read import *
from update import *

def main():
    st.title("Animal Adoption Centre")
    menu = ["Home", "Animal", "Customer", "Employee", "Shelter", "Government Body", "Donations", "Monitoring", "Rescues", "Cares"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Animal Adoption Centre")
    elif choice == "Animal":
        st.subheader("Animals")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter Animal details:")
            createAnimal()
        elif choice1 == "View":
            st.subheader("View Animals")
            readAnimal()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateAnimal()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteAnimal() 
    elif choice == "Customer":
        st.subheader("Customers")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter Customer details:")
            createCustomer()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readCustomer()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateCustomer()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteCustomer() 
    elif choice == "Employee":
        st.subheader("Employees")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createEmployee()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readEmployee()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateEmployee()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteEmployee()
    elif choice == "Shelter":
        st.subheader("Shelters")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createShelter()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readShelter()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateShelter()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteShelter() 
    elif choice == "Government Body":
        st.subheader("Government Body")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createGBody()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readGBody()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateGBody()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteGBody() 
    elif choice == "Donations":
        st.subheader("Donations")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createDonations()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readDonations()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateDonations()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteDonations()
    elif choice == "Monitoring":
        st.subheader("Monitoring")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createMonitor()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readMonitor()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateMonitor()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteMonitor()
    elif choice == "Rescues":
        st.subheader("Rescues")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createRescues()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readRescues()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateRescues()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteRescues()
    elif choice == "Cares":
        st.subheader("Cares")
        menu1 = ["View", "Add", "Update", "Remove"]
        choice1 = st.selectbox("", menu1)
        if choice1 == "Add":
            st.subheader("Enter passenger details:")
            createCares()
        elif choice1 == "View":
            st.subheader("View created tasks")
            readCares()
        elif choice1 == "Update":
            st.subheader("Update created tasks")
            updateCares()
        elif choice1 == "Remove":
            st.subheader("Delete created tasks")
            deleteCares()
    
    else:
        st.subheader("About tasks")

if __name__ == "__main__":
    main()