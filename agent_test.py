# Add your OpenAI token to the .env file as -> OPENAI_API_KEY
# Add your Discord bot token to the .env file as -> DISCORD_BOT_TOKEN
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# 1. Set up the model
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)

# 2. Initialize Discord tools
from langchain_discord_shikenso import DiscordToolkit
discord_tools = DiscordToolkit().get_tools()

# 3. Define the system prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """
     You are an AI assistant that manages Discord. 
     Use the provided tools to respond to user requests.
     """
    ),
    ("user", "{question}"),
    ("placeholder", "{agent_scratchpad}")
])

# 4. Create a single agent
agent = create_openai_tools_agent(
    llm=llm,
    tools=discord_tools,
    prompt=prompt
)

# 5. Configure the agent executor
executor = AgentExecutor(
    agent=agent,
    tools=discord_tools,
    verbose=True
)

# Example usage
channel_id = 123456789 # YOUR CHANNEL ID

# Example 1: Read the last 5 messages from a Discord channel
executor.invoke({'question': f"Read the last 5 messages from Discord channel {channel_id}"})

# Example 2: Send a message in a red card format to the channel
executor.invoke({
    'question': f"Send a message saying 'HELLO' to Discord channel {channel_id} "
                f"using a red-colored card format"
})
