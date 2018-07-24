from linebot.models import (
    TextSendMessage, ImageSendMessage,
)

def create_message(input):
    # 1. 固定メッセージを返す
    message = TextSendMessage(text = 'Hack Time!')

    return message
