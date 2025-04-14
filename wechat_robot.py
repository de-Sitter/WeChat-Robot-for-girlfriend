import requests
import time
import PyOfficeRobot
from PyOfficeRobot.core.WeChatType import WeChat
import re

wx=WeChat()
wx.ChatWith("Your Girlfriend's WeChat ID") #写入你女朋友的微信号
while True:
    news=wx.GetAllMessage[-1]
    print(news)
    person,message,times=news
    if person=="Yourself WeChat ID":
        time.sleep(60)  #如果检测到最后一条消息是你自己的话就等待60秒，因为此时女朋友还没有发消息，60秒后再检测更新，如果女朋友发消息比较频繁也可以缩短采样时间
    else:
        k=1
        while True:
            newss=wx.GetAllMessage[-k]
            persons,messages,timess=newss
            if persons=="Yourself WeChat ID":
                break
            else:
                k+=1  #监测女朋友发了多少条消息
        messagee=[]
        for i in range(k-1,0,-1):
            a,messagel,c=wx.GetAllMessage[-i]
            messagee.append(messagel)

        message=",".join(messagee)  #把所有女朋友发的消息拼接成一段文本
        print(message)
        response = requests.post(
            url="https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": "Bearer your_api_key"},  # 替换为你的API密钥
            json={"messages": [{"role": "user", "content": 
                    f'以下是我接收到的女朋友的微信消息，请你以她男朋友的身份给予无微不至和温暖贴心的回复，每条消息之间用句号分隔，不要生成表情，直接回复就行：{message}'}], #提示词可以自行修改以便符合你女朋友的性格
                "model":"deepseek-chat"}) #这里以deepseek为例，也可以选择其他的大模型
        reply=response.json()["choices"][0]["message"]["content"]
        print(reply)
        replys=re.split(r'[。]',reply) #将deepseek生成的文本分解为多条消息，逐一发送
        replys.append('')  #在最后添加一个空字符串，以便在循环中判断结束条件
        print(replys)
        t=0
        while True:
            if replys[t]=='':
                break
            else:
                PyOfficeRobot.chat.send_message(who="Your Girlfriend's WeChat ID", message=replys[t])  #将消息发送给女朋友
                print(replys[t])
                t+=1






    




    

    



    
