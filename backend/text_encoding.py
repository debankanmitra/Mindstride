# process of converting human-readable text into a numerical representation 
# that can be understood and processed by machine learning models.
# Model Compatibility: Machine learning models expect numerical input, 
# so encoding is essential for working with text-based tasks.

import tiktoken

tiktoken.encoding_for_model('gpt-3.5-turbo')

tokenizer = tiktoken.get_encoding('cl100k_base')

# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)