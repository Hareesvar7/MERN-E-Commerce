import spacy
import random

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to read text from an input file
def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to generate random sentences
def generate_random_sentences(text, num_sentences=5):
    doc = nlp(text)
    sentences = list(doc.sents)  # Extract sentences
    words = [token.text for token in doc if not token.is_punct]  # Extract words excluding punctuation
    
    random_sentences = []
    
    # Generate the required number of random sentences
    for _ in range(num_sentences):
        random.shuffle(words)  # Shuffle the words to form random sentences
        random_sentence = ' '.join(words[:random.randint(5, 12)])  # Take random length between 5 to 12 words
        random_sentences.append(random_sentence)
    
    return random_sentences

# Function to write generated sentences to an output file
def write_output_file(output_file, sentences):
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + "\n")

# Main function to orchestrate the process
def main(input_file, output_file, num_sentences=5):
    text = read_input_file(input_file)
    random_sentences = generate_random_sentences(text, num_sentences)
    write_output_file(output_file, random_sentences)
    print(f"Generated {num_sentences} random sentences and saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = 'input.txt'  # Path to your input file
    output_file = 'output.txt'  # Path to save the generated sentences
    main(input_file, output_file, num_sentences=5)
