# Mini CLI Agent

A small learning project for building a minimal Python CLI agent.

Current scope:

- REPL-style command-line interaction
- MiniMax through an Anthropic-compatible API
- `.env`-based local configuration
- In-process conversation history

Next step:

- Add the first tool, `bash`, then feed tool results back into the model loop.

## Setup

```bash
cd /Users/fangfei/Desktop/codex-fei/experience/mini-cli-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` with your real MiniMax API key. Do not commit `.env`.

## Run

```bash
python3 main.py
```

Use `quit` or `exit` to leave the REPL.
