import os

from fabric.api import local

def staticfiles():
    BASE_PATH = os.path.dirname(__file__)
    local('lessc %s/media/css/style.less %s/media/css/style.css' % (BASE_PATH, BASE_PATH))
    local('coffee -c %s/media/js/script.coffee' % BASE_PATH)
    try:
        local('hg commit -m "Autocommit by [fab staticfiles]"')
        local('hg push')
    except:
        pass
    local('%s/manage.py collectstatic' % BASE_PATH)

def deployall():
    staticfiles()
    deployapp()

def deployapp():
    local('hg push')
    local('hg push-heroku')