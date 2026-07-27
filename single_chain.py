from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
    Summarize the following text in one short paragraph.

    Text:
    {text}
    """
)

chain = prompt | llm

user_text = input("Enter the text to summarize:\n")

response = chain.invoke({"text": user_text})

print("\nSummary:")
print(response.content)