name-expansion
==============

Name expansion is tool to expand string between '[]' and '{}'

Example:
- [1-3]str -- 1str, 2str, 3str
- [2,5,7]str -- 2str, 5str, 7str
- [tw,hk,us]str -- twstr, hkstr, usstr

Use case, ::

  >>> ne = NameExpansionCore()
  >>> host = '[tw,hk][1-2].host[3,5].com'
  >>> host_list = list([host])
  >>> for match in ne.parse(host):
  ...   host_list = ne.expand(match, host_list)
  >>> host_list
  ['tw1.host3.com', 'hk1.host3.com', 'tw1.host5.com', 'hk1.host5.com', 'tw2.host3.com', 'hk2.host3.com', 'tw2.host5.com', 'hk2.host5.com']
