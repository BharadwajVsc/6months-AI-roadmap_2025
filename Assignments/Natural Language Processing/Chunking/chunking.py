import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#sample text
text = 'full stack datascience, generative ai, agentic ai, llm model keep increasing by different companies'

#toeknizing the text
token = word_tokenize(text)

#performing parts of speech tagging
tagged_tokens = pos_tag(token)

#define a chunk grammer
chucnk_grammer = r''' 
NP: {<DT>?<JJ>*<NN>}  #Noun Phrase
VP: {<VB.*><NP|PP>*}  # Verb Phrase
PP: {<IN><NP>}        # Prepositional Phrase
'''

cp = RegexpParser(chucnk_grammer)

chunked = cp.parse(tagged_tokens)

print(chunked)

chunked.draw()

# chunking in LLM: methids of processig input text in 
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a pre-trained model and tokenizer
model_name = "gpt2"  # You can replace with any other LLM
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chunk_text(text, max_length=512):
    """Chunk text into smaller pieces."""
    tokens = tokenizer.encode(text, return_tensors='pt')[0]
    chunks = []
   
    for i in range(0, len(tokens), max_length):
        chunk = tokens[i:i + max_length]
        chunks.append(chunk)

    return chunks

def generate_responses(chunks):
    """Generate responses for each chunk using the LLM."""
    responses = []
    for chunk in chunks:
        input_ids = chunk.unsqueeze(0)  # Add batch dimension
        output = model.generate(input_ids, max_length=100)  # Generate response
        responses.append(tokenizer.decode(output[0], skip_special_tokens=True))
   
    return responses

# Example long text
long_text = "Your long text goes here. " * 50  # Repeat to simulate long text

# Chunk the text
chunks = chunk_text(long_text)

# Generate responses for each chunk
responses = generate_responses(chunks)

# Print the responses
for i, response in enumerate(responses):
    print(f"Response for chunk {i+1}:\n{response}\n")