import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAssessment } from '../../../hooks/useAssessment';
import { ASSESSMENT_TYPES, DIRTY_DOZEN_LIKERT_SCALE } from '../../../utils/constants';
import Button from '../../common/Button';
import './DirtyDozen.css';

function DirtyDozen() {
  const navigate = useNavigate();
  const { questions, handleAnswer, submitAssessment, error } = useAssessment(ASSESSMENT_TYPES.DIRTY_DOZEN);

  const handleSubmit = () => {
    submitAssessment();
    navigate('/results');
  };

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="dirty-dozen">
      <h2>{ASSESSMENT_TYPES.DIRTY_DOZEN} Assessment</h2>
      {questions.map((question, index) => (
        <div key={index} className="question">
          <p>{question.text}</p>
          <div className="likert-scale">
            {DIRTY_DOZEN_LIKERT_SCALE.map((option) => (
              <label key={option.value}>
                <input
                  type="radio"
                  name={`question-${question.id}`}
                  value={option.value}
                  onChange={() => handleAnswer(question.id, option.value)}
                />
                {option.label}
              </label>
            ))}
          </div>
        </div>
      ))}
      <Button onClick={handleSubmit}>Submit</Button>
    </div>
  );
}

export default DirtyDozen;