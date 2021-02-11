# FB_Automation_using_Selenium
Using Selenium Automation of FB for Internship Task
- This is a FaceBook Bot.
- The FaceBook Bot is using Python's Module "Selenium".
- This is a Part of an Internship Task.


## How it Works
> - I have Used FaceBook's Old version to Automate the tasks.
> - The Bot performs Particular Tasks such as Opening facebook page, login to account, post story on timeline, add some random friend, comment on some random friend's recent post.
> - Using of Selenium library with Python made work easier.

## Requirements
 > - Python IDE (used VScode)
 > - Selenium library
 > - WebDriver_Manager
 
 # Automation of FB Bot Does
 
 ## Task 1
  > - Simply opens up the browser and go to the url [facebook](https://www.facebook.com/)
  > - The Bot enters the Emailid Or username and Password which is provided in the Email or Phone Field and Password Field in Facebook Page.
  > - Then After successfully entering email and password, it clicks Login.
  > - As a result , The bot logs in successfully
  
#### Login:
 <p>
 <img src = "https://github.com/Nitya-26/FB_Automation_using_Selenium/blob/main/task1.gif" alt = "Login Using FB Bot" />
 </p>

## Task 2
 > - After successful Login, It searches for people based on the given Loaction.
 > - If people in search are already friend, it doesn't do anything.
 > - When a person who is not a friend shows up, Then the Bot sends a friend request to that person.
 
#### Sending Friend Request:
<p>
 <img src = "https://github.com/Nitya-26/FB_Automation_using_Selenium/blob/main/task2.gif" alt= "Sending request" />
 </p>
 
## Task 3
> - The Bot posts some specifed text on the Timeline.
> - After Entering the Content , it clicks Post.

#### Posting on Timeline:
<p>
 <img src = "https://github.com/Nitya-26/FB_Automation_using_Selenium/blob/main/task3.gif" alt = "Posting on Timeline" />
 </p>
 
## Task 4
> - The Bot opens the timeline of a random friend .
> - It comments some random text on the most recent post.

#### Commenting on Friend's Timeline:
<p>
 <img src = "https://github.com/Nitya-26/FB_Automation_using_Selenium/blob/main/task4.gif" alt = "Commenting" />
 </p>
 
 ##### Note:
  > - I have used old version of Facebook for most of the automation because searching of elements is easier.
  > - The gifs of the Tasks are very slow and not great. As there's very less time. I did not edit.
  > - I have also automated the "Process of Recovery of the Facebook Account" as my account is in the state of recovery.
  
 - I have provided the whole Python code for the automation and performing several tasks using the bot.
 
 ###### References
 > - Selenium Documentataion [Selenium](https://selenium-python.readthedocs.io/)
 > - webdriver_manager Documentation [webdriver_manager](https://pypi.org/project/webdriver-manager/)
