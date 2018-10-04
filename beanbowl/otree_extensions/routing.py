from channels.routing import route_class
from .consumers import BubbleTracker

channel_routing = [
    route_class(BubbleTracker, path=BubbleTracker.url_pattern),
]
