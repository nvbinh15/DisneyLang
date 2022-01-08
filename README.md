# DisneyLang

A fun and annoying project submitted for HacknRoll 2022.
It basically censors profanity and replies to the things you said.

## Setup

- Clone the repo
- Create and activate virtual environment
- Create `.env` file with the following environment variable

```
export TOKEN='your_bot_token_goes_here'
```

- Activate the `.env` file by `$ source .env`

- Install dependencies (assuming you have `poetry` installed)

```
poetry install
```

- Run `main.py` file

## Basic Functions

- Censors users' slurs/profanity
- Rephrasing gone wrong: rephrases your message and make it longer (like how you did for essays)
- Grammar police: check your grammar/spelling mistakes
