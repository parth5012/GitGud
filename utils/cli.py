import json
from colorama import Fore, Style
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


def output_stream(chatbot, user_input):
    inputs = {"messages": [HumanMessage(content=user_input)]}

    for message_chunk, metadata in chatbot.stream(
        inputs,
        stream_mode="messages",
    ):
        # 1. Handle AI Messages (Thoughts & Text)
        if isinstance(message_chunk, AIMessage):
            # A: Check for Tool Calls (Thinking Phase)
            if message_chunk.tool_calls:
                for tool in message_chunk.tool_calls:
                    print (
                        f"\n{Fore.YELLOW}[THOUGHT] I'll use {tool['name']}...{Style.RESET_ALL}",
                        end="",flush=True
                    )

            # B: Check for Text Content (Streaming Phase)
            if message_chunk.content:
                content = message_chunk.content
                # Handle the list/dictionary structure error
                if isinstance(content, list):
                    text_parts = [
                        part.get("text", "")
                        for part in content
                        if isinstance(part, dict)
                    ]
                    print("".join(text_parts),end="",flush=True)
                        
                else:
                    print(content,end="",flush=True)

        # 2. Handle Tool Messages (Action Phase)
        elif isinstance(message_chunk, ToolMessage):
            tool_name = getattr(message_chunk, "name", "tool")
            print(f"\n{Fore.CYAN}[ACTION] Executing {tool_name}!!{Style.RESET_ALL}",end="",flush=True)


def _format_tool_content(content) -> str:
    """Convert tool output (str, dict, list) to a readable string."""
    if isinstance(content, str):
        return content
    try:
        return json.dumps(content, indent=2, default=str)
    except Exception:
        return str(content)


# Change to async def
async def async_output_stream(chatbot, user_input):
    inputs = {"messages": [HumanMessage(content=user_input)]}

    # Use .astream instead of .stream and 'async for'
    async for message_chunk, metadata in chatbot.astream(
        inputs,
        stream_mode="messages",
    ):
        # 1. Handle AI Messages (Thoughts & Text)
        if isinstance(message_chunk, AIMessage):
            # A: Check for Tool Calls (Thinking Phase)
            if message_chunk.tool_calls:
                for tool in message_chunk.tool_calls:
                    # yield works the same way in async generators
                    yield (f"\n[THOUGHT] I'll use {tool['name']}...")

            # B: Check for Text Content (Streaming Phase)
            if message_chunk.content:
                content = message_chunk.content
                if isinstance(content, list):
                    text_parts = [
                        part.get("text", "")
                        for part in content
                        if isinstance(part, dict)
                    ]
                    yield ("".join(text_parts))
                else:
                    yield (content)

        # 2. Handle Tool Messages (Action Phase)
        elif isinstance(message_chunk, ToolMessage):
            tool_name = getattr(message_chunk, "name", "tool")
            # Yield the "executing" label
            yield (f"\n[ACTION] Executed {tool_name}:")
            # Yield the actual tool result so it's always visible in the UI,
            # even if the LLM later silently drops or misrepresents the data.
            raw_content = _format_tool_content(message_chunk.content)
            if raw_content:
                yield (f"\n{raw_content}")