#To Import Requests
import requests


# For Top Business Headlines
def Business_Headlines():
    #Main Url for the Business Headlines
    main_url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=Enter your API here"

    #Now Getting Requests from the main_url in JSON Format
    web_app=requests.get(main_url).json()

    articles=web_app["articles"]

    # printing the Titles of the News Only
    i=1;
    for news in articles:
        print(str(i)+'.','Title:',news["title"])
        print()
        print ('Description:')
        print(news["description"])
        print()
        i=i+1;
        print('Check for full news at:')
        print(news['url'])
        print()

# For BitCoin News
def Bitcoin_Headlines():
    #Main Url for Bitcoin News
    main_url="https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-03&sortBy=publishedAt&apiKey=Enter your API here"

    web_app=requests.get(main_url).json()
    
    articles=web_app["articles"]
    
    i=1;
    for news in articles:
        print(str(i)+'.','Title:',news["title"])
        print()
        print ('Description:')
        print(news["description"])
        print()
        i=i+1;
        print('Check for full news at:')
        print(news['url'])
        print()


#Top headlines from TechCrunch

def tech_crunch():
    main_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=Enter your API here"

    web_app=requests.get(main_url).json()

    articles=web_app['articles']

    i=1;
    for news in articles:
        print(str(i)+'.','Title:',news["title"])
        print()
        print ('Description:')
        print(news["description"])
        print()
        i=i+1;
        print('Check for full news at:')
        print(news['url'])
        print()

#articles published by the Wall Street Journal in the last 6 months

def wall_street():
    main_url="https://newsapi.org/v2/everything?domains=wsj.com&apiKey=Enter your API here"

    web_app=requests.get(main_url).json()
    
    articles=web_app["articles"]
    
    i=1;
    for news in articles:
        print(str(i)+'.','Title:',news["title"])
        print()
        print ('Description:')
        print(news["description"])
        print()
        i=i+1;
        print('Check for full news at:')
        print(news['url'])
        print()
        
def Apple_news():
    main_url="https://newsapi.org/v2/everything?q=apple&from=2019-02-02&to=2019-02-02&sortBy=popularity&apiKey=Enter your API here"

    web_app=requests.get(main_url).json()

    articles=web_app['articles']

    i=1;
    for news in articles:
        print(str(i)+'.','Title:',news["title"])
        print()
        print ('Description:')
        print(news["description"])
        print()
        i=i+1;
        print('Check for full news at:')
        print(news['url'])
        print()


print('Hey user,Welcome to the NEWS api xd(:')
p='y'
while(p=='y'or p=='Y'):
   print('Select Your Choice:')
   print('1. Top Business Headlines')
   print('2. Top Bitcoin News')
   print('3. Top Tech Crunch')
   print('4. Top Wall Street Journals')
   print('5. Top Apple Headlines')
   ch=int(input("Enter Your Choice: "))
   print()
   if(ch==1):
       print('Top Business Headlines are:')
       Business_Headlines()

   elif(ch==2):
       print('Top Bitcoin News are:')
       Bitcoin_Headlines()

   elif(ch==3):
       print('Top Tech Crunch are:')
       tech_crunch()
        
   elif(ch==4):
       print('Top Wall Street Journals are:')
       wall_street()

   elif(ch==5):
       print('Top Apple Headlines are:')
       Apple_news()
   p=input('Are you looking for any news y/n: ')
   if(p=='n'or p=='N'):
      print()
      print('Hope you like this xd(:')
      break



#All the News Api's are from newsapi.org
