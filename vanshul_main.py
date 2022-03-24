import requests
import time 
import json
import random

def intro():
    print("hello my name is senku")
    time.sleep(1)
    print(" ")
    print("I am a fellow otaku")
    time.sleep(1)
    print(" ")
    print("I can tell the latest updates on the anime you like!")
    time.sleep(1)
    print(" ")
    print("go on search for an anime")

#intro()

query = '''
query ($id: Int, $page: Int, $perPage: Int, $search: String) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
        media (id: $id, search: $search) {
            id
            type
            status
            title {
                romaji
                english
            }
        }
    }
}
'''

x = input('enter anime name: ')





variables = {
    'search': str(x),
    'page': 1,
    'perPage': 3
}
url = 'https://graphql.anilist.co'
response = requests.post(url, json={'query': query, 'variables': variables})
response = (response.json())



res_storage = (response['data']['Page']['media'][1]) 

print('this piece of media is '+(str(res_storage['title']['romaji'])))

anime_id = (res_storage['id'])
#print(anime_id)
episodes_='''
query ($id : Int) {
  Media (id : $id) {
    reviews(perPage: 3) {
      nodes{
        summary
      }
    }
    episodes
    title {
      romaji
      english
      native
    }
  }
}
'''
variables = {
  'id': anime_id   
}


response2 = requests.post(url, json={'query': episodes_, 'variables': variables})

response2 = (response2.json())

res_storage_for_ep = (response2['data']['Media'])
no_of_eps = (res_storage_for_ep['episodes'])



reviews_ = (res_storage_for_ep['reviews']['nodes'][0]['summary'])

def questions():
    print("what would you like to know about it?")
    print("1. Episodes")
    print("2. Characters")
    print("3. reviews")
    q1 = int(input("Answer in 1 , 2 or 3 : "))
    if q1 == 1 :
        if no_of_eps == None:
            print('the anime or manga is still ongoing')
        else:
            print("the number of episodes is" , no_of_eps)
    elif q1 == 3 :
        print(reviews_)

questions()

def loop():
    print('would you like to know more or nah ')
    ans = input(' Y or N')
    if ans == 'Y' or ans == 'y':
        while ans == 'Y' or ans == 'y':
            x = input('enter anime name : ')
            break 

        questions()
        loop()
    elif ans == 'N' or ans == 'n':
        print('thank you for your time')
    else : 
        print('type error')

loop()