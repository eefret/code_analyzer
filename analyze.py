import os
import sys
import openai
import re
import pathlib


def print_usage_and_exit():
    print("Usage: python analyze.py <file> [<output_file>] [<openai_api_key>]")
    sys.exit(1)


def create_prompt(language, code):
    return (
        f"I want you to act as a code analyzer. Can you improve the following code for readability and maintainability?"
        f"\n\n```{language}\n{code}\n```\n"
    )


def extract_improved_code(full_response, language):
    code_pattern = re.compile(rf"```{language}\n(.*?)\n```", re.DOTALL)
    match = code_pattern.search(full_response)

    if match:
        return match.group(1).strip()
    else:
        raise ValueError("Could not find code markers in the response.")


def main():
    if len(sys.argv) < 2:
        print_usage_and_exit()

    file_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else \
        f"{pathlib.Path(file_path).stem}.ai-version{pathlib.Path(file_path).suffix}"
    api_key = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("OPENAI_API_KEY")

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
    language = get_language_by_extension(file_path)

    if not language:
        print("Error: Could not detect programming language based on the file extension.")
        sys.exit(1)

    prompt = create_prompt(language, code)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    full_response = response.choices[0].message.content.strip()
    improved_code = extract_improved_code(full_response, language)

    with open(output_file_path, "w") as output_file:
        output_file.write(improved_code)


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


if __name__ == "__main__":
    main()
