# execute pkill command to kill bashscript file killmenow

exec { 'killmenow':
  command => 'pkill -9 -f killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
