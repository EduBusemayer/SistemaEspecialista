import sys

class DevNull:
    def write(self, msg):
        pass
    
def calculoPorcentagem(value, perguntasFeitas):
    value: float = (100*value)/perguntasFeitas
    return value

def valorInvalido():
    print("#-----------------------------------------#\n"
          "Valor inválido!!\n"
          "#-----------------------------------------#\n")
    sys.stderr = DevNull()
    sys.exit()

#---------------------------------------------------------------------------------------------------------------------------------------------#

perguntasFeitas: int = 0
Jogos: dict = {
    "PUBG": 0,  
    "Minecraft": 0,
    "UNO": 0,
    "Apex Legends": 0,  
    "Fortnite": 0,  
    "Counter-Strike 2": 0, 
    "League of Legends": 0, 
    "Hearthstone: Heroes of Warcraft": 0, 
    "Call of Duty Mobile": 0, 
    "Among Us": 0,  
    "Call of Duty Warzone": 0,  
    "Dota 2": 0,
    "Forza": 0,
    "Free Fire": 0,  
    "Roblox": 0,  
    "CrossFire": 0,  
    "Assassin's Creed": 0,  
    "Slime Rancher": 0,  
    "Just Cause": 0,  
    "Outer Wilds": 0,  
    "Need For Speed": 0,
    "Star Wars: Jedi Fallen Order": 0, 
    "ARK Survival": 0,  
    "FIFA": 0,  
    "The Forest": 0, 
    "Payday 2": 0, 
    "The Witcher": 0, 
    "Watch Dogs": 0,  
    "Ghost of Tsushima": 0,  
    "Elden Ring": 0, 
    "Hitman": 0,
    "Rocket League": 0,
    "FarCry": 0,  
    "Read Dead Redemption 2": 0,  
    "Cyberpunk": 0,  
    "Albion Online": 0,
    "Hollow Knight": 0,
    "New World": 0,
    "Hades": 0,
    "Green Hell": 0,
    "Grid": 0,
    "Speed Drifters": 0,
    "Mario Kart": 0,
    "Out Last": 0,
    "Escape The Backrooms": 0,
    "Resident Evil": 0,
    "Project Zomboid": 0,
    "Gwent": 0,
    "Dauntless": 0,
    "Path of Exile": 0,
    "BloodBorn": 0,
    "Dark Souls": 0,
    "Golf Simulator": 0,
    "XCOM 2": 0,
}

