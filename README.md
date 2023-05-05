# Code Analyzer

This is a simple Python script that uses the OpenAI API to improve the readability and maintainability of your code. It detects the programming language based on the file extension and sends the code to the API for suggestions on how to improve it.

## Prerequisites

1. Python 3.6 or later
2. An OpenAI API key

## Installation

### Ubuntu

1. Install Python 3:

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Arch Linux

1. Install python 3:

```bash
sudo pacman -Syu
sudo pacman -S python python-pip
```

## Usage

1. Install the package, inside the project directory, with the following command:

```bash
pip install --editable .
```

2. Set your OpenAI API key as an environment variable or pass it as an argument:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

3. Run the script with the input file as the first argument, and optionally, the output file and API key as the second and third arguments:

```bash
code-analyzer <input_file> [<output_file>] [<openai_api_key>]
```

Example:

```bash
code-analyzer test_files/bad_code.js test_files/bad_code.ai.js
```

This will generate an improved version of the code in a file with the same name but with the .ai extension (e.g., bad_code.ai.js).

## Notes

- The script currently supports the following file extensions: .go, .py, .js, .java, .cs, .cpp, .rb, and .php.
- If the output file is not provided, it will be saved with the same name as the input file but with the .ai-version.{extension}.
- If the API key is not provided as an argument, the script will look for it in the environment variable OPENAI_API_KEY.