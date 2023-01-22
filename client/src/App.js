import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { AuthProvider } from "./utils/auth";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import Signup from "./pages/signup/Signup";
import UserProfile from "./pages/userProfile/UserProfile";
import { RequireAuth } from "./utils/requireAuth";

function App() {
  return (
    <AuthProvider>
    <BrowserRouter>
      <Routes>
      <Route exact path="/" element={<Home />}/>
      <Route exact path="/login" element={<Login />} />
      <Route exact path="/signup" element={<Signup />} />
      <Route exact path="/userprofile" element={<RequireAuth><UserProfile /></RequireAuth>} />
      </Routes>
    </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
