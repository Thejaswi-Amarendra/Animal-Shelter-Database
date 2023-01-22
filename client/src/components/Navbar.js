import React from "react";
import { useNavigate } from "react-router-dom";
// import Button from '@mui/material/Button';
import './Navbar.css';
import { useAuth } from "../utils/auth";

function Navbar()
{
    let navigate = useNavigate();
    const auth = useAuth();
    return (
        <div className="navbar">{!auth.user ? <div><button className="navbar-login" onClick={()=>navigate('/login')}>Login</button>
        <button className = "navbar-signup" onClick={()=>navigate("/signup")}>Signup</button></div> : null}
        
        </div>
    );
}

export default Navbar;