# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 21:37:37 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第三章 互動回傳功能
推播push_message與回覆reply_message
"""
from linebot import LineBotApi
from linebot.models import TextSendMessage
import time

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Hh9PN5m7XEyQ7hACpPL1EkpKHMEWCwylIJQ2V/iJGiWUBzw1dTwR2JHEKmeFud7phMRqc7lEPuP7+fdd743dYBweufZAfpJ7IU/xSPlRg1LQkYvQwXksQ4r3cXMSLOscc0e5X6D1XWlTtE+bnzR/JwdB04t89/1O/w1cDnyilFU=')
# 請填入您的ID
yourID = 'U28c064145d710b5cd528317faa2e1827'
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='安安您好！早餐吃了嗎？'))
# 用迴圈推播訊息
for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)