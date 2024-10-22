import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from '../../../contexts/AssessmentContext';
import SECS from './SECS';

const renderSECS = () => {
  render(
    <Router>
      <AssessmentProvider>
        <SECS />
      </AssessmentProvider>
    </Router>
  );
};

describe('SECS Component', () => {
  test('renders SECS assessment title', () => {
    renderSECS();
    expect(screen.getByText('Social and Economic Conservatism Scale (SECS) Assessment')).toBeInTheDocument();
  });

  test('renders all 12 questions', () => {
    renderSECS();
    const questions = screen.getAllByRole('slider');
    expect(questions).toHaveLength(12);
  });

  test('allows answering questions', () => {
    renderSECS();
    const firstQuestion = screen.getByText("Abortion");
    const slider = firstQuestion.parentElement.querySelector('input[type="range"]');
    fireEvent.change(slider, { target: { value: 75 } });
    expect(slider.value).toBe('75');
  });

  test('submit button is present', () => {
    renderSECS();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });
});