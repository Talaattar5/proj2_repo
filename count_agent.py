from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent


# Load API key from .env
load_dotenv()


# Create the word-counting agent
agent = create_agent(
    model=ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    ),
    tools=[],
    system_prompt=(
        "You are a word counting agent. "
        "Count how many times a specific word appears in the provided text. "
        "The counting must be case-insensitive. "
        "Return the result in this exact format: "
        'The word "WORD" appears NUMBER times.'
    )
)


if __name__ == "__main__":

    file_name = input("Enter the text file name:\n")
    target_word = input("Enter the word to count:\n")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            file_text = file.read()

        if not file_text.strip():
            print("The file is empty.")

        elif not target_word.strip():
            print("You must enter a word.")

        else:
            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": (
                                f'Count the word "{target_word}" in this text:\n\n'
                                f"{file_text}"
                            )
                        }
                    ]
                }
            )

            print("\nWord Count Result:")
            print(result["messages"][-1].content)

    except FileNotFoundError:
        print("File not found. Make sure the file name is correct.")