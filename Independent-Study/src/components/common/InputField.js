import React from 'react';
import './InputField.css';

function InputField({ type = 'text', label, value, onChange, name, required = false }) {
  return (
    <div className="input-field">
      <label htmlFor={name}>{label}</label>
      <input
        type={type}
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
      />
    </div>
  );
}

export default InputField;