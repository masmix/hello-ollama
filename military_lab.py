import ollama

# 1. CREATE A FICTIONAL, NON-SENSITIVE EXERCISE SCENARIO
INTEL_FILE = "op_order_alpha.txt"
with open(INTEL_FILE, "w", encoding="utf-8") as f:
    f.write("""FICTIONAL TABLETOP EXERCISE — SYNTHETIC DATA ONLY
Scenario: Alpha Shield (invented; not based on a real operation or location)
Time: 0700 exercise time
Conditions: Dense fog; visibility is below 200 m and is expected through 1400.
Exercise asset: SkyEye-1, a fictional observation drone.
Exercise constraint: A fictional communications-interference hazard has been
reported, but its source, range, and likelihood are unknown.
Known limitation: No information is provided about the drone's weather rating,
communications resilience, or applicable safety procedures.
""")

print(f"[*] Wrote synthetic exercise data to: {INTEL_FILE}")

# 2. READ THE EXERCISE DATA
with open(INTEL_FILE, "r", encoding="utf-8") as f:
    exercise_data = f.read()

# 3. BUILD A GROUNDED, STRUCTURED PROMPT
user_query = "For this fictional tabletop exercise, summarize the decision factors at 0700."

system_instructions = (
    "You are analyzing a fictional, non-operational tabletop exercise using synthetic data. "
    "Use only facts in the supplied scenario; do not invent capabilities, probabilities, "
    "or procedures. Distinguish known facts from unknowns. Do not provide real-world "
    "deployment instructions. Be concise and use this format: Facts, Uncertainties, "
    "General safety considerations, Information needed for a qualified decision-maker."
)

prompt_payload = f"""
<synthetic_exercise_data>
{exercise_data.strip()}
</synthetic_exercise_data>

<question>
{user_query}
</question>
"""

print("[*] Sending synthetic exercise data to the local Ollama model...")

# 4. RUN LOCAL INFERENCE
try:
    response = ollama.chat(
        model='llama3.2',
        messages=[
            {'role': 'system', 'content': system_instructions},
            {'role': 'user', 'content': prompt_payload},
        ]
    )
    
    # 5. DISPLAY EXERCISE OUTPUT
    print("\n================ TABLETOP EXERCISE SUMMARY ===================")
    print(response['message']['content'])
    print("==============================================================")

except Exception as e:
    print(f"\n[!] Error contacting local Ollama service: {e}")
    print("[!] Ensure Ollama is running in the background (`ollama serve`)")
