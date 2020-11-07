from django.db import models

class Conversation(models.Model):
    def getMessageList(self):
        return "oof"

class Message(models.Model):
    sender_id = models.Charfield(max_length=10)
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

#class Student