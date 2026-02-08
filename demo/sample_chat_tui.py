from textual.app import App, ComposeResult
from textual.widgets import Input, Markdown, Footer, Header
from textual.containers import Container , VerticalScroll

class GitGud(App):
    CSS = """
    #chat_history { height: 1fr; border: solid green; padding: 1; }
    Input { dock: bottom; margin-top: 1; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="chat_history"):
            yield Markdown("Welcome! How can I help you today?")
        yield Input(placeholder="Type your message...")
        yield Footer()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        # 1. Get user message
        user_message = event.value
        history = self.query_one("#chat_history")
        
        # 2. Clear input
        self.query_one(Input).value = ""
        
        # 3. Add user message to history
        await history.mount(Markdown(f"**You:** {user_message}"))
        
        # 4. (Example) Add bot response
        await history.mount(Markdown(f"**Agent:** I heard you say '{user_message}'"))
        history.scroll_end()

if __name__ == "__main__":
    GitGud().run()