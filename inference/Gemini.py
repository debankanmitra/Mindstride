import google.generativeai as genai


def Query_from_gemini(query, co, index):

    # # global keyword tells Python to use the global variables from the global scope
    # global co, index

    if co is None or index is None:
        raise ValueError(
            "The global variables 'co' and 'index' must be initialized before using this function."
        )

    # create the query embedding
    xq = co.embed(
        texts=[query],
        model="embed-english-light-v3.0",
        input_type="search_query",
        truncate="END",
    ).embeddings[0]

    # query, returning the top 3 most similar results
    query_results = index.query(vector=xq, top_k=3, include_metadata=True)

    # concatenate results
    context = ""
    for match in query_results["matches"]:
        context += match["metadata"]["text"]

    # Define the prompt template
    prompt_template = f"""
User Query: {query}

Context: {context}

Instructions: Based on the above context only, provide a response that addresses the user's query. Do not include any information or assumptions outside of the provided context. Ensure the response promotes mental health, well-being, personal development, and self-discovery. 

Important: The user query should strictly be related to mental health, personal growth, self-improvement, well-being, personal development, or self-discovery. If the user query is not related to any of these topics, respond with 'The query is not related to mental health, personal growth, self-improvement, well-being, personal development, or self-discovery. Please ask something related to these topics.'

Response:
"""


    # Generate the response
    model = genai.GenerativeModel("gemini-1.5-flash")
    # Generate the response using the model
    response = model.generate_content(prompt_template)

    return response.text
