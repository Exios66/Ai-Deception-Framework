import React, { useState, useEffect } from 'react';
import { HashRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from './contexts/AssessmentContext';
import Header from './components/Header/Header';
import Navigation from './components/Navigation/Navigation';
import AssessmentSelector from './components/AssessmentSelector/AssessmentSelector';
import Results from './components/Results/Results';
import DarkModeToggle from './components/DarkModeToggle/DarkModeToggle';
import Intro from './components/Intro/Intro';
import './App.css';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [showIntro, setShowIntro] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowIntro(false);
    }, 3000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <Router basename="/dark-triad-assessments">
      <AssessmentProvider>
        <div className={`App ${darkMode ? 'dark-mode' : ''}`}>
          {showIntro && <Intro />}
          <DarkModeToggle darkMode={darkMode} setDarkMode={setDarkMode} />
          <Header />
          <Navigation />
          <main>
            <AssessmentSelector />
            <Results />
          </main>
        </div>
      </AssessmentProvider>
    </Router>
  );
}

export default App;