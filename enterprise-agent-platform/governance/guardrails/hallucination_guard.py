def check_hallucination(
    text: str
):

    blocked_phrases = [

        "I searched the web",

        "According to Google",

        "I found online",

        "Based on internet search"
    ]

    for phrase in blocked_phrases:

        if phrase.lower() in text.lower():

            raise ValueError(
                f"Hallucination detected: {phrase}"
            )

    return True