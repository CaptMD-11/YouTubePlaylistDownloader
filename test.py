from googlesearch import search

user_input = input("Enter artist name: ")

for i in search(user_input, tld="com", num=10, stop=10, pause=2):
    print(i)
