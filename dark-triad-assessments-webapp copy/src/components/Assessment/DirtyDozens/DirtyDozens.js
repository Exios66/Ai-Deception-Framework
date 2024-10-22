import React from 'react';
import { useAssessment } from '../../../hooks/useAssessment';
import './DirtyDozens.css';

function DirtyDozens() {
  const { questions, handleAnswer, submitAssessment } = useAssessment('DirtyDozens');

  return (
    <div className="dirty-dozens">
      <h2>Dirty Dozen Assessment</h2>
      {questions.map((question, index) => (
        <div key={index} className="question">
          <p>{question.text}</p>
          {/* Add answer options here */}
        </div>
      ))}
      <button onClick={submitAssessment}>Submit</button>
    </div>
  );
}

export default DirtyDozens;