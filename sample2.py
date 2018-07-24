from linebot.models import (
    TextSendMessage, ImageSendMessage,
)

def create_message(input):
    # 2. オウム返し(+文字列結合)
    reply = input + '、と言いましたね？'
    message = TextSendMessage(text = reply)

    return message
