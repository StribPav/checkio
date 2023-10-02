MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

def morse_decoder(code):
    regex = "([.-]+|[ \t]{2,})"
    message = ""

    morse_code = re.split(regex, code)

    for morse_letter in morse_code:
        if bool(re.search(r' {2,}', morse_letter)) == True:
            message += " "
        else:
            for morse, char in MORSE.items():
                if morse == morse_letter:
                    message += char

    return message.capitalize()

print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

# These "asserts" are used for self-checking
assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

morse_decoder = lambda code: "".join([MORSE[i] for i in code.replace("   ", " + ").split()]).capitalize()

def morse_decoder(code):
    return re.sub(' ?(\S+) ?', lambda m: morse[m.group(1)], code).capitalize()

morse_decoder = lambda c: ''.join([MORSE[i] for i in c.replace('   ', '  ').split(" ")]).capitalize()
