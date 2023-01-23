import React from "react";

import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

import { useAuth } from "../../utils/auth";
import { useNavigate} from "react-router-dom";
import { useState } from "react";
import Axios from "axios";

function Signup()
{
    const [usernameReg, setUsernameReg] = useState("");
    const [passwordReg, setPasswordReg] = useState("");
    const [signupStatus, setSignupStatus] = useState("");
    const auth = useAuth();
    let navigate = useNavigate();
    
    function signup()
    {
        Axios.post("http://localhost:3001/signup", {username : usernameReg, password : passwordReg}).then((response)=>{
            if(response.data.message)
                {
                    setSignupStatus(response.data.message)
                }
            else
                {
                    setSignupStatus("Sign up successful")
                    auth.login(usernameReg);
                    navigate("/home")
                }
        });

    }

    return (
        <div style={{textAlign:"center", fontFamily: "Roboto, sans-serif"}}>
        <Button variant="outlined" onClick={()=>navigate("/login")}>Login</Button>
        <Button variant="outlined" onClick={()=>navigate("/")}>Home</Button>
        <br/><br/>
        <h1>Signup</h1>
        <div className="login">
            <TextField type = "text" onChange={(event)=>setUsernameReg(event.target.value)} label="Username" />
            <br/><br/>
            <TextField type = "password" onChange={(event)=>setPasswordReg(event.target.value)} label="Password" />
            <br/><br/>
            <Button variant = "contained" onClick={signup}>Signup</Button>
            <p>{signupStatus}</p>
        </div>
        
        </div>
    );
}

export default Signup;