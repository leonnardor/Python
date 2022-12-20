from datetime import datetime

boas_vindas = lambda nome: f"Olá, {nome}! Hoje é dia {datetime.now().day} de {datetime.now().month} de {datetime.now().year} e são exatamente {datetime.now().hour} horas e {datetime.now().minute} minutos."

print(boas_vindas("Leonardo"))


