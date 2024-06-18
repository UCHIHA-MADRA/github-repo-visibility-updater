## About the Project

The **GitHub Repo Visibility Updater** is a web application built with Flask that allows users to change the visibility of all their GitHub repositories to either public or private based on their choice. The app provides a user-friendly interface to manage repository visibility and skips public forks when changing repositories to private.

### Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [PyGithub](https://github.com/PyGithub/PyGithub)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.x
- GitHub Personal Access Token with `repo` and `admin:repo_hook` scopes

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/github-repo-visibility-updater.git
   ```
2. Navigate to the project directory:

```
    cd github-repo-visibility-updater
```

3.  Set up a virtual environment:

```
python -m venv venv
```

`source venv/bin/activate `

# On Windows use

`venv\Scripts\activate` 4. Install the required Python packages:

```
pip install Flask PyGithub

```

5.  Usage
    Replace 'your_token_here' in app.py with your actual GitHub Personal Access Token.

6.  Run the Flask app:

`python app.py`

Open your web browser and navigate to http://127.0.0.1:5000/.
