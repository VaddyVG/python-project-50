.PHONY: lint install test clean coverage check

# Установка зависимостей
install:
	poetry install

# Линтинг с помощью flake8
lint:
	poetry run flake8 .

# Запуск тестов с использованием pytest
test:
	poetry run pytest

# Генерация отчета о покрытии тестов
coverage:
	poetry run pytest --cov=gendiff --cov-report html:coverage_html_report --cov-report xml:coverage.xml

# Очистка временных файлов и кэша
clean:
	rm -rf __pycache__ .pytest_cache coverage.xml coverage_html_report

# Проверка всех шагов (линтинг, тесты, покрытие)
check: lint test coverage