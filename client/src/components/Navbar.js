import React from "react";
import { useNavigate } from "react-router-dom";
import Button from '@mui/material/Button';
import './Navbar.css';
import { useAuth } from "../utils/auth";

function Navbar()
{
    let navigate = useNavigate();
    const auth = useAuth();
    return (
        <div style={{textAlign:"center", fontFamily: "Roboto, sans-serif"}}>{!auth.user ? <div><Button variant="outlined" onClick={()=>navigate('/login')}>Login</Button>
        <Button variant="outlined" onClick={()=>navigate("/signup")}>Signup</Button></div> : null}
        
        </div>
    );
}

export default Navbar;