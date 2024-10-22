import React from 'react';
import './Button.css';

function Button({ onClick, children, className = '', disabled = false }) {
  return (
    <button
      className={`button ${className}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}

export default Button;