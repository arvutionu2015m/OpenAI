## 🎯 **Projekti eesmärk**  
"Ülesannete Jagaja" on Django-põhine veebirakendus, mis võimaldab kasutajatel:
- 📥 Kirjutada pikk või keeruline ülesanne
- 🧠 Jagada see automaatselt väikesteks alamülesanneteks OpenAI API abil
- ✅ Hallata iga alamülesannet (märgi tehtuks, jälgi edenemist)
- 📊 Visualiseerida progressi (protsent, graafik)
- 💌 Saada e-mailiga meeldetuletusi
- 💡 Küsida personaalseid soovitusi tehisintellektilt

---

## ⚙️ **Kasutatud tehnoloogiad**

| Kategooria           | Tehnoloogia                         |
|----------------------|--------------------------------------|
| Backend              | Python 3, Django                     |
| Virtuaalkeskkond     | `venv`                               |
| Frontend             | Bootstrap 4, Chart.js                |
| AI-integratsioon     | OpenAI API (GPT-3.5-turbo)           |
| Andmebaas            | SQLite (vaikimisi)                  |
| Meiliteenus          | SMTP (nt Gmail)                     |
| Failihaldus          | Django `MEDIA_ROOT` (pildid)         |
| Adminliides          | Täiustatud Django admin              |

---

## 🧩 **Peamised funktsioonid**

### 🔐 Kasutajakeskne süsteem
- Registreerimine, sisselogimine, väljalogimine
- Iga kasutaja näeb ainult oma ülesandeid

### 📋 Ülesannete jaotus AI abil
- Sisestad pika ülesandekirjelduse
- AI jagab selle loogilisteks alamülesanneteks
- Alamülesanded seotakse automaatselt

### ✅ Alamülesannete haldus
- Checkbox tehtud/tegemata märkimiseks
- Protsentuaalne edenemisriba iga ülesande all
- Kokkuvõtlik progress Chart.js doughnut-diagrammiga

### 📬 Meeldetuletused ja teavitused
- Tähtaegadega ülesanded saadavad meeldetuletusi e-mailile
- AI-põhine intelligentne kokkuvõte tähtsamatest ülesannetest

### 💡 AI Soovitused dashboardil
- Nupp "Küsi AI soovitusi"
- AI genereerib soovitused päevakava või prioriteedi põhjal
- Kuvatakse kasutajale eraldi lehel või AJAX-iga

---

## 🗂️ **Failistruktuuri võtmeosad**

```
├── jagaja/
│   ├── models.py           ← Ülesanne ja AlamÜlesanne mudelid
│   ├── views.py            ← home, lisa_ülesanne, AI-soovitused
│   ├── utils.py            ← OpenAI API suhtlus
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── ai_soovitused.html
│   ├── static/
│   │   ├── css/style.css
│   │   ├── img/plus-icon.png
│   └── management/commands/
│       ├── send_reminders.py
│       └── ai_reminders.py
```

---

## 💡 **Edasised ideed**
- 📆 Google Calendar sünkroonimine
- 🔔 Push-teavitused (brauseri kaudu)
- 🧭 Prioriteetide määramine (nt Eisenhoweri maatriks)
- 📱 Mobiilisõbralik progressive web app (PWA)
- 🧑‍💼 Admini kaudu käsitsi AI-soovituste jagamine

---
