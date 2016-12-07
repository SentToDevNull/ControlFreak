import sys
from twisted.web.static import File
from twisted.python import log
from twisted.web.server import Site
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol
from autobahn.twisted.resource import WebSocketResource
from turn_lights import Light

# This will be the files latest_coords
# TODO: we should put all of these (latest_coords, button_pushed etc.)
# in a single class called UI (or something like that)
latest_coords = [0, 0]


# This is a websocket server protocol
# It tells us what to do when we receive a websocket request
class SomeServerProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        # Every time a websocket handshake takes place
        # (Currently, just logs the details of request)
        print("Connection {}".format(request))

    def onMessage(self, payload, isBinary):
        # Currently the payload comes in the format:
        # "coords: 0.6 0.4"
        string = payload.decode('utf8')
        newPower = float(string.split(" ")[1]) * 100
        print("Power", newPower)
        latest_coords[0] = newPower

    def onOpen(self):
        print("something opened")


class MainServer:
    def runReactor(self):
        log.startLogging(sys.stdout)

        # static file server seving index.html as root
        # Everything in /client will be served normally
        root = File("./client")

        # Set up a websocket server
        factory = WebSocketServerFactory(u"ws://127.0.0.1:9999")
        factory.protocol = SomeServerProtocol
        resource = WebSocketResource(factory)
        # websockets resource on "/ws" path
        root.putChild(b"ws", resource)

        site = Site(root)
        # Listen for TCP requests on port 9999
        reactor.listenTCP(9999, site)
        l = Light()
        LoopingCall(l.loop, latest_coords).start(0)
        reactor.run()


if __name__ == "__main__":
    m = MainServer()
    m.runReactor()
