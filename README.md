# Змейка (Snake) на Python + pygame

Коротко: простая реализация игры "Змейка" с помощью pygame.

Требования:
- Python 3.8+
- pygame (см. `requirements.txt`)

Установка (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
```

Запуск:

```powershell
python snake_game.py
```

Управление:
- Стрелки — движение
- Esc — выйти
- R — рестарт после Game Over

Файлы:
- `snake_game.py` — исходный код игры
- `requirements.txt` — внешние зависимости

Примечания:
- Игра основана на клеточной сетке (размер клетки задаётся в начале файла).
- При увеличении счёта скорость повышается каждые 5 съеденных яблок.
- 
