# Notes

## To-do

- TDD unit tests and user registration

## Run tests + get coverage report

clear && pytest --cov=registration --cov-report=term-missing

## Design

- No math operators, just numbers + power-ups
- React + Tailwind + Python Fast API
- Give everyone own board to reduce syncing
- game end is scored based not time based

## Features

- 3 tier join calculation: if a team is more than 100,000 ahead in current game, then if tied overall losing team across games, then if tied random
- browser fingerprint: IP + timezone + available height + available width
- small, medium, large number factories (and you need 3 of a type to see next type on board) with idle game steady supply of numbers in the background
- Badges, like lucky chance multiplier
- Send enemy team a debuff: % chance for blocker tile, takes up space in grid
