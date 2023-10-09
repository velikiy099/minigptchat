# Simple chat app for GPT

## how to run

Set your OpenAI API key as an environmental variable in .env file.

If you place .env file under /app directory, it overrides the value set in system.

```sh
docker build -t minigptchat .
docker run --rm -d -p 80:80 --env-file .env minigptchat
```
