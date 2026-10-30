from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_core.output_parsers import StrOutputParser
out = StrOutputParser();

from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash"); 

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-120b", streaming=True);

import streamlit as st



st.title("Ask me anything 💬 - QnA Bot")
st.markdown("This is a simple QnA bot that uses Google Gemini and LangChain to answer your questions. Type your question below and hit enter to get an answer.")

if "messages" not in st.session_state:
    st.session_state.messages = [];

for message in st.session_state.messages:
    role = message["role"];
    content = message["content"];
    st.chat_message(role).markdown(content);

query = st.chat_input("Ask me anything ?");


# In Python, "with" creates a context in which the statements inside it are executed. Here, Streamlit uses that context to place the output inside the assistant's chat message.

if query:
    st.session_state.messages.append({"role": "user", "content": query});
    st.chat_message("user").markdown(query);
    res = llm.stream(query);
    
    with st.chat_message("ai"):
        text = "";
        markdown_placeholder = st.empty();
        for chunks in res:
            text += chunks.content;
            markdown_placeholder.markdown(text);
    
    st.session_state.messages.append({"role": "assistant", "content": text});
     

# while True:
#     query = input("User : ");

#     if query.lower() in ['quit', 'bye', 'exit']:
#         print("Good Bye 👋");
#         break;

#     res = llm.invoke(query);
#     text = out.invoke(res);
#     print("AI : ", text, "\n")

