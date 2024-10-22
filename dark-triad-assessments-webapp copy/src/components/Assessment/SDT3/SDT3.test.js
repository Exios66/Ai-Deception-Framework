import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from '../../../contexts/AssessmentContext';
import SDT3 from './SDT3';

const renderSDT3 = () => {
  render(
    <Router>
      <AssessmentProvider>
        <SDT3 />
      </AssessmentProvider>
    </Router>
  );
};

describe('SDT3 Component', () => {
  test('renders SDT3 assessment title', () => {
    renderSDT3();
    expect(screen.getByText('Short Dark Triad (SD3) Assessment')).toBeInTheDocument();
  });

  test('renders all 27 questions', () => {
    renderSDT3();
    const questions = screen.getAllByRole('group');
    expect(questions).toHaveLength(27);
  });

  test('allows answering questions', () => {
    renderSDT3();
    const firstQuestion = screen.getByText("It's not wise to tell your secrets.");
    const radioButtons = firstQuestion.parentElement.querySelectorAll('input[type="radio"]');
    fireEvent.click(radioButtons[2]); // Select the middle option (3)
    expect(radioButtons[2]).toBeChecked();
  });

  test('submit button is present', () => {
    renderSDT3();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });
});