import React from "react";

import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

import { useNavigate } from "react-router-dom";
import {useState} from "react";
import { useAuth } from "../../utils/auth";
import Axios from "axios";


function Login()
{
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const auth = useAuth();
    const [loginStatus, setLoginStatus] = useState("")

    let navigate = useNavigate();

    function Login()
    {
        Axios.post("http://localhost:3001/Login", {username : username, password : password})
        .then((response)=>
            {
                
                if(response.data.message)
                    {
                        setLoginStatus(response.data.message)
                    }
                else
                    {
                        
                        setLoginStatus(response.data[0].username)
                        auth.login(response.data[0].username)
                        console.log(auth.user)
                        
                        navigate("/home")
                        
                    }
            }).catch((err)=>{console.log(err)});
    }

    
    return (
        <div style={{
            textAlign: "center", fontFamily: "Roboto, sans-serif"
          }}><Button variant="outlined" onClick={()=>navigate("/signup")}>Signup</Button>
        <Button variant="outlined" onClick={()=>navigate("/")}>Home</Button>
        <br/><br/>
        <h1>Login</h1>
        
        <form>
        <TextField type = "text" onChange={(event)=>setUsername(event.target.value)} label="Username" variant="outlined"/>
        <br/><br/>
        <TextField type = "password" onChange={(event)=>setPassword(event.target.value)} label="Password" variant="outlined"/>
        <br/><br/>
        <Button variant="contained" onClick={Login}>Login</Button>
        </form>
        
        <h1 style = {{color: "red"}}>{loginStatus}</h1>
        
        </div>
    );
}

export default Login;