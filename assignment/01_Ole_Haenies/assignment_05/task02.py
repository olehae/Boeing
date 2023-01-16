import os
from task01 import get_speaker_text, normalize_text, remove_stopwords
from assignment.assignment_05_program_data import utils_ocr
import csv

macbeth_path = os.getcwd().split("\\0")[0] + r"\assignment_05_program_data\Macbeth.txt"
new_atlantis_path = os.getcwd().split("\\0")[0] + r"\assignment_05_program_data\NewAtlantis.txt"

with open(macbeth_path) as f:
    macbeth = f.read().splitlines()

with open(new_atlantis_path) as f:
    new_atlantis = f.read().splitlines()

macbeth_words = {}
new_atlantis_words = {}

macbeth = get_speaker_text(macbeth, begin="The Tragedie of Macbeth", end="FINIS. THE TRAGEDIE OF MACBETH.")
macbeth = normalize_text(macbeth)
macbeth = [utils_ocr.correct_ocr_errors(line) for line in macbeth]
macbeth = remove_stopwords(macbeth)

new_atlantis = get_speaker_text(new_atlantis, begin="THE NEW ATLANTIS", end="[The rest was not perfected.]")
new_atlantis = normalize_text(new_atlantis)
new_atlantis = remove_stopwords(new_atlantis)

for i in macbeth:
    if i in macbeth_words.keys():
        macbeth_words[i] += 1
    else:
        macbeth_words[i] = 1

for i in new_atlantis:
    if i in new_atlantis_words.keys():
        new_atlantis_words[i] += 1
    else:
        new_atlantis_words[i] = 1

macbeth_words = {key: val for key, val in sorted(macbeth_words.items(),
                                                 key=lambda element: element[1],
                                                 reverse=True)}
new_atlantis_words = {key: val for key, val in sorted(new_atlantis_words.items(),
                                                      key=lambda element: element[1],
                                                      reverse=True)}

# print(macbeth_words)
# print(new_atlantis_words)
frequencies = []
for i in macbeth_words.keys():
    frequencies.append([i, macbeth_words[i], 0, macbeth_words[i]])
existing = [x[0] for x in frequencies]
for i in new_atlantis_words.keys():
    if i in existing:
        index = existing.index(i)
        frequencies[index][2] = new_atlantis_words[i]
        frequencies[index][3] += new_atlantis_words[i]
    else:
        frequencies.append([i, 0, new_atlantis_words[i], new_atlantis_words[i]])

frequencies = sorted(frequencies, key=lambda x: x[3], reverse=True)
with open("frequencies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["word", "Macbeth frequency", "NewAtlantis frequency", "sum of frequencies"])
    for i in frequencies:
        writer.writerow([i[0].replace("\'", "").replace("\"", ""), i[1], i[2], i[3]])
