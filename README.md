# takasaki
A viewer of machine learning experiments.

## install

```
git clone https://github.com/aphlysia/takasaki.git
cd takasaki
python setup.py install
```

or

```
pip install takasaki
```


### requirements

- bottle

## example

```
cd example
python -m takasaki sample_net
```

then access http://localhost:8888/, and you will see a graph. Each node represents an expriment. Each edge represents parent-child relationship of experiments. If you click an edge, new window will open, and you will see the difference of the parent and the child.

