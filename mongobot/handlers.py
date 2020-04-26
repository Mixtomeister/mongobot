import random

RESPONSES = ['jajaja', 'que bueno', 'xd', 'que cojones xd', 'jaja', 'xddd', 'me parto xd']


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mmmm...Hola buenas!")

def response(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(RESPONSES))