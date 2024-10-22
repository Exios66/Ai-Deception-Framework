import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import Header from '../../src/components/Header/Header';

test('renders header with title and navigation', () => {
  render(
    <Router>
      <Header />
    </Router>
  );
  
  const titleElement = screen.getByText(/Dark Triad Assessments/i);
  expect(titleElement).toBeInTheDocument();

  const homeLink = screen.getByText(/Home/i);
  expect(homeLink).toBeInTheDocument();

  const assessmentsLink = screen.getByText(/Assessments/i);
  expect(assessmentsLink).toBeInTheDocument();

  const aboutLink = screen.getByText(/About/i);
  expect(aboutLink).toBeInTheDocument();
});