import cloudscraper
from datetime import date,timedelta
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup as bs 
import requests


def week():
    for i in range(3,8):
        tomorrow = date.today() + timedelta(days=float(i))
        day_week = tomorrow.strftime('%A')

        error = -1
        while True:
            scraper = cloudscraper.create_scraper()
            r = scraper.get("https://www.investing.com/economic-calendar/",timeout = 10)
            if r.status_code != 200:
                sleep(500)
                continue
            
            high_json = {
        
        "embeds": [
            {
            
            "title": "__***"+day_week+" "+str(tomorrow)+"***__   :star::star::star:",
            "color": 16711680,
            "fields": [
                
            ]
            }
        ],
        "username": "Economic Calendar",
        "attachments": []
        }
            if day_week == "Monday":
                high_json["content"] = "@everyone **NEXT WEEK NEWS**"
            
            
            headers = {
                'authority': 'www.investing.com',
                'accept': '*/*',
                'accept-language': 'it-IT,it;q=0.9',
                'origin': 'https://www.investing.com',
                'referer': 'https://www.investing.com/economic-calendar/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            payload = {
                'country[]': [
                    '25',
                    '32',
                    '6',
                    '37',
                    '72',
                    '22',
                    '17',
                    '39',
                    '14',
                    '10',
                    '35',
                    '43',
                    '56',
                    '36',
                    '110',
                    '11',
                    '26',
                    '12',
                    '4',
                    '5',
                ],
                'dateFrom': tomorrow,
                'dateTo': tomorrow,
                'timeZone': '16',
                'timeFilter': 'timeRemain',
                'limit_from': '0',
            }

            r = scraper.post("https://www.investing.com/economic-calendar/Service/getCalendarFilteredData",data=payload, headers=headers, timeout = 10)
            
            if r.status_code != 200:
                sleep(10)
                continue
            
            else:
                response = r.json()
                
                data = bs(response["data"], 'lxml')
                
                for i in data.find_all("tr"):
                    
                    try:
                        
                        for x in i.find_all("td"):
                            
                            
                            if "flagCur" in x["class"]:
                                country = x.find("span")["title"]
                            
                            if "event" in x["class"]:
                                event = x.text.rstrip().lstrip()
                                
                                
                            if "sentiment" in x["class"]:
                                importance = x["data-img_key"]
                                
                            if "js-time" in x["class"]:
                                time = x.text
                            
                            if "fore" in x["class"]:
                                forecast = x.text
                            
                            if "prev" in x["class"]:
                                previous = x.text
            
                                

                        if importance == "bull3":
                            dict_add = {}
                            dict_add["name"] ="**"+country+" "+event+"**"
                            dict_add["value"] = "> Time: *"+time+"*\n> Forecast: "+ forecast+" Previous: "+previous
                            high_json["embeds"][0]["fields"].append(dict_add)
                
                                        
                    except:
                        if ("country" in locals()) and ("importance" not in locals()):
                            for x in i.find_all("td"):
                                if "event" in x["class"]:
                                    event = x.text.rstrip().lstrip()
                            time = " "
                            forecast = " "
                            previous = " "

                            dict_add = {}
                            dict_add["name"] ="**"+" "+event+"**"
                            dict_add["value"] = "> Holiday"
                            high_json["embeds"][0]["fields"].append(dict_add)
                        
                        else:
                            error = error+1
                
                
                
                
                dict_err = {}
                dict_err["text"] = "Encountered "+str(error)+" errors"
                high_json["embeds"][0]["footer"] = dict_err
                
                del country, importance, time, forecast, previous, event

                
                
                while True:
                    webhook = "INSERT_WEBHOOK_HERE"
                    send = requests.post(webhook,json=high_json)
                    if send.status_code == 204:
                        sleep(10)
                        break
                    if send.status_code == 400:
                        error_json = {
                                "content": "error sending data",
                                "attachments": []
                                }
                        send = requests.post(webhook,json=error_json)
                        break
                    else:
                        sleep(10)
                break
        
    
    

