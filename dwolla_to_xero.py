#!/usr/bin/env python

import csv
with open('input.csv', 'r') as read_file:
  with open('test.csv', 'w') as write_file:
      a = csv.writer(write_file, delimiter=',')
      data = [['Me', 'You'],
              ['293', '219'],
              ['54', '13']]
      a.writerows(data)
