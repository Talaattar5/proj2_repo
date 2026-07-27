from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)



extract_prompt = ChatPromptTemplate.from_template(
    """
    Extract every separate task from the following text.

    Rules:
    - Put each task on a separate line.
    - Do not number the tasks.
    - Do not add explanations.
    - Do not merge different tasks.
    - Keep the original wording as much as possible.

    Text:
    {text_input}
    """
)

extract_chain = extract_prompt | llm




classify_prompt = ChatPromptTemplate.from_template(
    """
    Classify the following task into only one category:

    University/Academic
    Work
    Personal
    Shopping
    Health
    Home Maintenance
    Other

    Return only the category name.

    Task:
    {task}
    """
)

classify_chain = classify_prompt | llm



word_count_prompt = ChatPromptTemplate.from_template(
    """
    Count the number of words in the following task.

    Return only the number.

    Task:
    {task}
    """
)

word_count_chain = word_count_prompt | llm




if __name__ == "__main__":

    sample_text = """
    Complete the final report for the database management course before Friday.
    Book a dentist appointment for next week.
    Pay the monthly electricity and internet bills.
    Finish watching the recorded networking lecture.
    Order a new laptop charger online.
    Organize the files in the Downloads folder.
    Call the internship supervisor to confirm tomorrow's meeting.
    """

    print("\n--- Running Multi-Task Sequential Workflow ---")

    
    extract_response = extract_chain.invoke({
        "text_input": sample_text
    })

    raw_tasks = extract_response.content

    
    tasks = [
        task.strip().lstrip("-").strip()
        for task in raw_tasks.split("\n")
        if task.strip()
    ]

    print(f"\nTotal Tasks Extracted: {len(tasks)}")
    print("-" * 60)

    
    for index, task in enumerate(tasks, start=1):

        category_response = classify_chain.invoke({
            "task": task
        })

        word_count_response = word_count_chain.invoke({
            "task": task
        })

        category = category_response.content.strip()
        word_count = word_count_response.content.strip()

        print(f"\nTask {index}: {task}")
        print(f"Category: {category}")
        print(f"Word Count: {word_count} words")
        print("-" * 60)