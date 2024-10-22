import React from 'react';
import { useAssessment } from '../../../hooks/useAssessment';
import './MACHIV.css';

function MACHIV() {
  const { questions, handleAnswer, submitAssessment } = useAssessment('MACHIV');

  return (
    <div className="machiv">
      <h2>MACH-IV Assessment</h2>
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

export default MACHIV;