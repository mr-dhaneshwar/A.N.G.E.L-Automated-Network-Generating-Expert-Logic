from googletrans import Translator


tr = Translator()


def to_en(query):
    out = tr.translate(query, dest='en')
    return (out.text)


def to_hi(query):
    out = tr.translate(query, dest='hi')
    return (out.text)


def to_mr(query):
    out = tr.translate(query, dest='mr')
    return (out.text)

