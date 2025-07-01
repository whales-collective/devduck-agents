import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

#from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.runners import InMemoryRunner # Use InMemoryRunner
from google.genai import types # For types.Content
from typing import Optional
from google.adk.models import LlmResponse, LlmRequest


LiteLlm.set_verbose = True


root_agent = Agent(
    model=LiteLlm(
        model=f"openai/{os.environ.get('CEREBRAS_CHAT_MODEL')}",
        api_base=os.environ.get('CEREBRAS_BASE_URL'),  
        api_key=os.environ.get('CEREBRAS_API_KEY'),         # your API key directly here        
    ),
    name=os.environ.get('CEREBRAS_AGENT_NAME'),
    description=os.environ.get('CEREBRAS_AGENT_DESCRIPTION'),
    instruction=os.environ.get('CEREBRAS_AGENT_INSTRUCTION'),
)


