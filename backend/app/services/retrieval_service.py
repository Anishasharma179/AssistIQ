import os

UPLOAD_FOLDER = "storage/uploads"


def search_documents(query):

    documents = []
    sources = []

    for file in os.listdir(UPLOAD_FOLDER):

        path = os.path.join(UPLOAD_FOLDER, file)

        if os.path.isfile(path):

            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()

                documents.append(text)
                sources.append(file)

            except:
                pass

    return documents, sources