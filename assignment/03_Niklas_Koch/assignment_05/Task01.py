def get_speaker_text():
    with open("0ws3410.txt", "r") as play:
        lines = play.readlines()

    with open("0ws3410.txt", "w") as play:
        play.truncate()
        start = 0
        for number, line in enumerate(lines):
            if "Actus Primus" in line:
                start = number
            if "Actus" not in line and "Scena" not in line:
                play.write(line)
            normalize_text(line, lines)

        play.writelines(lines[start:])


def normalize_text(sentence, lines):
    sentence = sentence.lower()
    return lines


get_speaker_text()
                
                
