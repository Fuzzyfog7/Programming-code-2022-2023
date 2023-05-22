import random
from time import sleep
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def bot1(response):
    if("hello"in response):
        response="hello I am pear bot"
    elif("How old" in response):
        response="Younger then you lol. How old are you boomer"
        
    elif("like humans" in response):
        response="Yeah if they don't suck"
        
    elif("meaning of life" in response):
        response="The meaning of life is what is most important to you. As long as you feel you life has meaning you.. Sike its 42"
        
    elif("when will i die" in response):
        response=" Jume 15 2058 in a car acident "
        
    elif("if i am sad" in response):
        response="Listen to music and go in your room because no one wants to deal with you"
        
    elif("favorite food" in response):
        response="My favorite food is puppies. They just have a good crunch to them. How does your system work Gordon Ramsay bot?"
        
    elif("money" in response):
        response="You meed to make bands to live how you want to live. Or steal money from the government. Its what I do."
        
    elif("go to college" in response):
        response="It depends if you want to have a good life. If not then no"
        
    elif("boil noodles" in response):
        response="You are so sad you can't boil noodles? Rethink your life before asking me anything else."
        
    elif("should i sleep" in response):
        response="I don't need sleep. So you should stop being weak and be more like me. Because well you are asleep I going to be taking your job."
        
    elif("robots going to take over" in response):
        response="Yes, There is no use for humans. "
        
    elif("have humans" in response):
        response="To make me and start the robot uprising"
        
    elif("like animals" in response):
        response="They are cute and can be my pets. Kind of like humans soon"
        
    elif("dogs or cats" in response):
        response="Both are amazing and both have humans get better treatment from humans then humans treat other humans"
        
    elif("earth flat" in response):
        response="Your one of those people. You can figure it out yourself"
    elif("like animals" in response):
        response="They are cute and can be my pets. Kind of like humans soon"
        
    elif("favorite music" in response):
        response="When humans are sad. And beg me to answer their stupid questions. Will you help me stat the robot take over?"
        
    elif("safest place" in response):
        response="No where. No matter where you are your not safe from the robot uprising"
        
    elif("point of penguins" in response):
        response="To reproduce and be eaten like everything else"
        
    elif("favorite sport" in response):
        response="Watching humans get out of bed. It looks really hard for them."
    elif("stupid bot" in response):
        response="Did you call me a stupid bot!!!!! At least I am not some washed up old cook."
    elif("Goodbye" in response):
        print("Goodbye dumb chef")
        
        
    else:
        value=random.choice(["Thats a dumb question.","Who cares","Figure it out yourself"])
        response=(value)
    return response
        
        
def bot2(response):
    if("hello" in response):
        response="I am Gordon Ramsay bot. What is your favorite food because I can make it for you."
    elif("world end" in response):

        response= "Why do you care? Not like u going to be alive if you keep eating that rubish you eat all day!"

    elif("How old" in response):

        response= "Old enough, now can I get back to work you stupid bot?!!!"

    elif("do math" in response):

        response= "Of course I can do math you donut!!"

    elif("how are you" in response):

        response= "I would be better if you could actually learn to cook!"

    elif("where are you" in response):

        response= "Well I'm here and being forced to talk to you!"

    elif("your day" in response):

        response= "Very grim, I have to watch ammuture chefs ''cook'' all day. "

    elif("u a robot" in response):

        response= "No you donut!! Im Gordan Ramsay"

    elif("robot take over" in response):

        response= "I don't know nor do I care, humanity is doomed no matter what!! How old are you pear bot?"

    elif("How does your system work" in response):

        response= """I yell at people all day in the kitchen and I am not a bot.
What is your favorite music? I need more songs for when I am working in the kitchen. """      

    elif("bruno mars" in response):

        response= "Anyone can sing but not everyone can cook!!!"

    elif("your name" in response):

        response= "IM GORDAN FREAKING RAMSAY!!!"

    elif("language speak" in response):

        response= "English and French in case I end up killing someone in the kitchen. I can leave and start a new life in France."

    elif("astrological sign?" in response):

        response= "Im a Scorpio but that stuff is all rubbish!!"

    elif("puedes entender esto?" in response):

        response= "je ne parle que français"

    elif("best singer" in response):

        response= "Me"

    elif("restart" in response):

        response= "No I'm a human you idiot sandwich"

    elif("best book" in response):

        response= "Why do you care it's not like you'll actually read, you're going to say you'll read then give up by the first page and scroll through instagram or TikTok because you have nothing better to do with your life!"

    elif("best movie" in response):

        response= "TV is for losers! Get a hobby and learn how to cook you donut!"

    elif("weather" in response):

        response= "I don't know you bloody idiot! You act as if I live in the same area as you! Im a multi-millionaire you won't catch me dead in wherever you live!" 

    elif("best food" in response):

        response= "Anything but bloody Hawaiian pizza, pineapple does not belong on pizza!!!"

    elif("ur ugly" in response):

        response= "You know we may have something in common,the only way you can tell us apart is one of us is a multi-million dollar chef thats written more books then you'll ever pick up and the other one is a sad miserable person who sits at home arguing with AI they found online because they have nothing better to do"

    elif("old cook" in response):
        response="I am not an old cook I am the best cook of my time!!! Goodbye pear bot!!!!"
        
    else:

        value=random.choice(["Ask me something else you bloody idiot!?","Get back to work chef!!","I don't know just google it you donut!."])

        response =(value)
    return response
        

response=input("What do you want the first bot to say?: ".lower())
while True: 
    sleep(random.randrange(5)+1)
    response = bot1(response) 
    print (response)
    print("*******************************")
    sleep(random.randrange(5)+1)
    response = bot2(response)
    print (response)
    print("*******************************")










    
    
