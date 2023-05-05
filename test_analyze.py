import pytest
import analyze

def test_create_prompt():
    language = "python"
    code = "print('Hello, World!')"
    expected_prompt = (
        "I want you to act as a code analyzer. Can you improve the following code for readability and maintainability?"
        "\n\n```python\nprint('Hello, World!')\n```\n"
    )
    assert analyze.create_prompt(language, code) == expected_prompt


def test_extract_improved_code():
    response = (
        "Here's the improved code:\n\n"
        "```python\nprint('Hello, World!')\n```\n"
    )
    language = "python"
    expected_code = "print('Hello, World!')"
    assert analyze.extract_improved_code(response, language) == expected_code

    with pytest.raises(ValueError):
        analyze.extract_improved_code("Invalid response", language)

# Add any other necessary tests here
