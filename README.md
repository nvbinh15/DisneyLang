# DisneyLang

A fun and annoying project submitted for HacknRoll 2022.
It basically censors profanity and replies to the things you said.

Click (here)[https://discord.com/api/oauth2/authorize?client_id=928832278027730954&permissions=8&scope=bot] to add DisneyLang to your Discord server.

## Setup

- Clone the repo
- Create and activate virtual environment
- Create `.env` file with the following environment variable

```
export TOKEN='<your_bot_token_goes_here>'
```

- Activate the `.env` file by `$ source .env`

- Install dependencies (assuming you have `poetry` installed)

```
$ poetry install
```

- Run `main.py` file

## Basic Functions

- Censors users' slurs/profanity
- Rephrasing gone wrong: rephrases your message and make it longer (like how you did for essays)
- Grammar police: `!check <your-sentence>`: to check for grammar/spelling mistakes (grammar police may cause a delay of +- 10 seconds)
- Trivia fun quiz: `!quiz` for a short True/False trivia quiz to play with your friends
