import React, { useContext } from 'react';
import { AssessmentContext } from '../../contexts/AssessmentContext';
import { TRAIT_TYPES, ASSESSMENT_TYPES } from '../../utils/constants';
import './Visualization.css';

function Visualization() {
  const { results, currentAssessment } = useContext(AssessmentContext);

  if (!results) {
    return <div>No results to display. Please complete an assessment first.</div>;
  }

  const getMaxScore = () => {
    switch (currentAssessment) {
      case ASSESSMENT_TYPES.SDT3:
      case ASSESSMENT_TYPES.SDT4:
        return 5;
      case ASSESSMENT_TYPES.DIRTY_DOZEN:
        return 7;
      case ASSESSMENT_TYPES.SECS:
        return 100;
      default:
        return 5;
    }
  };

  const maxScore = getMaxScore();
  
  const getTraits = () => {
    switch (currentAssessment) {
      case ASSESSMENT_TYPES.SDT4:
        return Object.values(TRAIT_TYPES);
      case ASSESSMENT_TYPES.SDT3:
      case ASSESSMENT_TYPES.DIRTY_DOZEN:
        return Object.values(TRAIT_TYPES).slice(0, 3);
      case ASSESSMENT_TYPES.SECS:
        return ['SOCIAL', 'ECONOMIC'];
      case ASSESSMENT_TYPES.SBA:
        return ['SOCIAL_BEHAVIOR'];
      default:
        return [];
    }
  };

  const traits = getTraits();

  return (
    <div className="visualization">
      <h2>{currentAssessment} Results</h2>
      <div className="results-chart">
        {traits.map((trait) => (
          <div key={trait} className="trait-bar">
            <div className="trait-label">{trait}</div>
            <div className="trait-score-bar" style={{ width: `${(results[trait] / maxScore) * 100}%` }}>
              {results[trait].toFixed(2)}
            </div>
          </div>
        ))}
      </div>
      <div className="results-interpretation">
        <h3>Interpretation</h3>
        {currentAssessment === ASSESSMENT_TYPES.SECS ? (
          <p>
            These results show your scores on the Social and Economic Conservatism Scale. 
            Higher scores indicate more conservative attitudes in each domain.
            Remember, these results are for educational purposes only and should not be considered a definitive measure of political ideology.
          </p>
        ) : (
          currentAssessment === ASSESSMENT_TYPES.SBA ? (
            <p>
              This score represents your level of social behavior and extraversion. 
              A higher score indicates more extraverted and socially active tendencies.
              Remember, this assessment is for educational purposes only and should not be considered a definitive measure of personality.
            </p>
          ) : (
            <p>
              These results show your scores on the {currentAssessment === ASSESSMENT_TYPES.SDT4 ? 'Dark Tetrad' : 'Dark Triad'} traits. 
              Higher scores indicate a stronger presence of the trait.
              Remember, these results are for educational purposes only and should not be considered a clinical diagnosis.
            </p>
          )
        )}
      </div>
    </div>
  );
}

export default Visualization;