# Notes

## To-do

- TDD unit tests and user registration

## Run tests + get coverage report

clear && coverage run -m unittest discover && coverage report -m

## Design

- No math operators, just numbers and power-ups
- React + Tailwind + Python Fast API
- Give everyone own board to reduce syncing
- browser fingerprint: IP + timezone + available height + available width
- game end is scored based not time based

## Features

- Badges, like lucky chance multiplier
- Hierarchy for team join: first lower score, then if close, lower players
- Send enemy team a debuff: % chance for blocker tile, takes up space in grid