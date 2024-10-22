// Helper functions for the Dark Triad Assessments web application

export const calculateScore = (answers, scoringKey) => {
  // Implement scoring logic here
};

export const interpretResults = (scores) => {
  // Implement result interpretation logic here
};

export const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};

export const validateEmail = (email) => {
  const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return re.test(String(email).toLowerCase());
};

// Add more helper functions as needed