from utils.graphs import build_core_graph
from utils.cli import output_stream


def main():
    graph = build_core_graph()
    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input:
                continue

            print("\nAssistant: ", end="", flush=True)
            output_stream(graph, user_input)
            print()

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print()


if __name__ == "__main__":
    main()
