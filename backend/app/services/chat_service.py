def generate_answer(context, question):

    question = question.lower()

    for paragraph in context.split("\n"):

        if any(word in paragraph.lower() for word in question.split()):
            return paragraph

    return "I don't know based on the uploaded company documents."