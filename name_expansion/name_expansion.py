#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Hans Liu
Backyard: hcliu
'''

import re

class NameExpansionCore(object):
  '''
  The NameExpansionCore is tool to expand string between '[]' and '{}'

  example,
  [1-3]str -- 1str, 2str, 3str
  [2,5,7]str -- 2str, 5str, 7str
  [tw,hk,us]str -- twstr, hkstr, usstr

  >>> ne = NameExpansionCore()
  >>> host = '[tw,hk][1-2].host[3,5].com'
  >>> host_list = list([host])
  >>> for match in ne.parse(host):
  ...   host_list = ne.expand(match, host_list)
  >>> host_list
  ['tw1.host3.com', 'hk1.host3.com', 'tw1.host5.com', 'hk1.host5.com', 'tw2.host3.com', 'hk2.host3.com', 'tw2.host5.com', 'hk2.host5.com']
  '''
  def __init__(self):
    pass

  def parse(self, text):
    '''
    Keyword arguments:
    text -- the string which want to parse

    >>> NameExpansionCore().parse('tw[1,2].host[1-3,5].com')
    ['[1,2]', '[1-3,5]']

    >>> NameExpansionCore().parse('tw{1,2}.host{1-3,5}.com')
    ['{1,2}', '{1-3,5}']

    >>> NameExpansionCore().parse('[tw,hk].host.[com]')
    ['[tw,hk]', '[com]']

    >>> NameExpansionCore().parse('{tw,hk}.host.{com}')
    ['{tw,hk}', '{com}']
    '''
    match_list = []
    # fp dataset
    fp_list = [
    '\[\d+[,\-\d]*\d+\]',
    '\{\d+[,\-\d]*\d+\}',
    '\[\w+[A-Za-z][,\w]*\]',
    '\{\w+[A-Za-z][,\w]*\}'
    ]
    # parse data
    for fp in fp_list:
      match_list.extend(re.findall(fp, text))
    return match_list

  def expand(self, match, data_list):
    '''
    Keyword arguments:
    match -- the pattern which find by regular expression
    data_list -- the string list which want to expand

    >>> NameExpansionCore().expand('[1-3,5]', ['tw.host[1-3,5].com'])
    ['tw.host1.com', 'tw.host2.com', 'tw.host3.com', 'tw.host5.com']

    >>> NameExpansionCore().expand('{1-3,5}', ['tw.host{1-3,5}.com'])
    ['tw.host1.com', 'tw.host2.com', 'tw.host3.com', 'tw.host5.com']

    >>> NameExpansionCore().expand('[tw,hk]', ['[tw,hk].host.com'])
    ['tw.host.com', 'hk.host.com']

    >>> NameExpansionCore().expand('{tw,hk}', ['{tw,hk}.host.com'])
    ['tw.host.com', 'hk.host.com']
    '''
    expand_list = []
    # expand data
    for data in data_list:
      for item in match[1:len(match)-1].split(','):
        if '-' in item:
          seq = item.split('-')
          for i in range(int(seq[0]), int(seq[1]) + 1):
            expand_list.append(data.replace(match, str(i)))
        else:
          expand_list.append(data.replace(match, item))
    return expand_list

def main():
  import doctest
  doctest.testmod()
  pass

if __name__ == '__main__':
  main()
