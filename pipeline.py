from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain, fact_checker_chain
from agents import build_fact_checker_agent
from supervisor import run_supervisor
import os

def run_research_pipeline(topic: str) -> dict:

    state = {}

    # step 0 - supervisor plans the research
    print("\n" + " =" * 50)
    print("step 0 - Supervisor is planning the research ...")
    print("=" * 50)

    supervisor_output = run_supervisor(topic)
    state["plan"] = supervisor_output["plan"]
    state["queries"] = supervisor_output["queries"]

    print("\n Supervisor Plan:\n", state["plan"])

    # step 1 - search agent runs on each query from supervisor
    print("\n" + " =" * 50)
    print("step 1 - search agent is working ...")
    print("=" * 50)

    search_agent = build_search_agent()
    all_search_results = []

    for query in state["queries"]:
        result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {query}")]
        })
        all_search_results.append(result['messages'][-1].content)

    state["search_results"] = "\n\n---\n\n".join(all_search_results)
    print("\n search result ", state['search_results'])

    # step 2 - reader agent
    print("\n" + " =" * 50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("=" * 50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results']}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content
    print("\nscraped content: \n", state['scraped_content'])

    # step 3 - writer chain
    print("\n" + " =" * 50)
    print("step 3 - Writer is drafting the report ...")
    print("=" * 50)

    research_combined = (
        f"SUPERVISOR PLAN:\n{state['plan']}\n\n"
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    print("\n Final Report\n", state['report'])

    # step 4 - fact checker
    print("\n" + " =" * 50)
    print("step 4 - Fact checker is verifying claims ...")
    print("=" * 50)

    fact_checker_agent = build_fact_checker_agent()
    fact_result = fact_checker_agent.invoke({
        "messages": [("user",
            f"Fact-check the 3 most important claims from this report:\n\n{state['report']}"
        )]
    })
    state["fact_check_evidence"] = fact_result['messages'][-1].content

    state["fact_check"] = fact_checker_chain.invoke({
        "report": state["report"],
        "evidence": state["fact_check_evidence"]
    })
    print("\n Fact Check:\n", state["fact_check"])

    # step 5 - critic chain
    print("\n" + " =" * 50)
    print("step 5 - Critic is reviewing the report ...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })
    print("\n Critic Report:\n", state['feedback'])

    # step 6 - save report to file
    os.makedirs("output", exist_ok=True)
    filename = f"output/{topic[:50].replace(' ', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Research Report: {topic}\n\n")
        f.write(f"## Supervisor Plan\n{state['plan']}\n\n")
        f.write(f"## Report\n{state['report']}\n\n")
        f.write(f"## Fact Check\n{state['fact_check']}\n\n")
        f.write(f"## Critic Feedback\n{state['feedback']}\n")

    print(f"\n Report saved to {filename}")

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)