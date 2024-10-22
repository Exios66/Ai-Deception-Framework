import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from '../../../contexts/AssessmentContext';
import DirtyDozen from './DirtyDozen';

const renderDirtyDozen = () => {
  render(
    <Router>
      <AssessmentProvider>
        <DirtyDozen />
      </AssessmentProvider>
    </Router>
  );
};

describe('Dirty Dozen Component', () => {
  test('renders Dirty Dozen assessment title', () => {
    renderDirtyDozen();
    expect(screen.getByText('Dirty Dozen Assessment')).toBeInTheDocument();
  });

  test('renders all 12 questions', () => {
    renderDirtyDozen();
    const questions = screen.getAllByRole('group');
    expect(questions).toHaveLength(12);
  });

  test('allows answering questions', () => {
    renderDirtyDozen();
    const firstQuestion = screen.getByText("I tend to manipulate others to get my way.");
    const radioButtons = firstQuestion.parentElement.querySelectorAll('input[type="radio"]');
    fireEvent.click(radioButtons[3]); // Select the middle option (4)
    expect(radioButtons[3]).toBeChecked();
  });

  test('submit button is present', () => {
    renderDirtyDozen();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });
});