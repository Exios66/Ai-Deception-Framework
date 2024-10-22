import React, { createContext, useState } from 'react';

export const AssessmentContext = createContext();

export const AssessmentProvider = ({ children }) => {
  const [currentAssessment, setCurrentAssessment] = useState(null);
  const [answers, setAnswers] = useState({});
  const [results, setResults] = useState(null);

  const updateResults = (assessmentType, newResults) => {
    setResults((prevResults) => ({
      ...prevResults,
      [assessmentType]: newResults,
    }));
  };

  const value = {
    currentAssessment,
    setCurrentAssessment,
    answers,
    setAnswers,
    results,
    updateResults,
  };

  return (
    <AssessmentContext.Provider value={value}>
      {children}
    </AssessmentContext.Provider>
  );
};

export default AssessmentProvider;