from database import viewAnimalData, viewCustomerData, viewEmployeeData, viewShelterData, viewGData, viewCares, viewMonitor, viewRescues, viewDonations
import pandas as pd
import streamlit as st

def readAnimal():
    result = viewAnimalData()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Animal ID', 'Animal Name', 'Sex', 'PlaceofOrigin', 'Dead or Alive', 'Age', 'Neuterer', 'Euthanizer', 'Lives at', 'Adopted by', 'Species', 'Breed'])
    with st.expander("View all Animals"):
        st.dataframe(df)

def readCustomer():
    result = viewCustomerData()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Customer ID', 'Customer Name', 'Email', 'Age', 'Address', 'Sex'])
    with st.expander("View all Customers"):
        st.dataframe(df)

def readEmployee():
    result = viewEmployeeData()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Employee ID', 'Working at', 'Employee Name', 'Email', 'Age', 'Address', 'Sex'])
    with st.expander("View all Employees"):
        st.dataframe(df)

def readShelter():
    result = viewShelterData()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Shelter License', 'Jursidiction of funding Govt. Body', 'Shelter Website', 'Email', 'Shelter Name', 'Address', 'Phone'])
    with st.expander("View all Shelters"):
        st.dataframe(df)

def readGBody():
    result = viewGData()
    # st.write(result)
    df = pd.DataFrame(result, columns=['GName', 'Jursidiction', 'Address'])
    with st.expander("View all Government bodies"):
        st.dataframe(df)

def readDonations():
    result = viewDonations()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Customer SSN', 'Donation', 'Shelter License'])
    with st.expander("View all Donations"):
        st.dataframe(df)

def readRescues():
    result = viewRescues()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Customer SSN', 'Animal ID'])
    with st.expander("View all Rescues"):
        st.dataframe(df)

def readCares():
    result = viewCares()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Employee ID', 'Animal ID'])
    with st.expander("View all Employees who look after animals"):
        st.dataframe(df)

def readMonitor():
    result = viewMonitor()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Jurisdiction', 'Shelter License'])
    with st.expander("View all Govt Bodies montoring Shelters"):
        st.dataframe(df)

        