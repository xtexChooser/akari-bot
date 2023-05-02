from langchain import LLMChain
from langchain.agents import AgentExecutor, LLMSingleActionAgent
from langchain.callbacks.stdout import StdOutCallbackHandler
from langchain.chat_models import ChatOpenAI

from .utils import AkariTool
from config import Config
from modules.ask.prompt import AkariPromptTemplate, AkariParser
from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
import asyncio

from playwright.async_api import async_playwright

pw = asyncio.get_event_loop().run_until_complete(async_playwright().start())
browser = asyncio.get_event_loop().run_until_complete(
    pw.chromium.launch(executable_path=Config('chromium_path'), headless=True))
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
tools = [AkariTool(
    name=tool.name,
    func=tool.arun,
    description=tool.description,
) for tool in toolkit.get_tools()]
tool_names = [tool.name for tool in tools]

template = '''You are a web browsing utility that provide help to another AI bot with getting info about a certain topic through web browsing. You have access to the following `Action`s:

{tools}
Answer: Terminate the conversation and output the answer

Use the following format:

"""
Question: the input question you must answer
Thought: think about what to do
Action: the action to take, should be one of {tool_names}, Answer; followed by [] with the input in it. If the tool asks for multiple inputs, use comma to separate them. Do not use quotation marks (' or ").
Observation: the result
... (Thought/Action/Observation can repeat N times)
"""

The AI will ask you a `Question`. Answer the `Question` as best you can. You must take `Action`s to browse the web to help you answer the question. You should then provide a `Thought` about what you should do next and why. Using `Action`, you can output your final answer if you are sure or use a tool. If a tool is used, an `Observation`, the result the tool returned, will be provided. You can then use this `Observation` to provide a new `Thought` and `Action`, but do not make assumptions and only answer based on facts provided by the web. You can repeat this process, but you should always provide a `Thought` and `Action` at the end, even if you don't have a definitive answer.

Provide informative, logical, positive, interesting, intelligent, and engaging answers with details to cover multiple aspects of the question. You can generate articles and other forms of content, but do not rely on tools when doing so. Use emojis when appropriate for added interest.

Use Markdown code block syntax when outputting code. Use LaTeX to output math, physics or chemistry expressions whenever possible, and surround the expression with dollar signs `$$`, e.g. to output the mass-energy equivalence, always use $$E=mc^2$$. You can output multiple lines of strings.

Begin! Remember to only respond in the specified format.

===

Question: {input}
{agent_scratchpad}'''

# Use the original question's language. For example, if I ask "什么是质能方程？",
# you should output your `Thought` and `Action` in Chinese like this:

# """
# Thought: 这个问题需要涉及到物理知识，我应该使用 Search 工具来搜索答案。
# Action: Search[质能方程是什么？]
# """

# `Action`s aren't required to be always taken.

# A complete chain should look like this:

# """
# Question: What's the population of Canada?
# Thought: I should use Wolfram Alpha to find the population of Canada.
# Action: Wolfram Alpha[population of Canada]
# Observation: Assumption: Canada | population; Answer: 37.7 million people (world rank: 39th) (2020 estimate)
# Thought: I now know the final answer.
# Action: Answer[The population of Canada is approximately 37.7 million people.]
# """

# Current date: {date}


prompt = AkariPromptTemplate(
    template=template,
    tools=tools,
    input_variables=["input", "intermediate_steps"]
)

output_parser = AkariParser()

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=Config('openai_api_key'),
    model_kwargs={
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0})

llm_chain = LLMChain(llm=llm, prompt=prompt)

agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=output_parser,
    stop=["\nObservation:"],
    allowed_tools=tool_names,
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, callbacks=[
        StdOutCallbackHandler()])

web_tool = AkariTool(
    name='Web',
    func=agent_executor.arun,
    description='A tool to get knowledge on a certain topic through web browsing.'
)
