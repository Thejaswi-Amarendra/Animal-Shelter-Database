import React from "react";

import Button from '@mui/material/Button';

import { useNavigate } from "react-router-dom";
import { useAuth } from "../../utils/auth";

function Home()
{
    let navigate = useNavigate();
    const auth = useAuth();
    console.log(auth)
    const handleLogout = () =>
    {
        
        auth.logout();
        navigate("/login");
    }
    return (
        <div style = {{textAlign:"center", fontFamily: "Roboto, sans-serif"}}>
        <Button variant = "outlined" color = "error" onClick={handleLogout}>Logout</Button>
        <Button variant = "outlined" onClick={()=>navigate("/adopt")}>Adopt pet</Button>
        <h1>Welcome {auth.user}</h1>
        </div>
    );
}

export default Home;