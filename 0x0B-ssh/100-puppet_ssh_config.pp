#!/usr/bin/env bash
# connect with puppet

file_line { 'Use private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn_off_password_auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
