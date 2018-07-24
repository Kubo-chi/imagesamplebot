from linebot.models import (
    TextSendMessage, ImageSendMessage,
)

def create_message(input):
    # 4. 画像
    message = ImageSendMessage(
        preview_image_url = 'https://hacku-line-bot.herokuapp.com/images/question.png',
        original_content_url = 'https://hacku-line-bot.herokuapp.com/images/answer.png'
    )

    return message
