"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP =  5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
the agent's behaviour did NOT change because the tool implemented graceful degradation, 
maintaining its interface contract by substituting the stochastic FLUX generator with a deterministic placehold.co REST API call, 
ensuring the LangGraph loop received the expected success schema and image URL.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user wanted to check The Bow Bar first for 160 vegan guests. The first tool response showed that The Bow Bar's capacity is only 80, which is way below the required 160. 
So, it didn't meet the requirements. Then, the assistant moved on to check The Albanach next. The response for The Albanach shows a capacity of 180, which is more than 160, and they do have vegan options. The status is available, and meets_all_constraints is true. 
That means The Albanach is a suitable
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Okay, let's see. The user wants a venue for 300 people with vegan options. The known venues are The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one using the check_pub_availability function.\n\nThe Albanach has a capacity of 180, which is under 300. Haymarket Vaults is 160, also too small. 
Guilford Arms has 200 capacity but doesn't offer vegan options. 
The Bow Bar has 80 capacity and vegan, but it's full. 
None of them meet both the capacity and vegan requirements. So I need to inform the user that none of the available venues can accommodate their request. They might need to look for other options outside the known list or adjust their requirements.\n</think>\n\n
None of the known Edinburgh venues can accommodate 300 guests with vegan options. The closest options had either insufficient capacity (The Albanach: 180, Haymarket Vaults: 160, Bow Bar: 80) or lacked vegan provisions (Guilford Arms: 200 capacity). 
You may need to consider alternative venues outside this list or adjust your requirements.",
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """Okay, the user is asking about the last train time from Edinburgh Waverley to London tonight. Let me check the tools provided.\n\nLooking at the available functions: check_pub_availability, get_edinburgh_weather, calculate_catering_cost, generate_event_flyer. None of these are related to train schedules. The functions are for checking pub availability, weather, catering costs, and generating flyers. \n\nSince there's no tool for train times, I can't use any of the provided functions to answer this." \
I need to inform the user that I don't have access to that information and suggest they check a train service website or app.
I don't have access to real-time train schedules or transportation data. 
For the most accurate information about the last train from Edinburgh Waverley to London, 
I recommend checking:\n1. The National Rail website (https://www.nationalrail.co.uk)\n2. 
Train service apps like Citymapper or Trainline\n3. The specific train operator's website (e.g., LNER)\n\n
Would you like help with anything related to Edinburgh pubs, weather, or event planning instead?"
"""
# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this is acceptable and user-friendly because the agent correctly identified the request as out-of-scope and
avoided hallucinating a fake schedule.
The agent checked its available "State" (the list of tools it has access to) and 
realized none of the keys matched the "train" query. 
This shows the System Prompt and Reasoning Loop are working correctly.
Instead of just saying "Error: Tool Not Found," 
it provided a natural language explanation and helpful alternatives.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """

1. Graph Topology (Shape)
LangGraph: It is Cyclic. The tools --> agent arrow creates a loop. 
This allows the agent to fail, retry, or change tools as many times as it needs until the task is done.
Rasa CALM: It is Acyclic (Linear). Once a flow starts (like confirm_booking), it follows a specific sequence of steps 
(collect → collect → action). It doesn't loop back to "think" about what to do next; it just follows the recipe.

2. Decision Authority
LangGraph: The LLM decides the routing at every single step. 
If you ask for the weather twice, the graph allows it because the model is in control of the logic.
Rasa CALM: The Developer decides the routing at design-time. The LLM only decides which flow to start. 
Once inside confirm_booking, the "Director" is the Rasa engine, ensuring the agent doesn't skip a mandatory step
like collecting the deposit_amount_gbp.

3. Business Safety vs. Creativity
LangGraph (Research Agent): Ideal for "Researching." 
You can't predict how many pubs the agent will have to check. It needs to be "creative" and pivot.

Rasa CALM (Confirmation Agent): Ideal for "Transactions." 
When dealing with money (deposits) and real bookings, you want the agent to follow a strict script so 
that it is auditable—meaning you can look at the code and guarantee it will always ask for the guest count before confirming.

"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most surprising behavior was how the agent autonomously sequenced tools in Task A by 
reasoning through the docstrings of all available functions. In Task C, Scenario 2, I was 
impressed that even with an impossible constraint of 300 guests, the agent systematically 
checked every venue and returned a grounded result without hallucinating, stating: 
'None of them meet both the capacity and vegan requirements.'
"""