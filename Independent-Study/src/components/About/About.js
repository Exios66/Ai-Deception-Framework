import React from 'react';
import './About.css';

function About() {
  return (
    <div className="about">
      <h2>About Personality Assessments</h2>
      <p>
        This application provides various personality assessments, including:
      </p>
      <ul>
        <li>Short Dark Triad (SD3): Measures Machiavellianism, Narcissism, and Psychopathy</li>
        <li>Short Dark Tetrad (SD4): Measures Machiavellianism, Narcissism, Psychopathy, and Sadism</li>
        <li>Dirty Dozen: A brief measure of the Dark Triad traits (Machiavellianism, Narcissism, and Psychopathy)</li>
        <li>Social and Economic Conservatism Scale (SECS): Measures social and economic conservative attitudes</li>
      </ul>
      <p>
        These assessments are for educational and research purposes only and should not be used for clinical diagnosis.
      </p>
    </div>
  );
}

export default About;