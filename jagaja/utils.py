import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def soovita_olulised_ülesanded(ülesanded):
    ülesande_tekst = ""
    for ülesanne in ülesanded:
        ülesande_tekst += f"- {ülesanne.pealkiri} (tähtaeg: {ülesanne.tähtaeg}, kirjeldus: {ülesanne.kirjeldus})\n"

    prompt = (
        "Siin on nimekiri ülesannetest. Palun tuleta kasutajale meelde tähtsad või kriitilised ülesanded. "
        "Tee soovituslik plaan, mille järgi neid võiks lahendada:\n\n"
        f"{ülesande_tekst}\n\n"
        "Tagasta selge nimekiri soovitustega."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message['content']

def jagatud_ülesanded(pikk_kirjeldus):
    prompt = f"Jaga järgmine ülesanne väikesteks tegevusteks:\n\n{pikk_kirjeldus}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
