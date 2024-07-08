def Query_from_groq(query, co, groq, index):

    # global keyword tells Python to use the global variables from the global scope
    # global co, groq, index

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
    Important: Based on the above context only, provide a response that addresses the user's query. Do not include any information or assumptions outside of the provided context. Ensure the response promotes mental health, well-being, personal development, and self-discovery.

    Response:
    """

    # Generate the response
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_template,
            }
        ],
        model="gemma-7b-it",
    )

    return chat_completion.choices[0].message.content
