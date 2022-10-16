# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
客製化選單FlexSendMessage
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Hh9PN5m7XEyQ7hACpPL1EkpKHMEWCwylIJQ2V/iJGiWUBzw1dTwR2JHEKmeFud7phMRqc7lEPuP7+fdd743dYBweufZAfpJ7IU/xSPlRg1LQkYvQwXksQ4r3cXMSLOscc0e5X6D1XWlTtE+bnzR/JwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('082ad3a7c3851408e789a38d7f2f0611')

line_bot_api.push_message('U28c064145d710b5cd528317faa2e1827', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('選單',message):
        # Flex Message Simulator網頁：https://developers.line.biz/console/fx/
        flex_message = FlexSendMessage(
            alt_text='賴衣櫥',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip2.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Your closet",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://cdn-icons-png.flaticon.com/512/114/114829.png",
                        "size": "lg"
                      },
                      {
                        "type": "text",
                        "text": "Go",
                        "color": "#000000",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#9C8E7Ecc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://images.pexels.com/photos/2249248/pexels-photo-2249248.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "bottom",
            "align": "end",
            "position": "absolute",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Nearby thrift shops",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://cdn-icons-png.flaticon.com/512/126/126122.png"
                      },
                      {
                        "type": "text",
                        "text": "Go",
                        "color": "#000000",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#9C8E7Ecc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://images.pexels.com/photos/3873488/pexels-photo-3873488.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "bottom",
            "align": "start",
            "position": "absolute",
            "offsetStart": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Rewards",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://cdn-icons-png.flaticon.com/512/548/548427.png"
                      },
                      {
                        "type": "text",
                        "text": "Go",
                        "color": "#000000",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#9C8E7Ecc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('無法辨識'))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)