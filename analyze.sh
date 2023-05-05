#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file> <openai_api_key>"
    exit 1
fi

FILE=$1
API_KEY=$2

if [ ! -f "$FILE" ]; then
    echo "Error: File does not exist."
    exit 1
fi

CODE=$(cat "$FILE" | jq -Rs .)

PROMPT="I want you to act as a code analyzer. Can you improve the following code for readability and maintainability?\\n$CODE"

curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $API_KEY" -d "{\"engine\":\"davinci-codex\",\"prompt\":\"$PROMPT\",\"max_tokens\":300,\"n\":1,\"stop\":null,\"temperature\":0.5}" https://api.openai.com/v1/engines/davinci-codex/completions | jq '.choices[0].text'
