from github import Github
import os

gh = Github(os.getenv("GITHUB_TOKEN"))

def open_pr(repo, branch, title, body):
    r = gh.get_repo(repo)
    return r.create_pull(title=title, body=body, head=branch, base="main")
