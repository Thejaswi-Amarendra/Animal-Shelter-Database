import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { AuthProvider } from "./utils/auth";
import Entry from "./pages/entry/Entry";
import Login from "./pages/login/Login";
import Signup from "./pages/signup/Signup";
import Home from "./pages/home/Home";
import { RequireAuth } from "./utils/requireAuth";
import Adopt from "./pages/adopt/Adopt";

function App() {
  return (
    <AuthProvider>
    <BrowserRouter>
      <Routes>
      <Route exact path="/" element={<Entry />}/>
      <Route exact path="/login" element={<Login />} />
      <Route exact path="/signup" element={<Signup />} />
      {/* <Route exact path="/adopt" element={<Adopt />} /> */}
      <Route exact path="/adopt" element={<RequireAuth><Adopt /></RequireAuth>} />
      <Route exact path="/home" element={<RequireAuth><Home /></RequireAuth>} />
      </Routes>
    </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
