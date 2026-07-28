from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END

 
load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)



class TaskPlannerState(TypedDict):
    tasks: str
    summary: str
    classification: str
    priority: str
    smart_plan: str



def summarize_node(state: TaskPlannerState):

    prompt = ChatPromptTemplate.from_template(
        """
        Summarize the following tasks in one short and clear paragraph.

        Tasks:
        {tasks}
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "tasks": state["tasks"]
    })

    return {
        "summary": response.content
    }

 
def classify_node(state: TaskPlannerState):

    prompt = ChatPromptTemplate.from_template(
        """
        Classify every task into one of these categories only:

        - Work
        - Study
        - Personal

        Rules:
        - Write every task separately.
        - Do not remove any task.
        - Use this format:

        Task 1: ...
        Category: ...

        Task 2: ...
        Category: ...

        Tasks:
        {tasks}
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "tasks": state["tasks"]
    })

    return {
        "classification": response.content
    }



def priority_node(state: TaskPlannerState):

    prompt = ChatPromptTemplate.from_template(
        """
        Analyze the following tasks and assign a priority to each task.

        Use only:
        - High
        - Medium
        - Low

        Consider deadlines, urgency, and importance.

        Rules:
        - Do not remove any task.
        - Use this format:

        Task 1: ...
        Priority: ...

        Task 2: ...
        Priority: ...

        Tasks:
        {tasks}
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "tasks": state["tasks"]
    })

    return {
        "priority": response.content
    }


 
def smart_plan_node(state: TaskPlannerState):

    prompt = ChatPromptTemplate.from_template(
        """
        Create a smart and practical task plan.

        Original tasks:
        {tasks}

        Task classification:
        {classification}

        Task priority:
        {priority}

        Instructions:
        - Put high-priority tasks first.
        - Suggest the best order to complete the tasks.
        - Do not add unrelated tasks.
        - Use a numbered list.
        - Give a short reason for the order.

        Return only the smart plan.
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "tasks": state["tasks"],
        "classification": state["classification"],
        "priority": state["priority"]
    })

    return {
        "smart_plan": response.content
    }

builder = StateGraph(TaskPlannerState)



builder.add_node("summarize", summarize_node)
builder.add_node("classify", classify_node)
builder.add_node("prioritize", priority_node)
builder.add_node("smart_plan", smart_plan_node)


builder.add_edge(START, "summarize")
builder.add_edge("summarize", "classify")
builder.add_edge("classify", "prioritize")
builder.add_edge("prioritize", "smart_plan")
builder.add_edge("smart_plan", END)

 
graph = builder.compile()
def run_task_planner(tasks: str):

    return graph.invoke({
        "tasks": tasks,
        "summary": "",
        "classification": "",
        "priority": "",
        "smart_plan": ""
    })



if __name__ == "__main__":

    print("Enter your tasks.")
    print("Write all tasks in one paragraph or separate them with periods.\n")

    user_tasks = input("Tasks:\n")

    result = graph.invoke({
        "tasks": user_tasks,
        "summary": "",
        "classification": "",
        "priority": "",
        "smart_plan": ""
    })

    print("\n" + "=" * 60)
    print("AI TASK MANAGER & PLANNER GRAPH")
    print("=" * 60)

    print("\nSUMMARY:")
    print(result["summary"])

    print("\nCLASSIFICATION:")
    print(result["classification"])

    print("\nPRIORITY:")
    print(result["priority"])

    print("\nSMART PLAN:")
    print(result["smart_plan"])