import os
from langchain_community.llms import Tongyi
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Show title and description.
st.title("💬 Langchain——通义千问")


# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
if "history" not in st.session_state:
    st.session_state['history'] = ConversationBufferMemory()
    
tem = st.sidebar.select_slider(
    "选择合适的的temperature",
    options=[i/10 for i in range(0,11)])
st.write("当前temperature为", tem)
    
if tongyi_key := st.sidebar.text_input("Tongyi_API_KEY"):
    model_ty = Tongyi(temperature=tem,DASHSCOPE_API_KEY=tongyi_key)
    conversation = ConversationChain(
        llm=model_ty,  
        memory=st.session_state['history']
        )
    st.write("输入成功，请开始使用！")
else:
    st.write("请输入key后使用")

for i in st.session_state['history'].chat_memory.messages:
    st.chat_message(i.type).write(i.content)
    
if a := st.chat_input():
    st.chat_message("user").write(a)
    res = conversation.invoke(a)
    st.chat_message("AI").write(res['response'])

