# Roadmap

## Design

- For righthand Info tabs: to save on db reads, compute once on backend, then serve in-memory versions to all clients
- Keep DB access centralized to one file (database.py) so that migrating to a new db (like Postgres) is easier
- No math operators, just numbers + power-ups
- Give everyone own board to reduce syncing
- Game end is scored-based not time-based

## Milestone 0: Scaffolding

>> COOKIE + DB -- final major local infrastructure <<
- in events log: "Welcome, display_name. You are on <Team Name>." (proves cookie read+write and db read+write)
 
## Milestone 1: Playable local machine game 

- Create a blurb above Registration form describing game
- Captcha for the game: 5 digit even number embedded in various length prefix and postfix odds
- Username and display name fields must be enforced unique in db and Python and JavaScript (means we'll need db read to check for dupe names)
- One way hash the UUID password to save to db; maybe passlib?
- Browser property reading to set fingerprint (2 db columns: IP; hash of tuple of: timezone, hardware concurrency, screen width, screen height); https://amiunique.org/fingerprint
- Chain power up that repeats the next number selected X times over the next X cycles
- Captcha table with id, problem, solution so client receives id and problem and sends id and solution
- Use ahead/behind language instead of winning, losing to not let people lose hope
- pop a modal final score up at end of game for closure/satisfaction
- final score modal has Join Next Game button
- To pick what fills a cell: hierarchy of attempting probabilities of power ups then numbers (including size of number)
- 2 luck power ups: lucky percentage that goes up from 1%; lucky multiplier that starts at 2x
- 3 tier join calculation: if a team is more than 5% of total score needed ahead in current game do other team, then if less than 5% overall losing team across all games, then if still tied random
- Micro, Small, Medium, Large, Enormous number factories (and you need 3 of a type to see next type on board) with idle game steady supply of numbers in the background each cycle
- Send enemy team % chance of blocker tiles; takes up space in grid
- Maybe: power up to expand grid, e.g. start with 4x4, go up to 8x8

## Milestone 2: Playable AWS game

- Minify/obfuscate process before deploying
- Cloudflare HTTPS
- be aware of mixed content https issue with cloudfare: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/#limitations

## Milestone 3: Incorporate feedback from beta test

- ?
