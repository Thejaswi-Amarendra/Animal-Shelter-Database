import React from "react";
import { useNavigate } from "react-router-dom";
import {useState} from "react";
import Axios from "axios";

function Login()
{
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [loginStatus, setLoginStatus] = useState("")

    function login()
    {
        Axios.post("http://localhost:3001/login", {username : username, password : password}).then((response)=>{if(response.data.message){setLoginStatus(response.data.message)}else{setLoginStatus(response.data[0].username)}}).catch((err)=>{console.log(err)});
    }

    let navigate = useNavigate();
    return (
        <div>
        <h1>Login</h1>
        <div className="login">
            <input type = "text" onChange={(event)=>setUsername(event.target.value)} placeholder="Username" />
            <input type = "password" onChange={(event)=>setPassword(event.target.value)} placeholder="Password" />
            <button onClick={login}>Login</button>
        </div>
        <h1>{loginStatus}</h1>
        <button onClick={()=>navigate("/signup")}>Signup</button>
        <button onClick={()=>navigate("/")}>Home</button>
        </div>
    );
}

export default Login;