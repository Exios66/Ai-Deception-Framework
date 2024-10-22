import { useContext, useEffect, useState } from 'react';
import { AssessmentContext } from '../contexts/AssessmentContext';
import { getQuestions, calculateResults } from '../services/api';

export const useAssessment = (assessmentType) => {
  const { setCurrentAssessment, answers, setAnswers, setResults } = useContext(AssessmentContext);
  const [questions, setQuestions] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    setCurrentAssessment(assessmentType);
    setAnswers({}); // Reset answers when switching assessments
    try {
      const fetchedQuestions = getQuestions(assessmentType);
      setQuestions(fetchedQuestions);
    } catch (err) {
      setError('Failed to fetch questions. Please try again later.');
    }
  }, [assessmentType, setCurrentAssessment, setAnswers]);

  const handleAnswer = (questionId, answer) => {
    setAnswers((prevAnswers) => ({
      ...prevAnswers,
      [questionId]: answer,
    }));
  };

  const submitAssessment = () => {
    try {
      const results = calculateResults(assessmentType, answers);
      setResults(results);
    } catch (err) {
      setError('Failed to calculate results. Please try again later.');
    }
  };

  return {
    questions,
    handleAnswer,
    submitAssessment,
    error,
  };
};

export default useAssessment;