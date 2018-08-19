import json, subprocess, tempfile, argparse, importlib
from bottle import route, run, view, HTTPResponse

parser = argparse.ArgumentParser()
parser.add_argument('netpy',
                    help='network definition python file')
parser.add_argument('--port', default=8888)
args = parser.parse_args()

netpy = importlib.import_module(args.netpy)

def nodes2json(nodes):
  return json.dumps([nodes[k] for k in nodes])

@route('/')
@view('graph')
def graph():
  return dict(
    nodes=nodes2json(netpy.nodes),
    edges=json.dumps(netpy.edges),
  )

@route('/diff/<from_node>/<to_node>')
def diff(from_node, to_node):
  with tempfile.TemporaryFile() as buff:
    subprocess.call(['diff', '-uprN',
      netpy.nodes[int(from_node)]['label'],
      netpy.nodes[int(to_node)]['label']], stdout=buff)
    buff.seek(0)
    diff = buff.read().decode('utf-8')
  r = HTTPResponse(status=200, body=diff)
  r.set_header('Content-Type', 'text/plain')
  return r

run(host='localhost', port=args.port, debug=True)
