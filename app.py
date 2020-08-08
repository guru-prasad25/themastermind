import time
user_list = []
score = 0

print('Welcome to The Mastermind')
start_or_not = input("""
Would you like to test your knowledge?
Type in yes or no
> """)

if start_or_not.lower() == 'yes':
    print("Alright! But before we start, what is your name?")
    name = input('Name > ')

    user_list.append(name)

    time.sleep(5)

    print("Your questions were researched and formatted by Guru Prasad")

    time.sleep(5)

    print("""
  INSTRUCTIONS:
  After the question appears
  A seperate column asking for the answer will appear.
  Type in your answer after the '>' symbol. """)

    time.sleep(5)

    #question number 1
    print("""Here is your first question. 
  Post Independence, then Prime minister Jawaharlal Nehru was concerned that
  women were spending precious foreign exchange on imported Beauty and Cosmetics.
  So he requested JRD Tata to produce them in India. Hence this company was created.
  What is the name of this widely popular cosmetic company?
  
  Here is a clue: It was named after an Indian Goddess.
  """)
    answer_1 = input("Now let's hear your answer > ")
    if answer_1.lower() == 'lakme':
        print(
            'Excellent. The answer is indeeed Lakme. Initially owned completely by Tata Oil Mill Co. Off to a great start.'
        )
        score = score + 1
    else:
        print("""
    Uh oh. 
    The answer is quite not right. 
    The answer is 'Lakme'. Initially owned by Tata Oil Mill Co. """)

    time.sleep(4)

    #question number 2
    print("""
  Now for the second question.
  MGR was a highly successful actor during his heyday. There was surely one exception though. 
  Olivilakku released at the peak of MGR's career was a box office failure. 
  Certain sequences of the movie were shot again after release to change the plotline of the movie
  But the reason was a peculiar one. 
  What was the reason behind the the failure?
  
  Here is a clue: The reason has something to do with the love his fans had for him.
  Now the answer can be a paragraph explaining it but I am looking for a single keyword. """
        )

    answer_2 = input(" Now your answer > ")
    if 'death' or 'died' in answer_2.lower():
        print("""
    And..... 
    That is correct. 
    Woah, how did you manage to get it. 
    In Olivilakku MGR's character died somewhere along the movie and the fans couldn't aceept that their beloved 'Thalaivar' died. 
    So the movie had to be shot again, to pacify the fans, in which MGR's character did not die. 
    """)
        score = score + 1
    else:
        ("""
    OOOOh.... That is not correct.
    Tough luck. 
    In Olivilakku MGR's character died somewhere along the movie and the fans couldn't aceept that their beloved 'Thalaivar' died. 
    The movie was doomed to a box office failure and disdain among the fans. 
    So the movie had to be shot again, to pacify the fans, in which MGR's character did not die.
    It's okay though. You can get back up to speed in the next question.
    """)

    time.sleep(4)
    #question number 3
    print(""" 
  Here is the third question.
  This legendary South Indian actor is known for requesting the Filmfare committee to not
  give him any more awards. Instead he asked those awards to be given to newcomers to encourage them.
  Who is this actor? """)

    answer_3 = input("Now for your answer. > ")
    if answer_3.lower() == 'kamal hassan' or 'kamal' or 'kamalhassan':
        print("""Great. 
    The veteran actor requested the filmfare committee to stop giving him awards 
    for the above reason after recieving his award for Indian.  
    """)
        score = score + 1
    else:
        print("""Not quite right.
    The veteran actor requested the filmfare committee to stop giving him awards 
    for the above reason after recieving his award for Indian.
    """)
    time.sleep(4)
    #question number 4
    print("""
  Here is the fourth question.
  What do the following Bollywood movies have in common?
  1. Deewar
  2. Amar Akbar Anthony
  3. Majboor
  4. Don
  5. Trishul
  
  The common connect involves a legendary actor. """)

    answer_4 = input("""
  Who is the actor connecting these movies? 
  > """)

    if "rajini" or "rajinikanth" or "rajini kanth" in answer_4.lower():
        print("""
    That was a difficult one. 
    But you got it right. 
    All the movies were remade into Rajinikanth Movies in Tamil
    1. Deewar - Thee
    2. Amar Akbar Anthony - Shankar Salim Simon
    3. Majboor - Naan Vazhavaippen
    4. Don - Billa
    5. Trishul - Mr. Bharath """)

        score = score + 1

    else:
        print("""
    Quite not right. 
    That was a difficult one. 
    All the movies were remade into Rajinikanth Movies in Tamil
    1. Deewar - Thee
    2. Amar Akbar Anthony - Shankar Salim Simon
    3. Majboor - Naan Vazhavaippen
    4. Don - Billa
    5. Trishul - Mr. Bharath
    """)
    time.sleep(4)
    #question number 5
    print("""
  The last question for today. 
  Let's finish the quiz with a little dose of feeling home. 
  Which is the only Household appliance in India to have a Geographical Indicator Tag?
  """)
    answer_5 = input("""
  What is the answer?
  > 
  """)
    if "coimbatore" or "wet grinder" or "grinder" or "coimbatore wet grinder" or "coimbatore grinder" in answer_5.lower:
        print("""
    And that is the right answer.
    Coimbatore Wet grinder is the only home appliance to have a Geographical Indicator tag."""
              )
        score = score + 1

    else:
        print("""Not quite.
    Coimbatore Wet grinder is the only home appliance to have a Geographical Indicator tag.
    """)

    print(f' your score is {score}')
    print('Have a great day. Keep learning')

else:
    print("maybe another day")
