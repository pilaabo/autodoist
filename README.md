# autodoist

Проект **autodoist** объединяет автоматические тесты Todoist для API, веб-интерфейса и мобильного приложения  
Цель - гарантировать корректную работу сервиса при каждой поставке кода и минимизировать ручные проверки  

## Технологии

- Python 3.11  
- pytest - фреймворк для тестов  
- Playwright - UI-тесты веб-версии  
- Appium - UI-тесты мобильных приложений  
- requests - HTTP-клиент для API-тестов  
- Allure Report - визуализация результатов  
- Jenkins - непрерывная интеграция и исполнение пайплайнов  

## Структура репозитория

```
autodoist/
  tests/
    api/       # API-тесты
    web/       # веб-тесты
    mobile/    # мобильные тесты
  common/
    utils/     # вспомогательные модули
    fixtures/  # фикстуры и данные
.github/
  workflows/
    ci.yml     # конфигурация CI
README.md
requirements.txt
pytest.ini
```

## Быстрый старт

```bash
git clone https://github.com/pilaabo/autodoist.git
cd autodoist

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest tests/            # полный набор
pytest tests/api         # только API-тесты
pytest tests/web         # только веб-тесты
pytest tests/mobile      # только мобильные тесты
```

## Формирование отчета Allure

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## CI/CD

Jenkins выполняет три независимых джобы

1. API-тесты - быстрая проверка критических эндпоинтов  
2. Web-тесты - параллельный прогон в Playwright с видеозаписью падений  
3. Mobile-тесты - запуск на эмуляторе или реальном устройстве через Appium  

Отчеты Allure загружаются как артефакт сборки и доступны прямо из интерфейса Jenkins  

## Контакты

Автор: @pilaabo (Telegram)
