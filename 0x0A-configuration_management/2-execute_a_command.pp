# Kill process Killmenow

exec { 'pkill':
  command  => 'pkill Killmenow',
  provider => 'shell',
}
