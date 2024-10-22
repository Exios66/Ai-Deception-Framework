import React from 'react';
import './DarkModeToggle.css';

const DarkModeToggle = ({ darkMode, setDarkMode }) => {
  return (
    <button id="darkModeToggle" onClick={() => setDarkMode(!darkMode)}>
      {darkMode ? '☀️' : '🌙'}
    </button>
  );
};

export default DarkModeToggle;