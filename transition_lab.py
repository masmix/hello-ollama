import os
import ollama

# 1. LOCAL DATA FEED: The Planned IT Infrastructure & Monitoring Architecture
MONITORING_SPEC = """
SERVICE TRANSITION ARCHITECTURE SPECIFICATION
ENVIRONMENT: Production E-Commerce Checkout Cluster
MONITORING TOOLSTACK: Prometheus + Grafana + Alertmanager
METRIC THRESHOLDS PLANNED:
- CPU Utilization: Critical alert if > 85% for sustained 5 minutes.
- HTTP 5xx Error Rates: Critical alert if > 2% of total traffic over a 1-minute window.
- Disk I/O: Warning alert if latency > 20ms.

ALERT ROUTING & ESCALATION:
- Tier 1: Slack notification to #ops-alerts immediately.
- Tier 2: PagerDuty call to On-Call Engineer if Tier 1 is unacknowledged within 10 minutes.
"""

# 2. THE INCIDENT SCENARIO SIMULATION (The "Chaos Engine" Input)
SIMULATED_FAILURE_EVENT = """
INCIDENT INJECTION FOR TESTING:
At 14:02, a broken database migration script causes the E-Commerce Checkout API to drop 15% of all client connections, returning HTTP 500 Internal Server Errors. 
CPU utilization drops significantly to 12% because transactions are failing instantly instead of processing.
"""

# 3. CONSTRUCT THE TRANSITION PROMPT
user_query = (
    "Analyze the simulated failure event against the planned monitoring thresholds. "
    "Will our planned alert configuration successfully detect this specific issue? "
    "Identify any gaps or risks of alert failure or delayed escalation. "
    "Format your assessment nicely using Markdown headings, bullet points, and tables."
)

system_instructions = (
    "You are an expert ITIL Service Transition and Reliability Engineering assistant. "
    "Analyze configuration designs and failure parameters strictly using the provided documents."
)

prompt_payload = f"""
[PLANNED MONITORING SPECIFICATION]:
{MONITORING_SPEC}

[SIMULATED INCIDENT DATA]:
{SIMULATED_FAILURE_EVENT}

[TRANSITION VALIDATION TASK]:
{user_query}
"""

print("[*] Simulating service transition event locally inside Llama...")

try:
    response = ollama.chat(
        model='llama3.2',
        messages=[
            {'role': 'system', 'content': system_instructions},
            {'role': 'user', 'content': prompt_payload},
        ]
    )
    
    analysis_output = response['message']['content']
    
    # 4. EXPORT TO LOCAL MARKDOWN FILE
    output_filename = "service_transition_assessment.md"
    with open(output_filename, "w", encoding="utf-8") as md_file:
        md_file.write(f"# Service Transition Simulation Lab - Run Report\n\n")
        md_file.write(f"## 📋 Inputs Evaluated\n\n")
        md_file.write(f"### Planned Monitoring Specs:\n```text\n{MONITORING_SPEC.strip()}\n```\n\n")
        md_file.write(f"### Injected Incident Event:\n```text\n{SIMULATED_FAILURE_EVENT.strip()}\n```\n\n")
        md_file.write(f"## 🤖 LLM Analysis & Assessment Output\n\n")
        md_file.write(analysis_output)
        
    print(f"\n[+] Success! Report safely compiled and saved locally to: {output_filename}")

except Exception as e:
    print(f"\n[!] Local Ollama simulation failed: {e}")
