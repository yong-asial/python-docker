import sys
import time
def start():
  msg = 'start'
  print(msg + 'print')
  print(msg + 'err', file=sys.stderr)
  print(msg + 'out', file=sys.stdout)
  print('done', file=sys.stderr)
