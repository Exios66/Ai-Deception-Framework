import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import AssessmentSelector from '../../src/components/AssessmentSelector/AssessmentSelector';

test('renders assessment selector with all assessment types', () => {
  render(
    <Router>
      <AssessmentSelector />
    </Router>
  );
  
  const titleElement = screen.getByText(/Choose an Assessment/i);
  expect(titleElement).toBeInTheDocument();

  const sdt3Link = screen.getByText(/Short Dark Triad \(SD3\)/i);
  expect(sdt3Link).toBeInTheDocument();

  const sdt4Link = screen.getByText(/Short Dark Tetrad \(SD4\)/i);
  expect(sdt4Link).toBeInTheDocument();

  const machivLink = screen.getByText(/MACH-IV/i);
  expect(machivLink).toBeInTheDocument();

  const dirtyDozenLink = screen.getByText(/Dirty Dozen/i);
  expect(dirtyDozenLink).toBeInTheDocument();
});