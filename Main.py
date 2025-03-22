import os

def clean_text(text):
    remove = [f'＄＄＄', f'\\\\k', f'\\\\s', f'\\\\n', f'\\n', f'\\\\c', f'\\']

    for element in remove:
        text = text.replace(element, " ")

    return " ".join(text.split())

def get_data(data):
    lines = data.split("}")

    final_text = ""

    for line in lines:
        name = ""
        text = ""
        question = ""
        answer = ""

        if "chrName" in line:
            name = (line.split(r'chrName":"'))[1].split(r'","')[0]
        if "messageEN" in line:
            text = (line.split(r'messageEN":"'))[1].split(r'","seList"')[0]
            text = clean_text(text)
        if "questionEN" in line:
            question = (line.split(r'"questionEN":"'))[1].split(r'"answerEN":')[0]
            question = clean_text(question)
            answer = (line.split(r'"answerEN":'))[1].split(r',"answerNo"')[0]

        if (name != ""): 
            if (text != ""):
                final_text += f'{name}: {text}\n\n'
            else: final_text += f'{text}\n\n'
        if (question != ""):
            final_text += f'{question}\n{answer}\n\n'
        
    return final_text


files = os.listdir("./input")

for file in files:
    with open(f'./input/{file}') as text:
        data = text.read()
        transcript = get_data(data)
        with open(f'./output/{file}', "w") as f:
            f.write(transcript)

