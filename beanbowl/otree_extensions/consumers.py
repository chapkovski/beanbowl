from channels.generic.websockets import JsonWebsocketConsumer
from beanbowl.models import Constants, Group
import json


class BubbleTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/bubbletracker/(?P<group_pk>[0-9]+)$')

    def clean_kwargs(self):
        self.group_pk = self.kwargs['group_pk']

    def connection_groups(self, **kwargs):
        group_name = self.get_group().get_channel_group_name()
        return [group_name]

    def connect(self, message, **kwargs):
        print('someone connected')

    def disconnect(self, message, **kwargs):
        print('someone disconnected')

    def get_group(self):
        self.clean_kwargs()
        return Group.objects.get(pk=self.group_pk)

    def receive(self, text=None, bytes=None, **kwargs):
        group = self.get_group()
        print(text)
        print('====')
        updated_bubbleset = text['bubbleset']
        group.bubbleset = json.dumps(updated_bubbleset)
        group.save()
        self.group_send(group.get_channel_group_name(), {'updated_bubbleset': updated_bubbleset})
