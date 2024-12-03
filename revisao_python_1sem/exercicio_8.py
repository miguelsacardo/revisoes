temperaturaCelcius = float(input("Digite uma temperatura em Celsius: "))
estaQuente = float(input("A partir de que temperatura está quente para você? "))
estaModerado = float(input("A partir de que temperatura está moderado para você? "))
estaFrio = float(input("A partir de que temperatura está frio para você? "))

if temperaturaCelcius >= estaQuente:
    print(f"A temperatura {temperaturaCelcius}° é QUENTE!")
elif temperaturaCelcius >= estaModerado and temperaturaCelcius < estaQuente:
    print(f"A tempertatura {temperaturaCelcius}° é MODERADA!")
elif temperaturaCelcius >= estaFrio or temperaturaCelcius < estaFrio and temperaturaCelcius < estaModerado and temperaturaCelcius < estaQuente:
    print(f"A temperatura {temperaturaCelcius}° está FRIA!")