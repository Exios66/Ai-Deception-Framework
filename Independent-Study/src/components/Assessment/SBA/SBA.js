import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAssessment } from '../../../hooks/useAssessment';
import { ASSESSMENT_TYPES } from '../../../utils/constants';
import Button from '../../common/Button';
import './SBA.css';

function SBA() {
  const navigate = useNavigate();
  const { questions, handleAnswer, submitAssessment, error } = useAssessment(ASSESSMENT_TYPES.SBA);

  const handleSubmit = () => {
    submitAssessment();
    navigate('/results');
  };

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="sba">
      <h2>{ASSESSMENT_TYPES.SBA}</h2>
      <p>Please indicate whether each statement is true or false for you.</p>
      {questions.map((question, index) => (
        <div key={index} className="question">
          <p>{question.text}</p>
          <div className="true-false-buttons">
            <Button onClick={() => handleAnswer(question.id, true)}>True</Button>
            <Button onClick={() => handleAnswer(question.id, false)}>False</Button>
          </div>
        </div>
      ))}
      <Button onClick={handleSubmit}>Submit</Button>
    </div>
  );
}

export default SBA;