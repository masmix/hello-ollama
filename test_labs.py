"""Local Ollama smoke tests for the prompts used by the lab scripts."""

import pytest
import ollama


MODEL = "llama3.2"
PROMPTS = [
    pytest.param(
        [{"role": "user", "content": "Say Hello World"}],
        id="hello-lab",
    ),
    pytest.param(
        [
            {
                "role": "system",
                "content": "Use only the supplied synthetic facts. Be concise.",
            },
            {
                "role": "user",
                "content": (
                    "For a fictional tabletop exercise at 0700: dense fog is expected "
                    "through 1400; an unknown communications-interference hazard was "
                    "reported; the drone's weather rating and communications resilience "
                    "are unknown. Summarize the decision factors."
                ),
            },
        ],
        id="military-lab",
    ),
    pytest.param(
        [
            {
                "role": "system",
                "content": "Analyze the supplied monitoring thresholds and incident.",
            },
            {
                "role": "user",
                "content": (
                    "CPU is critical above 85%; HTTP 5xx is critical above 2%. "
                    "A simulated database migration failure causes 15% of checkout "
                    "connections to fail with HTTP 500 while CPU drops to 12%. "
                    "Will the planned alerts detect it?"
                ),
            },
        ],
        id="transition-lab",
    ),
]


@pytest.mark.parametrize("messages", PROMPTS)
def test_local_ollama_returns_message_text(messages):
    """Each lab scenario should get a well-formed, nonempty local response."""
    response = ollama.chat(model=MODEL, messages=messages)

# Use native object attributes exclusively
    assert response.message is not None
    assert response.message.role == "assistant"
    assert isinstance(response.message.content, str)
    assert response.message.content.strip() != ""