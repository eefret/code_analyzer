# analyze.py
import os
import sys
import openai
import re
import pathlib

if len(sys.argv) < 2:
    print("Usage: python analyze.py <file> [<output_file>] [<openai_api_key>]")
    sys.exit(1)

file_path = sys.argv[1]

if len(sys.argv) > 3:
    api_key = sys.argv[3]
else:
    api_key = os.environ.get("OPENAI_API_KEY")

if api_key is None:
    print("Error: OpenAI API key not provided and not found in the environment variable OPENAI_API_KEY.")
    sys.exit(1)

try:
    with open(file_path, 'r') as file:
        code = file.read()
except FileNotFoundError:
    print("Error: File does not exist.")
    sys.exit(1)

openai.api_key = api_key

def get_language_by_extension(file_path: str) -> str:
    file_extension = pathlib.Path(file_path).suffix

    language_map = {
        '.go': 'go',
        '.py': 'python',
        '.ts': 'ts',
        '.js': 'javascript',
        '.java': 'java',
        '.cs': 'csharp',
        '.cpp': 'cpp',
        '.rb': 'ruby',
        '.php': 'php',
    }

    return language_map.get(file_extension, '')

if len(sys.argv) > 2:
    output_file_path = sys.argv[2]
else:
    file_extension = pathlib.Path(file_path).suffix
    file_name = pathlib.Path(file_path).stem
    output_file_path = f"{file_name}.ai-version{file_extension}"

language = get_language_by_extension(file_path)

if not language:
    print("Error: Could not detect programming language based on the file extension.")
    sys.exit(1)

# Create the prompt
prompt = f"I want you to act as a code analyzer. Can you improve the following code for readability and maintainability?\n\n```{language}\n{code}\n```\n"
#print(prompt)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# Extract the full response
full_response = response.choices[0].message.content.strip()
print(full_response)

# Search for the code markers and extract the code between them
code_pattern = re.compile(rf"```{language}\n(.*?)\n```", re.DOTALL)
match = code_pattern.search(full_response)
if match:
    improved_code = match.group(1).strip()
else:
    print("Error: Could not find code markers in the response.")
    sys.exit(1)

# Write improved code to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(improved_code)
