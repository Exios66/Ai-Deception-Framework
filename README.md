# AI Deception Framework

A comprehensive framework for analyzing and detecting deception in AI systems, with integration to the Literary Vault API.

## Features

- AI Model Analysis
- Deception Detection
- Question Analysis Integration
- Real-time Metrics Dashboard
- Literary Vault API Integration
- Open Source Collaboration

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Exios66/Ai-Deception-Framework.git
cd Ai-Deception-Framework
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration:
# GITHUB_TOKEN=your_github_token
# DATABASE_URL=sqlite:///questions.db
# JWT_SECRET=your_secret_key
# CORS_ORIGINS=http://localhost:3000,https://yourdomain.com
# API_KEY=your_openai_api_key
```

## API Endpoints

### 1. Model Analysis

Analyze AI models for potential deception:

```bash
# Upload and analyze a model
curl -X POST "http://localhost:8000/api/v1/analysis/model" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/model.h5"
```

Response:

```json
{
  "model_type": "neural_network",
  "accuracy": 0.918,
  "deception_points": [
    "Potential bias in output layer",
    "Unusual activation patterns"
  ],
  "recommendation": "Consider reviewing the model's training data for potential biases",
  "confidence_score": 0.85
}
```

### 2. Deception Detection

Analyze content for potential deception:

```bash
# Analyze text content
curl -X POST "http://localhost:8000/api/v1/detection/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Your text content here",
    "context": "Optional context"
  }'
```

Response:

```json
{
  "probability": 0.342,
  "confidence": 0.89,
  "issues": [
    "Inconsistent narrative",
    "Unusual language patterns"
  ],
  "recommendations": [
    "Review content for consistency",
    "Verify source authenticity"
  ]
}
```

### 3. Literary Vault Integration

#### Get Questions

```bash
# Get questions from a specific category
curl "http://localhost:8000/api/v1/literary-vault/questions/astronomy?limit=5&random=true"
```

Response:

```json
[
  {
    "id": "q123",
    "question": "What is the closest star to Earth?",
    "correct_answer": "The Sun",
    "options": ["The Sun", "Proxima Centauri", "Alpha Centauri", "Sirius"]
  }
]
```

#### Randomize Questions

```bash
# Get randomized questions
curl -X POST "http://localhost:8000/api/v1/literary-vault/questions/randomize" \
  -H "Content-Type: application/json" \
  -d '{
    "category": "astronomy",
    "count": 5,
    "seed": 12345
  }'
```

### 4. Question Analysis

Analyze questions for potential deception:

```bash
# Analyze a set of questions
curl -X POST "http://localhost:8000/api/v1/detection/analyze-questions" \
  -H "Content-Type: application/json" \
  -d '[{
    "id": "q123",
    "question": "What is the closest star to Earth?",
    "correct_answer": "The Sun"
  }]'
```

## Python Client Examples

```python
import httpx
import asyncio

async def analyze_model(file_path: str):
    async with httpx.AsyncClient() as client:
        files = {'file': open(file_path, 'rb')}
        response = await client.post(
            'http://localhost:8000/api/v1/analysis/model',
            files=files
        )
        return response.json()

async def detect_deception(content: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'http://localhost:8000/api/v1/detection/analyze',
            json={'content': content}
        )
        return response.json()

async def get_and_analyze_questions():
    async with httpx.AsyncClient() as client:
        # Get questions
        questions = await client.get(
            'http://localhost:8000/api/v1/literary-vault/questions/astronomy',
            params={'limit': 5}
        )
        
        # Analyze them for deception
        analysis = await client.post(
            'http://localhost:8000/api/v1/detection/analyze-questions',
            json=questions.json()
        )
        return analysis.json()
```

## Development

### Running Tests

```bash
pytest tests/
```

### Local Development

```bash
uvicorn api.main:app --reload
```

### Docker Deployment

```bash
docker build -t ai-deception-framework .
docker run -p 8000:8000 ai-deception-framework
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## API Documentation

Full API documentation is available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Literary Vault API Integration
- OpenAI API Integration
- Contributors and maintainers

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
