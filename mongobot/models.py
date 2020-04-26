from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern


class MessageFilter(MongoModel):
    name = fields.CharField()
    text = fields.CharField()
    exclude = fields.BooleanField()
    full_text = fields.BooleanField()

    class Meta:
        connection_alias = 'mongobot'
        write_concern = WriteConcern(j=True)

class Message(MongoModel):
    name = fields.CharField()
    message_filter = fields.ReferenceField(MessageFilter)
    handler = fields.CharField()

    class Meta:
        connection_alias = 'mongobot'
        write_concern = WriteConcern(j=True)

class Command(MongoModel):
    name = fields.CharField()
    command = fields.CharField()
    handler = fields.CharField()

    class Meta:
        connection_alias = 'mongobot'
        write_concern = WriteConcern(j=True)


