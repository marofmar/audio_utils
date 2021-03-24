# today, I am gonna use RobertaTokenizer. Yey!

from transformers import RobertaTokenizer
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

def show_tokens(tokenizer, sentence):
    print(f"{sentence} -> {tokenizer(sentence)['input_ids']}")
    return tokenizer(sentence)['input_ids']


# show_tokens(tokenizer, "Honne")
show_tokens(tokenizer, "create memories. Not jpegs.")
show_tokens(tokenizer, "Just smile more.")
show_tokens(tokenizer, "안녕하세요")
# show_tokens(tokenizer, "sunrise in Georgia")
show_tokens(tokenizer, "Hola, que tal?")
show_tokens(tokenizer, "내 이름은 후추, 난 고양이야.")

# how does this work on foreign languages other than English?