import sys
script, input_encoding, error = sys.argv

languages = open("languages.txt", encoding="utf-8")
#open languages.txt and seve it to var languages

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
#perform .readline() on language_file
#and save that to var line
#for each line, run def print_line
#retun main????


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw = next_lang.encode(encoding, errors=errors)
    cooked_string = raw.decode(encoding, errors=errors)
# run def prin_line
# perform .strp() on line and save as var next_lang
# perform .encode() on next_lang and save as var raw
# perform .decode() on raw and save as cooked_string

    print(raw, "<===>", cooked_string)
    #print raw abd cooked_string
    


main(languages, input_encoding, error)
#call function main
