character ={
    "name" : "기사",
    "level" : 12,
    "items":{
        "sword": "불꽃의 검",
        "armor" : "풀플레이트",
    },
    "skill" : ["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str :
        print(key,":",character[key])
    elif type(character[key]) is list :
        for j in range(0,3):    
            print(key,":",character['skill'][j])
    elif type(character[key]) is dict:
        for i in character['items']:
            print(i,":",character['items'][i])
    else:print(key,":",character[key])
