import os


def get_speaker_text(text, **kwargs):
    if "begin" in kwargs.keys():
        begin_index = len(text) - 1 - text[::-1].index(kwargs["begin"])
        text = text[begin_index:]
    if "end" in kwargs.keys():
        end_index = text.index(kwargs["end"])
        text = text[:end_index]
    """ I don´t think you can reliably differentiate Headings and Stage instructions from the rest of the text because
    some Stage Instructions are written only one line after speaker text. This is why I only added a way for the user
    to manually enter a begin and end of the text. """
    return text


def normalize_text(text):
    replaced = (".", ",", ":", ";", "?", "!")
    normalized = []
    for i in text:
        x = i
        for j in replaced:
            x = x.replace(j, "")
        normalized.append(x.lower())
    return normalized


def remove_stopwords(text):
    with open(os.getcwd().split("\\0")[0] + r"\assignment_05_program_data\eng_stop_words.txt") as f:
        stop_words = f.read().splitlines()
    no_stopwords = []
    for i in text:
        x = i.split()  # this approach will also do the tokenization
        for j in x:
            if j not in stop_words:
                no_stopwords.append(j)

    return no_stopwords

