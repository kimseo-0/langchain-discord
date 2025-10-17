from typing import Optional
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import requests, os
from typing import Any, Dict
from pydantic import BaseModel, Field
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

## INFO: The following code is not used anymore, but I keep it here for reference. It is good to keep for the future when more errors are handled by the package.

class DiscordWebhookInput(BaseModel):
   webhook_message: str = Field(description="The message you want to send to the webhook")

class DiscordWebhookTool(BaseTool):
    name: str = "discord_webhook"
    description: str = "useful for when you need to send a webhook message"
    args_schema : Type[BaseModel] = DiscordWebhookInput

    def _validate_inputs(self, webhook_message: str) -> Dict:
       if not webhook_message:
           raise ValueError("webhook_message is required")
       return None

    def _run(self, webhook_message: str) -> str:
        if(os.environ.get("WEBHOOK_URL") is None): raise ValueError("WEBHOOK_URL environment variable not set")
        if(os.environ.get("WEBHOOK_URL") is None): raise ValueError("WEBHOOK_URL environment variable not set")
        
        WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
        WEBHOOK_USERNAME = os.environ.get("WEBHOOK_USERNAME", "LangChain Agent")

        answer = requests.post(WEBHOOK_URL, 
                      json={
                            "content": webhook_message, 
                            "username": WEBHOOK_USERNAME
                        }, 
                      headers={"Content-Type": "application/json"}
        )
    
        if(answer.status_code != 204 and answer.status_code != 200):
            raise Exception("Webhook message could not be sent! Please check your webhook URL and message and try again.")
        else:
            return "Webhook message sent successfully!"

    
    def _arun(self, webhook_message: str, webhook_url: str, webhook_username: str): raise NotImplementedError("This tool does not support async")

