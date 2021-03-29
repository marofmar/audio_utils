from transformers import pipeline

text_generator = pipeline("text-generation")
print(text_generator("As far as I kno,", max_length=50))


"""
returned:

[{'generated_text': 'As far as I know, 
this was not the first time people went into a bathroom while being chased, 
but this is the first time it has actually happened, probably just because the guy could not care less.'}]


"""