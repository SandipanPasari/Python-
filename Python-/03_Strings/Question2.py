letter = '''Dear <|Name|>
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "15th Jan 2024"))