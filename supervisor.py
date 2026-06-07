from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

supervisor_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research supervisor. Be concise and directive."),
    ("human", """Research Topic: {topic}

Generate a focused research plan.

Respond in this exact format:

Search Queries:
- ...

Key Questions to Answer:
1. ...
2. ...
3. ...

Quality Expectations:
- ..."""),
])


def run_supervisor(topic: str) -> dict:
    """Analyze topic and return structured plan for all agents."""

    print("\n[Supervisor] Analyzing topic and creating research plan...")

    # built inside function so it picks up key set at runtime from sidebar
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=os.environ.get("GROQ_API_KEY")
    )

    supervisor_chain = supervisor_prompt | llm | StrOutputParser()
    plan = supervisor_chain.invoke({"topic": topic})

    # extract search queries from plan
    lines = plan.split("\n")
    queries = []
    for i, line in enumerate(lines):
        if line.strip().startswith("-") and i > 0:
            prev = lines[i-1].strip().lower()
            if "search" in prev or line.strip()[2:].endswith("?") or len(queries) < 3:
                q = line.strip()[2:].strip()
                if q:
                    queries.append(q)

    # fallback if parsing fails
    if not queries:
        queries = [topic]

    return {
        "plan": plan,
        "queries": queries[:1]  
    }
