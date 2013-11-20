from hipchat.connection import partial, call_hipchat, HipChatObject

class Room(HipChatObject):
    sort = 'room'


class Message(HipChatObject):
    sort = 'message'


class MessageSentStatus(HipChatObject):
    sort = 'status'
    def __init__(self, jsono):
        self.jsono = jsono
        self.status = jsono.get('status')


Room.history = \
    classmethod(partial(call_hipchat, 
                        ReturnType=lambda x: map(Message, map(lambda y: {'message': y}, x['messages'])), 
                        url="rooms/history", 
                        data=False))
Room.list = \
    classmethod(partial(call_hipchat, 
                        ReturnType=lambda x: map(Room, map(lambda y: {'room': y}, x['rooms'])), 
                        url="rooms/list", 
                        data=False))

Room.create = classmethod(
    partial(call_hipchat, Room, url="rooms/create", data=True)
)
Room.topic = classmethod(
    partial(call_hipchat, ReturnType=lambda x: x['status'], url="rooms/topic", data=True)
)

Room.message = classmethod(partial(call_hipchat, ReturnType=MessageSentStatus, url="rooms/message", data=True))
Room.show = classmethod(partial(call_hipchat, Room, url="rooms/show", data=False))
