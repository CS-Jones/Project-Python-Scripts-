import falcon
import waitress
import json

fileCorpus = []

for line in open('sampleTweetsTime.json'):
    fileCorpus.append(json.loads(line))

fileCorpus2 = []

for line in open('twitDBa.json'):
    fileCorpus2.append(json.loads(line))

class HelloWorldResource:
    def on_post(self, req, resp):
        content = req.stream.read().decode()
        if content == 'getAll':
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.body = json.dumps(fileCorpus)
        elif content == 'getAll2':
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.body = json.dumps(fileCorpus2)  
        else:
            resp.status = falcon.HTTP_404


if __name__ == '__main__':
    api = falcon.API()
    api.add_route('/helloworld', HelloWorldResource())
    waitress.serve(api, host="0.0.0.0", port=8081, threads=4)