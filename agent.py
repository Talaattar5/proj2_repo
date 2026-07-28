from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent


# Load the API key from .env
load_dotenv()


# Create the summarization agent
agent = create_agent(
    model=ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    ),
    tools=[],
    system_prompt=(
        "You are a text summarization agent. "
        "Summarize the provided text in one short and clear paragraph. "
        "Do not add information that is not in the original text."
    )
)


if __name__ == "__main__":

    file_name = input("Enter the text file name:\n")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            file_text = file.read()

        if not file_text.strip():
            print("The file is empty.")

        else:
            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": file_text
                        }
                    ]
                }
            )

            print("\nSummary:")
            print(result["messages"][-1].content)

    except FileNotFoundError:
        print("File not found. Make sure the file name is correct.")