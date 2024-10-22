import React from 'react';
import { Link } from 'react-router-dom';
import { ASSESSMENT_TYPES } from '../../utils/constants';
import './AssessmentSelector.css';

const AssessmentSelector = () => {
  const assessments = [
    { id: 'sdt3', name: 'Short Dark Triad (SDT3)', description: 'The SDT3 assesses three personality traits: Machiavellianism, Narcissism, and Psychopathy.' },
    { id: 'dirtyDozen', name: 'Dirty Dozen', description: 'The Dirty Dozen is a brief measure of the Dark Triad personality traits.' },
    { id: 'sdt4', name: 'Short Dark Tetrad (SDT4)', description: 'The SDT4 measures four dark personality traits: Machiavellianism, Narcissism, Psychopathy, and Sadism.' },
    { id: 'machIV', name: 'MACH IV', description: 'The MACH IV is a test of Machiavellianism, measuring a person\'s willingness to manipulate others.' },
  ];

  return (
    <div id="assessments">
      {assessments.map((assessment) => (
        <div key={assessment.id} id={assessment.id} className="assessment">
          <h2>{assessment.name}</h2>
          <p>{assessment.description}</p>
          <Link to={`/assessment/${assessment.id}`}>
            <button>Start {assessment.name} Assessment</button>
          </Link>
        </div>
      ))}
    </div>
  );
};

export default AssessmentSelector;