import React from 'react'
import { useState, useEffect } from 'react';
import Axios from 'axios';
import AnimalCard from '../../components/AnimalCard';

const Adopt = () => {
    const [animals, setAnimals] = useState([]);
    
    useEffect(() => {
    Axios.get("http://localhost:3001/adopt").then((response) => {
    setAnimals(response.data)})}, [])

  return (
    <div >
        {
        animals.map((animal, index) => (
            <div style = {
                {'width':'25%', 'margin':'auto'}}>
            <AnimalCard name = {animal.aname} species = {animal.species} breed = {animal.breed} age = {animal.age} datePosted = {animal.datePosted} description = {animal.descr} key={index}/>
            <br/>
            </div>
        ))}
        
    </div>
  )
}

export default Adopt;