try:
    EstiloDeJogo = int(input("Qual estilo de jogo você deseja?\n"
                            "[1] FPS\n"
                            "[2] Battle Royale\n"
                            "[3] Corrida\n"
                            "[4] RPG\n"
                            "[5] MMORPG\n"
                            "[6] Mobile\n"
                            "[7] Rogue Like\n"
                            "[8] Souls Like\n"
                            "[9] Estratégia\n"
                            "[10] Exploração\n"
                            "[11] Terror\n"
                            "Digite sua opção: "))
    perguntasFeitas += 1

    # Caso seja opção inválida:
    if EstiloDeJogo > 11 or EstiloDeJogo < 1:
        exit(sys.exception)

    # Se o estilo de Jogo for FPS:
    if EstiloDeJogo == 1:
        Jogos["PUBG"] += 1
        Jogos["Apex Legends"] += 1
        Jogos["Counter-Strike 2"] += 1
        Jogos["Call of Duty Mobile"] += 1
        Jogos["Call of Duty Warzone"] += 1
        Jogos["CrossFire"] += 1
        Jogos["Payday 2"] += 1
        Jogos["FarCry"] += 1
        Jogos["Cyberpunk"] += 1
        Jogos["ARK Survival"] += 1
        Jogos["The Forest"] += 1
        Jogos["Green Hell"] += 1

    # Se o estilo de Jogo for Battle Royale:
    elif EstiloDeJogo == 2:
        Jogos["PUBG"] += 1
        Jogos["Fortnite"] += 1
        Jogos["Call of Duty Warzone"] += 1
        Jogos["Free Fire"] += 1

    # Se o estilo de Jogo for Corrida:
    elif EstiloDeJogo == 3:
        Jogos["Forza"] += 1
        Jogos["Grid"] += 1
        Jogos["Mario Kart"] += 1
        Jogos["Speed Drifters"] += 1
        Jogos["Need For Speed"] += 1
        Jogos["Rocket League"] += 1

    # Se o estilo de Jogo for RPG:
    elif EstiloDeJogo == 4:
        Jogos["Minecraft"] += 1
        Jogos["Gwent"] += 1
        Jogos["Resident Evil"] += 1
        Jogos["Hearthstone: Heroes of Warcraft"] += 1
        Jogos["Assassin's Creed"] += 1
        Jogos["Slime Rancher"] += 1
        Jogos["Just Cause"] += 1
        Jogos["ARK Survival"] += 1
        Jogos["The Forest"] += 1
        Jogos["The Witcher"] += 1
        Jogos["Elden Ring"] += 1
        Jogos["FarCry"] += 1
        Jogos["Read Dead Redemption 2"] += 1
        Jogos["Cyberpunk"] += 1
        Jogos["Hollow Knight"] += 1
        Jogos["New World"] += 1
        Jogos["Albion Online"] += 1
        Jogos["Hades"] += 1
        Jogos["Watch Dogs"] += 1

    # Se o estilo de Jogo for MMORPG:
    elif EstiloDeJogo == 5:
        Jogos["New World"] += 1
        Jogos["Albion Online"] += 1
        Jogos["Dauntless"] += 1
        Jogos["Path of Exile"] += 1
        
    # Se o estilo de Jogo for Mobile:
    elif EstiloDeJogo == 6:
        Jogos["Minecraft"] += 1
        Jogos["Hearthstone: Heroes of Warcraft"] += 1
        Jogos["Call of Duty Mobile"] += 1
        Jogos["Among Us"] += 1
        Jogos["Free Fire"] += 1
        Jogos["Roblox"] += 1
        
    # Se o estilo de Jogo for Rogue Like:
    elif EstiloDeJogo == 7:
        Jogos["Hollow Knight"] += 1
        Jogos["Hades"] += 1
        
    # Se o estilo de Jogo for Souls Like:
    elif EstiloDeJogo == 8:
        Jogos["Ghost of Tsushima"] += 1
        Jogos["Elden Ring"] += 1
        Jogos["Hollow Knight"] += 1
        Jogos["Dark Souls"] += 1
        Jogos["BloodBorn"] += 1
        
    # Se o estilo de Jogo for Estratégia:
    elif EstiloDeJogo == 9:
        Jogos["Hearthstone: Heroes of Warcraft"] += 1
        Jogos["Among Us"] += 1
        Jogos["Dota 2"] += 1
        Jogos["FIFA"] += 1
        Jogos["League of Legends"] += 1
        Jogos["Gwent"] += 1
        Jogos["Golf Simulator"] += 1
        Jogos["XCOM 2"] += 1
        Jogos["UNO"] += 1
        
    # Se o estilo de Jogo for Exploração:
    elif EstiloDeJogo == 10:
        Jogos["Minecraft"] += 1
        Jogos["Resident Evil"] += 1
        Jogos["Assassin's Creed"] += 1
        Jogos["Slime Rancher"] += 1
        Jogos["Just Cause"] += 1
        Jogos["Outer Wilds"] += 1
        Jogos["Star Wars: Jedi Fallen Order"] += 1
        Jogos["ARK Survival"] += 1
        Jogos["The Forest"] += 1
        Jogos["The Witcher"] += 1
        Jogos["Watch Dogs"] += 1
        Jogos["Ghost of Tsushima"] += 1
        Jogos["Elden Ring"] += 1
        Jogos["FarCry"] += 1
        Jogos["Read Dead Redemption 2"] += 1
        Jogos["Cyberpunk"] += 1
        Jogos["Green Hell"] += 1
        Jogos["Hollow Knight"] += 1
        
    # Se o estilo de Jogo for Terror:
    elif EstiloDeJogo == 11:
        Jogos["Out Last"] += 1
        Jogos["Resident Evil"] += 1
        Jogos["Escape The Backrooms"] += 1
        Jogos["Project Zomboid"] += 1

# Caso seja opção inválida:
except:
    valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser FPS:
