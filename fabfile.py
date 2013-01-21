#!/usr/bin/env python
import secrets
from fabric.api import *
from fabric.colors import red, green, blue

env.user = secrets.env_user
env.password = secrets.env_password
project_root = '/var/www/forum'
apache_conf_path = '/etc/apache2/sites-available'
apache_site_conf = 'default'

git_force_pull = "git fetch --all; git reset --hard origin/master"


@hosts(secrets.env_host)
def deploy():
  local('git push')

  with cd(project_root):
    print blue("\nupdating source from git repo..")
    run(git_force_pull)

    print blue("\nrestarting the apache service..")
    run('service apache2 force-reload')
    run('service apache2 restart')

    print green("app deployed..")


@hosts(secrets.env_host)
def apache_config():
  apache_http_config = 'http.conf'

  with cd(apache_conf_path):
    print blue("\nupdating the contents of the config file..")
    put(apache_http_config, apache_conf_path + '/' + apache_site_conf,
      use_sudo=True)

  print blue("\nrestarting the apache service..")
  run('service apache2 force-reload')
  run('service apache2 restart')

  print green("apache config updated..")


@hosts(secrets.env_host)
def apache_reload():
  run('service apache2 force-reload')
  run('service apache2 restart')
