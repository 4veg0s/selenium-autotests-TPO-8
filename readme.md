# 4 курс | Тестирование ПО
## ПЗ 8 | Тестирование https://arnypraht.com

## Порядок запуска:
### 1. Создание файла конфигурации
**PowerShell:** 
```
New-Item -Path "config" -ItemType Directory
New-Item -Path "config\config.yaml" -ItemType File
```

**cmd:**
```
mkdir config
type nul > config\config.yaml
```

### 2. Необходимо скопировать содержимое файла конфигурации из приложенного файла
### 3. Загрузка зависимостей
```
pip install -r requirements.txt
```
### 4. Запуск тестов
```
pytest
``` 
из корневой директории