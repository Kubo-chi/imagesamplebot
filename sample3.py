from linebot.models import (
    TextSendMessage, ImageSendMessage,
)

import random

def create_message(input):
    # 3. 条件分岐あり
    janken = ['グー', 'チョキ', 'パー']
    if input not in janken:
        message = TextSendMessage('グー・チョキ・パーのどれかを入力してね')
    else:
        reply = random.choice(janken)
        message = TextSendMessage(reply)

    return message
