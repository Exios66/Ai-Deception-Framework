import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from '../components/Home/Home';
import SDT3 from '../components/Assessment/SDT3/SDT3';
import SDT4 from '../components/Assessment/SDT4/SDT4';
import DirtyDozen from '../components/Assessment/DirtyDozen/DirtyDozen';
import SECS from '../components/Assessment/SECS/SECS';
import SBA from '../components/Assessment/SBA/SBA';
import Visualization from '../components/Visualization/Visualization';
import About from '../components/About/About';

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/assessment/sdt3" element={<SDT3 />} />
      <Route path="/assessment/sdt4" element={<SDT4 />} />
      <Route path="/assessment/dirty-dozen" element={<DirtyDozen />} />
      <Route path="/assessment/secs" element={<SECS />} />
      <Route path="/assessment/sba" element={<SBA />} />
      <Route path="/results" element={<Visualization />} />
      <Route path="/about" element={<About />} />
    </Routes>
  );
}

export default AppRoutes;