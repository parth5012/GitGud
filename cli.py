from textual.app import App, ComposeResult
from textual.widgets import Input, Markdown, Footer, Header, Static
from textual.containers import VerticalScroll
from utils.graphs import build_core_graph
from utils.cli import async_output_stream


class GitGud(App):
    CSS = """
    #chat_history { height: 1fr; border: solid green; padding: 1; }
    Input { dock: bottom; margin-top: 1; }
    """

    def __init__(
        self, driver_class=None, css_path=None, watch_css=False, ansi_color=False
    ):
        self.graph = build_core_graph()
        super().__init__(driver_class, css_path, watch_css, ansi_color)

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="chat_history"):
            yield Markdown("Welcome! How can I help you today?")
        yield Input(placeholder="Type your message...")
        yield Footer()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        # Get user message
        user_message = event.value
        container = self.query_one("#chat_history")

        # Clear input
        self.query_one(Input).value = ""

        # Add user message to history
        await container.mount(Markdown(f"**You:** {user_message}"))

        # Add bot response
        # 1. Create a placeholder for the streaming response
        bot_response_area = Static("Thinking...", classes="msg")
        await container.mount(bot_response_area)
        container.scroll_end()

        updated_text = "Agent:  "
        # 2. Iterate over the stream and update the widget
        async for chunk in async_output_stream(self.graph, user_message):
            updated_text += chunk
            bot_response_area.update(updated_text)
            container.scroll_end()


if __name__ == "__main__":
    GitGud().run()
