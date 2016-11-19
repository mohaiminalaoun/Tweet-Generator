import markovify

# Get raw text as string.

with open("lincoln.txt") as f:
    text = f.read()
    first_words = ' '.join(text.split()[:2])

# Build the model.
text_model = markovify.Text(text)
# Print five randomly-generated sentences

for i in range(10):
    cur_sentence = text_model.make_sentence_with_start("My")
    first_words = ' '.join(cur_sentence.split()[-2:])
    print(cur_sentence)