import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAssessment } from '../../../hooks/useAssessment';
import { ASSESSMENT_TYPES } from '../../../utils/constants';
import Button from '../../common/Button';
import './SECS.css';

function SECS() {
  const navigate = useNavigate();
  const { questions, handleAnswer, submitAssessment, error } = useAssessment(ASSESSMENT_TYPES.SECS);

  const handleSubmit = () => {
    submitAssessment();
    navigate('/results');
  };

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="secs">
      <h2>{ASSESSMENT_TYPES.SECS} Assessment</h2>
      <p>Please indicate the extent to which you feel positive or negative towards each issue. Scores of 0 indicate greater negativity, and scores of 100 indicate greater positivity. Scores of 50 indicate that you feel neutral about the issue.</p>
      {questions.map((question, index) => (
        <div key={index} className="question">
          <p>{question.text}</p>
          <input
            type="range"
            min="0"
            max="100"
            step="1"
            onChange={(e) => handleAnswer(question.id, parseInt(e.target.value))}
          />
          <div className="range-labels">
            <span>0</span>
            <span>50</span>
            <span>100</span>
          </div>
        </div>
      ))}
      <Button onClick={handleSubmit}>Submit</Button>
    </div>
  );
}

export default SECS;