from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from serpapi_search_tools import web_search
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# memory implementation
from langgraph.checkpoint.memory import InMemorySaver


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash");


agent = create_agent(
    model=llm,
    tools=[
        web_search(),
    ],
    system_prompt = "You are a search agent and can search for any question on Google",
    checkpointer = InMemorySaver()
);

while True:
    query = input("User : ");

    if query.lower() in ['quit', 'bye', 'exit']:
        print("Good Bye 👋");
        break;

    result = agent.invoke(
    {"messages": [{"role": "user", "content": query}]},
    {"configurable" : {"thread_id" : "1"}}
    )
    print("AI :", result['messages'][-1].content);


