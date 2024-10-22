import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from '../../../contexts/AssessmentContext';
import SDT4 from './SDT4';

const renderSDT4 = () => {
  render(
    <Router>
      <AssessmentProvider>
        <SDT4 />
      </AssessmentProvider>
    </Router>
  );
};

describe('SDT4 Component', () => {
  test('renders SDT4 assessment title', () => {
    renderSDT4();
    expect(screen.getByText('Short Dark Tetrad (SD4) Assessment')).toBeInTheDocument();
  });

  test('renders all 28 questions', () => {
    renderSDT4();
    const questions = screen.getAllByRole('group');
    expect(questions).toHaveLength(28);
  });

  test('allows answering questions', () => {
    renderSDT4();
    const firstQuestion = screen.getByText("It's not wise to tell your secrets.");
    const radioButtons = firstQuestion.parentElement.querySelectorAll('input[type="radio"]');
    fireEvent.click(radioButtons[2]); // Select the middle option (3)
    expect(radioButtons[2]).toBeChecked();
  });

  test('submit button is present', () => {
    renderSDT4();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });
});