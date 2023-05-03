# Creates a custom HTTP header response in Nginx

exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}

file_line { 'header':
  ensure => 'present'
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-served-By $HOSTNAME;',
}

exec { 'restart Nginx':
  command => 'sudo service nginx restart',
}
