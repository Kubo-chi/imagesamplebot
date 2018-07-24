import json
#from urllib import urlopen
#import requests
from os import path
import os
from linebot.models import (
    TextSendMessage, ImageSendMessage,
)


def create_message(input):
    # スタンプ
    #1,1の場合を作る！
    message=""
    if input=="あ":
        #message=TextSendMessage('わかりました')

        fout = open(url,"w")
        fout.write("あああ")

        message=TextSendMessage("あ")
        fout.close()

    else:
        message=TextSendMessage('はい')
    return message

def create_messageforsticker(inputpackageid,stickerid):
    message=""
    #NOスタンプ
    if inputpackageid=="2" and stickerid=="39":

        message=TextSendMessage('わかりました。きっぱり断ります')


    #sorryスタンプ
    elif inputpackageid=="2" and stickerid=="38":
        message=TextSendMessage('わかりました。やんわり断ります')
    else:
        message=TextSendMessage('対応なし')
    return message
