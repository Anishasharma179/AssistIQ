def generate_answer(context, question):

    if not context.strip():
        return "I couldn't find any relevant information in the uploaded company documents."

    question = question.lower()

    # Refund
    if "refund" in question:
        for line in context.split("\n"):
            if "refund" in line.lower():
                return line.strip()

    # Password
    if "password" in question or "forgot" in question or "login" in question:
        for line in context.split("\n"):
            if "password" in line.lower():
                return line.strip()

    # Office Timing
    if "time" in question or "timing" in question or "office" in question or "working" in question:
        for line in context.split("\n"):
            if "office" in line.lower() or "timing" in line.lower():
                return line.strip()

    # Email
    if "email" in question or "contact" in question or "support" in question:
        for line in context.split("\n"):
            if "email" in line.lower() or "support@" in line.lower():
                return line.strip()

    return "I couldn't find a relevant answer in the uploaded company documents."