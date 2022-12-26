from flask import Flask, json, request, jsonify
from datetime import datetime
import sys
import os
import datetime
import pandas as pd

app = Flask(__name__)

menuData = pd.read_csv("./table.csv", header=None, encoding="utf=8")

def get_img_content(coding='utf-8'):
    with open('./TodayPicture/TodayMenu.png', 'rb') as f:
        img_data = base64.b64encode(f.read()).decode(coding)
        return img_data


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        'type': 'buttons',
        'buttons': ['아무것도아님']
    }
    return jsonify(dataSend)

@app.route('/test', methods=['GET'])
def Test():
    return "hello"

@app.route('/message', methods=['POST'])
def Message():
    req = request.get_json()
    content = req["userRequest"]["utterance"]
    content = content.replace("\n", "")
    print(content)
    id_value = req["userRequest"]["user"]["id"]
    block_value = req["userRequest"]["block"]["id"]
    
    today={0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
    
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    price = "가격은 점심 : 5,500원\n천원의 밥상 : 1,000원";
    opening = "평일 11:00 ~ 14:00\n(토·일요일 및 공휴일 제외)"
    dayweek = datetime.datetime.today().weekday()
    # print(content)
    if content == "월요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[0][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "화요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[1][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "수요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[2][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "목요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[3][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "금요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[4][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "얼마야?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "가격정보",
                                    "description": price
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "언제 운영해?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "운영 시간",
                                    "description": opening
                                }
                            ]
                        }
                    }
                ],
            
            "quickReplies": [
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    elif content == "어디에 있어?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                {
                    "basicCard": {
                    "title": "광운대학교 함지마루",
                    "description": "복지관 3층",
                    "thumbnail": {
                        "imageUrl": "https://www.kw.ac.kr/KWData/webeditor/2020/2020_05_29_102245.jpg"
                    },
                    "profile": {
                        "imageUrl": "https://www.kw.ac.kr/KWData/webeditor/2020/2020_05_29_102245.jpg",
                        "nickname": "광운대학교"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "지도로 보기",
                        "webLinkUrl": "http://kko.to/dGDsPiDKJ"
                        }
                    ]
                    }
                }
                ],"quickReplies": [
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              }
            ]
            }
        }
        
    elif content == "내일 밥은?":
        if dayweek==6:
            dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "다음 주 식단은 아직 안나왔어요:)"
                    }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
        elif dayweek >=4:
            dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "내일은 휴무일입니다:)"
                    }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
        else :
            dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": today[dayweek+1] + " 메뉴",
                                    "description": menuData[dayweek+1][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }
            ]
            }
        }
    elif content == "이번 주 식단은?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "메뉴를 눌러주세요"
                    }
                }],
                "quickReplies": [
                    {
                        "action": "message",
                        "label": "월요일 메뉴",
                        "messageText": "월요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "화요일 메뉴",
                        "messageText": "화요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "수요일 메뉴",
                        "messageText": "수요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "목요일 메뉴",
                        "messageText": "목요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "금요일 메뉴",
                        "messageText": "금요일 메뉴"
                    }
                ]
            }
        }
    elif content == "오늘 밥은?":
        if dayweek >=5:
            dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "오늘은 휴무일입니다:)"
                    }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
        else :
            dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": today[dayweek] + " 메뉴",
                                    "description": menuData[dayweek][1]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "잘못된 입력입니다. 메뉴가 궁금하시면 다음버튼을 눌러주세요"
                        }
                    }],
                "quickReplies": [
                {
                   "action": "message",
                   "label": "언제 운영해?",
                   "messageText": "언제 운영해?"
              },
              {
                   "action": "message",
                   "label": "이번 주 식단은?",
                   "messageText": "이번 주 식단은?"
              },
                {
                   "action": "message",
                   "label": "오늘 밥은?",
                   "messageText": "오늘 밥은?"
              },
              {
                   "action": "message",
                   "label": "내일 밥은?",
                   "messageText": "내일 밥은?"
              },
              {
                   "action": "message",
                   "label": "얼마야?",
                   "messageText": "얼마야?"
              },
              {
                   "action": "message",
                   "label": "어디에 있어?",
                   "messageText": "어디에 있어?"
              }

            ]
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)