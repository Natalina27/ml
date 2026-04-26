# ML Coding Exercises

Учебный проект с небольшими задачами по машинному обучению на Python.

## Структура проекта

```text
ml-coding-exercises/
├── exercises/
│   └── 01_importing_preprocessing/
│       ├── README.md
│       ├── iris.csv
│       └── solution.py
├── notebooks/
├── src/
│   └── ml_exercises/
├── tests/
├── .gitignore
└── requirements.txt
```

## Быстрый старт

Создайте виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Запустите первое решение:

```bash
cd exercises/01_importing_preprocessing
python solution.py
```

## Как добавлять новые задачи

Для каждой новой задачи создавайте отдельную папку внутри `exercises/`:

```text
exercises/
└── 02_new_exercise/
    ├── README.md
    ├── data.csv
    └── solution.py
```
