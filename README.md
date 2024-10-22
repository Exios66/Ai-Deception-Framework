# AI Deception Framework

## Overview

The AI Deception Framework is an innovative project designed to explore and analyze the potential for deception in artificial intelligence systems. This framework provides tools and methodologies for researchers, developers, and ethicists to study, detect, and mitigate deceptive behaviors in AI models.

## Features

- **Deception Detection**: Advanced algorithms to identify potential deceptive patterns in AI outputs.
- **Scenario Simulation**: Create and run various scenarios to test AI responses in controlled environments.
- **Ethical Analysis Tools**: Evaluate the ethical implications of AI behaviors and decision-making processes.
- **Transparency Metrics**: Measure and report on the transparency of AI systems.
- **Mitigation Strategies**: Implement and test strategies to reduce the risk of AI deception.

## Installation

# Local File Fetcher for GPT

This application fetches a file from the local filesystem, decodes it, and returns the content along with parsed questions.

## Setup

1. Clone this repository.
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

You can run the application using the following method:

### Using Flask with HTTPS

1. Make the run script executable:

   ```
   chmod +x run.sh
   ```

2. Run the script:

   ```
   ./run.sh
   ```

The application will be available at `https://localhost:8000`. Note that you'll need to accept the self-signed certificate in your browser.

## API Usage

Send a GET request to `/fetch-local-questions` with the following query parameter:

- `file_path`: The path to the file on the local filesystem

Example:

```
https://localhost:8000/fetch-local-questions?file_path=/path/to/your/questions_with_choices.db
```

The API will return a JSON response containing the decoded content of the file and an array of parsed questions.

## OpenAPI Specification

The API is documented using OpenAPI 3.1.0. You can find the specification in the `openapi.yaml` file. The specification uses a relative path for the server URL:

```yaml
servers:
  - url: /
    description: Local development server
```

To use this specification with OpenAPI tools or validators that require a full URL, you may need to prepend the base URL. For local development, you would use:

```yaml
servers:
  - url: https://localhost:8000
    description: Local development server
```

For production or other environments, replace `https://localhost:8000` with the appropriate base URL.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
