from agent import run_once


def main():
    messages = []

    while True:
        query = input("mini-agent >>> ").strip()

        if query.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not query:
            continue

        messages.append({"role": "user", "content": query})
        answer = run_once(messages)
        print(answer)


if __name__ == "__main__":
    main()
