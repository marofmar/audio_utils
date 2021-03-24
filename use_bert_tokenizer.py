# today, I am gonna use RobertaTokenizer. Yey!

from transformers import RobertaTokenizer
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

def show_tokens(tokenizer, sentence):
    print(f"{sentence} -> {tokenizer(sentence)['input_ids']}")
    return tokenizer(sentence)['input_ids']


show_tokens(tokenizer, "Honne")
show_tokens(tokenizer, "create memories. Not jpegs.")
show_tokens(tokenizer, "Just smile more.")