file_name = 'example'

print(f'{file_name}.txt')  # 👉️ example.txt

with open(f'{file_name}.txt', 'w', encoding='utf-8') as f:
    f.write('first line' + '\n')
    f.write('second line' + '\n')
    
    

