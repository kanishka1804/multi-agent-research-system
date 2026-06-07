import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url, fact_check
from dotenv import load_dotenv

load_dotenv()


def get_llm(api_key=None):
    """Get LLM — key passed directly, fallback to env."""
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key or os.environ.get("GROQ_API_KEY")
    )


# 1st agent - Search (direct tool call)
def build_search_agent():
    def run(query: str) -> str:
        return web_search.invoke(query)
    return run


# 2nd agent - Reader (direct tool call)
def build_reader_agent():
    def run(url: str) -> str:
        return scrape_url.invoke(url)
    return run


# 3rd agent - Fact Checker (direct tool call)
def build_fact_checker_agent():
    def run(claim: str) -> str:
        return fact_check.invoke(claim)
    return run


# Writer prompt
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (ONLY list real URLs that appear in the Research Gathered above.
  DO NOT invent, guess, or hallucinate any sources.
  If no URLs are found, write "No verified URLs available.")

Be detailed, factual and professional.
Only use information from the Research Gathered above. Do not add outside knowledge or made-up statistics."""),
])


# Critic prompt
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be concise and specific."),
    ("human", """Review the report below strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])


# Fact checker prompt
fact_checker_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a precise fact-checker. Be concise."),
    ("human", """Fact-check the 3 most important claims from this report.

Report:
{report}

Fact-Check Evidence:
{evidence}

Respond in this exact format:

Claim 1: ...
Verdict: ✅ Verified / ❌ False / ⚠️ Partially True
Evidence: ...

Claim 2: ...
Verdict: ✅ Verified / ❌ False / ⚠️ Partially True
Evidence: ...

Claim 3: ...
Verdict: ✅ Verified / ❌ False / ⚠️ Partially True
Evidence: ...

Overall Credibility: X/10"""),
])


def get_writer_chain(api_key=None):
    return writer_prompt | get_llm(api_key) | StrOutputParser()

def get_critic_chain(api_key=None):
    return critic_prompt | get_llm(api_key) | StrOutputParser()

def get_fact_checker_chain(api_key=None):
    return fact_checker_prompt | get_llm(api_key) | StrOutputParser()


# kept for backward compatibility
writer_chain       = None
critic_chain       = None
fact_checker_chain = None