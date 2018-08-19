import os, json, subprocess, tempfile, argparse, importlib
import bottle
from bottle import route, run, view, HTTPResponse
import takasaki
bottle.TEMPLATE_PATH.insert(0,
  os.path.join(list(takasaki.__path__)[0], 'views'))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('netpy',
    help='network definition python file')
  parser.add_argument('--port', default=8888)
  parser.add_argument('--width', default=800)
  parser.add_argument('--height', default=600)
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
      width=args.width,
      height=args.height,
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
