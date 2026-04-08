# MAI Lab 8

Модель задач и очередь задач

## Работа

- `Task` с валидацией через дескрипторы
- `TaskQueue` с итератором и ленивыми фильтрами

## Запуск

```bash
python3 -m src.main
```

## Тесты и покрытие

```bash
pytest -q
pytest --cov=src --cov-report=term-missing -q
```
