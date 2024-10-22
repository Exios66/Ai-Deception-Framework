import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Header() {
  return (
    <header className="app-header">
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/assessment/sdt3">SDT3</Link></li>
          <li><Link to="/assessment/sdt4">SDT4</Link></li>
          <li><Link to="/assessment/dirty-dozen">Dirty Dozen</Link></li>
          <li><Link to="/assessment/secs">SECS</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;