
from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check API Key
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Configure external Gemini-compatible OpenAI client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configure runner
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the agent
agent = Agent(
    name="translator",
    instructions="You are a helpful translator. Always translate English sentences into clear and simple Urdu."
)


# Continuous input loop
print("💬 English to Urdu Translator (type 'exit' to quit):\n")
while True:
    user_input = input("👉 Enter English sentence: ").strip()
    if user_input.lower() == "exit":
        print("👋 Exiting translator.")
        break

    # Run the translation
    try:
        response = Runner.run_sync(
            agent,
            input=user_input,
            run_config=config
        )
        print("📘 Urdu Translation:", response, "\n")
    except Exception as e:
        print("❌ Error:", e)










# from dotenv import load_dotenv
# import os 
# from agents import Agent , Runner, AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig

# load_dotenv()
# gemini_api_key = os.getenv ("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )


# agent = Agent(
#     name= "translator ",
#     instructions= "you are a helpful translator. Always translate english sentences into clear and simple urdu. ",

# )

# response = Runner.run_sync(
#     agent,
#     input=" my name is Rao hasaan, I am 18 year old.",
#     run_config = config

# )

# print(response)