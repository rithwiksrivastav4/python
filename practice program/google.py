from googlesearch import search

query = input("ask anything: ")

for i,url in  enumerate(search(query, num = 10) , start = 1 ):
    print(url)
    if i == 10 :
        break