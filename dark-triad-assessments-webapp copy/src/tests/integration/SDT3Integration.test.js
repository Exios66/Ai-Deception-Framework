import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from '../../contexts/AssessmentContext';
import App from '../../App';

const renderApp = () => {
  render(
    <Router>
      <AssessmentProvider>
        <App />
      </AssessmentProvider>
    </Router>
  );
};

describe('SDT3 Integration', () => {
  test('navigates from home to SDT3 assessment', async () => {
    renderApp();
    const sdt3Link = screen.getByText('SDT3 Assessment');
    fireEvent.click(sdt3Link);
    await waitFor(() => {
      expect(screen.getByText('Short Dark Triad (SD3) Assessment')).toBeInTheDocument();
    });
  });

  test('completes SDT3 assessment and navigates to visualization', async () => {
    renderApp();
    const sdt3Link = screen.getByText('SDT3 Assessment');
    fireEvent.click(sdt3Link);

    // Answer all questions
    const radioButtons = screen.getAllByRole('radio');
    radioButtons.forEach((radio, index) => {
      if (index % 5 === 0) { // Select first option for each question
        fireEvent.click(radio);
      }
    });

    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText('Assessment Results')).toBeInTheDocument();
      expect(screen.getByText('Machiavellianism:')).toBeInTheDocument();
      expect(screen.getByText('Narcissism:')).toBeInTheDocument();
      expect(screen.getByText('Psychopathy:')).toBeInTheDocument();
    });
  });
});