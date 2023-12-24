from model import get_answer


# Тест на получение ответа
def test_get_answer():
    result = get_answer('What are the advantages of using Transformers models?',
                        'Transformers is a family of machine learning models that represent a significant step forward in natural language processing. They provide outstanding performance in tasks such as machine translation, question-answer system, text summarization and more. The advantages of using Transformers models include high accuracy, the ability to learn from large amounts of data, and the ability to apply to various text processing tasks. These models have also become the basis for many state-of-the-art NLP solutions.')
    assert len(result['answer']) > 10


# Тест на пустой вопрос
def test_empty_question():
    result = get_answer(" ", "context")
    assert result['answer'] == "context"


# Тест на пустой контекст
def test_empty_context():
    result = get_answer("Some question?", " ")
    assert result['answer'] == ""
