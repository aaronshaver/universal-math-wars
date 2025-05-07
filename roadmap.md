# Roadmap

## Design

- For righthand Info tabs: to save on db reads, compute once on backend, then serve in-memory versions to all clients
- Keep DB access centralized to one file (database.py) so that migrating to a new db (like Postgres) is easier
- No math operators, just numbers + power-ups
- Give everyone own board to reduce syncing
- Game end is scored based not time based

## Milestone 0: Scaffolding

>> COOKIE + DB -- final major local infrastructure <<
- in events log: "Welcome, display_name. You are on <Team Name>." (proves cookie use and db read+write)
 
## Milestone 1: Playable local machine game 

- Captcha for the game: 5 digit even number embedded in various length prefix and postfix odds
- Username and display name fields must be enforced unique in db and Python and JavaScript
- One way hash the UUID password to save to db; maybe passlib
- Browser property reading to set fingerprint (3 files: IP, avail width, avail height); https://amiunique.org/fingerprint
- Chain power up that repeats the next number selected X times over the next X cycles
- Captcha table with id, problem, solution so client receives id and problem and sends id and solution
- Use ahead/behind language instead of winning, losing to not let people lose hope
- pop a modal final score up at end of game for closure/satisfaction
- final score modal has Join Next Game button
- To pick what fills a cell: hierarchy of attempting probabilities of power ups then numbers (including size of number)
- 2 luck power ups: lucky percentage that goes up from 1%; lucky multiplier that starts at 2x
- 3 tier join calculation: if a team is more than 100,000 ahead in current game, then if tied overall losing team across games, then if tied random
- Small, medium, large number factories (and you need 3 of a type to see next type on board) with idle game steady supply of numbers in the background
- Badges, like lucky chance multiplier
- Send enemy team a debuff: % chance for blocker tile, takes up space in grid

## Milestone 2: Playable AWS game

- Minify/obfuscate JS before deploying to AWS
- Get https set up so that we can send username and password freely with each REST request to authenticate user each request

## Milestone 3: Incorporate feedback from beta test

