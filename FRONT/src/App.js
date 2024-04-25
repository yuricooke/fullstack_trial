import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import UserContext from './api/UserContext';

import Home from './pages/Home';
import Hikes from './pages/Hikes';
import HikeDetails from './pages/HikeDetails';

export default function App() {
  const [user, setUser] = useState(null);

  return (
    <div>
      <BrowserRouter>
        <UserContext.Provider value={{ user, setUser }}>
          <Routes>
            <Route path='/' element={<Home />}></Route>
            <Route path='/Hikes' element={<Hikes />}></Route>
            <Route path='/Hikes/:id' element={<HikeDetails />}></Route>
          </Routes>
        </UserContext.Provider>
      </BrowserRouter>
    </div>
  );
}