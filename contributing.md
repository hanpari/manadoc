



# 🐍 Pokyny pro přispívání (Python + Django)

Díky, že chcete přispět! Tento dokument popisuje technické kroky pro přispívání do projektu postaveného na Pythonu a frameworku Django.

## 🗂️ Struktura projektu

- `manadoc/` – hlavní Django projekt
- `core/` – hlavní funkce
- `tests/` – testy (může být rozděleno podle aplikací)
- `requirements.txt` – seznam závislostí nutných pro běh aplikace
- `requirements-dev.txt` – seznam závislostí nutných pro vývojáře
- `manage.py` – hlavní skript pro správu projektu

## ⚙️ Instalace a spuštění

1. Vytvořte virtuální prostředí:
   ```bash
   python -m venv venv
   source venv/bin/activate  # nebo venv\Scripts\activate na Windows
   ```

2. Nainstalujte závislosti:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. Spusťte migrace a dev server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 🧪 Testování

Spusťte testy pomocí:

```bash
python manage.py test
```

Přidejte testy pro nové funkcionality. Pull request bez testů může být zamítnut.

## 🧹 Styl kódu

Dodržujte standardy PEP 8. Doporučené nástroje:
- `black` pro formátování
- `flake8` pro formátování


Před odesláním změn spusťte:

```bash
black .
flake8 .
```

## 🧬 Pull request proces

1. Forkněte repozitář
2. Vytvořte větev:
   ```bash
   git checkout -b feature/nazev-funkce
   ```
3. Proveďte změny a přidejte testy
4. Pošlete pull request s jasným popisem

## 🚫 Zakázané praktiky

- Nepřispívejte přímo do `main` větve
- Nezahrnujte citlivé údaje do kódu (hesla, tokeny...)

## 🔄 CI/CD

Projekt je napojen na GitHub Actions (nebo jiný systém) pro automatické testování. Každý pull request je automaticky kontrolován.

## 📬 Kontakt

Máte otázky nebo návrhy? Vytvořte issue nebo kontaktujte správce repozitáře.
