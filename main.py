from dotenv import load_dotenv
from typing import Annotated, List
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from pydantic import BaseModel

load_dotenv()
llm = init_chat_model(model="gpt-4o")


class State(TypedDict):
    messages: Annotated[list, add_messages]
    user_question: str | None
    google_results: str | None
    bing_results: str | None
    reddit_results: str | None
    selected_reddit_urls: list[str] | None
    reddit_post_data: list | None
    google_analysis: str | None
    bing_analysis: str | None
    reddit_analysis: str | None
    final_answer: str | None


def google_search(state: State):
    pass


def bing_search(state: State):
    pass


def reddit_search(state: State):
    pass


def analyze_reddit_posts(state: State):
    pass


def retrieve_reddit_posts(state: State):
    pass


def analyze_google_results(state: State):
    pass


def analyze_bing_results(state: State):
    pass


def analyze_reddit_results(state: State):
    pass


def sythesize_analyses(state: State):
    pass


graph_builder = StateGraph(State)

graph_builder.add_node("google_search", google_search)
graph_builder.add_node("bing_search", bing_search)
graph_builder.add_node("reddit_search", reddit_search)
graph_builder.add_node("analyze_reddit_posts", analyze_reddit_posts)
graph_builder.add_node("retrieve_reddit_posts", retrieve_reddit_posts)
graph_builder.add_node("analyze_google_results", analyze_google_results)
graph_builder.add_node("analyze_bing_results", analyze_bing_results)
graph_builder.add_node("analyze_reddit_results", analyze_reddit_results)
graph_builder.add_node("sythesize_analyses", sythesize_analyses)

