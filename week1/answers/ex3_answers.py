"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  I'm calling to confirm a booking.
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  I'm calling to confirm a booking.
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  I'm calling to confirm a booking.
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
The CALM agent identified the parking request as out-of-scope because 
it didn't match any Flow Descriptions in flows.yml. 
It triggered the utter_out_of_scope template from domain.yml to redirect the user, 
but then immediately steered the conversation back to the unfinished booking flow. 
This ensured the primary business task was completed by automatically resuming the conversation exactly where it was interrupted."""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In Exercise 2, the LangGraph agent relied on the ReAct loop and LLM reasoning to inspect the Tool Registry. 
Finding no match, it defaulted to its internal knowledge to generate a "helpful refusal."
In contrast, Rasa CALM uses a more deterministic approach via Flows and Guardrails. 
Instead of the LLM "improvising" a response, Rasa CALM identifies the intent as out_of_scope and triggers a specific policy or conversation flow. 
This ensures the agent stays within the defined Business Logic rather than relying on the LLM's general training.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I followed these steps:
1.Used the 'if True' hack in actions.py to trigger the guard since it was currently midnight.
2.Retrained the model using uv run rasa train.
3.Restarted the action server.
4.Started a session via rasa shell and provided the information for the required slots.
5.Confirmed that the agent correctly escalated with the 'insufficient time' message.
This works because ActionValidateBooking is called by the Rasa Server only after CALM finishes collecting all slots defined in flows.yml
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
The transition to CALM gains flexibility and efficiency. 
By offloading NLU examples and regex to the LLM's "probabilistic reasoning", 
the agent handles synonyms and natural speech (like 'about 160') out of the box. 

However, this costs "absolute predictability". While we trust the LLM to handle the "language," 
we still use Python for "business rules" because they must remain deterministic. 
You cannot 'reason' with a capacity limit or a 4:45 PM cutoff; 
these require the hard logic of Python to ensure the assistant never negotiates away requirements.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The heavy setup of Rasa CALM buys you "conversation control and safety". 
Unlike LangGraph, which can improvise responses or hallucinate steps using its ReAct loop, CALM is restricted to defined "Flows". 
The CALM agent cannot call a tool that isn't in flows.yml
or improvise a response it wasn't trained for. While this seems like a limitation, 
it is actually a "critical feature" for a booking assistant. It prevents the 'hallucination' seen in Exercise 2, 
ensuring the agent stays strictly within "business boundaries" 
and only executes actions that are legally and operationally safe for the company.
"""