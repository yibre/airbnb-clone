from django.db import models
from core import models as core_models

# Create your models here.
class Conversation(core_models.TimeStampedModel):
    """ Conversation Model Definition """

    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        #return str(self.created)
        # conversation을 만들었는데 이게 list로 들어감 > str 로 들어갔는데 이게 str이 아님
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ",".join(usernames) # str method

    def count_messages(self):
        return self.messages.count() # message는 conversation foreignkey를 가지고 있고 related name은 messages임
    
    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()
    
    count_participants.short_description = "Number of Participants"

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )
    # message는 conversation foreignkey를 가지고 있고 related name은 messages임
    def __str__(self):
        return f"{self.user} says: {self.message}"