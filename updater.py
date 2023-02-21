import git
from settings import settings

def update():
  if(settings.updater.BETA):
    print('Development mode enabled')
    print('Updating from dev branch...')
    repo_path = '.'
    repo = git.Repo(repo_path)
    # Set the remote URL to use the personal access token
    repo.git.remote('set-url', 'origin', 'https://github.com/Carter2565/Python-Database.git')
    repo.git.fetch()
    repo.git.checkout('BETA')
    repo.git.reset('--hard', 'origin/BETA')
    # print('Restart required to use updated files')


  else:
    print('Development mode not enabled')
    print('Updating from main branch...')
    repo_path = '.'
    repo = git.Repo(repo_path)
    # Set the remote URL to use the personal access token
    repo.git.remote('set-url', 'origin', 'https://github.com/Carter2565/Python-Database.git')
    repo.git.fetch()
    # repo.git.checkout('main')
    repo.git.reset('--hard', 'origin/main')
    # print('Restart required to use updated files')