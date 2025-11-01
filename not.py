import json

# Читаем notebook
with open('Untitled.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Удаляем проблемные widgets из метаданных
if 'metadata' in nb and 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']
    print("Удалены проблемные метаданные widgets")

# Сохраняем исправленный файл
with open('Untitled.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook исправлен!")