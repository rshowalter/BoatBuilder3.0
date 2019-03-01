# BoatBuilder 3.0
Below are the files for the BoatBuilder 2.0. Please feel free to edit them and improve this version of boat builder as you wish. 


   (                 )     (             (   (                   )       ) 
 ( )\          )  ( /(   ( )\    (   (   )\  )\ )   (   (     ( /(    ( /( 
 )((_)  (   ( /(  )\())  )((_)  ))\  )\ ((_)(()/(  ))\  )(    )(_))   )\())
((_)_   )\  )(_))(_))/  ((_)_  /((_)((_) _   ((_))/((_)(()\  ((_)    ((_)\ 
 | _ ) ((_)((_)_ | |_    | _ )(_))(  (_)| |  _| |(_))   ((_) |_  )   /  (_)
 | _ \/ _ \/ _` ||  _|   | _ \| || | | || |/ _` |/ -_) | '_|  / /  _| () | 
 |___/\___/\__,_| \__|   |___/ \_,_| |_||_|\__,_|\___| |_|   /___|(_)\__/  

1.Click designated material.
2. Click designated boat
3. _____________________  ___
___/  __)__    |__   |/  /
__/  __ |_  /| |_  /|_/ / 
_/  /_//_  ___ |  /  / /  
/_____/ /_/  |_/_/  /_/   /
                           a wild boat has appeared
	                                                                 



# LeaderBoard

The boat builder leaderboard is accessed through cloud9 using the python requests module

# Added Features and edits 3/1/19

sc1341 edits:
1. Added feature that allows username to be displayed to the screen
2. Added drop down menu that links to the github as well as the leaderboard and the not finished name you boat feature
3. Started the back-end web API for the score system
4. 


# Known errors
1. instance error with the name your boat feature, we need to figure out how to 


# API functionality

The api is run on my cloud 9 account that runs a webserver which allows get requests to add data to the leaderboard, as well as pull data from the existing leaderboard data. It is important to note that I use GET requests and do not use any POST requests for the data, All Back end files are attached to this repository under the backend folder. The leaderboard.json file is where the leaderboard data is held, when pulled down by Python requests, the data is formatted into a dict inside of a list. Visit the https://boatbuilder-api-sc1341.c9users.io website to learn more about the API