# GPTProject
## Участники команды

- Гуляев Николай Алексеевич (РИМ-130906)
- Седиров Арсен Русланович (РИМ-130906)

**Модель:** deepset/roberta-base-squad2


## Описание работы модели

Модель разработана для ответов на вопрос по заранее подготовленному контексту.

### Пример использования

Пример использования модели в Python:

```python
 result = get_answer('What are the advantages of using Transformers models?',
                        'Transformers is a family of machine learning models that represent a significant step forward in natural language processing. They provide outstanding performance in tasks such as machine translation, question-answer system, text summarization and more. The advantages of using Transformers models include high accuracy, the ability to learn from large amounts of data, and the ability to apply to various text processing tasks. These models have also become the basis for many state-of-the-art NLP solutions.')

```


## Описание работы программы в streamlit

Данная программа представляет собой интерфейс для ответов на вопрос по контексту. 

### Интерфейс приложения

1. **Заголовок страницы**
   - Отображает на странице приложения заголовок "Вопросно-ответный ассистент".

2. **Форма для ввода текста**
   - Две Области для ввода текста, который необходимо ввести.

3. **Отображение ответа**
   - После ввода текста и его подтверждения пользователем, программа выводит ответ на вопрос.

### Использование

Программа использует библиотеку Streamlit для построения интерфейса и функцию `get_answer` из модуля `model` для выполнения ответа на вопрос.

## Тесты

### Тест на получение ответа

Проверяет корректность работы функции при передаче валидных входных данных: вопроса и контекста. Ожидается, что длина полученного ответа будет больше 10 символов.(test_get_answer())

### Тест на пустой вопрос

Проверяет корректность обработки функцией сценария, когда передается пустой вопрос. Ожидается, что функция вернет ответ равный переданному контексту.(test_empty_question())

### Тест на пустой контекст

Проверяет корректность обработки функцией сценария, когда передается пустой контекст. Ожидается, что функция вернет пустой ответ.(test_empty_context()