if EstiloDeJogo == 1:
    # Pergunta Modalidade:
    try:
        Modalidade = int(input("#-----------------------------------------#\n"
                               "|                 FPS                     |\n"
                               "#-----------------------------------------#\n"
                               "Você deseja qual Modalidade de Jogos FPS?\n"
                               "[1] Survival\n"
                               "[2] Casual\n"
                               "[3] Competitive\n"
                               "Digite sua opção: "))
        perguntasFeitas += 1
        
        # Caso seja opção inválida:
        if Modalidade > 3 or Modalidade < 1:
            exit(sys.exception)           

        # Se a pessoa gosta de Survival:
        if Modalidade == 1:
            Jogos["Green Hell"] += 1
            Jogos["The Forest"] += 1
            Jogos["ARK Survival"] += 1

            # Pergunta Dificuldade:
            try:
                Dificuldade = int(input("#-----------------------------------------#\n"
                                        "Você deseja qual dificuldade?\n"
                                        "[1] Normal\n"
                                        "[2] Difícil\n"
                                        "Digite sua opção: "))
                perguntasFeitas += 1
                
                # Caso seja opção inválida:
                if Dificuldade > 2 or Dificuldade < 1:
                    exit(sys.exception)
        
                # Se for Normal:
                if Dificuldade == 1:
                    Jogos["The Forest"] += 1
            
                # Se for Difícil:
                elif Dificuldade == 2:
                    Jogos["Green Hell"] += 1
                    Jogos["ARK Survival"] += 1

                # Pergunta Preço:
                Preco = int(input("#-----------------------------------------#\n"
                                        "Você deseja pagar quanto pelo Jogo?\n"
                                        "[1] R$ 30-40\n"
                                        "[2] R$ 40-50\n"
                                        "Digite sua opção: "))
                perguntasFeitas += 1

                 # Caso seja opção inválida:
                if Preco > 2 or Preco < 1:
                    exit(sys.exception)
        
                # Se for 30-40:
                if Preco == 1:
                    Jogos["The Forest"] += 1
            
                # Se for 40-50:
                elif Preco == 2:
                    Jogos["Green Hell"] += 1
                    Jogos["ARK Survival"] += 1
                
            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Se a pessoa gosta de Casual:
        elif Modalidade == 2:
            Jogos["Cyberpunk"] += 1
            Jogos["FarCry"] += 1
            Jogos["Payday 2"] += 1
        
            # Pergunta Formato:
            try:
                Formato = int(input("#-----------------------------------------#\n"
                                    "Você deseja qual Formato?\n"
                                    "[1] História\n"
                                    "[2] Cooperativo\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1
                
                # Caso seja opção inválida:
                if Formato > 2 or Formato < 1:
                    exit(sys.exception)
        
                # Se for História:
                if Formato == 1:
                    Jogos["FarCry"] += 1
                    Jogos["Cyberpunk"] += 1
            
                # Se for Cooperativo:
                elif Formato == 2:
                    Jogos["Payday 2"] += 1

                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                    "Você deseja qual Estilo?\n"
                                    "[1] Futurista\n"
                                    "[2] Realista\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1
                
                # Caso seja opção inválida:
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)
        
                # Se for História:
                if Estilo == 1:
                    Jogos["Cyberpunk"] += 1
            
                # Se for Cooperativo:
                elif Estilo == 2:
                    Jogos["Payday 2"] += 1
                    Jogos["FarCry"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)
            
        # Se a pessoa gosta de Competitive:
        elif Modalidade == 3:
            Jogos["PUBG"] += 1
            Jogos["Apex Legends"] += 1
            Jogos["Counter-Strike 2"] += 1
            Jogos["Call of Duty Mobile"] += 1
            Jogos["Call of Duty Warzone"] += 1
            Jogos["CrossFire"] += 1
    
    # Caso seja opção inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Battle Royale:
if EstiloDeJogo == 2:
    # Pergunta Plataforma:
    try:
        Plataforma = int(input("#-----------------------------------------#\n"
                               "|             Battle Royale               |\n"
                               "#-----------------------------------------#\n"
                               "Você deseja jogar em qual Plataforma?\n"
                                "[1] PC\n"
                                "[2] Mobile\n"
                                "[3] Console\n"
                                "Digite sua opção: "))
        perguntasFeitas += 1
        
        # Caso seja opção inválida:
        if Plataforma > 3 or Plataforma < 1:
            exit(sys.exception)

        # Se a pessoa joga em PC:
        if Plataforma == 1:
            Jogos["PUBG"] += 1
            Jogos["Fortnite"] += 1
            Jogos["Call of Duty Warzone"] += 1
        
            # Pergunta Fantasia:
            try:
                Fantasia = int(input("#-----------------------------------------#\n"
                                    "Você deseja jogar um jogo Realista ou com Fantasia?\n"
                                    "[1] Realista\n"
                                    "[2] Fantasia\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1
            
                # Caso seja opção inválida:
                if Fantasia > 2 or Fantasia < 1:
                    exit(sys.exception)

                # Se for Realista:
                if Fantasia == 1:
                    Jogos["Call of Duty Warzone"] += 1
                    Jogos["PUBG"] += 1
                
                # Se for Fantasia:
                elif Fantasia == 2:
                    Jogos["Fortnite"] += 1
                    
            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)
      
        # Se a pessoa joga em Mobile:
        if Plataforma == 2:
            Jogos["Free Fire"] += 1
      
        # Se a pessoa joga em Console:
        if Plataforma == 3:
           Jogos["Fortnite"] += 1
           Jogos["Call of Duty Warzone"] += 1
       
           # Pergunta Fantasia:
           try:
                Fantasia = int(input("#-----------------------------------------#\n"
                                     "Você deseja jogar um jogo Realista ou com Fantasia?\n"
                                     "[1] Realista\n"
                                     "[2] Fantasia\n"
                                     "Digite sua opção: "))
                perguntasFeitas += 1
           
                # Caso seja opção inválida:
                if Fantasia > 2 or Fantasia < 1:
                    exit(sys.exception)
        
                # Se for Realista:
                if Fantasia == 1:
                    Jogos["Call of Duty Warzone"] += 1
            
                # Se for Fantasia:
                elif Fantasia == 2:
                    Jogos["Fortnite"] += 1
                
           # Caso seja opção inválida:
           except:
                sys.stderr = DevNull()
                exit(sys.exception)
            
    # Caso seja opção inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Corrida:
if EstiloDeJogo == 3:
    try:
        # Pergunta Plataforma:
        Plataforma = int(input("#-----------------------------------------#\n"
                               "|                Corrida                  |\n"
                               "#-----------------------------------------#\n"
                               "Você deseja Jogar em qual Plataforma?\n"
                               "[1] PC\n"
                               "[2] Mobile\n"
                               "[3] Console\n"
                               "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção inválida:
        if Plataforma > 3 or Plataforma < 1:
            exit(sys.exception)
        
        # Se a pessoa joga em PC:
        if Plataforma == 1:
            Jogos["Rocket League"] += 1
            Jogos["Forza"] += 1
            Jogos["Need For Speed"] += 1

            try:
                # Pergunta Preço:
                Preco = int(input("#-----------------------------------------#\n"
                                        "Você deseja pagar quanto pelo Jogo?\n"
                                        "[1] Grátis\n"
                                        "[2] R$ 20-30\n"
                                        "[3] R$ 30-40\n"
                                        "[4] R$ 100+\n"
                                        "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção inválida:
                if Preco > 4 or Preco < 1:
                    exit(sys.exception)

                # Caso seja Grátis:
                if Preco == 1:
                    Jogos["Rocket League"] += 1

                # Caso seja 20-30:
                if Preco == 2:
                    Jogos["Need For Speed"] += 1

                # Caso seja 30-40:
                if Preco == 3:
                    Jogos["Need For Speed"] += 1

                # Caso seja 100+:
                if Preco == 4:
                    Jogos["Forza"] += 1
            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)
        
        # Se a pessoa joga em Mobile:
        if Plataforma == 2:
            Jogos["Speed Drifters"] += 1
            Jogos["Grid"] += 1
        
        # Se a pessoa joga em Console:
        if Plataforma == 3:
            Jogos["Rocket League"] += 1
            Jogos["Forza"] += 1
            Jogos["Mario Kart"] += 1
            Jogos["Need For Speed"] += 1
    
    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser RPG:
if EstiloDeJogo == 4:
    try:
        # Pergunta Modelo:
        Modelo = int(input("#-----------------------------------------#\n"
                           "|                    RPG                  |\n"
                           "#-----------------------------------------#\n"
                           "Você deseja jogar em qual Modelo?\n"
                           "[1] 2D\n"
                           "[2] Aventura\n"
                           "[3] Futurista\n"
                           "[4] Fantasia\n"
                           "[5] Multijogador\n"
                           "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção Inválida
        if Modelo > 5 or Modelo < 1:
            exit(sys.exception)

        # Se for 2D:
        if Modelo == 1:
            Jogos["Hollow Knight"] += 1
            Jogos["Hades"] += 1
            Jogos["Gwent"] += 1
            Jogos["Hearthstone: Heroes of Warcraft"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                    "Você deseja jogar um jogo de História ou Cartas?\n"
                                    "[1] História\n"
                                    "[2] Cartas\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for História:
                if Estilo == 1:
                    Jogos["Hollow Knight"] += 1
                    Jogos["Hades"] += 1

                # Se for Cartas:
                if Estilo == 2:
                    Jogos["Gwent"] += 1
                    Jogos["Hearthstone: Heroes of Warcraft"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Se for Aventura:
        if Modelo == 2:
            Jogos["Minecraft"] += 1
            Jogos["Assassin's Creed"] += 1
            Jogos["Slime Rancher"] += 1
            Jogos["Just Cause"] += 1
            Jogos["The Forest"] += 1
            Jogos["FarCry"] += 1
            Jogos["Read Dead Redemption 2"] += 1
            Jogos["Resident Evil"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                    "Você deseja jogar uma aventura de Fantasia ou Realista baseado em História?\n"
                                    "[1] Realista\n"
                                    "[2] Fantasia\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for Realista:
                if Estilo == 1:
                    Jogos["Assassin's Creed"] += 1
                    Jogos["Just Cause"] += 1
                    Jogos["The Forest"] += 1
                    Jogos["FarCry"] += 1
                    Jogos["Read Dead Redemption 2"] += 1

                # Se for Fantasia:
                if Estilo == 2:
                    Jogos["Minecraft"] += 1
                    Jogos["Slime Rancher"] += 1
                    Jogos["Resident Evil"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Se for Futurista:
        if Modelo == 3:
            Jogos["ARK Survival"] += 1
            Jogos["Cyberpunk"] += 1
            Jogos["Watch Dogs"] += 1

        # Se for Fantasia:
        if Modelo == 4:
            Jogos["The Witcher"] += 1
            Jogos["Elden Ring"] += 1
            Jogos["Slime Rancher"] += 1
            Jogos["Hollow Knight"] += 1
            Jogos["Hades"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                   "Você deseja jogar um jogo baseado em Poderes?\n"
                                   "[1] Sim\n"
                                   "[2] Não\n"
                                   "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Caso Sim:
                if Estilo == 1:
                    Jogos["The Witcher"] += 1
                    Jogos["Elden Ring"] += 1
                    Jogos["Hades"] += 1

                # Caso Não:
                if Estilo == 2:
                    Jogos["Slime Rancher"] += 1
                    Jogos["Hollow Knight"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Se for Multijogador:
        if Modelo == 5:
            Jogos["New World"] += 1
            Jogos["Albion Online"] += 1
            Jogos["Gwent"] += 1
            Jogos["Hearthstone: Heroes of Warcraft"] += 1
            Jogos["Minecraft"] += 1
            Jogos["The Forest"] += 1
            Jogos["ARK Survival"] += 1
            Jogos["Elden Ring"] += 1
            Jogos["Watch Dogs"] += 1
            Jogos["FarCry"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                   "Você deseja jogar Online ou Cooperativo?\n"
                                   "[1] Online\n"
                                   "[2] Cooperativo\n"
                                   "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for Online:
                if Estilo == 1:
                    Jogos["Gwent"] += 1
                    Jogos["Hearthstone: Heroes of Warcraft"] += 1
                    Jogos["ARK Survival"] += 1
                    Jogos["Elden Ring"] += 1
                    Jogos["Watch Dogs"] += 1
                    Jogos["FarCry"] += 1

                # Se for Cooperativo:
                if Estilo == 2:
                    Jogos["New World"] += 1
                    Jogos["Albion Online"] += 1
                    Jogos["Minecraft"] += 1
                    Jogos["The Forest"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser MMORPG:
if EstiloDeJogo == 5:
    try:
        # Pergunta Preço:
        Preco = int(input("#-----------------------------------------#\n"
                          "|                 MMORPG                  |\n"
                          "#-----------------------------------------#\n"
                          "Você deseja jogar de forma Grátis ou Paga?\n"
                          "[1] Grátis\n"
                          "[2] Pago\n"
                          "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção inválida:
        if Preco > 2 or Preco < 1:
            exit(sys.exception)
        
        # Se for Grátis:
        if Preco == 1:
            Jogos["Dauntless"] += 1
            Jogos["Path of Exile"] += 1
        
        # Se for Pago:
        if Preco == 2:
            Jogos["New World"] += 1
            Jogos["Albion Online"] += 1
            
        # Pergunta Estilo:
        Estilo = int(input("#-----------------------------------------#\n"
                        "Você deseja jogar um MMO de Fantasia?\n"
                        "[1] Sim\n"
                        "[2] Não\n"
                        "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção inválida:
        if Estilo > 2 or Estilo < 1:
            exit(sys.exception)
        
        # Se Sim:
        if Estilo == 1:
            Jogos["Dauntless"] += 1
            Jogos["Path of Exile"] += 1 
            
        # Se Não:
        if Estilo == 2:
            Jogos["New World"] += 1
            Jogos["Albion Online"] += 1

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Mobile:
if EstiloDeJogo == 6:
    try:
        # Pergunta Estrategia:
        Estrategia = int(input("#-----------------------------------------#\n"
                               "|                 Mobile                  |\n"
                               "#-----------------------------------------#\n"
                               "Você deseja jogar de forma Casual ou voltado a Estratégia?\n"
                               "[1] Casual\n"
                               "[2] Estratégia\n"
                               "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção inválida:
        if Estrategia > 2 or Estrategia < 1:
            exit(sys.exception)
        
        # Se for Casual:
        if Estrategia == 1:
            Jogos["Minecraft"] += 1
            Jogos["Among Us"] += 1
            Jogos["Roblox"] += 1
        
        # Se for Estratégia:
        if Estrategia == 2:
            Jogos["Hearthstone: Heroes of Warcraft"] += 1
            Jogos["Call of Duty Mobile"] += 1
            Jogos["Free Fire"] += 1
        
        # Pergunta Preço:
        Preco = int(input("#-----------------------------------------#\n"
                        "Você deseja jogar de forma Grátis ou Paga?\n"
                        "[1] Grátis\n"
                        "[2] Pago\n"
                        "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção inválida:
        if Preco > 2 or Preco < 1:
            exit(sys.exception)
        
        # Se for Grátis:
        if Preco == 1:
            Jogos["Among Us"] += 1
            Jogos["Roblox"] += 1
            Jogos["Free Fire"] += 1
            Jogos["Call of Duty Mobile"] += 1
        
        # Se for Pago:
        if Preco == 2:
            Jogos["Minecraft"] += 1
            Jogos["Hearthstone: Heroes of Warcraft"] += 1

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Rogue Like:
if EstiloDeJogo == 7:
    try:
        # Pergunta Estilo:
        Estilo = int(input("#-----------------------------------------#\n"
                           "|               Rogue Like                |\n"
                           "#-----------------------------------------#\n"
                           "Você deseja jogar em qual Estilo?\n"
                           "[1] Hack and Slash\n"
                           "[2] 2D Casual\n"
                           "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção Inválida:
        if Estilo > 2 or Estilo < 1:
            exit(sys.exception)
        
        # Se for Hack and Slash:
        if Estilo == 1:
            Jogos["Hades"] += 1
    
        # Se for 2D Casual:
        if Estilo == 2:
            Jogos["Hollow Knight"] += 1

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Souls Like:
if EstiloDeJogo == 8:
    try:
        # Pergunta Estilo:
        Estilo = int(input("#-----------------------------------------#\n"
                           "|               Souls Like                |\n"
                           "#-----------------------------------------#\n"
                           "Você deseja jogar em qual Estilo?\n"
                           "[1] Souls Like Difícil\n"
                           "[2] 2D Casual\n"
                           "Digite sua opção: "))
        perguntasFeitas += 1
        
        # Caso seja opção Inválida:
        if Estilo > 2 or Estilo < 1:
            exit(sys.exception)

        # Se for Souls Like Difícil:
        if Estilo == 1:
            Jogos["Dark Souls"] += 1
            Jogos["Ghost of Tsushima"] += 1
            Jogos["Elden Ring"] += 1
            Jogos["BloodBorn"] += 1
    
        # Se for 2D Casual:
        if Estilo == 2:
            Jogos["Hollow Knight"] += 1
        
        # Pergunta Modelo:
        Modelo = int(input("#-----------------------------------------#\n"
                        "Você deseja jogar um Souls Like de Fantasia?\n"
                        "[1] Sim\n"
                        "[2] Não\n"
                        "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção Inválida:
        if Modelo > 2 or Modelo < 1:
            exit(sys.exception)
        
        # Se Sim:
        if Modelo == 1:
            Jogos["Hollow Knight"] += 1
            Jogos["Elden Ring"] += 1
        
        # Se Não:
        if Modelo == 2:
            Jogos["BloodBorn"] += 1
            Jogos["Dark Souls"] += 1
            Jogos["Ghost of Tsushima"] += 1

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Estratégia:
if EstiloDeJogo == 9:
    try:
        # Pergunta Estilo:
        Estilo = int(input("#-----------------------------------------#\n"
                           "|               Estratégia                |\n"
                           "#-----------------------------------------#\n"
                           "Você deseja jogar em qual Estilo?\n"
                           "[1] Competitive\n"
                           "[2] Casual\n"
                           "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção Inválida:
        if Estilo > 2 or Estilo < 1:
            exit(sys.exception)

        # Se for Competitive:
        if Estilo == 1:
            Jogos["League of Legends"] += 1
            Jogos["Dota 2"] += 1
    
        # Se for Casual:
        if Estilo == 2:
            Jogos["Hearthstone: Heroes of Warcraft"] += 1
            Jogos["Among Us"] += 1
            Jogos["FIFA"] += 1
            Jogos["Gwent"] += 1
            Jogos["Golf Simulator"] += 1
            Jogos["XCOM 2"] += 1
        
        Modelo = int(input("#-----------------------------------------#\n"
                        "Você deseja jogar em qual Modelo?\n"
                        "[1] Cartas\n"
                        "[2] Esportes\n"
                        "[3] Fantasia\n"
                        "[4] Em Turnos\n"
                        "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção Inválida:
        if Modelo > 4 or Modelo < 1:
            exit(sys.exception)
        
        # Se for Cartas:
        if Modelo == 1:
            Jogos["Gwent"] += 1
            Jogos["Hearthstone: Heroes of Warcraft"] += 1
            Jogos["UNO"] += 1
    
        # Se for Esportes:
        if Modelo == 2:
            Jogos["FIFA"] += 1
            Jogos["Golf Simulator"] += 1
            
        # Se for Fantasia:
        if Modelo == 3:
            Jogos["Among Us"] += 1
            Jogos["League of Legends"] += 1
            Jogos["Dota 2"] += 1
            
        # Se for Em Turnos:
        if Modelo == 4:
            Jogos["XCOM 2"] += 1

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Exploração:
if EstiloDeJogo == 10:
    try:
        # Pergunta Modelo:
        Modelo = int(input("#-----------------------------------------#\n"
                           "|               Exploração                |\n"
                           "#-----------------------------------------#\n"
                           "Você deseja que Modalidade de Jogo?\n"
                           "[1] Fantasia\n"
                           "[2] Terror\n"
                           "[3] 2D\n"
                           "[4] Realista\n"
                           "[5] Futurista\n"
                           "[6] Difícil\n"
                           "Digite sua opção: "))
        perguntasFeitas += 1
    
        # Caso seja Inválida:
        if Modelo > 6 or Modelo < 1:
            exit(sys.exception)

        # Caso seja Fantasia:
        if Modelo == 1:
            Jogos["Minecraft"] += 1
            Jogos["Slime Rancher"] += 1
            Jogos["Outer Wilds"] += 1
            Jogos["Star Wars: Jedi Fallen Order"] += 1
            Jogos["The Witcher"] += 1
            Jogos["Elden Ring"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                   "Você deseja um Jogo em que Estilo?\n"
                                   "[1] Gráficos Desenhados\n"
                                   "[2] Mítico\n"
                                   "[3] Futurista\n"
                                   "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja Inválida:
                if Estilo > 3 or Estilo < 1:
                    exit(sys.exception)

                # Caso seja Gráficos Desenhados:
                if Estilo == 1:
                    Jogos["Minecraft"] += 1
                    Jogos["Slime Rancher"] += 1
                    Jogos["Outer Wilds"] += 1

                # Caso seja Mítico:
                if Estilo == 2:
                    Jogos["The Witcher"] += 1
                    Jogos["Elden Ring"] += 1

                # Caso seja Futurista:
                if Estilo == 3:
                    Jogos["Star Wars: Jedi Fallen Order"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Caso seja Terror:
        if Modelo == 2:
            Jogos["Resident Evil"] += 1
            Jogos["The Forest"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                   "Você deseja jogar Cooperativo?\n"
                                   "[1] Sim\n"
                                   "[2] Não\n"
                                   "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for Sim:
                if Estilo == 1:
                    Jogos["The Forest"] += 1

                # Se for Não:
                if Estilo == 2:
                    Jogos["Resident Evil"] += 1

            # Caso seja opção inválida:
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Caso seja 2D:
        if Modelo == 3:
            Jogos["Hollow Knight"] += 1

        # Caso seja Realista:
        if Modelo == 4:
            Jogos["Assassin's Creed"] += 1
            Jogos["Just Cause"] += 1
            Jogos["Ghost of Tsushima"] += 1
            Jogos["FarCry"] += 1
            Jogos["Read Dead Redemption 2"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                    "Você deseja uma Exploração com armas mais Atuais ou Clássicas?\n"
                                    "[1] Armas Atuais\n"
                                    "[2] Armas Clássicas\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for Armas Atuais:
                if Estilo == 1:
                    Jogos["FarCry"] += 1
                    Jogos["Read Dead Redemption 2"] += 1
                    Jogos["Just Cause"] += 1

                # Se for Armas Clássicas:
                if Estilo == 2:
                    Jogos["Ghost of Tsushima"] += 1
                    Jogos["Assassin's Creed"] += 1

            # Caso seja opção Inválida
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Caso seja Futurista:
        if Modelo == 5:
            Jogos["ARK Survival"] += 1
            Jogos["Watch Dogs"] += 1
            Jogos["Cyberpunk"] += 1
            Jogos["Star Wars: Jedi Fallen Order"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                    "Você deseja uma Exploração com armas mais Fictícias ou Clássicas?\n"
                                    "[1] Armas Fictícias\n"
                                    "[2] Armas Clássicas\n"
                                    "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for Armas Fictícias:
                if Estilo == 1:
                    Jogos["Star Wars: Jedi Fallen Order"] += 1

                # Se for Armas Clássicas:
                if Estilo == 2:
                    Jogos["ARK Survival"] += 1
                    Jogos["Watch Dogs"] += 1
                    Jogos["Cyberpunk"] += 1

            # Caso seja opção Inválida
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

        # Caso seja Difícil:
        if Modelo == 6:
            Jogos["Green Hell"] += 1
            Jogos["Ghost of Tsushima"] += 1
            Jogos["Elden Ring"] += 1
            Jogos["ARK Survival"] += 1

            try:
                # Pergunta Estilo:
                Estilo = int(input("#-----------------------------------------#\n"
                                   "Você deseja uma Exploração com elementos de Sobrevivência?\n"
                                   "[1] Sim\n"
                                   "[2] Não\n"
                                   "Digite sua opção: "))
                perguntasFeitas += 1

                # Caso seja opção Inválida
                if Estilo > 2 or Estilo < 1:
                    exit(sys.exception)

                # Se for Sim:
                if Estilo == 1:
                    Jogos["Green Hell"] += 1
                    Jogos["ARK Survival"] += 1

                # Se for Não:
                if Estilo == 2:
                    Jogos["Ghost of Tsushima"] += 1
                    Jogos["Elden Ring"] += 1

            # Caso seja opção Inválida
            except:
                sys.stderr = DevNull()
                exit(sys.exception)

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Se a pessoa quiser Terror:
if EstiloDeJogo == 11:
    try:
        # Pergunta Modalidade:
        Modalidade = int(input("#-----------------------------------------#\n"
                               "|                Terror                   |\n"
                               "#-----------------------------------------#\n"
                               "Você deseja jogar com qual Modalidade?\n"
                               "[1] História\n"
                               "[2] Escape Room\n"
                               "[3] Terror Psicológico\n"
                               "Digite sua opção: "))
        perguntasFeitas += 1

        # Caso seja opção Inválida:
        if Modalidade > 3 or Modalidade < 1:
            exit(sys.exception)
        
        # Se for História:
        if Modalidade == 1:
            Jogos["Resident Evil"] += 1
    
        # Se for Escape Room:
        if Modalidade == 2:
            Jogos["Escape The Backrooms"] += 1
            
        # Se for Terror Psicológico:
        if Modalidade == 3:
            Jogos["Project Zomboid"] += 1
            Jogos["Out Last"] += 1

    # Caso seja opção Inválida:
    except:
        valorInvalido()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Array ordenado de acordo com a pontuação
ordenado = sorted(Jogos.items(), key=lambda item: item[1], reverse=True)

# Printa os Resultados
print("#-----------------------------------------#\n")
for i in ordenado:
    for a in range(3):
        if a > 1:
            value = calculoPorcentagem(i[1], perguntasFeitas)
            if value == 100:
                print(f"Recomendo você jogar {i[0]}. ({value}%)")
print()
for i in ordenado:
    for a in range(3):
        if a > 1:
            value = calculoPorcentagem(i[1], perguntasFeitas)
            if value > 0 and value < 100:
                print(f"Você também pode gostar de {i[0]}. ({value}%)")