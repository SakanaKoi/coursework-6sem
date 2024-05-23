import re


def read_data(data):
    if isinstance(data, str):
        text = data
    elif hasattr(data, 'read'):
        text = data.read()
    else:
        raise ValueError("Неподдерживаемый тип данных. Ожидается строка или файл.")
    return text


def remove_hashtags(data):
    text = read_data(data)
    hashtag_pattern = r'\#\w+'
    return re.sub(hashtag_pattern, '', text)


def get_hashtags(data):
    text = read_data(data)
    hashtag_pattern = r'\#\w+'
    return re.findall(hashtag_pattern, text)


def replace_hashtags(data, replacement):
    text = read_data(data)
    hashtag_pattern = r'\#\w+'
    return re.sub(hashtag_pattern, replacement, text)


def count_hashtags(data):
    text = read_data(data)
    hashtag_pattern = r'\#\w+'
    return len(re.findall(hashtag_pattern, text))
