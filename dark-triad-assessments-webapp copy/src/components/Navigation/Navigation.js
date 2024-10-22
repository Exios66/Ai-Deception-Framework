import React from 'react';
import { Link } from 'react-router-dom';
import './Navigation.css';

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/sdt3">SDT3</Link></li>
        <li><Link to="/dirtyDozen">Dirty Dozen</Link></li>
        <li><Link to="/sdt4">SDT4</Link></li>
        <li><Link to="/machIV">MACH IV</Link></li>
      </ul>
    </nav>
  );
};

export default Navigation;