import { ASSESSMENT_TYPES, TRAIT_TYPES } from '../utils/constants';

// Mock data for questions
const questions = {
  [ASSESSMENT_TYPES.SDT3]: [
    { id: 1, text: "It's not wise to tell your secrets.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
    { id: 2, text: "I like to use clever manipulation to get my way.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
    // Add more questions for SDT3
  ],
  [ASSESSMENT_TYPES.SDT4]: [
    { id: 1, text: "I tend to want others to admire me.", trait: TRAIT_TYPES.NARCISSISM },
    { id: 2, text: "I tend to lack remorse.", trait: TRAIT_TYPES.PSYCHOPATHY },
    // Add more questions for SDT4
  ],
  // Add questions for MACHIV and DIRTY_DOZENS
};

export const getQuestions = (assessmentType) => {
  return questions[assessmentType] || [];
};

export const calculateResults = (assessmentType, answers) => {
  // Implement the scoring logic for each assessment type
  // This is a simplified example and should be replaced with actual scoring algorithms
  const results = {};
  const relevantQuestions = questions[assessmentType];

  Object.values(TRAIT_TYPES).forEach(trait => {
    const traitQuestions = relevantQuestions.filter(q => q.trait === trait);
    const traitScores = traitQuestions.map(q => answers[q.id] || 0);
    results[trait] = traitScores.reduce((sum, score) => sum + score, 0) / traitQuestions.length;
  });

  return results;
};

// Add more data-related functions as needed