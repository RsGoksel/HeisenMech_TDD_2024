from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
import os
from openai import OpenAI

from config import Config
Config = Config()

def get_conversation():

    groq_chat = ChatGroq(
            model_name = Config.model,
            api_key    = Config.API
            )
    
    chat_history = []
    
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=Config.system_prompt 
            ),  
    
            MessagesPlaceholder(
                variable_name="chat_history"
            ),  
    
            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            ),  
        ]
    )
    
    
    conversation = LLMChain(
        
        llm     = groq_chat,  
        prompt  = prompt,  
        verbose = False,  
        memory  = ConversationBufferWindowMemory(k=Config.memory, memory_key="chat_history", return_messages=True),  
    )
    
    return conversation


   
def Get_Nvidia(api):

    return OpenAI(
      base_url = "https://integrate.api.nvidia.com/v1",
        #  "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" number 1
        #  "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" number 2
      api_key = api
    )

def predict(client, string): 
    completion = client.chat.completions.create(
      model="nvidia/nemotron-4-340b-instruct",
      #model = "nvidia/nemotron-4-340b-reward",
      messages=[{"role":"user","content": string}],
      temperature=0.5,
      top_p=0.7,
      max_tokens=2048,
      #stream=True
    )


    
    return completion.choices[0].message.content
    # for chunk in completion:
    #   if chunk.choices[0].delta.content is not None:
    #     print(chunk.choices[0].delta.content, end="")
    

