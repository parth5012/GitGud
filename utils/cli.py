from colorama import Fore,Style
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage



def output(chatbot, user_input):
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
                    yield (f"\n{Fore.YELLOW}[THOUGHT] I'll use {tool['name']}...{Style.RESET_ALL}")
            
            # B: Check for Text Content (Streaming Phase)
            if message_chunk.content:
                content = message_chunk.content
                # Handle the list/dictionary structure error
                if isinstance(content, list):
                    text_parts = [part.get('text', '') for part in content if isinstance(part, dict)]
                    yield ("".join(text_parts))
                else:
                    yield (content)

        # 2. Handle Tool Messages (Action Phase)
        elif isinstance(message_chunk, ToolMessage):
            tool_name = getattr(message_chunk, "name", "tool")
            print(f"\n{Fore.CYAN}[ACTION] Executing {tool_name}!!{Style.RESET_ALL}")

