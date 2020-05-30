import os
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
import todatabase
import datetime
from datetime import date,datetime
import time
import calendar
from linebot.exceptions import InvalidSignatureError, LineBotApiError
import sys
import mysql.connector
users=['<User You are going to sent>']  
def notice():
    destclass=["<Class are going to find>"]
    output="體溫警示：\n\n"
    for i in destclass:
        flag=0
        lssh1 = mysql.connector.connect(
        host = todatabase.host(),
        port = "3306",
        user = todatabase.username(),
        password = todatabase.password(),
        database= i,)
        gcpsql= lssh1.cursor()
        sql_select_Query = """select stu_id,morning,evening from body_temperture WHERE morning IS NOT NULL"""
        #targetclass=destclass[0]+'.'+'body_temperture'
        #target=targetclass
        gcpsql.execute(sql_select_Query)
        records=gcpsql.fetchall()
        output+=i[4]+i[5]+i[6]+" 班\n"
        for row in records:
            if(row[1]>=37.5): 
                flag=1
                output+=i[4]+i[5]+i[6]+str(row[0])+" "+str(row[1])+"\n"
        if(flag==0): output+="本日無異常體溫\n"
        output+="\n"
    return output
def push():
    channel_access_token='Your LINE Channel Access Token'
    line_bot_api = LineBotApi(channel_access_token)    
    output=notice()
    a=len(users)
    #print(a)
    for i in range (0,a):
        user=users[i]
        line_bot_api.push_message(user, TextSendMessage(text=output))