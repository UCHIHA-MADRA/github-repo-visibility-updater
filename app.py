from flask import Flask, redirect, url_for, session, render_template, request, flash
from authlib.integrations.flask_client import OAuth
import os
import requests

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_secret_key')

# OAuth configuration
oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id='your_github_client_id',
    client_secret='your_github_client_secret',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    client_kwargs={'scope': 'user repo'},
)

@app.route('/')
def repo_visibility():
    if 'token' not in session:
        return redirect(url_for('login'))
    
    headers = {
        'Authorization': f"token {session['token']['access_token']}",
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    repos = response.json()
    github_username = session['github_username']  # Assuming you store GitHub username in session
    return render_template('repo_visibility.html', repos=repos, github_username=github_username)

@app.route('/start_github_login')
def start_github_login():
    redirect_uri = url_for('authorized', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/login/authorized')
def authorized():
    token = github.authorize_access_token()
    session['token'] = token
    # Assuming you retrieve and store GitHub username here
    session['github_username'] = get_github_username(token)
    return redirect(url_for('repo_visibility'))

# Example function to retrieve GitHub username from GitHub API
def get_github_username(token):
    headers = {
        'Authorization': f"token {token['access_token']}",
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        return response.json()['login']
    else:
        return 'GitHub User'

if __name__ == '__main__':
    app.run(debug=True)
