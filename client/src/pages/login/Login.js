import React from "react";
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
                        navigate("/userprofile")
                        
                    }
            }).catch((err)=>{console.log(err)});
    }

    
    return (
        <div>
        <h1>Login</h1>
        <div className="Login">
            <form>
            <input type = "text" onChange={(event)=>setUsername(event.target.value)} placeholder="Username" />
            <input type = "password" onChange={(event)=>setPassword(event.target.value)} placeholder="Password" />
            <button onClick={Login}>Login</button>
            </form>
        </div>
        <h1>{loginStatus}</h1>
        <button onClick={()=>navigate("/signup")}>Signup</button>
        <button onClick={()=>navigate("/")}>Home</button>
        </div>
    );
}

export default Login;