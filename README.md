# In My Channels

A web application that enables targeted video search exclusively across your YouTube subscribed channels, providing a focused and personalized content discovery experience.

---

### Features

- **Personalized Search**: Search for videos exclusively within your YouTube subscribed channels
- **Focused Discovery**: Eliminate noise from the broader YouTube ecosystem
- **Clean Interface**: Intuitive, distraction-free user experience
- **Local-First Architecture**: Self-contained application that respects your privacy
- **No Deployment Needed**: Run locally without complex infrastructure requirements

---

### Technology Stack

**Backend**

- **Python**: Core server-side logic with robust data handling capabilities
- **Flask**: Lightweight web framework for efficient API routing
- **Requests**: Simplified HTTP communication with YouTube Data API
- **Pytest**: Comprehensive testing framework

**Frontend**

- **HTML5**: Semantic markup for accessibility and structure
- **CSS3**: Modern styling with responsive design principles
- **Vanilla JavaScript**: Efficient client-side logic without framework overhead

---

### Project Structure

```text
in-my-channels/
├── app.py                   # Flask application entry point
├── pyproject.toml           # Poetry configuration
├── static/                  # Frontend assets
│   ├── css/
│   │   └── style.css        # Application styles
│   └── js/
│       └── main.js          # Client-side functionality
├── templates/
│   └── index.html           # Main application interface
├── tests/                   # Test suite
├── .pre-commit-config.yaml  # Pre-commit hooks
└── .gitignore               # Git exclusion rules
```

0. poetry init
1. poetry add flask requests python-dotenv
2. Estrutura
 mkdir -p static/css static/js templates tests
 touch app.py README.md
 touch static/css/style.css static/js/main.js
 touch templates/index.html
 
---

Project ID (único dentro do Google Cloud)

Credenciais (API key, Client ID, Client Secret)

Redirect URI que você configurar.