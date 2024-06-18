from flask import Flask, request, render_template, redirect, url_for
from github import Github

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        token = request.form['token']
        visibility = request.form['visibility']
        g = Github(token)
        user = g.get_user()

        if visibility not in ['public', 'private']:
            return "Invalid visibility choice. Please enter 'public' or 'private'.", 400

        changes = []
        for repo in user.get_repos():
            try:
                if visibility == 'public' and repo.private:
                    repo.edit(private=False)
                    changes.append(f"Changed {repo.name} to public")
                elif visibility == 'private' and not repo.private and not repo.fork:
                    repo.edit(private=True)
                    changes.append(f"Changed {repo.name} to private")
                elif visibility == 'private' and repo.fork:
                    changes.append(f"Skipped {repo.name} (it's a fork)")
                else:
                    changes.append(f"{repo.name} is already {visibility}")
            except Exception as e:
                changes.append(f"Failed to change {repo.name} to {visibility}: {e}")

        return render_template('result.html', changes=changes)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
