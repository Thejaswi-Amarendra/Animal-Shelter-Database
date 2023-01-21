import React from "react";
import { useNavigate } from "react-router-dom";
import Button from '@mui/material/Button';
import './Navbar.css';

function Navbar()
{
    let navigate = useNavigate();

    return (
        <div className="navbar">
        <Button className="navbar-login" onClick={()=>navigate('/login')}>Login</Button>
        <Button className = "navbar-signup" onClick={()=>navigate("/signup")}>Signup</Button>
        </div>
    );
}

export default Navbar;