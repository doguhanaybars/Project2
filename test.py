import requests
import random
import datetime
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

key = input('Key Degerini Giriniz : ')
token = input('Token Degerini Giriniz :')
board_name=input('Board Name Giriniz : ')
list_name=input('List Name Giriniz : ')
card_name1=input('1. Card Name Giriniz : ')
card_name2=input('2. Card Name Giriniz : ')

class CreateDirectory():
    def Logsirectory(): 
        # Create directory
        dirName = f'Logs'
        try:
            # Create target Directory
            os.mkdir(dirName)
            print(Fore.GREEN)
            print(dirName ,  "Klasoru olusturuldu ")
            print(Style.RESET_ALL)
        except FileExistsError:
            print(Fore.YELLOW)
            print(dirName ,  "Klasoru zaten mevcut")
            print(Style.RESET_ALL)

CreateDirectory.Logsirectory()
date=(datetime.datetime.now().strftime("%Y.%m.%d.%H.%M"))
hour=(datetime.datetime.now().strftime("%H.%M"))
def create_board():
    logs = open(f"./Logs/{date}_{hour}.txt","w",encoding="utf-8") 
    try:       
        url = "https://api.trello.com/1/boards/"
        querystring = {"name": board_name, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        board_id = response.json()["shortUrl"].split("/")[-1].strip()

        print(Fore.GREEN)
        print("Basarili Sekilde Board Olusturuldu")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde Board Olusturuldu"))
    except:
        print(Fore.RED)
        print("HATA : Board Olusturulurken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : Board Olusturulurken Hata Alindi"))
    logs.write(str('\n'))
    try:
        url = f"https://api.trello.com/1/boards/{board_id}/lists"
        querystring = {"name": list_name, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        list_id = response.json()["id"]

        print(Fore.GREEN)
        print("Basarili Sekilde Liste Olusturuldu")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde Liste Olusturuldu"))
    except:
        print(Fore.RED)
        print("HATA : Liste Olusturulurken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : Liste Olusturulurken Hata Alindi"))
    logs.write(str('\n'))           
    try:
        url = f"https://api.trello.com/1/cards"
        querystring = {"name": card_name1, "idList": list_id, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        card_id1 = response.json()["id"]
        print(Fore.GREEN)
        print("Basarili Sekilde 1.Kart Olusturuldu")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde 1.Kart Olusturuldu"))
    except:
        print(Fore.RED)
        print("HATA : 1.Kart Olusturulurken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : 1.Kart Olusturulurken Hata Alindi"))
    logs.write(str('\n'))        
    try:
        url = f"https://api.trello.com/1/cards"
        querystring = {"name": card_name2, "idList": list_id, "key": key, "token": token}
        response = requests.request("POST", url, params=querystring)
        card_id2 = response.json()["id"]
        print(Fore.GREEN)
        print("Basarili Sekilde 2.Kart Olusturuldu")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde 2.Kart Olusturuldu"))
    except:
        print(Fore.RED)
        print("HATA : 2.Kart Olusturulurken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : 2.Kart Olusturulurken Hata Alindi"))
    logs.write(str('\n')) 
    try:   
        
        i=random.randint(1,2)
        if i==1:
            url = f"https://api.trello.com/1/cards/{card_id1}/cover"
            headers = {"Accept": "application/json"}
            query = {
            'key': key,
            'token': token,
            'name': 'New Name 1',
            'value': {'color': 'green','name':'NewName1'}
            }
            response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=query)
            
        else:
            url = f"https://api.trello.com/1/cards/{card_id2}/cover"
            headers = {"Accept": "application/json"}
            query = {
            'key': key,
            'token': token,
            'name': 'New Name 2',
            'value': {'color': 'red','name':'NewName'}
            }
            response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=query)
        print(Fore.GREEN)
        print("Basarili Sekilde Kart Degistirildi")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde Kart Degistirildi"))
    except:
        print(Fore.RED)
        print("HATA : Kart Degistirilirken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : Kart Degistirilirken Hata Alindi"))
    logs.write(str('\n')) 
    try:   
        url = f"https://api.trello.com/1/cards/{card_id1}?key={key}&token={token}"
        querystring = {"name": card_name1, "idList": list_id, "key": key, "token": token}
        response = requests.request("DELETE", url, params=querystring)
        print(Fore.GREEN)
        print("Basarili Sekilde 1.Kart Silindi")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde 1.Kart Silindi"))
    except:
        print(Fore.RED)
        print("HATA : 1.Kart Silinirken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : 1.Kart Silinirken Hata Alindi"))
    logs.write(str('\n')) 
    try:
        url = f"https://api.trello.com/1/cards/{card_id2}?key={key}&token={token}"
        querystring = {"name": card_name2, "idList": list_id, "key": key, "token": token}
        response = requests.request("DELETE", url, params=querystring)
        print(Fore.GREEN)
        print("Basarili Sekilde 2.Kart Silindi")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde 2.Kart Silindi"))
    except:
        print(Fore.RED)
        print("HATA : 2.Kart Silinirken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : 2.Kart Silinirken Hata Alindi"))
    logs.write(str('\n')) 
    try:
        url = f"https://api.trello.com/1/boards/{board_id}?key={key}&token={token}"
        querystring = {"name": board_name, "idList": list_id, "key": key, "token": token}
        response = requests.request("DELETE", url, params=querystring)
        print(Fore.GREEN)
        print("Basarili Sekilde Board Silindi")
        print(Style.RESET_ALL)
        logs.write(str("Basarili Sekilde Board Silindi"))
    except:
        print(Fore.RED)
        print("HATA : Board Silinirken Hata Alindi")
        print(Style.RESET_ALL)
        logs.write(str("HATA : Board Silinirken Hata Alindi"))
    logs.write(str('\n')) 

create_board()











