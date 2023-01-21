import React from "react";
import { useNavigate} from "react-router-dom";
import { useState } from "react";
import Axios from "axios";

function Signup()
{
    const [usernameReg, setUsernameReg] = useState("");
    const [passwordReg, setPasswordReg] = useState("");

    let navigate = useNavigate();
    
    function signup()
    {
        
        Axios.post("http://localhost:3001/signup", {username : usernameReg, password : passwordReg}).then((response)=>{console.log(response)});
    }

    return (
        <div>
        <h1>Signup</h1>
        <div className="login">
            <input type = "text" onChange={(event)=>setUsernameReg(event.target.value)} placeholder="Username" />
            <input type = "password" onChange={(event)=>setPasswordReg(event.target.value)} placeholder="Password" />
            <button onClick={signup}>Signup</button>
        </div>
        <button onClick={()=>navigate("/login")}>Login</button>
        <button onClick={()=>navigate("/")}>Home</button>
        </div>
    );
}

export default Signup;