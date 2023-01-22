import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../utils/auth";

function UserProfile()
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
        <div>
        <h1>Welcome {auth.user}</h1>
        <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default UserProfile;