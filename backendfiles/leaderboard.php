<?php

//User varibles that are taken in from the get request sent from python
//To add more or change variables, add it here below and change the url in 
//the python code around line 121 in the post_data_to_leaderboard func
$playername = $_GET["playername"];
$boattype = $_GET["boattype"];
$leaderboardfile = fopen("leaderboard.json", "w");

//The data must be parsed and made sure it is actually supposed to go on the 
//leaderboard

function parse_data($playername, $boattype) {
    if ($playername){
        
    }
}






?>