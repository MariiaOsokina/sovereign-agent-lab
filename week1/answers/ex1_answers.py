"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
- The MAIN MODEL correctly identified valid venues in all conditions. 
I suggest that since XML or Sandwich solutions combat Attention Dilution, 
they will be helpful in maintaining correct answers in cases where the prompt is longer 
and the Signal-to-Noise Ratio (SNR) is lower (more distractors).

- Interestingly, the model shifted its preference from 'The Haymarket Vaults' in PLAIN text 
to 'The Albanach' when using XML or Sandwich formatting. My suggestion is that XML tags shift 
attention weights toward different parts of the context.

- "Token Tax": We also see an increase in tokens from Plain → XML → Sandwich; 
we spend these extra tokens to buy "Attention Insurance."
"""


# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the most challenging distractor because it satisfies the high-capacity and vegan requirements, 
failing only on the 'status' check.

It is harder than 'The New Town Vault' because:

1- Exact Keyword Match: It hits the number '160' exactly. The model's attention mechanism assigns it a high relevance score 
as soon as it sees that exact match.

2 - Category vs. Status: Models prioritize 'what' a venue is (Size/Food) over administrative details (Availability). 
The model may 'skim' the status because the other attributes are a perfect match.

3- Position: The failure point (status=full) is at the very end of the line. 
By the time the model gets there, it is already very confident it has found the correct answer.

While the results of Part B remained correct despite these distractors, I suggest we might see the "Lost in the Middle" phenomenon 
and false positive answers if the model had a smaller attention budget or if the prompt were significantly longer.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """

The SMALL MODEL gives answers that are logically correct and we don't see the "Lost in the Middle" phenomenon. 
I suggest it is because the total context length was still small enough 
that the model's attention budget was not fully exhausted, keeping the signal clear even without extra structure.

However, its PLAIN answer is not fully accurate in style (omitting the article 'The'). 
My suggestion is that when XML tags were added, they acted as structural anchors that helped the small model provide 
a more complete and stable output. 
This proves that formatting doesn't just help with logic; it improves instruction adherence in smaller attention budgets.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when working with smaller models or low Signal-to-Noise environments 
where "near-miss" distractors can cause Attention Dilution. 
While structural techniques like XML or Sandwiching incur a "Token Tax," they provide necessary structural anchors 
and leverage the Recency Effect to ensure the model stays focused on the specific constraints of the task. 
This leads to more robust and stable agent behavior.
"""
