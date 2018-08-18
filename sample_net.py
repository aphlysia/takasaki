nodes = {
  1: {'id': 1, 'label': 'a.py', 'goodness': 10},
  2: {'id': 2, 'label': 'b.py', 'goodness': 20},
  3: {'id': 3, 'label': 'c'},
  4: {'id': 4, 'label': 'd'},
}

edges = (
  {'from': 1, 'to': 2, 'arrows':'to', 'label': 'use variable'},
  {'from': 2, 'to': 3, 'arrows':'to', 'label': 'make directory'},
  {'from': 3, 'to': 4, 'arrows':'to', 'label': 'add log'},
)
