# Dark Triad Assessments Web Application

This web application provides various assessments related to the Dark Triad and Dark Tetrad personality traits: Machiavellianism, Narcissism, Psychopathy, and Sadism. It includes multiple assessment types and visualizations of results.

## Features

- Multiple assessment types:
  - Short Dark Triad (SD3)
  - Short Dark Tetrad (SD4)
  - MACH-IV
  - Dirty Dozen
- Interactive user interface
- Visualization of results
- Responsive design

## Assessments

### Short Dark Triad (SD3)

The SD3 is a brief measure of the Dark Triad of personality, measuring Machiavellianism, Narcissism, and Psychopathy. It consists of 27 items, with 9 items per trait.

### Short Dark Tetrad (SD4)

The SD4 extends the Dark Triad by including a fourth trait, Sadism. It measures Machiavellianism, Narcissism, Psychopathy, and Sadism. The SD4 typically consists of 28 items, with 7 items per trait.

### MACH-IV

The MACH-IV is a specific measure of Machiavellianism. It consists of 20 items designed to assess an individual's willingness to manipulate others for personal gain.

### Dirty Dozen

The Dirty Dozen is a concise measure of the Dark Triad traits. It consists of 12 items, with 4 items each measuring Machiavellianism, Narcissism, and Psychopathy.

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm (v6 or later)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/dark-triad-assessments-webapp.git
   ```

2. Navigate to the project directory:

   ```
   cd dark-triad-assessments-webapp
   ```

3. Install dependencies:

   ```
   npm install
   ```

4. Start the development server:

   ```
   npm start
   ```

5. Open your browser and visit `http://localhost:3000`

## Running Tests

To run the test suite:

```shell
npm test
```

## Deployment

This project is set up to deploy automatically to GitHub Pages using GitHub Actions. Every push to the `main` branch will trigger a new deployment.

To deploy manually:

1. Update the `homepage` field in `package.json` with your GitHub Pages URL:

   ```json
   "homepage": "https://your-username.github.io/dark-triad-assessments-webapp"
   ```

2. Run the deployment script:

   ```shell
   npm run deploy
   ```

This will build the app and push it to the `gh-pages` branch of your repository.

## Built With

- React
- React Router
- Context API for state management

## Project Structure

```
dark-triad-assessments-webapp/
├── public/
├── src/
│   ├── components/
│   │   ├── Assessment/
│   │   │   ├── SDT3/
│   │   │   ├── SDT4/
│   │   │   ├── MACHIV/
│   │   │   └── DirtyDozens/
│   │   ├── common/
│   │   ├── Header/
│   │   ├── Footer/
│   │   └── Visualization/
│   ├── contexts/
│   ├── hooks/
│   ├── routes/
│   ├── services/
│   └── utils/
├── tests/
└── ...
```

## Changelog and Versioning

This project uses [Semantic Versioning](https://semver.org/) and maintains a changelog to document notable changes. The changelog is automatically updated using a Python script.

### Viewing the Changelog

The full changelog can be found in the [CHANGELOG.md](CHANGELOG.md) file in the root of the project.

### Updating the Changelog

The changelog is automatically updated after each commit using a Git post-commit hook. The update script analyzes the commit message to determine the type of change and updates the CHANGELOG.md file accordingly.

If you need to manually update the changelog, you can run the following command:

```shell
python update_changelog.py
```

When writing commit messages, use the following prefixes to categorize your changes:

- `feat:` for new features (increments the minor version)
- `fix:` for bug fixes (increments the patch version)
- `BREAKING CHANGE:` for breaking changes (increments the major version)
- `docs:`, `style:`, `refactor:`, `perf:`, `test:` for other changes (updates the changelog without changing the version)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Short Dark Triad (SD3)](https://openpsychometrics.org/tests/SD3/)
- [Short Dark Tetrad (SD4)](https://openpsychometrics.org/tests/SD4/)
- [MACH-IV](https://openpsychometrics.org/tests/MACH-IV/)
- [Dirty Dozen](https://openpsychometrics.org/tests/DD/)