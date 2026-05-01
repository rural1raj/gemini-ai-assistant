import re

# ==============================
# 🧠 Clean & Format AI Response
# ==============================
def format_response(text):
    """
    Improve readability of AI response
    """

    if not text:
        return ""

    # Remove extra spaces
    text = text.strip()

    # Fix multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Add line breaks after sentences
    text = re.sub(r"\. ", ".\n", text)

    # Improve bullet points
    text = text.replace("•", "\n•")
    text = text.replace("- ", "\n- ")
import re


# ==============================
# 🧠 Clean & Format AI Response
# ==============================
def format_response(text):
    """
    Improve readability of AI response
    """

    if not text:
        return ""

    text = str(text).strip()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Add line breaks after sentences
    text = re.sub(r"\. ", ".\n", text)

    # Improve bullet points
    text = text.replace("•", "\n•")
    text = text.replace("- ", "\n- ")

    return text


# ==============================
# 🎯 Enhance Prompt (for better AI output)
# ==============================
def enhance_prompt(prompt):
    """
    Add extra instructions to improve AI response quality
    """

    enhancement = (
        "Answer clearly and concisely. "
        "Use bullet points if needed. "
        "Keep response simple and structured."
    )

    return f"{prompt}\n\n{enhancement}"


# ==============================
# 🔍 Highlight Keywords (SAFE FIX)
# ==============================
def highlight_keywords(text, keywords):
    """
    Highlight important keywords (Markdown safe)
    """

    if not text or not keywords:
        return text

    for word in keywords:
        if word:
            text = re.sub(
                rf"\b({re.escape(word)})\b",
                r"**\1**",
                text,
                flags=re.IGNORECASE
            )

    return text


# ==============================
# 🧾 Shorten Long Text
# ==============================
def truncate_text(text, max_length=300):
    """
    Trim long responses for preview
    """

    if not text:
        return ""

    text = str(text)

    if len(text) <= max_length:
        return text

    return text[:max_length].rsplit(" ", 1)[0] + "..."


# ==============================
# 🎯 Enhance Prompt (for better AI output)
# ==============================
def enhance_prompt(prompt):
    """
    Add extra instructions to improve AI response quality
    """

    enhancement = (
        "Answer clearly and concisely. "
        "If needed, use bullet points for better readability."
    )

    return f"{prompt}\n\n{enhancement}"


# ==============================
# 🔍 Highlight Keywords (UI friendly)
# ==============================
def highlight_keywords(text, keywords):
    """
    Highlight important keywords (for UI display)
    """

    for word in keywords:
        text = re.sub(
            f"({word})",
            r"**\1**",   # Markdown bold
            text,
            flags=re.IGNORECASE
        )

    return text


# ==============================
# 🧾 Shorten Long Text
# ==============================
def truncate_text(text, max_length=300):
    """
    Trim long responses for preview
    """

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."