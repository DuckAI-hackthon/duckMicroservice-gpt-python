from openai import OpenAI

client = OpenAI(api_key='')

def qea(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7)
    obj = {id: completion.id,
           "response": completion.choices[0].message.content }
    return obj

def translate(prompt, from_lang, to_lang):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Traduza {prompt} de {from_lang} para {to_lang}"}],
    temperature=0.7)
    obj = {id: completion.id,
           "response": completion.choices[0].message.content }
    return obj

def summarize(prompt, amount):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Seu objetivo é resumir textos de acordo com 3 níveis: 1(O mínimo possível), 2 (Medianamente) ou 3 (O máximo possível). É importante não retirar o sentido do texto. Resuma este texto:\n {prompt}\n No nível {amount}"}],
        temperature=0.7
    )

    obj = {"id": completion.id, "response": completion.choices[0].message.content}
    return obj

def get_keywords(prompt, keyNum):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Identifique {keyNum} palavras-chave deste texto: {prompt}"}],
    temperature=0.7)
    obj = {id: completion.id,
           "response": completion.choices[0].message.content }
    return obj

def summarize_in(prompt, words):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Resuma este texto em {words} palavras:\n {prompt}"}],
    temperature=0.7)
    obj = {id: completion.id,
           "response": completion.choices[0].message.content }
    return obj

