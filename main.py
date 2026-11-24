import os

LINE = "Horoscope for Judge this week: Mercury retrogrades, your prompts get shorter, and a stranger brings you cake — take it, you earned it."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# The entry line is fixed and deterministic; see README.md for the text.