while True:


    while True:
            

            now = datetime.now()
            hh_mm_now = str(now.strftime("%H:%M"))
            if hh_mm_now == "18:30":
                break

            else:
                print("WAITING...")
                sleep(30)




    error = -1
    
    tomorrow = date.today() + timedelta(days=1)
    day_week = tomorrow.strftime('%A')

    if day_week == "Saturday":
        week()
        sleep(60)
        continue
    
    
    if day_week == "Sunday":
        continue
    
    scraper = cloudscraper.create_scraper()
    r = scraper.get("https://www.investing.com/economic-calendar/",timeout = 10)
    if r.status_code != 200:
        sleep(500)
        continue

    
    high_json = {
  "content": "@everyone",
  "embeds": [
    {
      "title": "__***HIGH IMPACT NEWS***__   :star::star::star:",
      "description": "**"+day_week+" "+str(tomorrow)+"**",
      "color": 16711680,
      "fields": [
        
      ],
      "image": {
        "url": "https://media.discordapp.net/attachments/1034758586531844108/1036318003127648276/unknown.png"
      }
    }
  ],
  "username": "Economic Calendar",
  "attachments": []
}

    headers = {
        'authority': 'www.investing.com',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9',
        'origin': 'https://www.investing.com',
        'referer': 'https://www.investing.com/economic-calendar/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    payload = {
        'country[]': [
            '25',
            '32',
            '6',
            '37',
            '72',
            '22',
            '17',
            '39',
            '14',
            '10',
            '35',
            '43',
            '56',
            '36',
            '110',
            '11',
            '26',
            '12',
            '4',
            '5',
        ],
        'dateFrom': tomorrow,
        'dateTo': tomorrow,
        'timeZone': '16',
        'timeFilter': 'timeRemain',
        'limit_from': '0',
    }
    
    r = scraper.post("https://www.investing.com/economic-calendar/Service/getCalendarFilteredData",data=payload, headers=headers, timeout = 10)
    
    if r.status_code != 200:
        sleep(500)
        continue
    
    else:
        response = r.json()
        
        data = bs(response["data"], 'lxml')
        
        for i in data.find_all("tr"):
            
            try:
                
                for x in i.find_all("td"):
                    
                    
                    if "flagCur" in x["class"]:
                        country = x.find("span")["title"]
                    
                    if "event" in x["class"]:
                        event = x.text.rstrip().lstrip()
                        
                        
                    if "sentiment" in x["class"]:
                        importance = x["data-img_key"]
                           
                    if "js-time" in x["class"]:
                        time = x.text
                    
                    if "fore" in x["class"]:
                        forecast = x.text
                    
                    if "prev" in x["class"]:
                        previous = x.text
    
                        

                if importance == "bull3":
                    dict_add = {}
                    dict_add["name"] ="**"+country+" "+event+"**"
                    dict_add["value"] = "> Time: *"+time+"*\n> Forecast: "+ forecast+" Previous: "+previous
                    high_json["embeds"][0]["fields"].append(dict_add)
        
                                
            except:
                if ("country" in locals()) and ("importance" not in locals()):
                    for x in i.find_all("td"):
                        if "event" in x["class"]:
                            event = x.text.rstrip().lstrip()
                    time = " "
                    forecast = " "
                    previous = " "

                    dict_add = {}
                    dict_add["name"] ="**"+" "+event+"**"
                    dict_add["value"] = "> Holiday"
                    high_json["embeds"][0]["fields"].append(dict_add)
                
                else:
                    error = error+1
        
        
        dict_add = {}        
        dict_add["name"] ="Investing.com Link"
        dict_add["value"] = "["+str(tomorrow)+"](https://www.investing.com/economic-calendar/)"
        high_json["embeds"][0]["fields"].append(dict_add)
        
        dict_err = {}
        dict_err["text"] = "Encountered "+str(error)+" errors"
        high_json["embeds"][0]["footer"] = dict_err
        
        del country, importance, time, forecast, previous, event

        
        
        while True:
            webhook = "INSERT WEBHOOK HERE"
            send = requests.post(webhook,json=high_json)
            if send.status_code == 204:
                sleep(60)
                break
            if send.status_code == 400:
                error_json = {
                        "content": "error sending data",
                        "attachments": []
                        }
                send = requests.post(webhook,json=error_json)
                break
            else:
                sleep(50)

                  
    
    
    
    

