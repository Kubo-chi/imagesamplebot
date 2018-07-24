from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
import codecs

def yomiage_message():
    session = Session(region_name="us-west-2")
    polly = session.client("polly")
    try:
        f=codecs.open('data.txt','r','utf-8')
        contents=f.read()
        response = polly.synthesize_speech(Text=contents, OutputFormat="mp3", VoiceId="Mizuki")
        f.close()
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = "speech.mp3"
            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
            print("synthesize_speech OK ->>" + output)
    else:
        print("Could not stream audio")
        sys.exit(-1)
