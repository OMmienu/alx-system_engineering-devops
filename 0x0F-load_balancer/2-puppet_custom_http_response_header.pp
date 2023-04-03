# Configure HTTP header in a nginx server

# update ubuntu server
exec { 'update server':
  command => 'apt-get update',
  user    => 'root',
  provider => 'shell',
}
->
# install nginx server on a remote server
package { 'nginx':
  ensure   => presnet,
  provider => 'apt'
}
->
# custom Nginx response header
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server:',
  line   => 'add_header by $hostname:'
}
->
# start service
service { 'nginx':
  ensure  => 'running',
  enable  => 'true,
  require => Package['nginx']
}
