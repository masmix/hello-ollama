# Repository Guidelines

## Project Structure & Module Organization

This repository contains small, standalone Python examples for running local Ollama prompts. `helllo.py` is the basic chat example; `military_lab.py` demonstrates loading a local text file into a prompt; and `transition_lab.py` analyzes a simulated monitoring incident and writes `service_transition_assessment.md`. `op_order_alpha.txt` is sample input, and `requirements.txt` pins the Python dependencies. There is no separate package, test, or asset directory. Keep generated reports and input fixtures at the repository root unless a larger structure is introduced.

## Build, Test, and Development Commands

Use Python 3 with a virtual environment and a locally installed, running Ollama service. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
ollama serve                 # In a separate terminal, if Ollama is not already running
ollama pull llama3.2
python helllo.py
python military_lab.py
python transition_lab.py
```

The scripts call the `llama3.2` model. The first two print model output; `transition_lab.py` also overwrites the assessment report. No automated test command or test framework is configured. For a quick syntax check, run `python -m py_compile helllo.py military_lab.py transition_lab.py`.

## Coding Style & Naming Conventions

Follow the existing Python style: four-space indentation, descriptive `UPPER_SNAKE_CASE` constants, and `snake_case` variables. Keep scripts readable and self-contained, and use UTF-8 when reading or writing text files. Keep model names and generated file paths explicit. If adding tooling or formatting rules, document the command here and pin it with the project dependencies.

## Testing Guidelines

There are currently no unit tests or coverage requirements. When changing prompt behavior, run the affected script with Ollama available and inspect both its console output and any generated report. Avoid treating successful model execution as a deterministic assertion; model responses can vary.

## Commit & Pull Request Guidelines

Git history is not available in this checkout, so no established commit convention can be inferred. Use short, imperative commit subjects (for example, `Add Ollama connection guidance`). Pull requests should explain the example or prompt change, list the commands used to verify it, and include relevant output or screenshots only when they clarify a behavior change. Call out any new model, dependency, or generated-file expectations.

## Security & Configuration Tips

These are local demonstrations, not secure data-handling tools. Use synthetic or non-sensitive prompt data, do not commit credentials, and check script behavior before running it: `military_lab.py` writes its sample input, and `transition_lab.py` replaces its report.
