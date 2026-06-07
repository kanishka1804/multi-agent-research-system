import os
from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


def get_tavily():
    """Get Tavily client — reads key from env set at runtime."""
    return TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and Snippets."""
    try:
        tavily = get_tavily()
        results = tavily.search(query=query, max_results=2)

        out = []
        for r in results['results']:
            out.append(
                f"Title: {r['title']}\n"
                f"URL: {r['url']}\n"
                f"Snippet: {r['content'][:150]}\n"
            )

        urls = "\n".join([f"- {r['url']}" for r in results['results']])
        out.append(f"\nALL URLS FOUND:\n{urls}")

        return "\n----\n".join(out)

    except Exception as e:
        return f"Search failed: {str(e)}"


@tool
def scrape_url(url: str) -> str:
    """Extract clean content from a URL using Tavily. Handles bot-protected sites reliably."""
    try:
        tavily = get_tavily()
        response = tavily.extract(urls=[url])

        if response and response.get("results"):
            content = response["results"][0].get("raw_content", "")
            if content:
                return content[:1500]
            else:
                return f"No content extracted from: {url}"
        else:
            return f"Tavily could not extract content from: {url}"

    except Exception as e:
        return f"Extraction failed for {url}: {str(e)}"


@tool
def fact_check(claim: str) -> str:
    """Fact-check a specific claim by searching for supporting or contradicting evidence."""
    try:
        tavily = get_tavily()
        results = tavily.search(
            query=f"fact check: {claim}",
            max_results=2,
            search_depth="advanced"
        )

        out = [f"Fact-checking: '{claim}'\n"]
        for r in results['results']:
            out.append(
                f"Source: {r['title']}\n"
                f"URL: {r['url']}\n"
                f"Evidence: {r['content'][:200]}\n"
            )

        return "\n----\n".join(out)

    except Exception as e:
        return f"Fact-check failed: {str(e)}"