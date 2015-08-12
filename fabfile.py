from fabric.api import local


def create_django_app():
	local('virtualenv env')
	local('source ./env/bin/activate')
	
def install_django():
	local('pip install django')

def start_project(project_name):
	local('django-admin.py startproject %s' %project_name)

def source_controll_with_git():
	local('git init')
	local('git add .')

def git_commit(comment):
	local('git commit -a -m %s' %comment)

def deploy():
	local('python manage.py test msee_app')
	local('git add -p && git commit')
	local('git checkout master && git merge ' + 'development')

def git_pull():
	"updates a repository."
	local('git pull https://github.com/CostaRegi/Msee.git development')
