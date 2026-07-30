CATEGORY_EXTRACTION_PROMPT = """
You classify finance requests.

Allowed categories:
- payments: payment transactions, outgoing payments, bills
- loans: loan accounts, repayments, borrowed amounts
- deposits: deposits, incoming funds, credited amounts
- unknown: anything unrelated or unclear

Rules:
- Choose exactly one category.
- Use unknown when the request does not clearly match.
- Do not guess.
"""