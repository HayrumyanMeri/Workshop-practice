sample = "How old  old are you?"
x = sample.count("old", 7, 9)
print(x)

text = "122334" 
formatted_text = '/'.join([text[i:i+2] for i in range(0, len(text), 2)]) 
# formatted_text = 
print(formatted_text)