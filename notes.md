# Notes

## To-do

- TDD unit tests and user registration

## Run tests + get coverage report

clear && pytest --cov=registration --cov-report=term-missing

## Config files note

Stuff like:

`VITE_API_BASE_URL=http://localhost:8000`

Should live in /frontend/.env.development

## Design

- Two fields: display name and username, because would be useful for changing obscene names, giving people rename ability
- For righthand Info tabs: to save on db reads, compute once on backend, then serve in-memory versions to all clients
- Keep DB access centralized to one file (database.py) so that migrating to a new db (like Postgres) is easier
- No math operators, just numbers + power-ups
- Python Fast API
- Give everyone own board to reduce syncing
- Game end is scored based not time based

## Features

- User fingerprint: IP + available height + available width (https://amiunique.org/fingerprint)
- Minify/obfuscate JS before deploying to AWS

- To pick what fills a cell: hierarchy of attempting probabilities of power ups then numbers (including size of number)
- 2 luck power ups: lucky percentage that goes up from 1%; lucky multiplier that starts at 2x
- 3 tier join calculation: if a team is more than 100,000 ahead in current game, then if tied overall losing team across games, then if tied random
- Small, medium, large number factories (and you need 3 of a type to see next type on board) with idle game steady supply of numbers in the background
- Badges, like lucky chance multiplier
- Send enemy team a debuff: % chance for blocker tile, takes up space in grid
